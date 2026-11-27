---
title: "Tuần 9: CI/CD với GitHub Actions và đề xuất dự án Ownword"
date: 2026-11-13
weight: 9
chapter: false
pre: " <b>1.9.</b> "
---

09/11-15/11/2026

## Mục tiêu tuần 9

- Tự động hóa việc build và triển khai container image.
- Hiểu đề xuất dự án Ownword và thống nhất kiến trúc AWS với nhóm.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu các khái niệm CI/CD<br>- **Thực hành:**<br>&emsp;+ Clone GitHub template và đẩy code<br>&emsp;+ Tạo thông tin xác thực cho pipeline<br>&emsp;+ Kiểm tra kết quả GitHub Actions | 09/11/2026 | 09/11/2026 | [CI/CD với GitHub Actions](https://000017.awsfcaj.com/4-cicd-github/) |
| 3 | - **Thực hành:**<br>&emsp;+ Build bằng CodeBuild và tạo release tag<br>&emsp;+ Giám sát container bằng Container Insights<br>&emsp;+ Dọn dẹp tài nguyên ECS và ECR | 10/11/2026 | 10/11/2026 | [CI/CD với CodeBuild](https://000017.awsfcaj.com/5-cicd-codebuild/)<br>[Container Insights](https://000017.awsfcaj.com/6-monitoring-with-container-insights/) |
| 4 | - Đọc đề xuất dự án Ownword: vấn đề, đối tượng, phạm vi pilot<br>- Trao đổi với nhóm về phần việc của mình trong dự án | 11/11/2026 | 11/11/2026 | [Đề xuất Ownword](../../2-proposal/) |
| 5 | - Nghiên cứu kiến trúc Ownword:<br>&emsp;+ Luồng request trên production<br>&emsp;+ Luồng release (GitHub Actions → ECR → Lightsail)<br>&emsp;+ Đối chiếu các trụ cột Well-Architected | 12/11/2026 | 12/11/2026 | [Workshop 5.1 Tổng quan](../../5-workshop/5.1-overview/)<br>[Workshop 5.3 Kiến trúc](../../5-workshop/5.3-architecture/) |
| 6 | - Chuẩn bị môi trường lab:<br>&emsp;+ Kiểm tra quyền AWS và các điều kiện cần<br>&emsp;+ Tải mã nguồn và cài công cụ trên máy<br>&emsp;+ Ghi lại các thông số lab | 13/11/2026 | 13/11/2026 | [Workshop 5.2 Chuẩn bị](../../5-workshop/5.2-prerequisites/) |

## Kết quả đạt được tuần 9

- Dựng được pipeline CI/CD tự động kiểm thử, build và đẩy container image.
- Hiểu mục tiêu của Ownword: giúp người học tìm, lưu và chủ động dùng từ tiếng Anh mới, đồng thời nhận góp ý cho bài viết.
- Giải thích được kiến trúc Ownword từ đầu đến cuối: CloudFront và WAF → Caddy và Next.js trên Lightsail → RDS private, dùng Cognito để đăng nhập, Bedrock để tìm từ theo ý nghĩa và S3 để lưu bản sao lưu.
- Chuẩn bị xong máy làm việc và ghi lại các thông số cần cho lab.
