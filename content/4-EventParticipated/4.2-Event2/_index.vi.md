---
title: "AWS Cloud and AI Day Hanoi 2026"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>4.2.</b> "
---

| Thông tin | Chi tiết |
|---|---|
| Ngày | Thứ Ba, 29/09/2026 |
| Hội nghị chính | Khách sạn JW Marriott Hà Nội |
| Nơi mình tham dự | Điểm cầu TP. Hồ Chí Minh |
| Phiên mình theo dõi | DVT205, điểm cầu của phiên "Building software like never before with agentic AI" |
| Vai trò | Người tham dự |

## Tổng quan sự kiện

Sự kiện chính diễn ra ở Hà Nội với keynote buổi sáng và các phiên song song từ 11:00 về AI, dữ liệu và phân tích, di chuyển hệ thống và ứng dụng hiện đại. Lịch chương trình có các phiên như nền tảng phát triển nội bộ trên Amazon EKS của VPBank, đưa agentic AI từ demo vào triển khai cùng Katalon, xây dựng nền tảng dữ liệu sẵn sàng cho AI và di chuyển hệ thống quy mô lớn với AWS Transform. Nhóm mình theo dõi tại điểm cầu TP. Hồ Chí Minh, nơi phiên 11:00 nói về xây dựng phần mềm bằng agentic AI.

{{< event-photo file="cloud_day_1.jpg" alt="Ảnh nhóm tại điểm cầu với màn hình đang chiếu chương trình hội nghị" caption="Tại điểm cầu TP. Hồ Chí Minh." >}}

## Điều mình học được

### Cộng đồng đứng sau sự kiện

Một slide trong keynote làm mình nhớ hơn mọi thông báo sản phẩm. Slide ghi hơn 157.000 người đã được đào tạo về cloud và AI, hơn 54.000 thành viên AWS Study Group và hơn 15.000 người tham gia hệ sinh thái First Cloud AI Journey. Mình là một trong 15.000 người đó. Nhờ vậy mình thấy các bài lab và blog mình dùng mỗi tuần là một phần của cộng đồng lớn hơn nhiều, và đó cũng là lý do để chia sẻ lại những gì mình học được cho nhóm.

### Agent viết code, nhưng vẫn phải có người chịu trách nhiệm

Phiên tại điểm cầu nói về việc dùng AI agent xuyên suốt vòng đời phần mềm, không chỉ để gợi ý code mà còn để lên kế hoạch, sửa và kiểm thử những phần việc lớn hơn. Ý mình nghe nhắc lại nhiều lần trong ngày là khi agent có thể gọi API, sửa code hoặc kích hoạt triển khai, nó đặt ra những câu hỏi giống như khi có thành viên mới trong nhóm: dùng định danh nào, được phép làm gì, ai duyệt thay đổi và xem lại thao tác của nó ở đâu. Code được tạo nhanh hơn không có nghĩa là bỏ qua bước rà soát. Công sức chỉ chuyển từ viết code sang đọc và kiểm tra code.

### Tự động hóa càng nhiều càng cần rào chắn

Platform engineering được nhắc đến như nền móng cho AI chứ không phải một chủ đề riêng. Khi tự động hóa nhiều hơn, nhóm càng phải dựa vào mẫu triển khai dùng chung, cấu hình an toàn mặc định và kiểm tra chính sách, vì không còn ai xem thủ công từng thay đổi. Mình liên hệ điều này với các lab CI/CD đã học: một pipeline chỉ an toàn bằng những bước kiểm tra nó chạy trước khi đưa thay đổi lên production.

### Định danh không phải con người cũng là ranh giới bảo mật

Workload, pipeline, dịch vụ và AI agent đều gọi API của AWS và đều cần một định danh. Lời khuyên mình ghi lại là nên dùng thông tin xác thực ngắn hạn và federation thay cho key dài hạn, thiết kế trust policy cẩn thận và liên tục kiểm tra định danh nào đang thực sự được dùng. Đây chính là bài học trong lab tuần 3 về IAM role cho EC2, chỉ là ở quy mô lớn hơn nhiều.

## Liên hệ với Ownword

Ownword có nhiều định danh không phải con người: Lightsail host gọi Amazon Bedrock, job sao lưu ghi vào S3, Lambda Pre sign-up trong Cognito và GitHub Actions đẩy image lên ECR. Kiến trúc hiện tại đã tách riêng IAM policy cho quyền gọi Bedrock, quyền sao lưu lên S3 và quyền liên kết tài khoản, nên định danh này không thể âm thầm làm việc của định danh khác. Sau sự kiện này, mình muốn đi thêm một bước: thay mọi access key dài hạn còn sót lại bằng thông tin xác thực tạm thời, và ghi rõ với mỗi định danh ai chịu trách nhiệm và nó được phép làm gì.


## Tài liệu tham khảo

- [Tổng quan hội nghị](https://aws.amazon.com/events/cloud-day-hanoi/)
- [Lịch chương trình](https://aws.amazon.com/events/cloud-day-hanoi/agenda/)
- [Bài tổng kết trên AWS Builder Center](https://builder.aws.com/content/3KMpKxUhRFeSlclpmwu5ZxBQBYL/aws-cloud-and-ai-day-hanoi-2026-building-for-the-next-phase-of-cloud-and-ai)
- [Thông tin xác thực tạm thời trong IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
