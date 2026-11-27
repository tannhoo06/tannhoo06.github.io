---
title: "Tuần 3: IAM role cho EC2, AWS CLI và Amazon S3"
date: 2026-11-13
weight: 3
chapter: false
pre: " <b>1.3.</b> "
---

28/09-04/10/2026

## Mục tiêu tuần 3

- Cho ứng dụng gọi dịch vụ AWS mà không cần ghi cứng access key.
- Quản lý tài nguyên AWS bằng dòng lệnh.
- Lưu trữ và phân phối tệp bằng Amazon S3.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - **Thực hành:**<br>&emsp;+ Truy cập S3 từ EC2 bằng access key của IAM user<br>&emsp;+ Thay access key bằng IAM role gắn vào EC2<br>- So sánh hai cách làm | 28/09/2026 | 28/09/2026 | [Dùng access key](https://000048.awsfcaj.com/2-accesskey/)<br>[IAM role trên EC2](https://000048.awsfcaj.com/3-iamroleec2/) |
| 3 | - Cài đặt và cấu hình AWS CLI<br>&emsp;+ Access Key, Secret Key, Region mặc định<br>- **Thực hành:**<br>&emsp;+ Kiểm tra tài nguyên bằng CLI<br>&emsp;+ Làm việc với S3, SNS và IAM bằng CLI | 29/09/2026 | 29/09/2026 | [Cài AWS CLI](https://000011.awsfcaj.com/3-installcli/)<br>[AWS CLI với S3](https://000011.awsfcaj.com/5-s3/)<br>[AWS CLI với IAM](https://000011.awsfcaj.com/7-iam/) |
| 4 | - **Thực hành:**<br>&emsp;+ Tạo VPC, subnet, Internet Gateway và route table bằng CLI<br>&emsp;+ Tạo EC2 bằng CLI<br>&emsp;+ Xử lý các lỗi CLI thường gặp | 30/09/2026 | 30/09/2026 | [AWS CLI với Networking](https://000011.awsfcaj.com/8-network/)<br>[Tạo EC2 bằng AWS CLI](https://000011.awsfcaj.com/9-ec2/) |
| 5 | - Tìm hiểu Amazon S3: bucket, object, storage class<br>- **Thực hành:**<br>&emsp;+ Tạo bucket và bật static website hosting<br>&emsp;+ Cấu hình Block Public Access và public object | 01/10/2026 | 01/10/2026 | [Giới thiệu S3](https://000057.awsfcaj.com/1-introduce/)<br>[Bật static website](https://000057.awsfcaj.com/3-staticwebsite/) |
| 6 | - **Thực hành:**<br>&emsp;+ Chặn toàn bộ public access và phân phối website qua CloudFront<br>&emsp;+ Bật bucket versioning<br>&emsp;+ Sao chép object sang Region khác<br>- Đọc ghi chú và best practice về S3 | 02/10/2026 | 02/10/2026 | [Tăng tốc bằng CloudFront](https://000057.awsfcaj.com/7-cloudfront/)<br>[Bucket Versioning](https://000057.awsfcaj.com/8-versioning/)<br>[Ghi chú và best practice](https://000057.awsfcaj.com/12-notes/) |

## Kết quả đạt được tuần 3

- Hiểu vì sao IAM role an toàn hơn access key lưu trên server: thông tin xác thực chỉ dùng tạm thời và được tự động xoay vòng.
- Cài đặt, cấu hình AWS CLI và dùng nó để kiểm tra tài nguyên, tạo VPC, subnet và EC2.
- Host được website tĩnh trên S3, sau đó chuyển bucket sang private và phân phối qua CloudFront.
- Dùng versioning và sao chép sang Region khác để bảo vệ dữ liệu trên S3.
