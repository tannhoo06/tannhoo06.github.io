---
title: "Tuần 11: Ownword: đăng nhập bằng Cognito, chạy ứng dụng và CloudFront"
date: 2026-11-13
weight: 11
chapter: false
pre: " <b>1.11.</b> "
---

23/11-29/11/2026

## Mục tiêu tuần 11

- Cấu hình đăng nhập bằng email và Google với Amazon Cognito.
- Chạy Ownword và public qua CloudFront và AWS WAF.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tạo Cognito user pool và public app client<br>- Cấu hình callback URL và PKCE | 23/11/2026 | 23/11/2026 | [Workshop 5.5 bước 1](../../5-workshop/5.5-auth/) |
| 3 | - Cấu hình Google làm identity provider<br>- Triển khai Lambda Pre sign-up để liên kết tài khoản Google đã xác minh với tài khoản có sẵn<br>- Thử đăng nhập bằng tài khoản mới và tài khoản đã có | 24/11/2026 | 24/11/2026 | [Workshop 5.5 bước 2](../../5-workshop/5.5-auth/) |
| 4 | - Chuẩn bị thông tin xác thực cho các nhà cung cấp model (Amazon Bedrock và OpenRouter)<br>- Chỉ lưu key của model trên server | 25/11/2026 | 25/11/2026 | [Workshop 5.5 bước 3](../../5-workshop/5.5-auth/) |
| 5 | - Build và chạy ứng dụng kết nối RDS<br>- Chạy migration database và kiểm tra log ứng dụng | 26/11/2026 | 26/11/2026 | [Workshop 5.5 bước 4](../../5-workshop/5.5-auth/#launch-app) |
| 6 | - Yêu cầu chứng chỉ ACM cho tên miền public<br>- Tạo CloudFront distribution đứng trước origin Caddy<br>- Gắn web ACL của AWS WAF<br>- Kiểm tra ứng dụng qua URL public | 27/11/2026 | 27/11/2026 | [Workshop 5.5 bước 5](../../5-workshop/5.5-auth/) |

## Kết quả đạt được tuần 11

- Thiết lập Cognito user pool cho phép đăng nhập bằng email, mật khẩu và Google, dùng luồng OAuth code có PKCE.
- Triển khai Lambda Pre sign-up để người học đã có tài khoản khi đăng nhập bằng Google vẫn giữ được WordBoard.
- Chạy được Ownword trên Lightsail, kết nối với RDS private.
- Public ứng dụng qua CloudFront với chứng chỉ ACM và web ACL của AWS WAF.
