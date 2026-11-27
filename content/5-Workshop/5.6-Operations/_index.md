---
title: "Back up RDS and configure monitoring"
date: 2026-11-20
weight: 6
chapter: false
pre: " <b>5.6.</b> "
---

## 1. Give the backup role read access to RDS

In the Lightsail SSH session, once the migration in chapter 5.5 finishes, connect using the RDS endpoint and the app owner's password from chapter 5.4.

```bash
cd "$HOME/ownword-lab"
RDS_HOST='YOUR_RDS_ENDPOINT'
docker run --rm -it \
  --mount "type=bind,source=$PWD/deploy/lightsail/.secrets/rds-ca.pem,target=/rds-ca.pem,readonly" \
  -e PGSSLMODE=verify-full -e PGSSLROOTCERT=/rds-ca.pem \
  postgres:16-alpine psql -h "$RDS_HOST" -U ownword_app -d ownword -W
```

Inside `psql`, first check that the connection uses TLS and that the migration journal has entries. Then give the backup role read access to the app's tables and sequences, including the Drizzle journal. The default grants also cover objects `ownword_app` creates later.

```text
\set ON_ERROR_STOP on
SELECT current_user, ssl, version FROM pg_stat_ssl WHERE pid = pg_backend_pid();
SELECT count(*) FROM drizzle.__drizzle_migrations;
GRANT CONNECT ON DATABASE ownword TO ownword_backup;
GRANT USAGE ON SCHEMA public, drizzle TO ownword_backup;
GRANT SELECT ON ALL TABLES IN SCHEMA public, drizzle TO ownword_backup;
GRANT SELECT ON ALL SEQUENCES IN SCHEMA public, drizzle TO ownword_backup;
ALTER DEFAULT PRIVILEGES IN SCHEMA public, drizzle
  GRANT SELECT ON TABLES TO ownword_backup;
ALTER DEFAULT PRIVILEGES IN SCHEMA public, drizzle
  GRANT SELECT ON SEQUENCES TO ownword_backup;
\q
```

