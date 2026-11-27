---
title: "Tuần 12: Ownword: sao lưu, giám sát, kiểm chứng và viết báo cáo"
date: 2026-11-13
weight: 12
chapter: false
pre: " <b>1.12.</b> "
---

30/11-06/12/2026

## Mục tiêu tuần 12

- Sao lưu database lên S3 và cảnh báo khi bản sao lưu bị cũ.
- Kiểm chứng hệ thống, ước tính chi phí hằng tháng và hoàn thiện báo cáo thực tập.

## Công việc trong tuần

| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Tài liệu tham khảo |
| --- | --- | --- | --- | --- |
| 2 | - Cấp quyền đọc RDS cho role backup<br>- Tạo S3 bucket private cho bản sao lưu, bucket lưu access log và một định danh riêng cho việc sao lưu | 30/11/2026 | 30/11/2026 | [Workshop 5.6 bước 1–2](../../5-workshop/5.6-operations/) |
| 3 | - Kiểm tra bản sao trên S3<br>- Khôi phục bản export vào một container PostgreSQL tách biệt | 01/12/2026 | 01/12/2026 | [Workshop 5.6 bước 3](../../5-workshop/5.6-operations/) |
| 4 | - Gửi metric `BackupFresh` mỗi giờ<br>- Tạo CloudWatch alarm và SNS topic được mã hóa bằng KMS<br>- Kiểm tra email cảnh báo có đến | 02/12/2026 | 02/12/2026 | [Workshop 5.6 bước 4–5](../../5-workshop/5.6-operations/) |
| 5 | - Chạy các bước kiểm chứng:<br>&emsp;+ Request hợp lệ được lưu vào database<br>&emsp;+ Kiểm tra CloudWatch Logs<br>&emsp;+ Request không hợp lệ bị từ chối<br>- Ước tính chi phí hằng tháng bằng AWS Pricing Calculator | 03/12/2026 | 03/12/2026 | [Workshop 5.7 Kiểm chứng](../../5-workshop/5.7-verification/) |
| 6 | - Dọn dẹp tài nguyên lab và kiểm tra lại bằng AWS CLI<br>- Hoàn thiện báo cáo thực tập: nhật ký, sự kiện, tự đánh giá và góp ý | 04/12/2026 | 04/12/2026 | [Workshop 5.7 Dọn dẹp](../../5-workshop/5.7-verification/) |

## Kết quả đạt được tuần 12

- Thiết lập export PostgreSQL hằng ngày lên S3 bucket private có mã hóa và thử khôi phục thành công vào database tách biệt.
- Cấu hình CloudWatch alarm `BackupFresh` gửi email cho người vận hành qua SNS topic được mã hóa bằng KMS.
- Vượt qua các bước kiểm chứng cho request hợp lệ, ghi log và request không hợp lệ, đồng thời ước tính chi phí hằng tháng cho bản pilot.
- Dọn dẹp toàn bộ tài nguyên lab và hoàn thiện báo cáo thực tập song ngữ.
