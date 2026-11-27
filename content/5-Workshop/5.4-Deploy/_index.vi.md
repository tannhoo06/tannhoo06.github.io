---
title: "Chuẩn bị Lightsail và RDS riêng tư"
date: 2026-11-20
weight: 4
chapter: false
pre: " <b>5.4.</b> "
---

## 1. Tạo máy Lightsail và cấu hình DNS máy chủ gốc

1. Trong **Lightsail → Instances → Create instance**, chọn **Singapore**, **Linux/Unix → OS Only → Ubuntu 24.04 LTS** và gói x86-64 có IPv4 công khai với ít nhất 2 GB RAM. Đặt tên `ownword-lab` và ghi lại IPv4 riêng. Chọn khóa SSH bạn đang giữ hoặc tải khóa bí mật tương ứng từ trang SSH keys của tài khoản Lightsail.
2. Tạo IPv4 tĩnh tại Singapore và gắn vào máy. Tại nhà cung cấp DNS, tạo bản ghi A trỏ tên miền máy chủ gốc, ví dụ `origin-lab.example.com`, thẳng tới IP tĩnh (dùng chế độ chỉ DNS nếu nhà cung cấp có proxy). Nếu không có tên miền riêng, bỏ qua bước tạo bản ghi DNS và dùng `origin-lab.<A-B-C-D>.sslip.io` (IPv4 tĩnh thay dấu chấm bằng dấu gạch nối); `sslip.io` tự động phân giải về máy của bạn để Caddy cấp chứng chỉ TLS công khai. Tên miền công khai sẽ được cấu hình với CloudFront ở chương 5.5.
3. Trong tường lửa Lightsail, mở TCP 80 và 443 để Caddy xác thực chứng chỉ công khai và phục vụ HTTPS. Giới hạn TCP 22 theo IP công khai của máy bạn. Nếu dùng SSH trên trình duyệt Lightsail, bật tùy chọn truy cập riêng tương ứng. Không mở cổng 3000 và 5432 ra Internet. Rà soát riêng quy tắc IPv6 nếu dùng. [Tạo máy Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/getting-started.html) · [IP tĩnh](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-create-static-ip.html) · [Tường lửa Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-firewall-and-port-mappings-in-amazon-lightsail.html)

**Điểm kiểm tra.** Máy đang chạy, tên miền máy chủ gốc phân giải về IPv4 tĩnh và bạn có thể SSH bằng tài khoản `ubuntu`.

## 2. Tạo PostgreSQL riêng tư

