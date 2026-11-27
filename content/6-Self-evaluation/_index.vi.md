---
title: "Tự đánh giá"
date: 2026-11-13
weight: 6
chapter: false
pre: " <b>6.</b> "
---

Từ 14/09 đến 14/12/2026, mình tham gia kỳ thực tập First Cloud AI Journey với tư cách thành viên Gi Group. Tám tuần đầu mình xây nền tảng AWS qua các bài lab trên Cloud Journey, từ IAM, VPC đến RDS, Lightsail, CloudFront, Cognito và sao lưu. Bốn tuần cuối mình áp dụng những gì đã học vào Ownword, ứng dụng học từ vựng và luyện viết tiếng Anh của nhóm. Mình tự triển khai lại toàn bộ hệ thống trên tài khoản lab của mình, tham gia kiểm thử luồng đăng nhập, sao lưu và giám sát, đồng thời viết phần của mình trong báo cáo song ngữ này.

## Bảng tự đánh giá

| STT | Tiêu chí | Nội dung tự đánh giá | Tốt | Khá | Trung bình |
| ---: | --- | --- | :---: | :---: | :---: |
| 1 | Khối lượng công việc | Mức độ công việc trong nhóm tôi đảm nhận và hoàn thành | ⬜ | ✅ | ⬜ |
| 2 | Mức độ đóng góp | Phần việc tôi làm giúp cải thiện gì cho Ownword hoặc cho nhóm | ✅ | ⬜ | ⬜ |
| 3 | Tính chủ động | Tôi có nhận ra thiếu sót, đề xuất thay đổi hoặc chủ động hỗ trợ không | ⬜ | ✅ | ⬜ |
| 4 | Làm việc nhóm | Tôi có cập nhật tiến độ, lắng nghe và hỗ trợ các thành viên khi cần không | ✅ | ⬜ | ⬜ |
| 5 | Hiệu quả học tập | Cách tôi xử lý khi gặp vướng mắc và thời điểm hỏi hỗ trợ | ⬜ | ✅ | ⬜ |
| 6 | Tiếp thu góp ý | Cách tôi tiếp nhận góp ý để cải thiện công việc | ✅ | ⬜ | ⬜ |
| 7 | Nắm vững nền tảng AWS | Tôi có giải thích được các dịch vụ AWS đã học và khi nào nên dùng không | ✅ | ⬜ | ⬜ |
| 8 | Ứng dụng AWS vào Ownword | Mức độ phù hợp của các dịch vụ tôi tham gia cấu hình với nhu cầu dự án | ✅ | ⬜ | ⬜ |
| 9 | Đảm bảo tiến độ | Tôi có hoàn thành đúng hạn và báo sớm khi có nguy cơ trễ không | ✅ | ⬜ | ⬜ |
| 10 | Xác định ưu tiên | Tôi có tập trung vào việc nhóm cần nhất không | ⬜ | ✅ | ⬜ |
| 11 | Tính đều đặn | Mức độ duy trì tiến độ và cập nhật nhật ký công việc | ✅ | ⬜ | ⬜ |
| 12 | Chất lượng công việc | Mức độ tự kiểm tra trước khi bàn giao và lượng việc phải sửa lại | ✅ | ⬜ | ⬜ |

Mình chấm **Tốt** ở tám tiêu chí có bằng chứng rõ ràng. Mình giải thích được các dịch vụ AWS đã học và khi nào nên dùng, những phần của Ownword mình kiểm thử đều chạy đúng, worklog được cập nhật đều mỗi tuần, và mình hoàn thành việc đúng hạn, tự kiểm tra trước khi bàn giao. Bốn tiêu chí còn lại mình chấm **Khá** vì biết mình vẫn còn dư địa để tiến bộ. Nhóm trưởng là người gánh phần lớn công việc và các quyết định kiến trúc, mình lẽ ra có thể chủ động đề xuất thay đổi nhiều hơn thay vì chờ được giao, và đôi khi mình mất quá nhiều thời gian cho một vấn đề trước khi hỏi người khác hoặc xác định việc nào quan trọng hơn.

## Phần đóng góp của tôi trong dự án Ownword

- **Triển khai lại toàn bộ hệ thống.** Mình làm theo bài workshop trên tài khoản AWS của mình: Lightsail host, RDS PostgreSQL private kết nối qua VPC peering, đăng nhập Cognito với Google, và CloudFront kèm AWS WAF đứng trước ứng dụng. Mỗi khi một bước chưa rõ hoặc bị lỗi, mình ghi lại chuyện gì đã xảy ra và cách xử lý, để hướng dẫn được kiểm chứng trên một tài khoản mới hoàn toàn.
- **Kiểm thử đăng nhập, sao lưu và giám sát.** Mình thử đăng nhập bằng email, mật khẩu và bằng Google, kể cả trường hợp tài khoản đã có liên kết với Google mà vẫn giữ được WordBoard. Mình cũng kiểm tra bản export hằng ngày đã lên S3, khôi phục thử vào một container PostgreSQL tách biệt và xác nhận alarm `BackupFresh` gửi được email qua SNS.
- **Kiểm chứng, chi phí và tài liệu.** Mình chạy các bước kiểm chứng cho request hợp lệ, request không hợp lệ và CloudWatch Logs, cùng xem lại bảng ước tính chi phí hằng tháng và đảm bảo tài nguyên lab được dọn sạch. Mình cũng tự viết worklog, bài viết sự kiện và phần chia sẻ trong báo cáo này bằng cả tiếng Anh và tiếng Việt.

## Những điểm cần cải thiện

- **Hỏi sớm hơn.** Khi bị kẹt, chẳng hạn với lỗi `AccessDenied` lúc đẩy bản sao lưu lên S3, mình thường tự thử quá lâu. Lần sau mình sẽ đặt giới hạn thời gian, ghi lại những gì đã thử rồi mới hỏi đồng đội hoặc mentor với đầy đủ thông tin đó.
- **Hiểu cả code ứng dụng, không chỉ hạ tầng.** Giờ mình đã quen với AWS console và CLI, nhưng còn hiểu chưa nhiều về cách ứng dụng Next.js quản lý phiên đăng nhập và gọi Bedrock. Mình muốn tự đọc và thử phần code đó để có thể lần theo một lỗi từ trình duyệt xuống tận cơ sở dữ liệu.
- **Ghi chép ngay khi làm.** Một số mục worklog mình viết lại sau khi làm xong. Mình muốn ghi lệnh, lỗi và ảnh chụp ngay trong lúc làm để báo cáo chính xác hơn và đỡ mất thời gian vào cuối kỳ.
