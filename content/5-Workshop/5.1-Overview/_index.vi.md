---
title: "Tổng quan và luồng học từ"
date: 2026-11-20
weight: 1
chapter: false
pre: " <b>5.1.</b> "
---

## Bạn sẽ xây dựng gì

Khi bản Ownword của bạn chạy, hãy đăng nhập và thử dùng như một người học. Tra từ theo khái niệm qua Bedrock, lưu một gợi ý vào WordBoard rồi luyện nhớ lại. Bạn cũng có thể gửi một bài viết giả lập để xem phản hồi. WordBoard theo dõi từ ở các trạng thái New, Practicing và Active. Chuỗi ngày học ghi lại những ngày bạn có hoạt động.

Lưu ý về định tuyến mô hình: tính năng tra theo khái niệm dùng Kimi K3.1 Pro trên Amazon Bedrock. Mô-đun Viết dùng GPT-6.1 Terra mức suy luận thấp qua OpenRouter vì yêu cầu gọi GPT-6 Luna trên Bedrock trả về `AccessDeniedException` trên tài khoản AWS Free Tier ngay cả sau khi đã chấp nhận thỏa thuận mô hình. Phần làm giàu từ vựng và chấm luyện tập dùng Gemini 3.6 Flash qua OpenRouter vì chấm luyện tập ổn định và chi phí thấp, còn dòng Gemini chưa có trên Amazon Bedrock.

## Bạn sẽ thực hành gì

1. Tạo máy Lightsail và RDS PostgreSQL riêng tư tại Singapore. Kết nối qua Lightsail VPC peering và kiểm tra TLS của cơ sở dữ liệu.
2. Cấu hình Cognito tại Singapore, kiểm tra đăng nhập mật khẩu và liên kết Google. Đưa ứng dụng lên CloudFront HTTPS với WAF web ACL.
3. Dùng Bedrock qua Bắc Virginia để tra theo khái niệm và OpenRouter cho từ vựng và đánh giá bài viết.
4. Sao lưu RDS lên S3 riêng tư, khôi phục vào container tạm và kiểm tra CloudWatch gửi email qua SNS có mã hóa.
5. Kiểm tra ứng dụng, tính thử chi phí một tháng rồi dọn tài nguyên bạn đã tạo.

[Bắt đầu: Chuẩn bị môi trường lab](../5.2-prerequisites/)
