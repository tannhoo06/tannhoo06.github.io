"""Run in AWS CloudShell to attach Ownword's Google account-linking trigger.

Usage:
  python3 google-linker-cloudshell.py --pool-id ap-southeast-1_EXAMPLE
  python3 google-linker-cloudshell.py --pool-id ap-southeast-1_EXAMPLE --apply

The first command is read-only. The second creates an IAM role and Lambda, then
updates the user pool while preserving every setting accepted by UpdateUserPool.
"""

from __future__ import annotations

import argparse
import io
import json
import os
from pathlib import Path
import sys
import time
import zipfile

import boto3
from botocore.exceptions import ClientError


HANDLER_CODE = r'''import json
import os

import boto3
from botocore.config import Config


def handler(event, context):
    pool_id = os.environ["USER_POOL_ID"]
    if event.get("userPoolId") != pool_id:
        raise ValueError("Unexpected user pool")
    if event.get("triggerSource") != "PreSignUp_ExternalProvider":
        return event

    username = event.get("userName", "")
    prefix, separator, google_subject = username.partition("_")
    if prefix.lower() != "google" or not separator or not google_subject:
        return event

    attributes = event.get("request", {}).get("userAttributes", {})
    email = attributes.get("email", "")
    if not email or "@" not in email or '"' in email or "\\" in email:
        raise ValueError("A valid Google email is required")
    if str(attributes.get("email_verified", "")).lower() != "true":
        raise ValueError("A verified Google email is required")

    client = boto3.client(
        "cognito-idp",
        config=Config(connect_timeout=1, read_timeout=2, retries={"max_attempts": 1}),
    )
    matches = []
    next_token = None
    while True:
        params = {
            "UserPoolId": pool_id,
            "Filter": "email = " + json.dumps(email),
            "Limit": 60,
        }
        if next_token:
            params["PaginationToken"] = next_token
        page = client.list_users(**params)
        matches.extend(page.get("Users", []))
        if len(matches) > 60:
            raise ValueError("Too many accounts with this email")
        next_token = page.get("PaginationToken")
        if not next_token:
            break

    same_email = []
    for user in matches:
        user_attributes = {item["Name"]: item["Value"] for item in user.get("Attributes", [])}
        if user_attributes.get("email", "").casefold() == email.casefold():
            same_email.append((user, user_attributes))

    if not same_email:
        # A new Google user: Cognito creates a normal federated profile.
        return event
    if len(same_email) != 1:
        raise ValueError("Multiple accounts have this email; contact support")

    destination, saved_attributes = same_email[0]
    saved_username = destination["Username"]
    if "_" in saved_username and saved_username.split("_", 1)[0].lower() in {
        "google", "facebook", "loginwithamazon", "signinwithapple"
    }:
        raise ValueError("A federated account already has this email; contact support")
    if destination.get("Enabled") is not True or destination.get("UserStatus") != "CONFIRMED":
        raise ValueError("Existing account is not active and confirmed")
    if saved_attributes.get("email_verified", "").lower() != "true":
        raise ValueError("Existing account email is not verified")
    if any(identity.get("providerName") == "Google" for identity in json.loads(saved_attributes.get("identities", "[]"))):
        raise ValueError("Existing account is already linked to Google")

    client.admin_link_provider_for_user(
        UserPoolId=pool_id,
        DestinationUser={"ProviderName": "Cognito", "ProviderAttributeValue": saved_username},
        SourceUser={
            "ProviderName": "Google",
            "ProviderAttributeName": "Cognito_Subject",
            "ProviderAttributeValue": google_subject,
        },
    )
    print("Linked verified Google identity to existing Cognito account")
    return event
'''


def project_to_shape(value, shape):
    """Keep fields accepted by the live SDK operation model, recursively."""
    if shape.type_name == "structure":
        return {
            key: project_to_shape(value[key], child_shape)
            for key, child_shape in shape.members.items()
            if key in value
        }
    if shape.type_name == "list":
        return [project_to_shape(item, shape.member) for item in value]
    if shape.type_name == "map":
        return {key: project_to_shape(item, shape.value) for key, item in value.items()}
    return value


def update_input(client, pool):
    shape = client.meta.service_model.operation_model("UpdateUserPool").input_shape
    params = project_to_shape(pool, shape)
    params["UserPoolId"] = pool["Id"]
    if "PoolName" in shape.members and "Name" in pool:
        params["PoolName"] = pool["Name"]
    return params