1. Trong **Lightsail → Account → Advanced**, bật **VPC peering** cho Singapore. VPC đích phải là default VPC của tài khoản tại Singapore. Trong console VPC, kiểm tra kết nối peering đã hoạt động và bảng định tuyến của các subnet RDS có đường tới mạng Lightsail qua peering. Dùng tuyến và CIDR thực tế hiện trên tài khoản.
2. Trong default VPC đó, dùng DB subnet group có subnet thuộc ít nhất hai Availability Zone. Tạo security group riêng cho DB và cho phép TCP 5432 đi vào từ IPv4 riêng /32 của máy Lightsail. Gắn group này vào RDS và bỏ quy tắc rộng hơn nếu trình tạo tự thêm.
3. Trong **RDS → Databases → Create database → Standard create**, chọn **PostgreSQL 16**, **Single DB instance**, `db.t4g.micro` nếu có, và 20 GiB gp3 có mã hóa. Chọn default VPC, DB subnet group và security group ở hai bước trước. Đặt **Public access: No**, cổng 5432, giữ bản sao tự động tối thiểu một ngày và bật deletion protection. Lưu mật khẩu quản trị riêng. Để trống tên cơ sở dữ liệu ban đầu để tạo cơ sở dữ liệu với đúng chủ sở hữu ở phần sau. [VPC peering cho Lightsail](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-vpc-peering-with-aws-resources.html) · [VPC và subnet group cho RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) · [Tạo RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

**Điểm kiểm tra.** RDS ở trạng thái **Available**, mục **Publicly accessible** là **No** và có endpoint DNS. Dùng endpoint này để kiểm tra tên máy chủ qua TLS.

## 3. Chuyển mã nguồn và chuẩn bị Ubuntu

**Trên máy cá nhân.** Mở terminal ở thư mục chứa gói mã nguồn rồi điền đường dẫn khóa SSH và IP của máy lab.

```bash
KEY="$HOME/.ssh/ownword-lab.pem"
LIGHTSAIL_IP='YOUR_LIGHTSAIL_STATIC_IPV4'
scp -i "$KEY" ownword-lab-source-c8a903e.tar.gz "ubuntu@$LIGHTSAIL_IP:~/"
ssh -i "$KEY" "ubuntu@$LIGHTSAIL_IP"
```

**Trong phiên SSH trên Lightsail.** Giải nén gói vào thư mục mới rồi chạy script cài đặt. Thoát và kết nối SSH lại để tài khoản nhận quyền từ nhóm Docker.

```bash
mkdir "$HOME/ownword-lab"
tar -xzf "$HOME/ownword-lab-source-c8a903e.tar.gz" -C "$HOME/ownword-lab"
cd "$HOME/ownword-lab"
bash deploy/lightsail/bootstrap-ubuntu.sh
```

Sau khi kết nối lại:

```bash
cd "$HOME/ownword-lab"
docker compose version
free -h
docker pull postgres:16-alpine
install -d -m 700 deploy/lightsail/.secrets
curl -fsSL https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem \
  -o deploy/lightsail/.secrets/rds-ca.pem
chmod 644 deploy/lightsail/.secrets/rds-ca.pem
```

Script cài Docker và Compose, đồng thời thêm 2 GiB swap. Tệp CA của RDS là tệp công khai. Ở các bước sau, bạn cũng sẽ dùng thư mục `.secrets` để lưu tệp môi trường riêng. [Docker trên Ubuntu](https://docs.docker.com/engine/install/ubuntu/) · [Tệp CA của RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)

## 4. Tạo tài khoản ứng dụng và sao lưu

**Trong phiên SSH trên Lightsail.** Điền endpoint RDS và tên tài khoản quản trị. Nhập mật khẩu quản trị khi container hỏi. Với `verify-full`, PostgreSQL kiểm tra chuỗi chứng chỉ và tên endpoint trên chứng chỉ.

```bash
cd "$HOME/ownword-lab"
RDS_HOST='YOUR_RDS_ENDPOINT'
RDS_ADMIN='YOUR_RDS_MASTER_USERNAME'
docker run --rm -it \
  --mount "type=bind,source=$PWD/deploy/lightsail/.secrets/rds-ca.pem,target=/rds-ca.pem,readonly" \
  -e PGSSLMODE=verify-full -e PGSSLROOTCERT=/rds-ca.pem \
  postgres:16-alpine psql -h "$RDS_HOST" -p 5432 -U "$RDS_ADMIN" -d postgres -W
```

**Trong `psql`.** Chạy các lệnh một lần trên instance mới. Tạo hai mật khẩu ngẫu nhiên khác nhau, chẳng hạn bằng `openssl rand -hex 32`, rồi nhập khi được hỏi. Tài khoản ứng dụng sở hữu cơ sở dữ liệu và chạy migration Drizzle. Ở chương 5.6, khi đã có schema, bạn sẽ cấp quyền đọc cho tài khoản sao lưu.

```text
\set ON_ERROR_STOP on
\conninfo
CREATE ROLE ownword_app LOGIN;
\password ownword_app
CREATE ROLE ownword_backup LOGIN;
\password ownword_backup
GRANT ownword_app TO CURRENT_USER WITH SET TRUE;
CREATE DATABASE ownword OWNER ownword_app;
\q
```

**Điểm kiểm tra.** Xem `\conninfo` có báo SSL không, rồi kiểm tra hai role và cơ sở dữ liệu đã được tạo. Nếu kết nối quá thời gian, xem lại peering, đường định tuyến của subnet và IPv4 riêng trong security group. Nếu lỗi chứng chỉ, kiểm tra bạn đang dùng đúng endpoint RDS và tệp CA AWS. [TLS cho RDS PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html) · [Chủ sở hữu cơ sở dữ liệu PostgreSQL](https://www.postgresql.org/docs/16/sql-createdatabase.html)

{{< figure src="/images/workshop/production-rds-tls.png" alt="Phiên PostgreSQL báo SSL đang bật và dùng TLSv1.3" caption="Truy vấn chỉ đọc từ ứng dụng Ownword trên Lightsail xác nhận kết nối TLS 1.3 đến Amazon RDS đang vận hành tại Singapore." >}}

[Tiếp theo: Cấu hình đăng nhập, chạy ứng dụng và kết nối CloudFront](../5.5-auth/)
