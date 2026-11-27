---
title: "Sao lưu RDS và cấu hình giám sát"
date: 2026-11-20
weight: 6
chapter: false
pre: " <b>5.6.</b> "
---

## 1. Cấp quyền đọc RDS cho role sao lưu

Trong phiên SSH trên Lightsail, sau khi chạy xong migration ở chương 5.5, dùng endpoint RDS và mật khẩu của role ứng dụng từ chương 5.4 để kết nối.

```bash
cd "$HOME/ownword-lab"
RDS_HOST='YOUR_RDS_ENDPOINT'
docker run --rm -it \
  --mount "type=bind,source=$PWD/deploy/lightsail/.secrets/rds-ca.pem,target=/rds-ca.pem,readonly" \
  -e PGSSLMODE=verify-full -e PGSSLROOTCERT=/rds-ca.pem \
  postgres:16-alpine psql -h "$RDS_HOST" -U ownword_app -d ownword -W
```

Trong `psql`, trước hết kiểm tra xem kết nối có dùng TLS và bảng ghi migration có dữ liệu không. Sau đó cấp quyền đọc cho role sao lưu đối với bảng và sequence của ứng dụng, gồm cả bảng ghi Drizzle. Quyền mặc định cũng áp dụng cho những đối tượng `ownword_app` tạo sau này.

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