def package_handler():
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as archive:
        archive.writestr("index.py", HANDLER_CODE)
    return output.getvalue()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pool-id", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    region, separator, suffix = args.pool_id.partition("_")
    if not separator or region != "ap-southeast-1" or not (suffix.isascii() and suffix.isalnum()):
        parser.error("Expected a Singapore Cognito user pool ID such as ap-southeast-1_EXAMPLE")

    session = boto3.Session(region_name=region)
    account_id = session.client("sts").get_caller_identity()["Account"]
    cognito = session.client("cognito-idp")
    pool = cognito.describe_user_pool(UserPoolId=args.pool_id)["UserPool"]
    google = cognito.describe_identity_provider(
        UserPoolId=args.pool_id, ProviderName="Google"
    )["IdentityProvider"]
    mapping = google.get("AttributeMapping", {})
    if mapping.get("email") != "email" or mapping.get("email_verified") != "email_verified":
        raise SystemExit("Google must map both email and email_verified to matching Cognito attributes.")
    previous_trigger = pool.get("LambdaConfig", {}).get("PreSignUp")
    print(f"AWS account: {account_id}")
    print(f"User pool: {pool['Id']} ({pool.get('Name', '')})")
    print(f"Cognito domain prefix: {pool.get('Domain', '<none>')}")
    print(f"Current pre sign-up trigger: {previous_trigger or '<none>'}")
    print(f"Other configured triggers: {', '.join(sorted(k for k in pool.get('LambdaConfig', {}) if k != 'PreSignUp')) or '<none>'}")
    print("Google email and email_verified mappings: confirmed")
    if previous_trigger:
        raise SystemExit("A pre sign-up trigger already exists. Stop and integrate with it instead of replacing it.")
    if not args.apply:
        print("Read-only inspection complete. Run again with --apply to deploy and attach.")
        return

    function_name = f"ownword-google-link-{suffix}"
    role_name = f"ownword-google-link-role-{suffix}"
    iam = session.client("iam")
    lam = session.client("lambda")
    logs = session.client("logs")
    try:
        iam.get_role(RoleName=role_name)
    except iam.exceptions.NoSuchEntityException:
        pass
    else:
        raise SystemExit(f"IAM role {role_name} already exists. Stop to inspect it before re-running.")
    try:
        lam.get_function(FunctionName=function_name)
    except lam.exceptions.ResourceNotFoundException:
        pass
    else:
        raise SystemExit(f"Lambda {function_name} already exists. Stop to inspect it before re-running.")

    backup = Path(f"ownword-pool-before-google-link-{args.pool_id}-{int(time.time())}.json")
    backup.write_text(json.dumps(pool, default=str, indent=2), encoding="utf-8")
    backup.chmod(0o600)
    print(f"Saved pool backup: {backup}")

    pool_arn = pool["Arn"]
    log_group = f"/aws/lambda/{function_name}"
    log_arn = f"arn:aws:logs:{region}:{account_id}:log-group:{log_group}:*"
    trust = {
        "Version": "2012-10-17",
        "Statement": [{"Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}],
    }
    role = iam.create_role(
        RoleName=role_name,
        AssumeRolePolicyDocument=json.dumps(trust),
        Description="Ownword verified Google-to-Cognito account linking trigger",
    )["Role"]
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {"Effect": "Allow", "Action": ["cognito-idp:ListUsers", "cognito-idp:AdminLinkProviderForUser"], "Resource": pool_arn},
            {"Effect": "Allow", "Action": ["logs:CreateLogStream", "logs:PutLogEvents"], "Resource": log_arn},
        ],
    }
    iam.put_role_policy(RoleName=role_name, PolicyName="ownword-google-link", PolicyDocument=json.dumps(policy))
    try:
        logs.create_log_group(logGroupName=log_group)
    except ClientError as error:
        if error.response["Error"]["Code"] != "ResourceAlreadyExistsException":
            raise
    logs.put_retention_policy(logGroupName=log_group, retentionInDays=14)

    for attempt in range(6):
        try:
            created = lam.create_function(
                FunctionName=function_name,
                Runtime="python3.12",
                Role=role["Arn"],
                Handler="index.handler",
                Code={"ZipFile": package_handler()},
                Description="Link verified Google users to verified existing Ownword password accounts",
                Timeout=5,
                MemorySize=256,
                Environment={"Variables": {"USER_POOL_ID": args.pool_id}},
            )
            break
        except ClientError as error:
            if attempt == 5 or error.response["Error"]["Code"] != "InvalidParameterValueException":
                raise
            time.sleep(5)
    function_arn = created["FunctionArn"]
    for _ in range(20):
        state = lam.get_function_configuration(FunctionName=function_name)["State"]
        if state == "Active":
            break
        if state == "Failed":
            raise RuntimeError("Lambda entered Failed state; pool trigger was not changed")
        time.sleep(2)
    else:
        raise RuntimeError("Lambda did not become Active; pool trigger was not changed")

    lam.add_permission(
        FunctionName=function_name,
        StatementId="AllowOwnwordCognitoUserPool",
        Action="lambda:InvokeFunction",
        Principal="cognito-idp.amazonaws.com",
        SourceArn=pool_arn,
        SourceAccount=account_id,
    )

    current = cognito.describe_user_pool(UserPoolId=args.pool_id)["UserPool"]
    if current.get("LastModifiedDate") != pool.get("LastModifiedDate"):
        raise RuntimeError("User pool changed during deployment; Lambda was created but the trigger was not attached")
    if current.get("LambdaConfig", {}).get("PreSignUp"):
        raise RuntimeError("Another pre sign-up trigger was attached during deployment; pool was not changed")
    params = update_input(cognito, current)
    params["LambdaConfig"] = dict(params.get("LambdaConfig", {}), PreSignUp=function_arn)
    cognito.update_user_pool(**params)
    updated = cognito.describe_user_pool(UserPoolId=args.pool_id)["UserPool"]
    if updated.get("LambdaConfig", {}).get("PreSignUp") != function_arn:
        raise RuntimeError("Trigger attachment could not be verified")
    print(f"Attached pre sign-up Lambda: {function_arn}")
    print("Wait 70 seconds for Cognito propagation before testing with a fresh email/password account.")


if __name__ == "__main__":
    try:
        main()
    except ClientError as error:
        print(f"AWS error: {error.response['Error']['Code']}: {error.response['Error'].get('Message', '')}", file=sys.stderr)
        sys.exit(1)
