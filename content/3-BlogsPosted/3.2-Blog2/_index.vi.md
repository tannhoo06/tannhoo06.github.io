---
title: "Đóng Port 22 Lại Đi! Truy Cập EC2 Trong Private Subnet Bằng Session Manager 🔐"
menuTitle: "Session Manager thay cho SSH"
weight: 2
chapter: false
pre: " <b>3.2.</b> "
---

| Thông tin bài đăng | Nội dung |
| --- | --- |
| Ngày đăng | 18/11/2026 |
| Liên kết bài đăng | [Bài viết gốc trên Facebook](https://www.facebook.com/share/p/1CmPTgzM4j/) |
| Chủ đề bài đăng | Truy cập EC2 an toàn bằng AWS Systems Manager Session Manager, không cần SSH key, mở port hay bastion host |

{{< figure src="/images/blogs/blog2.png" alt="Ảnh bìa: Đóng port 22 lại đi!" caption="Hình 3.2. Ảnh bìa dùng trong bài đăng Facebook." >}}

Hồi mới học EC2, cách mình vào server rất "truyền thống": tạo key pair, tải file `.pem` về, mở port 22 trong Security Group (và thú thật là để source `0.0.0.0/0` cho nhanh), rồi `ssh -i key.pem ec2-user@...`. Đến khi học VPC và đặt EC2 vào private subnet thì mình bị chặn: instance không có public IP, không có Internet, vậy vào kiểu gì? Cách quen thuộc là dựng thêm một bastion host ở public subnet rồi SSH "nhảy" qua. Chạy được, nhưng sau khi làm workshop Session Manager trên First Cloud Journey, mình thấy có cách gọn và an toàn hơn nhiều.

## Vấn đề của SSH và bastion

- Phải mở port 22 ra ngoài, chỗ mà bot quét liên tục.
- Phải quản lý, chia sẻ, thu hồi file `.pem` cho từng người trong team. Một người nghỉ việc mà vẫn giữ key là rủi ro.
- Bastion là thêm một server phải vá lỗi, giám sát và trả tiền.
- Ai đã vào server, gõ lệnh gì? Muốn biết thì phải tự cấu hình log.

## Session Manager giải quyết thế nào?

Session Manager là một tính năng của AWS Systems Manager. Thay vì mình kết nối vào instance, SSM Agent trên instance chủ động kết nối ra dịch vụ Systems Manager qua HTTPS (443). Khi mình mở session từ Console hoặc CLI, lệnh đi qua kênh đó. Hệ quả là:

- **Không cần inbound rule** nào trong Security Group, không mở port 22 hay 3389.
- **Không cần SSH key:** quyền truy cập do IAM quản lý, ví dụ ai được `ssm:StartSession` vào instance nào.
- **Không cần bastion host.**
- **Có log:** lệnh gọi API được ghi vào CloudTrail, nội dung session có thể đẩy ra S3 hoặc CloudWatch Logs.

## Những gì cần chuẩn bị (theo workshop FCJ 000058)

1. **SSM Agent trên instance.** Amazon Linux và Windows AMI của AWS thường đã cài sẵn.
2. **IAM Role cho EC2** có managed policy `AmazonSSMManagedInstanceCore`. Policy này đủ quyền tối thiểu để dùng Session Manager.
3. **Đường mạng ra 3 endpoint `ssm`, `ssmmessages`, `ec2messages` qua HTTPS 443.**
   - Instance ở public subnet: đi qua Internet Gateway là được.
   - Instance ở private subnet, không NAT: tạo VPC Interface Endpoint cho cả 3 dịch vụ, và nhớ bật **DNS hostnames và DNS resolution** cho VPC. Bước này mình quên lúc đầu nên instance mãi không hiện trong Fleet Manager 😅
4. **(Tùy chọn) Ghi log session ra S3:** cập nhật IAM Role cho phép ghi vào bucket, tạo S3 Gateway Endpoint để instance private đẩy log lên S3 mà không cần Internet.

Workshop còn có phần **Port Forwarding**: mở tunnel từ máy mình tới một port trên instance (ví dụ RDP 3389 của Windows server private) mà vẫn không mở inbound nào.

## Một vài điều mình để ý thêm

- Interface Endpoint tính phí theo giờ cho mỗi AZ và theo lượng dữ liệu. Với lab thì nhớ xóa endpoint ở bước dọn dẹp. Với hệ thống thật thì vẫn thường rẻ hơn chạy NAT Gateway và bastion chỉ để quản trị.
- Theo tài liệu AWS, SSM Agent bản mới đã chuyển sang dùng `ssmmessages`. Ở các Region ra mắt từ 2024, `ec2messages` không còn được dùng cho chức năng này. Workshop vẫn tạo đủ 3 endpoint để chạy được ở mọi Region.
- Session Manager không thay thế việc phân quyền: vẫn nên giới hạn ai được mở session vào instance nào (dùng tag và IAM condition), thay vì cho cả team `ssm:*`.

## Lời kết

Điều mình học được không chỉ là "thêm một cách vào server". Đó là thay đổi tư duy: đừng mở cổng nếu không cần, và để IAM quản lý danh tính thay vì những file key nằm rải rác trên laptop mọi người. Từ giờ mỗi lần tạo Security Group mà định thêm rule port 22, mình sẽ hỏi lại bản thân: có thật sự cần không?

## Nguồn tham khảo

- [AWS Systems Manager: Session Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html)
- [AWS: Using AWS PrivateLink (VPC endpoints) for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html)
- [AWS Cloud Operations Blog: Session Manager without an Internet Gateway](https://aws.amazon.com/blogs/mt/automated-configuration-of-session-manager-without-an-internet-gateway)

## Thực hành trên First Cloud Journey

- [Session Manager](https://000058.awsfcaj.com)
- [Systems Manager](https://000031.awsfcaj.com)
- [IAM Role for EC2](https://000048.awsfcaj.com)
- [VPC](https://000003.awsfcaj.com)
