---
title: "Tuần 6: Lớp biên và giám sát: CloudFront, AWS WAF và CloudWatch"
date: 2026-11-13
weight: 6
chapter: false
pre: " <b>1.6.</b> "
---

19/10-25/10/2026

## Mục tiêu tuần 6

- Đặt CDN và tường lửa ứng dụng web trước ứng dụng.
- Giám sát tài nguyên bằng metric, log, alarm và dashboard.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu Amazon CloudFront: distribution, origin, cache<br>- **Thực hành:**<br>&emsp;+ Tạo S3 origin và tải lên index.html<br>&emsp;+ Cấu hình CloudFront distribution | 19/10/2026 | 19/10/2026 | [Tạo S3 bucket](https://000094.awsfcaj.com/1.1-t%E1%BA%A1o-nh%C3%B3m-s3/)<br>[Cấu hình CloudFront](https://000094.awsfcaj.com/1.3-c%E1%BA%A5u-h%C3%ACnh-amazon-cloudfront/) |
| 3 | - Tìm hiểu AWS WAF<br>- **Thực hành:**<br>&emsp;+ Triển khai ứng dụng web mẫu<br>&emsp;+ Tạo web ACL với managed rule | 20/10/2026 | 20/10/2026 | [Giới thiệu WAF](https://000026.awsfcaj.com/1-introduction/)<br>[Web ACL với managed rule](https://000026.awsfcaj.com/3-useawswaf/3.1-createswebacl/) |
| 4 | - **Thực hành:**<br>&emsp;+ Viết custom rule và advanced custom rule<br>&emsp;+ Kiểm tra rule mới<br>&emsp;+ Bật ghi log request<br>&emsp;+ Dọn dẹp tài nguyên | 21/10/2026 | 21/10/2026 | [Custom Rule](https://000026.awsfcaj.com/3-useawswaf/3.2-createcustomrule/)<br>[Ghi log request](https://000026.awsfcaj.com/3-useawswaf/3.5-logging/) |
| 5 | - Tìm hiểu CloudWatch metric<br>- **Thực hành:**<br>&emsp;+ Xem metric<br>&emsp;+ Dùng search expression và math expression<br>&emsp;+ Dùng log group, Logs Insights và metric filter | 22/10/2026 | 22/10/2026 | [CloudWatch Metrics](https://000008.awsfcaj.com/3-cloud-watch-metric/)<br>[CloudWatch Logs](https://000008.awsfcaj.com/4-cloud-watch-logs/) |
| 6 | - **Thực hành:**<br>&emsp;+ Tạo CloudWatch alarm<br>&emsp;+ Tạo CloudWatch dashboard<br>&emsp;+ Dọn dẹp tài nguyên | 23/10/2026 | 23/10/2026 | [CloudWatch Alarms](https://000008.awsfcaj.com/5-cloud-watch-alarm/)<br>[CloudWatch Dashboards](https://000008.awsfcaj.com/6-cloud-watch-dashboard/) |

## Kết quả đạt được tuần 6

- Cấu hình được CloudFront distribution và hiểu cách cache, origin ảnh hưởng đến request.
- Bảo vệ ứng dụng bằng web ACL của AWS WAF với managed rule, custom rule và ghi log request.
- Dùng CloudWatch metric, Logs Insights và metric filter để theo dõi hoạt động của ứng dụng.
- Tạo được alarm và dashboard. Sau này Ownword dùng đúng cách này: một CloudWatch alarm trên metric backup tự định nghĩa.
