---
title: "Tuần 4: Cơ sở dữ liệu với Amazon RDS và host đơn giản với Amazon Lightsail"
date: 2026-11-13
weight: 4
chapter: false
pre: " <b>1.4.</b> "
---

05/10-11/10/2026

## Mục tiêu tuần 4

- Chạy cơ sở dữ liệu quan hệ được quản lý trong private subnet.
- Tìm hiểu Amazon Lightsail, nền tảng sau này nhóm chọn để chạy Ownword.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu Amazon RDS: engine, Multi-AZ, backup<br>- **Thực hành:**<br>&emsp;+ Tạo VPC và Security Group<br>&emsp;+ Tạo DB subnet group | 05/10/2026 | 05/10/2026 | [Giới thiệu RDS](https://000005.awsfcaj.com/1-introduce/)<br>[Các bước chuẩn bị](https://000005.awsfcaj.com/2-prerequiste/) |
| 3 | - **Thực hành:**<br>&emsp;+ Tạo RDS database instance<br>&emsp;+ Tạo EC2 và triển khai ứng dụng mẫu<br>&emsp;+ Kết nối ứng dụng với RDS | 06/10/2026 | 06/10/2026 | [Tạo RDS instance](https://000005.awsfcaj.com/3-create-rds/)<br>[Triển khai ứng dụng](https://000005.awsfcaj.com/5-deploy-app/) |
| 4 | - **Thực hành:**<br>&emsp;+ Tạo snapshot và khôi phục database<br>&emsp;+ Dọn dẹp tài nguyên<br>- Ghi lại các cấu hình RDS dùng lại cho dự án (mã hóa, private subnet) | 07/10/2026 | 07/10/2026 | [Sao lưu và khôi phục](https://000005.awsfcaj.com/6-backup/) |
| 5 | - Tìm hiểu Amazon Lightsail<br>- **Thực hành:**<br>&emsp;+ Tạo Lightsail database<br>&emsp;+ Triển khai WordPress và gắn static IP | 08/10/2026 | 08/10/2026 | [Tạo Lightsail database](https://000045.awsfcaj.com/1-create-database/)<br>[Triển khai WordPress](https://000045.awsfcaj.com/2-wordpress-instance/) |
| 6 | - **Thực hành:**<br>&emsp;+ Bảo mật ứng dụng<br>&emsp;+ Tạo snapshot<br>&emsp;+ Chuyển sang instance lớn hơn<br>&emsp;+ Tạo cảnh báo<br>&emsp;+ Dọn dẹp tài nguyên | 09/10/2026 | 09/10/2026 | [Bảo mật ứng dụng](https://000045.awsfcaj.com/4-secure-the-applications/)<br>[Tạo snapshot](https://000045.awsfcaj.com/5-create-snapshots/)<br>[Tạo cảnh báo](https://000045.awsfcaj.com/7-create-alarms/) |

## Kết quả đạt được tuần 4

- Tạo được RDS trong private subnet, chỉ nhận kết nối từ Security Group của ứng dụng.
- Triển khai ứng dụng mẫu trên EC2 đọc và ghi dữ liệu vào RDS, rồi thực hành snapshot và khôi phục.
- Hiểu cách Lightsail gói sẵn máy chủ, ổ lưu trữ, static IP và mạng với giá cố định mỗi tháng, phù hợp với bản pilot nhỏ như Ownword.
- Thực hành snapshot Lightsail, nâng lên instance lớn hơn và đặt cảnh báo.
