---
title: "Buildrathon Kickoff: Code the Future with CMC Global"
date: 2026-11-13
weight: 1
chapter: false
pre: " <b>4.1.</b> "
---

| Thông tin | Chi tiết |
|---|---|
| Ngày | Thứ Bảy, 26/09/2026 |
| Thời gian | 09:00-11:20 |
| Địa điểm | Bitexco Financial Tower, số 2 Hải Triều, TP. Hồ Chí Minh |
| Đơn vị tổ chức | CMC Global và cộng đồng First Cloud AI Journey |
| Vai trò | Người tham dự, đi cùng các bạn trong nhóm Ownword |

## Vì sao mình tham gia

Đây là sự kiện đầu tiên cả nhóm cùng đi. Lúc đó mình mới học xong hai tuần lab AWS, nên mình muốn xem những người có kinh nghiệm hơn bắt tay xây dựng một sản phẩm thật trên AWS như thế nào, đồng thời làm quen với các bạn thực tập khác trước khi thử thách Buildrathon bắt đầu.

{{< event-photo file="cmc.jpg" alt="Ảnh nhóm cạnh bảng tên CMC Global và First Cloud AI Journey" caption="Nhóm mình tại buổi khởi động Buildrathon ở Bitexco Financial Tower." >}}

## Chương trình buổi sáng

Chương trình ngắn và thiên về thực hành. Mở đầu là mục tiêu của thử thách và phần giới thiệu tổng quan về AWS, AI tạo sinh và cách xây dựng AI agent bằng các dịch vụ AWS. Sau phần làm quen là tọa đàm với người trong ngành, phần hỏi đáp và cuối cùng là thử thách thực hành 30 phút có mentor hỗ trợ ngay tại chỗ.

## Điều mình rút ra

### Mười lăm phút làm quen thay đổi cách cả nhóm làm việc

Phần làm quen chỉ kéo dài mười lăm phút nhưng lại giúp phần còn lại của buổi sáng diễn ra suôn sẻ. Khi bắt đầu thực hành, nhóm đã biết ai quen viết prompt, ai thích đọc tài liệu và ai muốn đứng ra trình bày. Trong 30 phút không có thời gian để bàn chia việc, nên hiểu điểm mạnh của nhau từ trước giúp cả nhóm không làm trùng một việc.

### Xây agent chủ yếu là quyết định nó không được làm gì

Trong phần thực hành, mentor giới thiệu các thành phần của một giải pháp AI trên AWS: thiết kế prompt, tạo sinh tăng cường truy xuất (RAG), kho tri thức và agent. Điều làm mình bất ngờ là phần lớn công việc nằm ở việc đặt giới hạn. Một agent hẹp, làm tốt một việc sẽ dễ kiểm thử và dễ giải thích hơn một trợ lý làm đủ thứ. Mình cũng nhận ra phải nắm chắc các kiến thức nền trong worklog (quyền IAM, log, chi phí) trước khi dám cấp cho agent quyền truy cập vào bất cứ thứ gì.

### Cứ hỏi câu mình ngại hỏi

Ở phần hỏi đáp, nhiều bạn hỏi những câu rất cơ bản về chứng chỉ và nên bắt đầu học AWS từ đâu. Với mình đây là phần hữu ích nhất, vì câu trả lời biến một danh sách dài các dịch vụ thành thứ tự học rõ ràng: học các dịch vụ cốt lõi, thực hành qua lab, rồi tự xây một sản phẩm hoàn chỉnh. Lộ trình này khá giống con đường mình đi trong worklog, kết thúc bằng việc triển khai Ownword.

### Nghe người trong nghề kể giúp con đường nghề nghiệp rõ hơn

Phần tọa đàm nói về cách các tổ chức dùng AWS và agentic AI trong dự án thật. Nghe mọi người kể công việc hằng ngày làm nghề cloud bớt trừu tượng với mình. Mình cũng được nhắc rằng giải thích thiết kế cho người không chuyên là một phần của công việc chứ không phải việc phụ.

## Liên hệ với Ownword

Ownword dùng AI ở nhiều chỗ: tìm từ theo ý nghĩa bằng Amazon Bedrock, góp ý bài viết, làm giàu từ vựng và chấm bài luyện tập qua OpenRouter. Sau sự kiện này mình chú ý hơn đến giới hạn của các tính năng đó. Key của model chỉ nằm trên server, gợi ý được kiểm tra trước khi đến tay người học, và mỗi tính năng chỉ làm một việc được định nghĩa rõ. Nếu sau này thêm tính năng AI, mình sẽ viết ra trước những điều tính năng đó tuyệt đối không được làm, rồi kiểm thử các trường hợp đó đầu tiên.

## Tài liệu tham khảo

- [Lịch của ban tổ chức (Luma)](https://luma.com/8fe9vvps)
- [Amazon Bedrock là gì?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
