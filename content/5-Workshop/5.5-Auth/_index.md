---
title: "Configure sign-in, deploy Ownword and connect CloudFront"
date: 2026-11-20
weight: 5
chapter: false
pre: " <b>5.5.</b> "
---

## 1. Create the Cognito pool and public client {#base-cognito}

1. In **Amazon Cognito, Asia Pacific (Singapore)**, create a lab user pool with email sign-in, password authentication, self-registration, and email verification. Require only the email attribute so the Ownword form can register users. Create a public app client without a secret, such as the **Single-page application** client type. Use verified email for account recovery.
2. Enable the **Cognito user pool** identity provider, **Authorization code grant**, and scopes `openid email profile` in the app client's login settings. Set the callback to `https://app-lab.example.com/auth/callback` and sign-out URL to `https://app-lab.example.com/`, using your public lab hostname. Create a Cognito prefix domain and assign a managed-login branding style if required.
3. In **Authentication flows**, enable username-and-password sign-in (`ALLOW_USER_PASSWORD_AUTH`). Ownword's server uses `USER_PASSWORD_AUTH` for the custom form and the OAuth code grant with PKCE for managed login. Record the pool ID, client ID and Cognito domain. [Cognito app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html) · [Authorization and PKCE](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) · [App client API and auth flows](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html)

## 2. Configure Google and link verified accounts

1. In Google Auth Platform, configure **Branding** and **Audience** for the lab OAuth project. For a Cognito prefix domain, add `amazoncognito.com` under authorized domains. Request the basic OpenID, email and profile scopes. Create a **Web application** OAuth client. If the Google project is in testing mode, add the lab Google accounts as test users.
2. On the Google client, set **Authorized JavaScript origins** to `https://YOUR_PREFIX.auth.ap-southeast-1.amazoncognito.com` and **Authorized redirect URIs** to that domain plus `/oauth2/idpresponse`. Then add **Google** in the Cognito pool using the Google client ID and secret, request `openid email profile`, and map Google `email` and `email_verified` to the matching Cognito attributes. Enable **Google** alongside **Cognito user pool** in the app client and make the mapped attributes writable. [Google federation settings](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-social-idp-google.html) · [Cognito attribute mapping](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html)
3. Download {{< workshop-download "downloads/google-linker-cloudshell.py" "the Singapore account-linking script" >}} and upload it to your home directory in **Singapore CloudShell**. Run the dry run first and verify the account, pool and mappings. Run `--apply` only on your lab pool. Record the function and execution role that the script creates. Wait at least 70 seconds for propagation before testing a first Google sign-in. [Pre sign-up trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) · [Linking federated profiles](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html)

```bash
POOL_ID='ap-southeast-1_YOUR_LAB_POOL_SUFFIX'
python3 ~/google-linker-cloudshell.py --pool-id "$POOL_ID"
python3 ~/google-linker-cloudshell.py --pool-id "$POOL_ID" --apply
aws cognito-idp describe-user-pool --region ap-southeast-1 --user-pool-id "$POOL_ID" \
  --query 'UserPool.LambdaConfig.PreSignUp' --output text
```

If `--apply` stops partway through, use the suffix after the underscore in the pool ID to find any lab resources it created. The function is `ownword-google-link-<suffix>`, the role is `ownword-google-link-role-<suffix>`, and the log group is `/aws/lambda/ownword-google-link-<suffix>`. Check the trigger configuration before retrying. If you need a fresh attempt, detach the new trigger if it was attached, then delete the function, role and log group from that failed attempt. Keep the pool and OAuth client for the retry.

## 3. Prepare credentials for the model providers

