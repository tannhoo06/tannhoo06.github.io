---
title: "Tuần 8: Bảo mật và độ tin cậy: KMS, Secrets Manager, SNS/SQS và AWS Backup"
date: 2026-11-13
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

02/11-08/11/2026

## Mục tiêu tuần 8

- Mã hóa dữ liệu lưu trữ và quản lý secret an toàn.
- Gửi thông báo bằng SNS và SQS.
- Sao lưu tài nguyên và kiểm tra khôi phục.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu AWS KMS và customer-managed key<br>- **Thực hành:**<br>&emsp;+ Tạo policy, role, group và user<br>&emsp;+ Tạo KMS key<br>&emsp;+ Tải dữ liệu đã mã hóa lên S3 | 02/11/2026 | 02/11/2026 | [Tạo KMS key](https://000033.awsfcaj.com/3-create-kms/)<br>[Tạo S3](https://000033.awsfcaj.com/4-create-s3/) |
| 3 | - **Thực hành:**<br>&emsp;+ Ghi log sử dụng key bằng CloudTrail<br>&emsp;+ Truy vấn log CloudTrail bằng Athena<br>&emsp;+ Kiểm tra và chia sẻ dữ liệu đã mã hóa | 03/11/2026 | 03/11/2026 | [CloudTrail và Athena](https://000033.awsfcaj.com/5-create-cloudtrail/)<br>[Kiểm tra dữ liệu mã hóa](https://000033.awsfcaj.com/6-demo/) |
| 4 | - Tìm hiểu AWS Secrets Manager<br>- **Thực hành:**<br>&emsp;+ Lưu thông tin đăng nhập RDS vào Secrets Manager<br>&emsp;+ Đọc secret từ Fargate task | 04/11/2026 | 04/11/2026 | [Dùng với RDS](https://000096.awsfcaj.com/3-rds-phase/)<br>[Dùng với Fargate](https://000096.awsfcaj.com/4-fargate-phase/) |
| 5 | - Tìm hiểu SNS topic và SQS queue<br>- **Thực hành:**<br>&emsp;+ Đăng ký email và kiểm tra fan-out<br>&emsp;+ Dùng message filtering và advanced filter policy | 05/11/2026 | 05/11/2026 | [Pub/Sub và Fan-Out](https://000077.awsfcaj.com/3-simplesubpub/)<br>[Lọc message](https://000077.awsfcaj.com/4-messagefiltering/) |
| 6 | - Tìm hiểu AWS Backup<br>- **Thực hành:**<br>&emsp;+ Tạo backup plan<br>&emsp;+ Thiết lập thông báo<br>&emsp;+ Kiểm tra khôi phục<br>&emsp;+ Dọn dẹp tài nguyên | 06/11/2026 | 06/11/2026 | [Tạo backup plan](https://000013.awsfcaj.com/3-createbackupplan/)<br>[Kiểm tra khôi phục](https://000013.awsfcaj.com/5-testrestore/) |

## Kết quả đạt được tuần 8

- Tạo được customer-managed KMS key, mã hóa dữ liệu trên S3 và kiểm tra việc sử dụng key bằng CloudTrail và Athena.
- Lưu thông tin đăng nhập database vào Secrets Manager thay vì ghi trong code.
- Dựng được SNS topic có đăng ký email, fan-out sang SQS và dùng filter policy.
- Hiểu rằng bản sao lưu chỉ đáng tin khi đã thử khôi phục. Ownword áp dụng đúng nguyên tắc này bằng một bước thử khôi phục riêng.
