---
title: "Tuần 2: Mạng với Amazon VPC và máy chủ với Amazon EC2"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>1.2.</b> "
---

21/09-27/09/2026

## Mục tiêu tuần 2

- Hiểu các thành phần cốt lõi của Amazon VPC.
- Khởi tạo, kết nối và quản lý máy chủ Amazon EC2.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu các khái niệm VPC:<br>&emsp;+ Subnet<br>&emsp;+ Route table<br>&emsp;+ Internet Gateway và NAT Gateway<br>- Tìm hiểu Security Group và Network ACL | 21/09/2026 | 21/09/2026 | [Giới thiệu VPC](https://000003.awsfcaj.com/1-introduce/)<br>[Tường lửa trong VPC](https://000003.awsfcaj.com/2-firewallinvpc/) |
| 3 | - **Thực hành:**<br>&emsp;+ Tạo VPC, public subnet và private subnet<br>&emsp;+ Tạo Internet Gateway và route table<br>&emsp;+ Tạo Security Group<br>&emsp;+ Bật VPC Flow Logs | 22/09/2026 | 22/09/2026 | [Các bước chuẩn bị](https://000003.awsfcaj.com/3-prerequisite/) |
| 4 | - **Thực hành:**<br>&emsp;+ Tạo EC2 trong public subnet và private subnet<br>&emsp;+ Kiểm tra kết nối và tạo NAT Gateway<br>&emsp;+ Dùng Reachability Analyzer<br>&emsp;+ Kết nối bằng Session Manager | 23/09/2026 | 23/09/2026 | [Triển khai EC2](https://000003.awsfcaj.com/4-createec2server/)<br>[Session Manager](https://000003.awsfcaj.com/4-createec2server/4.6-sessionmanager/) |
| 5 | - Tìm hiểu EC2 cơ bản:<br>&emsp;+ Instance type<br>&emsp;+ AMI<br>&emsp;+ EBS<br>- **Thực hành:**<br>&emsp;+ Tạo Amazon Linux instance và kết nối bằng SSH | 24/09/2026 | 24/09/2026 | [Giới thiệu EC2](https://000004.awsfcaj.com/1-introduce/)<br>[Tạo Amazon Linux Instance](https://000004.awsfcaj.com/4-launchlinuxinstance/) |
| 6 | - **Thực hành:**<br>&emsp;+ Đổi instance type<br>&emsp;+ Tạo EBS snapshot và custom AMI<br>&emsp;+ Tạo instance từ custom AMI<br>&emsp;+ Giới hạn dùng EC2 theo Region và instance type bằng IAM<br>&emsp;+ Dọn dẹp tài nguyên | 25/09/2026 | 25/09/2026 | [EC2 cơ bản](https://000004.awsfcaj.com/5-amazonec2basic/)<br>[Quản trị chi phí bằng IAM](https://000004.awsfcaj.com/8-costusagegovernance/) |

## Kết quả đạt được tuần 2

- Hiểu cách subnet, route table, Internet Gateway và NAT Gateway phối hợp với nhau trong VPC.
- Biết khi nào dùng Security Group (stateful, gắn theo instance) và khi nào dùng Network ACL (stateless, gắn theo subnet).
- Dựng được VPC có public subnet, private subnet và kiểm tra kết nối bằng Reachability Analyzer.
- Tạo và kết nối EC2 bằng SSH và Session Manager. Kết nối qua Session Manager không cần mở port 22.
- Tạo được EBS snapshot, custom AMI và dùng điều kiện IAM để giới hạn Region và loại instance được phép dùng.
