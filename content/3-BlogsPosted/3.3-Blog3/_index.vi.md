---
title: "Web Tĩnh Trên S3: Public Bucket Hay CloudFront + OAC? 🌐"
menuTitle: "Web tĩnh trên S3 và CloudFront + OAC"
weight: 3
chapter: false
pre: " <b>3.3.</b> "
---

| Thông tin bài đăng | Nội dung |
| --- | --- |
| Ngày đăng | 19/11/2026 |
| Liên kết bài đăng | [Bài viết gốc trên Facebook](https://www.facebook.com/share/p/1exGpxarnX/) |
| Chủ đề bài đăng | Host website tĩnh trên Amazon S3 an toàn với CloudFront và Origin Access Control |

{{< figure src="/images/blogs/blog3.png" alt="Ảnh bìa: Web tĩnh trên S3, public bucket hay CloudFront + OAC?" caption="Hình 3.3. Ảnh bìa dùng trong bài đăng Facebook." >}}

Một trong những bài lab đầu tiên mình làm là host website tĩnh trên Amazon S3. Upload `index.html`, bật Static website hosting, bấm vào link… và website chạy thật! Cảm giác rất "wow" 😄 Nhưng khi đọc kỹ các bước, mình thấy để chạy được, mình đã phải tắt Block Public Access và cho cả thế giới đọc bucket. Workshop S3 trên First Cloud Journey cũng không dừng ở đó: phần sau hướng dẫn chặn toàn bộ public access lại và đưa CloudFront lên phía trước. Bài này mình so sánh hai cách và ghi lại những lỗi mình gặp.

## Cách A: S3 static website endpoint và bucket public

Các bước: tạo bucket, upload file, bật Static website hosting, tắt Block Public Access, thêm bucket policy cho phép `s3:GetObject` với Principal `"*"`.

- **Ưu điểm:** nhanh, dễ, rất hợp để học S3.
- **Nhược điểm:** website endpoint chỉ có HTTP, không có HTTPS; bucket public nên ai cũng đọc thẳng được; không có cache gần người dùng.

## Cách B: CloudFront và Origin Access Control (OAC)

Ý tưởng: bucket giữ private hoàn toàn, người dùng chỉ vào qua CloudFront. CloudFront ký mỗi request tới S3 bằng SigV4, và bucket policy chỉ chấp nhận request từ đúng distribution đó.

1. Bật lại **Block all public access** cho bucket.
2. Tạo CloudFront distribution, origin chọn S3 bucket (**REST endpoint**), không phải website endpoint.
3. Ở Origin access, chọn **Origin access control settings (recommended)**, tạo OAC, giữ Signing behavior là **Sign requests**.
4. Cập nhật bucket policy: Principal là `cloudfront.amazonaws.com`, kèm điều kiện `AWS:SourceArn` bằng ARN của distribution. Console có nút copy policy sẵn.
5. Đặt **Default root object** là `index.html`.

## OAC khác gì OAI?

Khi tìm hiểu mình gặp cả hai khái niệm. OAI (Origin Access Identity) là cách cũ, nay AWS xếp vào "legacy". OAC ra mắt năm 2022 và là cách AWS khuyến nghị vì:

- dùng chữ ký SigV4, hỗ trợ tất cả Region của S3,
- hỗ trợ bucket mã hóa SSE-KMS (OAI thì không),
- hỗ trợ nhiều HTTP method hơn.

Nếu project cũ còn dùng OAI, AWS có hướng dẫn chuyển sang OAC.

## Những lỗi mình đã gặp

- **403 Access Denied ngay sau khi tạo distribution:** do mình quên dán bucket policy, hoặc dán nhầm ARN distribution.
- **Chọn nhầm website endpoint làm origin:** OAC không dùng được với S3 website endpoint, vì endpoint đó coi như là custom origin public. Phải chọn REST endpoint của bucket.
- **Truy cập `/about/` bị lỗi:** Default root object chỉ áp dụng cho đường dẫn gốc `/`, không tự thêm `index.html` cho thư mục con như website endpoint. Cách xử lý là thêm một CloudFront Function để viết lại URL.
- **Sửa file mà web không đổi:** do CloudFront đang cache. Tạo Invalidation (ví dụ `/*`) hoặc đặt tên file có version.

## Vậy nên chọn cách nào?

- **Học, demo nhanh trong nội bộ:** Cách A vẫn ổn, miễn là nhớ dọn dẹp.
- **Website cho người dùng thật:** Cách B. Có HTTPS, gắn được domain riêng với ACM, cache ở edge, gắn thêm AWS WAF được, và bucket không bao giờ phải public.
- Một điểm thú vị: trang workshop FCJ có ghi chú rằng AWS hiện khuyến nghị **AWS Amplify Hosting** cho website tĩnh. Amplify làm sẵn phần CloudFront, S3 và CI/CD, còn bài lab S3 thì giúp mình hiểu "bên dưới" Amplify đang làm gì.

## Lời kết

Cùng một kết quả "website chạy được", nhưng hai cách khác nhau rất nhiều về bảo mật. Bài học lớn nhất mình rút ra là: đừng để bucket public chỉ vì đó là cách nhanh nhất để thấy kết quả. Giữ S3 private và để CloudFront làm "cửa chính" là thói quen nên có ngay từ đầu.

## Nguồn tham khảo

- [Amazon CloudFront: Restrict access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [AWS re:Post Knowledge Center: Configure OAC and migrate from OAI](https://repost.aws/knowledge-center/cloudfront-oac-origins)
- [AWS DevOps Blog: CDK L2 construct for CloudFront OAC](https://aws.amazon.com/blogs/devops/a-new-aws-cdk-l2-construct-for-amazon-cloudfront-origin-access-control-oac)

## Thực hành trên First Cloud Journey

- [S3 Static Website + CloudFront](https://000057.awsfcaj.com)
- [CloudFront with an S3 origin](https://000094.awsfcaj.com)
- [CloudFront & Lambda@Edge](https://000130.awsfcaj.com)
- [AWS WAF](https://000026.awsfcaj.com)
