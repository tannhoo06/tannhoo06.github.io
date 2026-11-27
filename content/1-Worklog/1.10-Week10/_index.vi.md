---
title: "Tuần 10: Ownword: triển khai Lightsail và RDS private"
date: 2026-11-13
weight: 10
chapter: false
pre: " <b>1.10.</b> "
---

16/11-22/11/2026

## Mục tiêu tuần 10

- Dựng lớp hosting của Ownword trên Amazon Lightsail.
- Kết nối với cơ sở dữ liệu PostgreSQL private, có mã hóa trên Amazon RDS.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tạo Lightsail host ở Singapore<br>- Gắn static IP và tạo bản ghi DNS cho origin<br>- Bật VPC peering cho Lightsail | 16/11/2026 | 16/11/2026 | [Workshop 5.4 bước 1](../../5-workshop/5.4-deploy/) |
| 3–4 | - Tạo PostgreSQL instance private:<br>&emsp;+ Single-AZ, có mã hóa, nằm trong private subnet<br>&emsp;+ Security Group chỉ mở port 5432 cho IP private của Lightsail<br>- Kiểm tra kết nối với TLS `verify-full` | 17/11/2026 | 18/11/2026 | [Workshop 5.4 bước 2](../../5-workshop/5.4-deploy/) |
| 5 | - Chuyển mã nguồn lên host<br>- Cài đặt ban đầu cho Ubuntu: Docker, Caddy, firewall | 19/11/2026 | 19/11/2026 | [Workshop 5.4 bước 3](../../5-workshop/5.4-deploy/) |
| 6 | - Tạo tài khoản ứng dụng và một tài khoản backup chỉ đọc riêng trong PostgreSQL<br>- Ghi lại các lỗi đã gặp và cách xử lý | 20/11/2026 | 20/11/2026 | [Workshop 5.4 bước 4](../../5-workshop/5.4-deploy/) |

## Kết quả đạt được tuần 10

- Triển khai Lightsail host có static IP, DNS cho origin và peering với VPC chứa RDS.
- Tạo RDS PostgreSQL private có mã hóa, chỉ nhận kết nối từ IP private /32 của Lightsail host.
- Cài đặt Docker và Caddy cho host, sẵn sàng chạy Ownword.
- Tạo tài khoản database riêng cho ứng dụng và cho việc sao lưu, theo nguyên tắc quyền tối thiểu.