1. Check that your account can call the Kimi K3.1 Pro U.S. inference profile from **N. Virginia**. AWS may ask you to enable access or complete a provider subscription. Even if the profile shows Active, check that your account can invoke it. Run the commands in **N. Virginia CloudShell** as an administrator who can read the profile. The generated policy uses your profile ARN and the ARN of each destination model. Review both results before attaching the policy. [Bedrock model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) · [Inference profile IAM prerequisites](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-prereq.html) · [GetInferenceProfile CLI](https://docs.aws.amazon.com/cli/latest/reference/bedrock/get-inference-profile.html)

```bash
aws bedrock get-inference-profile --region us-east-1 \
  --inference-profile-identifier us.moonshotai.kimi-k3.1 > ownword-lab-profile.json
jq -e '.status == "ACTIVE" and (.models | length > 0)' ownword-lab-profile.json
jq '{
  Version: "2012-10-17",
  Statement: [
    {Effect:"Allow", Action:"bedrock:InvokeModel", Resource:.inferenceProfileArn},
    {Effect:"Allow", Action:"bedrock:InvokeModel", Resource:[.models[].modelArn],
     Condition:{StringEquals:{"bedrock:InferenceProfileArn":.inferenceProfileArn}}}
  ]
}' ownword-lab-profile.json > ownword-lab-bedrock-policy.json
```

2. Attach the inline policy to a separate identity for the lab app, such as the IAM user `ownword-lab-bedrock` with programmatic access. Give the app its own credentials and keep them private. If you use temporary credentials, include the session token and refresh them before they expire. Keep the administrator and backup credentials separate. [IAM access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) · [Bedrock Converse permissions](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
3. Create two lab OpenRouter keys. Use one for vocabulary and practice grading. The Writing key needs access to GPT-6.1 Terra Low with strict structured output and zero data retention. Set a spend limit at the provider. If a model call is denied, record the error and confirm access before you mark that part of the exercise complete.

## 4. Build and start the app against RDS {#launch-app}

This step builds the app container on Lightsail, runs the PostgreSQL migrations against RDS, and starts Caddy and Next.js.

**In the Lightsail SSH session.** Create both environment files from the unpacked source directory. Enter secrets in the editor. Use a different random hexadecimal password for each lab database role so the values are easy to enter in the files.

```bash
cd "$HOME/ownword-lab"
umask 077
cp deploy/lightsail/.env.example deploy/lightsail/.env
chmod 600 deploy/lightsail/.env
nano deploy/lightsail/.env
nano deploy/lightsail/.secrets/app-rds.env
```

Set these values in `deploy/lightsail/.env`:

| Setting | Lab value |
|---|---|
| `APP_DOMAIN` | Origin hostname only, for example `origin-lab.example.com` |
| `APP_PUBLIC_ORIGIN` | Public URL, for example `https://app-lab.example.com` |
| `COGNITO_ISSUER` | `https://cognito-idp.ap-southeast-1.amazonaws.com/YOUR_POOL_ID` |
| `COGNITO_DOMAIN` and `COGNITO_CLIENT_ID` | Full Cognito prefix-domain URL and the public client ID from step 1 |
| `CUSTOM_AUTH_ENABLED` and `GOOGLE_SIGN_IN_ENABLED` | Both `true` after steps 1 and 2 |
| `POSTGRES_PASSWORD` | A separate random placeholder for the base Compose file's unused local DB service. The RDS overlay supplies the actual app password. |
| `OPENROUTER_API_KEY` and `OPENROUTER_MODEL` | Lab vocabulary key and a verified compatible model. The archive defaults to `google/gemini-3.6-flash`. |
| `BEDROCK_CONCEPT_MODEL` | `us.moonshotai.kimi-k3.1` |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` | Bedrock runtime credentials from step 3. Leave the token empty for a long-lived IAM key. |
| `WRITING_MODULE_ENABLED` and `WRITING_TERRA_ENABLED` | Both `true` |
| `WRITING_TERRA_OPENROUTER_API_KEY`, `WRITING_TRENDS_ENABLED` | Separate Writing key and `false` for trends |

In `deploy/lightsail/.secrets/app-rds.env`, enter:

```dotenv
OWNWORD_RDS_HOST=YOUR_RDS_ENDPOINT
OWNWORD_RDS_DATABASE=ownword
OWNWORD_RDS_USER=ownword_app
OWNWORD_RDS_PASSWORD=YOUR_APP_ROLE_PASSWORD
OWNWORD_RDS_CA_FILE=/home/ubuntu/ownword-lab/deploy/lightsail/.secrets/rds-ca.pem
```

Save the helper below so the migration and app commands use the same environment files and RDS override. Source it again when you open a new SSH session, then use `ownword_compose` for the lab. The `--no-deps` flag leaves the base Compose file's local `db` service off.

```bash
cat > "$HOME/ownword-lab/compose-lab.sh" <<'EOF'
ownword_compose() {
  local app_root="$HOME/ownword-lab"
  docker compose --project-name ownword \
    --env-file "$app_root/deploy/lightsail/.env" \
    --env-file "$app_root/deploy/lightsail/.secrets/app-rds.env" \
    -f "$app_root/deploy/lightsail/compose.yaml" \
    -f "$app_root/deploy/lightsail/compose.rds.yaml" "$@"
}
EOF
source "$HOME/ownword-lab/compose-lab.sh"
ownword_compose config --quiet &&
  ownword_compose build app &&
  ownword_compose --profile tools run --rm --no-deps migrate &&
  ownword_compose up -d --no-deps app web &&
  ownword_compose ps
```

**Checkpoint.** The migration exits successfully and Compose shows `app` and `web` running. From the workstation, `curl -fsS https://origin-lab.example.com/ -o /dev/null` succeeds with a valid origin certificate. If it fails, check the origin A record, Lightsail ports and `ownword_compose logs --tail=60 web app`.

## 5. Publish through CloudFront and AWS WAF

{{% notice tip %}}
If you do not have a custom domain, you do not need to rent one for this lab. Skip step 1 (ACM) and step 5 (DNS CNAME), leave **Alternate domain names** empty in step 2 so CloudFront uses its default `*.cloudfront.net` certificate, and use `https://<distribution>.cloudfront.net` for `APP_PUBLIC_ORIGIN` in `deploy/lightsail/.env` and for the Cognito callback and sign-out URLs in section 1.
{{% /notice %}}

1. In **ACM, N. Virginia**, request a public certificate for the public hostname. Add the ACM validation CNAME at your DNS provider and wait for **Issued**. Keep that CNAME for renewal. Caddy serves the separate origin certificate. [CloudFront certificate requirements](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html) · [ACM DNS validation](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html)
2. Create a standard CloudFront distribution for a custom origin. Enter the origin hostname, no origin path, **HTTPS only** on port 443 for the origin, and **Redirect HTTP to HTTPS** for viewers. Add your public hostname as an alternate domain name and select the ACM certificate. Select pay-as-you-go for this disposable lab so the distribution can be removed after testing. [Origin settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html) · [Distribution settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html)
3. For the default behavior, allow all HTTP methods so the application can process POST and other writes. Select **CachingDisabled** and **AllViewerExceptHostHeader** for the origin request policy. Cookies, query strings and viewer headers pass through, and CloudFront sends the origin hostname in `Host` so it matches Caddy's virtual host and certificate. This preserves the OAuth callback, session cookies, and same-origin checks. Use an origin response timeout appropriate to the lab's AI calls and verify it with real lab requests. [Cache behavior settings](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html) · [Managed cache policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) · [Managed origin request policies](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html)
4. Attach a CloudFront-scope AWS WAF web ACL. For the lab, add a managed rule group such as **AWSManagedRulesCommonRuleSet** with its rule actions overridden to Count. After the DNS step, run normal sign-in and Writing requests and review sampled requests before switching to blocking. The web ACL protects traffic served by CloudFront. [Associate a WAF web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html) · [Test WAF protections](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html)
5. When the distribution is **Deployed**, create a DNS CNAME from the lab's public subdomain to the distribution hostname, or an alias at Route 53. Keep the origin A record pointed to Lightsail. Run these checks from the workstation with your public hostname. [CloudFront alternate domain names](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html)

```bash
LAB_HOST='app-lab.example.com'
curl -fsS -D - -o /dev/null "https://$LAB_HOST/"
curl -fsS -D - -o /dev/null "https://$LAB_HOST/auth/signin?hosted=1"
```

**Checkpoint.** The homepage should return 200 through CloudFront. The hosted sign-in URL should send you to Cognito with the public callback. Register and verify a test email through Ownword's form. Sign in, save a word, and sign out. Then use Google with that verified email for the first time in this pool. You should see the same WordBoard. Try another Google account to make sure it has a separate board. For a 502, check DNS, origin TLS, and the forwarded host. If Cognito rejects the redirect, compare the callback and sign-out URLs character by character.

{{< figure src="/images/workshop/production-wordboard.png" alt="Ownword WordBoard showing saved words at app.ownword.co over HTTPS" caption="After sign-in, WordBoard opens over HTTPS at the production URL and displays the learner's saved words." >}}

[Next: Back up RDS and configure monitoring](../5.6-operations/)
