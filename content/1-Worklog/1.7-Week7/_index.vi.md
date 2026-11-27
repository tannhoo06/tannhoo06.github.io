---
title: "Tuần 7: Serverless và định danh: AWS Lambda, Amazon Cognito và VPC Peering"
date: 2026-11-13
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

26/10-01/11/2026

## Mục tiêu tuần 7

- Tự động hóa tác vụ bằng AWS Lambda.
- Thêm đăng ký và đăng nhập người dùng bằng Amazon Cognito.
- Kết nối riêng tư hai VPC bằng VPC Peering.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu AWS Lambda<br>- **Thực hành:**<br>&emsp;+ Gắn tag cho EC2 và tạo role cho Lambda<br>&emsp;+ Viết hàm Lambda để dừng và bật instance<br>&emsp;+ Gửi kết quả về Slack | 26/10/2026 | 26/10/2026 | [Tạo role cho Lambda](https://000022.awsfcaj.com/4-createroleforlambda/)<br>[Tạo hàm Lambda](https://000022.awsfcaj.com/5-createlambdafunction/) |
| 3 | - Tìm hiểu Cognito user pool và app client<br>- **Thực hành:**<br>&emsp;+ Tạo user pool<br>&emsp;+ Tạo API và hàm Lambda<br>&emsp;+ Kiểm tra đăng nhập từ front-end | 27/10/2026 | 27/10/2026 | [Tạo User Pool](https://000081.awsfcaj.com/2-create-user-pool/)<br>[Kiểm tra với front-end](https://000081.awsfcaj.com/4-test-front-end/) |
| 4 | - **Thực hành:**<br>&emsp;+ Triển khai Cognito dùng chung cho hai website<br>&emsp;+ Đọc phần giải thích code luồng OAuth<br>&emsp;+ Kiểm tra và dọn dẹp | 28/10/2026 | 28/10/2026 | [Giải thích code](https://000141.awsfcaj.com/3-note-code/)<br>[Triển khai và kiểm tra](https://000141.awsfcaj.com/4-app-configuration/) |
| 5 | - Tìm hiểu VPC Peering<br>- **Thực hành:**<br>&emsp;+ Chạy CloudFormation template<br>&emsp;+ Cập nhật Network ACL<br>&emsp;+ Tạo peering connection | 29/10/2026 | 29/10/2026 | [Giới thiệu VPC Peering](https://000019.awsfcaj.com/1-introduce/)<br>[Tạo peering connection](https://000019.awsfcaj.com/4-vpcpeering/) |
| 6 | - **Thực hành:**<br>&emsp;+ Cập nhật route table ở hai phía<br>&emsp;+ Bật cross-peer DNS<br>&emsp;+ Dọn dẹp tài nguyên<br>- Ghi chú cách Lightsail peering với default VPC để kết nối RDS | 30/10/2026 | 30/10/2026 | [Route Table](https://000019.awsfcaj.com/5-routetables/)<br>[Cross-Peer DNS](https://000019.awsfcaj.com/6-crosspeerdns/) |

## Kết quả đạt được tuần 7

- Viết được hàm Lambda dùng role quyền tối thiểu để bật và tắt EC2 theo lịch.
- Tạo được Cognito user pool, app client và hiểu luồng OAuth authorization code có PKCE.
- Kết nối hai VPC bằng VPC Peering, cập nhật route table, Network ACL và bật cross-peer DNS.
- Hiểu ba thành phần Ownword dùng cho đăng nhập và truy cập database: Cognito, Lambda trigger Pre sign-up và VPC peering của Lightsail.