[TLS cho Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html) · [Quyền mặc định trong PostgreSQL](https://www.postgresql.org/docs/16/sql-alterdefaultprivileges.html)

## 2. Tạo nơi lưu S3 và danh tính sao lưu riêng

1. Trong S3 tại Singapore, tạo bucket general purpose với tên riêng cho lab. Giữ **Block all public access** và **Bucket owner enforced**. Bật versioning và SSE-S3. Tạo lifecycle rule cho `daily/`, hết hạn phiên bản hiện tại sau 30 ngày và phiên bản cũ sau 7 ngày.
2. Để tái hiện nhật ký truy cập của hệ thống đang vận hành, tạo bucket riêng thứ hai trong cùng tài khoản và vùng. Bật **Server access logging** trên bucket sao lưu và chọn bucket thứ hai làm đích. Kiểm tra policy của bucket đích cho phép `logging.s3.amazonaws.com` ghi vào prefix đã chọn. Đặt thời gian lưu 30 ngày cho prefix nhật ký. [Tạo bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) · [Lifecycle](https://docs.aws.amazon.com/AmazonS3/latest/userguide/intro-lifecycle-rules.html) · [Nhật ký truy cập](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html)
3. Tạo IAM user `ownword-lab-backup` chỉ truy cập qua API với access key riêng. Thay tên bucket trong inline policy dưới đây. `s3:GetObject` cho phép tải tệp và đọc metadata. Điều kiện của CloudWatch giới hạn việc ghi metric theo namespace. [Quyền HeadObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_HeadObject.html) · [Điều kiện IAM cho CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/iam-cw-condition-keys-namespace.html)

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

Trong phiên SSH trên Lightsail, chọn Singapore làm vùng mặc định khi chạy `aws configure`. Kiểm tra lệnh cuối trả về IAM user sao lưu của lab.

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

Nhập vào `deploy/lightsail/.secrets/backup.env`:

```bash
export AWS_PROFILE=ownword-lab-backup
export AWS_REGION=ap-southeast-1
S3_BACKUP_BUCKET='YOUR_BACKUP_BUCKET'
BACKUP_METRIC_INSTANCE='ownword-lab'
```

Nếu một lab khác trong tài khoản đã dùng `ownword-lab` cho dimension của metric, hãy chọn giá trị khác. Điền vào `deploy/lightsail/.secrets/rds-backup.env` theo mẫu dưới đây.

```dotenv
PGHOST=YOUR_RDS_ENDPOINT
PGPORT=5432
PGDATABASE=ownword
PGUSER=ownword_backup
PGPASSWORD=YOUR_BACKUP_ROLE_PASSWORD
```

Khi có tệp `rds-backup.env`, `backup-postgres.sh` lấy bản dump từ RDS. Script dùng CA tại `deploy/lightsail/.secrets/rds-ca.pem`, mạng Compose `ownword_private` và image `postgres:16-alpine` bạn đã tải ở chương 5.4.

## 3. Kiểm tra bản sao trên S3 và thử khôi phục riêng

Trong phiên SSH trên Lightsail, chạy sao lưu rồi kiểm tra bản sao còn mới không. Script kiểm tra bản dump trước khi tải lên với checksum SHA-256, sau đó đối chiếu kích thước tệp trên S3. Tìm hai dòng `Verified off-instance backup` và `BackupFresh=1`. [Kiểm tra tính toàn vẹn khi tải lên S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/checking-object-integrity-upload.html)

```bash
cd "$HOME/ownword-lab"
bash deploy/lightsail/backup-postgres.sh && bash deploy/lightsail/backup-health.sh
```

Thay tên tệp mẫu bằng tên trong khóa S3 của bạn. Các lệnh tải bản dump, đối chiếu với tệp cục bộ rồi khôi phục trong container PostgreSQL tạm, không có mạng ngoài hay cổng công khai. Sau khi kiểm tra bảng ghi migration và số từ đã lưu, script dọn container và tệp vừa tải. [Checksum của S3 GetObject](https://docs.aws.amazon.com/cli/latest/reference/s3api/get-object.html) · [pg_restore](https://www.postgresql.org/docs/16/app-pgrestore.html)

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

Xác nhận lệnh khôi phục thành công và truy vấn trả về số dòng, rồi ghi lại thời gian đo được. Sau khi kiểm tra thủ công xong, dùng `crontab -e` dưới tài khoản `ubuntu` để đặt lịch. Kiểm tra VM dùng UTC bằng `timedatectl`. Nếu thiếu `crontab`, cài và bật gói `cron` của Ubuntu. Lịch đầu chạy lúc 23:00 UTC hằng ngày, lịch thứ hai chạy vào phút 15 mỗi giờ và lịch thứ ba thử bổ sung thông tin cho từ đang chờ mỗi phút.

```cron
PATH=/usr/local/bin:/usr/bin:/bin
0 23 * * * /bin/bash "$HOME/ownword-lab/deploy/lightsail/backup-postgres.sh"
15 * * * * /bin/bash "$HOME/ownword-lab/deploy/lightsail/backup-health.sh"
* * * * * /usr/bin/flock -n /tmp/ownword-lab-word-enrichment.lock /bin/bash "$HOME/ownword-lab/deploy/lightsail/enrich-manual-words.sh"
```

## 4. Cấu hình cảnh báo sao lưu có mã hóa

1. Tại Singapore, tạo SNS Standard topic `ownword-lab-operator-alerts` và xác nhận đăng ký email từ hộp thư lab. Ghi ARN của topic. Chọn trước tên alarm `ownword-lab-backup-stale`, có ARN `arn:aws:cloudwatch:ap-southeast-1:YOUR_ACCOUNT_ID:alarm:ownword-lab-backup-stale`.
2. Thay các giá trị mẫu rồi thêm statement sau vào access policy hiện có của SNS. Giữ quyền hiện có của chủ topic. [Policy từ CloudWatch tới SNS](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Notify_Users_Alarm_Changes.html)

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

3. Tạo khóa KMS đối xứng do bạn quản lý tại Singapore, alias `ownword-lab-alerts`. Thêm hai đối tượng dưới đây vào mảng `Statement` của key policy và giữ quyền quản trị hiện có. Bật mã hóa topic bằng khóa này. CloudWatch cần hai quyền KMS để gửi tới topic SNS đã mã hóa. [Mã hóa SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-enable-encryption-for-topic.html) · [Quyền KMS cho CloudWatch và SNS](https://docs.aws.amazon.com/sns/latest/dg/sns-key-management.html)

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

4. Trong CloudWatch, mở **Alarms** và chọn **Create alarm**. Chọn `Ownword/Pilot → BackupFresh` với đúng dimension `Instance` của bước 2. Nếu vừa gửi metric, đợi metric xuất hiện. Chọn **Minimum**, chu kỳ 1 giờ, nhỏ hơn 1, 1 trên 1 và coi dữ liệu thiếu là vượt ngưỡng. Dùng tên đã chọn và gửi tới SNS đã mã hóa khi **In alarm**. [Alarm CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Alarms.html) · [Xử lý dữ liệu thiếu](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/alarms-and-missing-data.html)

## 5. Kiểm tra gửi cảnh báo

{{< figure src="/images/workshop/production-backup-alarm.png" alt="CloudWatch hiển thị cảnh báo sao lưu Ownword ở trạng thái OK và chỉ số BackupFresh bằng 1" caption="Trong CloudWatch tại Singapore, BackupFresh bằng 1 và cảnh báo sao lưu của Ownword ở trạng thái OK." >}}

Trong CloudShell tại Singapore, đợi alarm lab báo **OK** rồi dùng đúng tên alarm để gửi thử. CloudWatch sẽ tự quay lại đánh giá metric. Kiểm tra lịch sử gửi và email trong hộp thư. Để kiểm tra cả ngưỡng, quan sát thêm khi bản sao quá cũ hoặc metric bị thiếu. [SetAlarmState](https://docs.aws.amazon.com/cli/latest/reference/cloudwatch/set-alarm-state.html)

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

Xem lịch sử trong CloudWatch và tìm email cảnh báo thử trong hộp thư. Nếu chưa nhận được, xem lỗi trong lịch sử rồi kiểm tra đăng ký email, policy SNS và key policy KMS.

[Tiếp theo: Kiểm chứng, ước tính chi phí và dọn tài nguyên](../5.7-verification/)