[Amazon RDS TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html) · [PostgreSQL default privileges](https://www.postgresql.org/docs/16/sql-alterdefaultprivileges.html)

## 2. Create S3 storage and a dedicated backup identity

1. In S3 (Singapore), create a general purpose lab bucket with a unique name. Keep **Block all public access** and **Bucket owner enforced**. Enable versioning and SSE-S3. Add a lifecycle rule for `daily/` with current expiration after 30 days and noncurrent expiration after 7 days.
2. To reproduce the production access logs, create a second private bucket in the same account and Region, then enable **Server access logging** on the backup bucket. Use the separate bucket as the destination and verify its policy permits `logging.s3.amazonaws.com` to write to the selected prefix. Apply a 30-day expiration to the log prefix. [Create a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) · [Lifecycle rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) · [Access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
3. Create the programmatic IAM identity `ownword-lab-backup` with a dedicated access key and no console access. Use this inline policy, replacing the bucket name. `s3:GetObject` covers downloading and checking object metadata. The CloudWatch condition limits metric writes to the workshop's namespace. [HeadObject permissions](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) · [CloudWatch IAM conditions](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-namespace.html)

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": ["s3:PutObject", "s3:GetObject"],
      "Resource": "arn:aws:s3:::YOUR_BACKUP_BUCKET/daily/*"
    },
    {
      "Effect": "Allow",
      "Action": "cloudwatch:PutMetricData",
      "Resource": "*",
      "Condition": {"StringEquals": {"cloudwatch:namespace": "Ownword/Pilot"}}
    }
  ]
}
```

In the Lightsail SSH session, choose Singapore when `aws configure` asks for the default Region, and confirm the final identity is the lab backup user.

```bash
cd "$HOME/ownword-lab"
bash deploy/lightsail/install-aws-cli.sh
aws configure --profile ownword-lab-backup
chmod 600 "$HOME/.aws/credentials"
umask 077
nano deploy/lightsail/.secrets/backup.env
nano deploy/lightsail/.secrets/rds-backup.env
chmod 600 deploy/lightsail/.secrets/backup.env deploy/lightsail/.secrets/rds-backup.env
aws sts get-caller-identity --profile ownword-lab-backup
```

Enter these values in `deploy/lightsail/.secrets/backup.env`:

```bash
export AWS_PROFILE=ownword-lab-backup
export AWS_REGION=ap-southeast-1
S3_BACKUP_BUCKET='YOUR_BACKUP_BUCKET'
BACKUP_METRIC_INSTANCE='ownword-lab'
```

If another lab in your account already uses `ownword-lab` for its metric dimension, choose a different value. Fill in `deploy/lightsail/.secrets/rds-backup.env` as shown below.

```dotenv
PGHOST=YOUR_RDS_ENDPOINT
PGPORT=5432
PGDATABASE=ownword
PGUSER=ownword_backup
PGPASSWORD=YOUR_BACKUP_ROLE_PASSWORD
```

When `rds-backup.env` exists, `backup-postgres.sh` takes the dump from RDS. It uses the CA at `deploy/lightsail/.secrets/rds-ca.pem`, the `ownword_private` Compose network, and the `postgres:16-alpine` image you pulled in chapter 5.4.

## 3. Verify the S3 copy and restore it in isolation

In the Lightsail SSH session, run the backup and check its freshness. The script checks the archive before uploading it with a SHA-256 checksum, then checks the object size in S3. Look for `Verified off-instance backup` and `BackupFresh=1`. [S3 upload integrity](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html)

```bash
cd "$HOME/ownword-lab"
bash deploy/lightsail/backup-postgres.sh && bash deploy/lightsail/backup-health.sh
```

Replace the sample filename with the one in your S3 key. The commands download the dump, compare it with the local copy, and restore it into a temporary PostgreSQL container with no external network or published ports. After checking the migration journal and saved words, the script removes the container and the downloaded file. [S3 GetObject checksum](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html) · [PostgreSQL pg_restore](https://www.postgresql.org/docs/16/app-pgrestore.html)

```bash
cd "$HOME/ownword-lab"
(
  set -euo pipefail
  source deploy/lightsail/.secrets/backup.env
  umask 077
  restore_dir="$(mktemp -d)"
  restore_container="ownword-lab-restore-$$"
  started=false
  cleanup() {
    if [[ "$started" == true ]]; then
      docker rm -f "$restore_container" >/dev/null 2>&1 || true
    fi
    rm -f -- "$restore_dir/backup.dump"
    rmdir -- "$restore_dir"
  }
  trap cleanup EXIT

  backup_name='YOUR_BACKUP_FILENAME.dump'
  aws s3api get-object --region "$AWS_REGION" --bucket "$S3_BACKUP_BUCKET" \
    --key "daily/$backup_name" --checksum-mode ENABLED "$restore_dir/backup.dump" >/dev/null
  cmp -- "deploy/lightsail/backups/$backup_name" "$restore_dir/backup.dump"

  docker run -d --rm --name "$restore_container" --network none \
    -e POSTGRES_PASSWORD="$(openssl rand -hex 32)" postgres:16-alpine >/dev/null
  started=true
  for attempt in {1..30}; do
    if docker exec "$restore_container" pg_isready -h 127.0.0.1 -U postgres -d postgres >/dev/null; then
      break
    fi
    sleep 1
  done
  docker exec "$restore_container" pg_isready -h 127.0.0.1 -U postgres -d postgres
  docker exec "$restore_container" createdb -U postgres ownword_restore
  time docker exec -i "$restore_container" pg_restore --exit-on-error --no-owner --no-acl \
    -U postgres -d ownword_restore < "$restore_dir/backup.dump"
  docker exec "$restore_container" psql -U postgres -d ownword_restore -v ON_ERROR_STOP=1 \
    -c 'SELECT count(*) AS migrations FROM drizzle.__drizzle_migrations' \
    -c 'SELECT count(*) AS saved_words FROM public.user_word'
)
```

Confirm that the restore command exits successfully and the queries return counts, then record the elapsed time. After the manual checks pass, use `crontab -e` under `ubuntu` to install the jobs below. Confirm the VM uses UTC with `timedatectl`, and install and enable Ubuntu's `cron` package if `crontab` is missing. The first job runs daily at 23:00 UTC, the second hourly at :15, and the third retries pending manual-word enrichment once a minute.

```cron
PATH=/usr/local/bin:/usr/bin:/bin
0 23 * * * /bin/bash "$HOME/ownword-lab/deploy/lightsail/backup-postgres.sh"
15 * * * * /bin/bash "$HOME/ownword-lab/deploy/lightsail/backup-health.sh"
* * * * * /usr/bin/flock -n /tmp/ownword-lab-word-enrichment.lock /bin/bash "$HOME/ownword-lab/deploy/lightsail/enrich-manual-words.sh"
```

## 4. Configure the encrypted backup alarm

1. In Singapore, create a Standard SNS topic `ownword-lab-operator-alerts` and confirm an email subscription from your lab inbox. Record its ARN. Reserve the alarm name `ownword-lab-backup-stale`. Its ARN is `arn:aws:cloudwatch:ap-southeast-1:YOUR_ACCOUNT_ID:alarm:ownword-lab-backup-stale`.
2. Append the following statement to the existing SNS access policy after replacing each placeholder. Keep the topic owner's existing permissions. [CloudWatch to SNS topic policy](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html)

```json
{
  "Sid": "AllowOwnwordLabAlarm",
  "Effect": "Allow",
  "Principal": {"Service": "cloudwatch.amazonaws.com"},
  "Action": "sns:Publish",
  "Resource": "YOUR_TOPIC_ARN",
  "Condition": {
    "ArnEquals": {"aws:SourceArn": "YOUR_ALARM_ARN"},
    "StringEquals": {"aws:SourceAccount": "YOUR_ACCOUNT_ID"}
  }
}
```

3. Create a customer-managed symmetric encrypt/decrypt KMS key in Singapore with alias `ownword-lab-alerts`. Append the following two objects to its existing `Statement` array, keeping the administrative statements. Enable topic encryption and choose this key. CloudWatch needs those two KMS permissions to publish through the encrypted topic. [SNS encryption](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html) · [KMS permissions for CloudWatch and SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html)

```json
[
  {
    "Sid": "AllowOwnwordLabAlarmKeyUse",
    "Effect": "Allow",
    "Principal": {"Service": "cloudwatch.amazonaws.com"},
    "Action": ["kms:GenerateDataKey*", "kms:Decrypt"],
    "Resource": "*",
    "Condition": {
      "ArnEquals": {"aws:SourceArn": "YOUR_ALARM_ARN"},
      "StringEquals": {"aws:SourceAccount": "YOUR_ACCOUNT_ID"}
    }
  },
  {
    "Sid": "AllowOwnwordLabTopicKeyUse",
    "Effect": "Allow",
    "Principal": {"Service": "sns.amazonaws.com"},
    "Action": ["kms:GenerateDataKey*", "kms:Decrypt"],
    "Resource": "*",
    "Condition": {
      "StringEquals": {"kms:EncryptionContext:aws:sns:topicArn": "YOUR_TOPIC_ARN"}
    }
  }
]
```

4. In CloudWatch, open **Alarms** and choose **Create alarm**. Select the custom metric `Ownword/Pilot → BackupFresh` with the exact `Instance` dimension from step 2. If it was just emitted, wait for it to show up. Use **Minimum**, a 1-hour period, **Lower than 1**, 1 out of 1, and **Treat missing data as breaching**. Name the alarm as reserved above and choose the encrypted SNS topic for the **In alarm** action. [CloudWatch alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) · [Missing metric data](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html)

## 5. Verify alarm delivery

{{< figure src="/images/workshop/production-backup-alarm.png" alt="CloudWatch showing the Ownword pilot backup alarm in OK state and the BackupFresh metric at 1" caption="In CloudWatch Singapore, BackupFresh is 1 and the Ownword pilot backup alarm is in the OK state." >}}

In Singapore CloudShell, wait until your lab alarm shows **OK**, then use its exact name to trigger a test. CloudWatch returns to evaluating the metric automatically. Look for a successful action and the email in your inbox. To check the threshold as well, observe what happens when the backup is stale or the metric is missing. [SetAlarmState](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/set-alarm-state.html)

```bash
ALARM='ownword-lab-backup-stale'
state="$(aws cloudwatch describe-alarms --region ap-southeast-1 \
  --alarm-names "$ALARM" --query 'MetricAlarms[0].StateValue' --output text)"
if [[ "$state" == OK ]]; then
  aws cloudwatch set-alarm-state --region ap-southeast-1 \
    --alarm-name "$ALARM" --state-value ALARM --state-reason 'Ownword lab email test'
else
  printf 'Wait for the lab alarm to be OK. Current state: %s\n' "$state"
fi
aws cloudwatch describe-alarm-history --region ap-southeast-1 \
  --alarm-name "$ALARM" --history-item-type Action --max-items 5
```

Check the CloudWatch action history and your inbox for the test alert. If the email doesn't arrive, look at the error in the history, then check the subscription, SNS policy, and KMS key policy.

[Next: Run acceptance checks, estimate cost and remove the lab](../5.7-verification/)
