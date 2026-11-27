---
title: "Fireside Chat với Tiến sĩ Werner Vogels"
date: 2026-11-13
weight: 3
chapter: false
pre: " <b>4.3.</b> "
---

| Thông tin | Chi tiết |
|---|---|
| Chủ đề | Navigating the Future of Cloud & AI in Vietnam |
| Ngày | Thứ Sáu, 02/10/2026 |
| Địa điểm | TP. Hồ Chí Minh |
| Khách mời | Tiến sĩ Werner Vogels, Giám đốc Công nghệ của Amazon |
| Vai trò | Người tham dự |

## Tổng quan sự kiện

Tiến sĩ Werner Vogels đã dành hơn hai mươi năm xây dựng hạ tầng cho Amazon và AWS. Trong buổi trò chuyện tổ chức cho cộng đồng First Cloud AI Journey, ông chia sẻ bài học từ quãng thời gian đó và nói về việc làm lập trình viên khi AI đã có thể viết code. Mình đến với suy nghĩ sẽ nghe về công nghệ, nhưng ra về lại nghĩ nhiều nhất về thói quen làm việc: cách chọn công cụ, cách trình bày đánh đổi và cách tiếp tục học.

{{< event-photo file="fireside_1.jpg" alt="Slide mở đầu của First Cloud AI Journey ghi chủ đề và ngày 02/10/2026" caption="Slide mở đầu buổi Fireside Chat." >}}

## Điều mình học được

### Chọn công cụ theo khối lượng công việc thực tế

Tiến sĩ Vogels kể về một mùa mua sắm cao điểm khi cụm cơ sở dữ liệu quan hệ bị quá tải và làm hệ thống lưu dữ liệu khách hàng ngừng hoạt động cả một ngày. Khi các kỹ sư Amazon xem lại ứng dụng thực sự làm gì, khoảng 70% yêu cầu chỉ là tra cứu khóa-giá trị đơn giản, khoảng 20% chỉ dùng một bảng và chỉ khoảng 10% cần đầy đủ tính năng quan hệ. Điều mình rút ra không phải là "hãy tự viết cơ sở dữ liệu" mà là "đo trước rồi mới chọn". Rất dễ dùng một công cụ quen thuộc cho mọi việc. Tốt hơn là nhìn vào các yêu cầu thật trước đã.

### Mọi thứ đều có thể hỏng, nên hãy chuẩn bị trước

Một ý ông nhắc lại nhiều lần là mọi thứ đều có thể hỏng bất cứ lúc nào. Hệ thống cần được thiết kế để khi mất một thành phần, thậm chí cả một trung tâm dữ liệu, dịch vụ vẫn chạy. Amazon tổ chức các buổi GameDay, cố tình tắt hạ tầng để kiểm tra việc chuyển đổi dự phòng có diễn ra tự động hay không. Với một dự án sinh viên, điều này nghe có vẻ xa vời, nhưng nguyên tắc vẫn áp dụng được ở quy mô nhỏ: quyết định trước điều gì sẽ xảy ra khi từng phần bị lỗi và tập dượt thay vì chỉ hy vọng.

{{< event-photo file="fireside_2.jpg" alt="Tiến sĩ Werner Vogels trò chuyện cùng người dẫn chương trình" caption="Tiến sĩ Werner Vogels trong buổi trò chuyện." >}}

### Giải thích đánh đổi bằng ngôn ngữ dễ hiểu

Trong những phẩm chất của "Renaissance developer" mà ông nêu, phẩm chất mình cần nhất là giao tiếp. Ví dụ của ông là chênh lệch chi phí giữa uptime 99,9% và 99,99%. Thêm một số "9" không phải chi tiết kỹ thuật mà là một quyết định kinh doanh, và kỹ sư cần giải thích để người chi tiền có thể lựa chọn. Các phẩm chất còn lại là tò mò, tư duy hệ thống, tinh thần chịu trách nhiệm và chuyên môn hình chữ T: đi sâu vào một lĩnh vực nhưng hiểu đủ các phần lân cận như giao diện, logic nghiệp vụ và cơ sở dữ liệu.

### AI là trình biên dịch nhanh nhưng thiếu chính xác

Ông ví AI như một trình biên dịch dùng ngôn ngữ tự nhiên nhưng không chính xác. AI đã rút ngắn thời gian làm prototype từ vài tuần xuống vài giờ, nhưng kết quả vẫn phải được kiểm tra về bảo mật, trường hợp biên và hiệu năng. Kỹ sư vẫn chịu trách nhiệm cho những gì đưa lên production. Ông kết thúc bằng lời cảnh báo của Grace Hopper rằng tư duy "trước giờ vẫn làm vậy" rất nguy hiểm. Với mình, điều đó có nghĩa là không nên né tránh công cụ AI nhưng cũng không được tin nó một cách mù quáng.

## Liên hệ với Ownword

Ownword chạy trên một VM Lightsail và một cơ sở dữ liệu RDS Single-AZ. Đó là đánh đổi có chủ đích cho bản pilot nhỏ: chi phí thấp hơn đổi lại ít dự phòng hơn. Sau buổi nói chuyện, mình giải thích lựa chọn này rõ ràng hơn. Nếu database gặp sự cố, nhóm dựa vào bản export hằng ngày lên S3 đã thực sự được khôi phục thử ở môi trường tách biệt, và alarm `BackupFresh` sẽ báo nếu bản sao lưu bị thiếu. Nếu bản pilot mở rộng, chuyển sang Multi-AZ chính là số "9" mà nhóm sẽ cân nhắc cùng chi phí hằng tháng của nó. Mình cũng muốn tiếp tục rà soát từng dòng code có AI hỗ trợ, đặc biệt ở phần đăng nhập và truy cập cơ sở dữ liệu.

{{< event-photo file="fireside_3.jpg" alt="Ảnh nhóm cùng các bạn tham dự tại sự kiện First Cloud AI Journey" caption="Cùng các bạn trong nhóm sau buổi Fireside Chat." >}}

## Tài liệu tham khảo

- [Bài tổng kết buổi Fireside Chat trên AWS Builder Center](https://builder.aws.com/content/3KBSLeKsdkk6uMUPq7d9Xxa5jbS/the-invariable-lessons-of-tech-and-humanity-key-takeaways-from-amazon-cto-werner-vogels)
- [Bài báo Dynamo của Amazon](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
- [Trụ cột Reliability trong AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
