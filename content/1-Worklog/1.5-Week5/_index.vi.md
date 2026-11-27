---
title: "Tuần 5: Container: Docker, Amazon ECR và Lightsail Containers"
date: 2026-11-13
weight: 5
chapter: false
pre: " <b>1.5.</b> "
---

12/10-18/10/2026

## Mục tiêu tuần 5

- Đóng gói ứng dụng thành Docker image và chạy bằng Docker Compose.
- Đẩy image lên Amazon ECR và chạy container trên AWS.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu container, image và Dockerfile<br>- **Thực hành:**<br>&emsp;+ Cài đặt thư viện và chạy ứng dụng trên máy<br>&emsp;+ Kiểm tra ứng dụng | 12/10/2026 | 12/10/2026 | [Giới thiệu Docker](https://000015.awsfcaj.com/1-introduction/)<br>[Triển khai trên máy](https://000015.awsfcaj.com/2-deploy-local/) |
| 3 | - **Thực hành:**<br>&emsp;+ Chuẩn bị VPC, Security Group và IAM role cho ECR<br>&emsp;+ Tạo RDS instance<br>&emsp;+ Cấu hình EC2 | 13/10/2026 | 13/10/2026 | [Chuẩn bị](https://000015.awsfcaj.com/3-preparation/)<br>[Tạo RDS](https://000015.awsfcaj.com/4-configure-rds/)<br>[Cấu hình EC2](https://000015.awsfcaj.com/5-configure-ec2/) |
| 4 | - **Thực hành:**<br>&emsp;+ Triển khai bằng một Docker image<br>&emsp;+ Triển khai bằng Docker Compose<br>&emsp;+ Đẩy image lên Amazon ECR | 14/10/2026 | 14/10/2026 | [Triển khai bằng Docker Image](https://000015.awsfcaj.com/6-docker-image/)<br>[Triển khai bằng Docker Compose](https://000015.awsfcaj.com/7-docker-compose/)<br>[Đẩy image lên ECR](https://000015.awsfcaj.com/8-push-image/8.1-use-ecr/) |
| 5 | - **Thực hành:**<br>&emsp;+ Tạo Lightsail container service<br>&emsp;+ Triển khai public image | 15/10/2026 | 15/10/2026 | [Tạo container service](https://000046.awsfcaj.com/1-create-container-service/)<br>[Triển khai public image](https://000046.awsfcaj.com/2-deploy-public-image/) |
| 6 | - **Thực hành:**<br>&emsp;+ Build và đẩy image của mình<br>&emsp;+ Triển khai image của mình và dọn dẹp<br>- So sánh Lightsail container với chạy Docker trên Lightsail VM | 16/10/2026 | 16/10/2026 | [Build và đẩy image](https://000046.awsfcaj.com/3-build-and-push-image/)<br>[Triển khai image](https://000046.awsfcaj.com/4-deploy-your-image/) |

## Kết quả đạt được tuần 5

- Viết được Dockerfile, Docker Compose và chạy ứng dụng nhiều container kết nối database.
- Đẩy image lên repository private trên Amazon ECR bằng IAM role thay vì access key.
- Triển khai container trên Lightsail và hiểu ưu nhược điểm. Cuối cùng Ownword chạy Docker trên Lightsail VM và kéo image từ ECR.
