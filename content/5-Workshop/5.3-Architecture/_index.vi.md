---
title: "Kiến trúc và luồng dữ liệu"
date: 2026-11-20
weight: 3
chapter: false
pre: " <b>5.3.</b> "
---

## Luồng yêu cầu trên hệ thống đang vận hành

{{< ownword-architecture alt="Luồng yêu cầu qua CloudFront, Lightsail và RDS, cùng các luồng đăng nhập Cognito, gọi mô hình và sao lưu. GitHub Actions phát hành image lên ECR riêng tư tại Singapore để Lightsail tải về." caption="Kiến trúc Ownword và luồng tự động phát hành. Chọn sơ đồ để xem ở kích thước đầy đủ." >}}

| Bước | Luồng xử lý |
|---|---|
| **1-3. HTTPS công khai và máy chủ gốc** | Trình duyệt kết nối tới `app.ownword.co` qua CloudFront, với chứng chỉ ACM và web ACL của AWS WAF. CloudFront kết nối TLS tới Caddy tại `origin.ownword.co`. Caddy chuyển yêu cầu đến Next.js qua cổng 3000 trong mạng Docker Compose riêng. |
| **4. Cơ sở dữ liệu** | Next.js đọc và ghi dữ liệu vào Amazon RDS for PostgreSQL riêng tư tại Singapore qua kết nối VPC peering của Lightsail. RDS Single-AZ nằm trong subnet riêng tại `ap-southeast-1a`, mã hóa dữ liệu lưu trữ bằng khóa RDS do AWS quản lý và chỉ nhận kết nối TLS qua cổng 5432 từ địa chỉ riêng của máy Lightsail. |
| **5-8. Đăng nhập** | Next.js gọi Amazon Cognito tại Singapore để đăng nhập bằng mật khẩu và đổi mã OAuth. Khi đăng nhập bằng Google, trình duyệt đi qua luồng OAuth của Cognito rồi quay về `/auth/callback` để Next.js đổi mã bằng PKCE. Ở lần đăng nhập liên kết đầu tiên đủ điều kiện, Cognito có thể gọi Pre sign-up Lambda tại Singapore để liên kết danh tính Google đã xác minh. Next.js ánh xạ danh tính Cognito vào hồ sơ người học trong PostgreSQL. |
| **9-10. Gọi mô hình** | Tính năng tra cứu theo khái niệm gọi Amazon Bedrock qua endpoint Bắc Virginia và dùng cấu hình suy luận tại Mỹ của Kimi K3.1 Pro. Đánh giá bài viết gọi GPT-6.1 Terra Low qua OpenRouter, còn phần làm giàu từ vựng và chấm luyện tập gọi Gemini 3.6 Flash qua OpenRouter (dòng Gemini không có trên Bedrock). Mọi lượt gọi mô hình đều xuất phát từ máy chủ. |
| **11-14. Sao lưu và cảnh báo** | Tác vụ trên Lightsail đọc dữ liệu RDS với quyền riêng, xuất bản sao PostgreSQL hằng ngày và tải lên bucket S3 riêng tư. Bucket sao lưu và bucket nhật ký truy cập riêng đều dùng SSE-S3. Tác vụ kiểm tra hằng giờ gửi `BackupFresh`. Khi bản sao quá hạn hoặc thiếu tín hiệu, CloudWatch gửi thông báo qua SNS được mã hóa bằng khóa KMS do khách hàng quản lý. |

## Luồng phát hành

Khi có bản push vào `release/lightsail`, GitHub Actions kiểm tra mã nguồn, tạo Docker image rồi dùng thông tin xác thực AWS ngắn hạn qua GitHub OIDC để đẩy image lên Amazon ECR riêng tư ở Singapore. Lightsail kiểm tra ECR hai phút một lần. Khi có image mới, máy tải đúng phiên bản theo digest, chạy migration trên RDS và kiểm tra trang chủ cùng trang đăng nhập sau khi khởi động lại ứng dụng. Nếu bản mới không khởi động được, máy khôi phục image ứng dụng trước đó.

## Đối chiếu năm trụ cột AWS Well-Architected

| Trụ cột | Cách Ownword áp dụng |
|---|---|
| Vận hành xuất sắc (Operational Excellence) | GitHub Actions kiểm tra TypeScript và bài kiểm thử trước khi đóng gói image ECR gắn thẻ bất biến; Lightsail tải bản phát hành theo digest và tự quay về bản trước nếu kiểm tra tuyến thất bại. Chỉ số `BackupFresh` hằng giờ cùng cảnh báo CloudWatch phát hiện sớm lỗi sao lưu. |
| Bảo mật (Security) | CloudFront và AWS WAF đứng trước máy chủ gốc. RDS chạy trong subnet riêng, mã hóa dữ liệu lưu trữ, chỉ mở cổng 5432 cho IPv4 riêng `/32` của Lightsail và bắt buộc TLS `verify-full`. Cognito dùng PKCE cho OAuth, khóa API mô hình giữ trên máy chủ và IAM tách riêng quyền cho Bedrock, sao lưu S3 và Lambda liên kết tài khoản. |
| Độ tin cậy (Reliability) | Tách PostgreSQL khỏi máy Lightsail sang RDS giúp lỗi ứng dụng không kéo theo mất cơ sở dữ liệu. Bản sao `pg_dump` hằng ngày được tải lên bucket S3 riêng có versioning, kiểm tra SHA-256 và thử khôi phục trong container cô lập; cảnh báo sao lưu coi dữ liệu thiếu là vượt ngưỡng. Cấu hình Single-AZ là đánh đổi chủ đích cho giai đoạn thử nghiệm và có quy trình khôi phục đi kèm. |
| Hiệu năng (Performance Efficiency) | CloudFront kết thúc HTTPS gần người dùng rồi chuyển yêu cầu về Singapore (`ap-southeast-1`) gần nhóm người học mục tiêu. RDS chạy trên `db.t4g.micro` dùng chip Graviton kèm ổ gp3, và ứng dụng tái sử dụng kết quả tra khái niệm Bedrock đã lưu cho lượt tra lặp lại để giảm độ trễ gọi mô hình. |
| Tối ưu chi phí (Cost Optimization) | Hạ tầng cố định gọn nhẹ với gói Lightsail 2 GB và RDS `db.t4g.micro` Single-AZ. Dùng lại kết quả tra khái niệm, giới hạn token đầu ra, đặt hạn mức chi tiêu trên OpenRouter, cấu hình vòng đời S3 (30 ngày cho bản hiện tại, 7 ngày cho bản cũ) và giới hạn số image ECR giúp kiểm soát chi phí biến đổi. Xem [chương 5.7](../5.7-verification/#2-lập-dự-toán-hằng-tháng). |

## Cấu hình thực hành

Trước hết, bạn sẽ tạo Lightsail và RDS riêng tư cho lab. Có hai tên miền cần phân biệt. Cognito đưa người dùng về tên miền công khai sau khi đăng nhập, còn Caddy phục vụ tên miền máy chủ gốc. Tác vụ sao lưu đọc dữ liệu bằng một role PostgreSQL riêng. Ở phần sau, bạn sẽ thử khôi phục trong container PostgreSQL cô lập.

**Điểm kiểm tra.** Lần theo một yêu cầu đến RDS, một cảnh báo sao lưu đến hộp thư người vận hành và một image phát hành từ GitHub đến Lightsail.

[Tiếp theo: Chuẩn bị Lightsail và RDS riêng tư](../5.4-deploy/)
