---
title: "Chia sẻ và góp ý"
date: 2026-11-13
weight: 7
chapter: false
pre: " <b>7.</b> "
---

## Môi trường thực tập

Trước kỳ thực tập, AWS với mình chủ yếu chỉ là một danh sách tên dịch vụ. Điều thay đổi suy nghĩ đó là được học cùng cộng đồng thay vì học một mình. Trong AWS Study Group và cộng đồng First Cloud AI Journey, lúc nào cũng có người từng gặp đúng lỗi mình đang gặp, còn các bài lab trên Cloud Journey cho mình một lộ trình rõ ràng theo từng tuần. Trong Gi Group, mọi người cập nhật tiến độ thường xuyên, so sánh ghi chép khi làm lab và cùng nhau đi sự kiện. Vì cả nhóm cùng hướng tới một sản phẩm chung, việc đặt câu hỏi rất dễ dàng, bởi phần việc của ai cũng gắn vào cùng một hệ thống.

## Sự hỗ trợ từ mentor và các anh chị quản trị

Mentor và các anh chị quản trị rất kiên nhẫn với những câu hỏi cơ bản, và thường chỉ cho mình đúng bài lab hoặc tài liệu cần đọc thay vì đưa ngay đáp án. Nhờ vậy mình phải tự đọc tài liệu và hiểu vì sao cần làm từng bước. Các sự kiện được tổ chức, từ buổi khởi động Buildrathon đến buổi trò chuyện với Tiến sĩ Werner Vogels, là cơ hội để nghe những người đang vận hành hệ thống thật chia sẻ, điều mà sinh viên khó có được ở nơi khác.

## Quá trình học qua dự án Ownword

Ownword cho mình thấy các dịch vụ đã học khớp với nhau như thế nào. Trong lab, mỗi dịch vụ đứng riêng lẻ. Trong Ownword, CloudFront, WAF, Lightsail, RDS, Cognito, Lambda, S3, CloudWatch và SNS phải chạy cùng nhau như một hệ thống, và một lỗi ở chỗ này có thể lộ ra ở chỗ khác.

Lỗi mình nhớ nhất là thông báo `AccessDenied` khi kiểm thử sao lưu database. Bước export chạy bình thường trên Lightsail host, nhưng bước tải lên S3 thì thất bại. Mình chắc chắn định danh sao lưu đã có quyền S3 vì policy có ghi tên bucket. Phải một lúc sau mình mới nhận ra policy chỉ cho phép `s3:PutObject` trên ARN của bucket, trong khi thao tác tải lên cần quyền trên các object bên trong (`bucket/*`). Sửa lại ARN xong thì tải lên thành công, mà định danh đó vẫn không làm được gì ngoài việc ghi bản sao lưu. Từ đó mình đọc lỗi IAM kỹ hơn nhiều: thông báo lỗi ghi rõ hành động và tài nguyên nào bị từ chối, và câu trả lời thường nằm ngay ở đó. Lỗi này cũng cho mình thấy vì sao nguyên tắc quyền tối thiểu cần sự kiên nhẫn. Nếu cấp luôn toàn quyền S3 thì lỗi chỉ bị che đi chứ không được sửa.

## Ý nghĩa với định hướng nghề nghiệp

Kỳ thực tập giúp mình chắc chắn hơn về việc theo đuổi nghề cloud engineering. Giờ mình đã có kinh nghiệm thực tế triển khai và vận hành một ứng dụng thật trên AWS, không chỉ làm các bài lab riêng lẻ. Mục tiêu tiếp theo của mình là lấy một chứng chỉ AWS và tiếp tục tự làm các dự án nhỏ, tự lo từ hạ tầng đến giám sát và chi phí.

## Một góp ý nhỏ

Các bài lab rất tốt để học từng dịch vụ một. Mình đề xuất cứ vài tuần có thêm một bài lab ngắn kiểu "ghép các mảnh lại", kết hợp những dịch vụ của các bài trước thành một ứng dụng nhỏ, ví dụ ứng dụng chạy trên Lightsail, dùng RDS private và sao lưu lên S3. Như vậy thực tập sinh sẽ được tập xử lý lỗi xuyên nhiều dịch vụ sớm hơn, trước khi vào dự án cuối kỳ. Mỗi bài lab cũng nên có một ghi chú ngắn về chi phí dự kiến và những tài nguyên cần xóa trước, để người mới tránh bị tính phí ngoài ý muốn.
