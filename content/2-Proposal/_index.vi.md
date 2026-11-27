---
title: "Đề xuất"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>2.</b> "
---

## Tóm tắt dự án

Ownword dành cho người học tiếng Anh nhận ra nhiều từ khi đọc nhưng khó nhớ để dùng khi viết. Ứng dụng giúp người học tìm từ mình đang cần, lưu lại và luyện đến khi tự nhớ ra được. Phần Viết giúp người học xác định đoạn nào trong bản nháp cần sửa và xem bản chỉnh sửa đã xử lý góp ý đến đâu.

Bản thử nghiệm chạy trên AWS. Amazon Bedrock dùng Kimi K3.1 Pro để tra từ theo khái niệm, còn OpenRouter cung cấp mô hình cho việc đánh giá bản nháp và kiểm tra bản chỉnh sửa. Người đọc có thể [xem video demo](https://youtu.be/VEdfxhcqqCk), [dùng thử ứng dụng đang chạy](https://app.ownword.co/) hoặc tự triển khai theo [workshop song ngữ](../5-workshop/).

Khi hoàn tất báo cáo (30/11/2026), nhóm vẫn đang chờ AWS Support xử lý quyền truy cập mô hình. Các yêu cầu gọi GPT-6 Luna trên Amazon Bedrock từ tài khoản AWS Free Tier vẫn trả về `AccessDeniedException` dù nhóm đã chấp nhận thỏa thuận sử dụng mô hình. Nhóm tiếp tục dùng OpenRouter để truy cập GPT-6 Luna phục vụ đánh giá. Sau nhiều đợt thử nghiệm chấm bản nháp và kiểm tra bản chỉnh sửa, nhóm chọn GPT-6.1 Terra với mức suy luận thấp qua OpenRouter cho tính năng Viết đang vận hành vì mô hình cân bằng tốt nhất giữa chất lượng phản hồi và chi phí với khối lượng sử dụng của Ownword. Với phần làm giàu từ vựng và chấm luyện tập, nhóm chọn Gemini 3.6 Flash qua OpenRouter vì mô hình giải nghĩa và chấm câu ổn định với chi phí thấp, trong khi Gemini 3.6 Flash không có trong danh mục mô hình của Amazon Bedrock.

## Vấn đề

Có những từ mình nhận ra ngay khi đọc, nhưng đến lúc viết lại dùng một từ quen thuộc hơn. Tra được một từ phù hợp giúp mình viết tiếp ngay lúc đó, nhưng lần sau có thể vẫn phải tra lại. Khi sửa bài cũng có chuyện tương tự. Mình có thể thấy một câu chưa ổn mà chưa rõ cần sửa phần nào.

Ownword bắt đầu từ bản nháp hoặc ý người học muốn diễn đạt. Ứng dụng nối lúc tìm được từ với những buổi luyện sau đó. Phản hồi về bài viết chỉ ra những đoạn cụ thể mà người học có thể xem lại khi sửa.

## Đối tượng và vòng lặp học tập

Bản thử nghiệm dành cho người học tiếng Anh nâng cao muốn tự học. Luồng từ vựng đi qua sáu bước: viết, khám phá, chọn, luyện tập, truy hồi và vận dụng. Trên WordBoard, từ đã lưu chuyển qua **New**, **Practicing** và **Active** khi người học nhớ lại và sử dụng từ ở nhiều thời điểm, trong nhiều ngữ cảnh.

Ví dụ, nếu muốn diễn tả một trải nghiệm vừa vui vừa buồn, người học có thể mô tả cảm giác đó bằng tiếng Anh hoặc tiếng Việt, xem gợi ý như *bittersweet* rồi lưu vào WordBoard. Khi ôn nhanh, người học có thể đánh dấu nếu quên từ. Trong Full Practice, họ thử nhớ lại và đặt câu về một chủ đề tự chọn.

Phần Viết có luồng riêng. Người học chọn đề, viết bài, đọc phản hồi theo từng đoạn rồi tự chỉnh sửa. Bản gốc được giữ lại để người học đối chiếu chỗ đã đổi và xem bản sửa đáp ứng góp ý nào.

## Phạm vi bản thử nghiệm

| Tính năng | Bản thử nghiệm hỗ trợ gì |
| --- | --- |
| Khám phá từ vựng | Tìm gợi ý từ bản nháp hoặc mô tả một khái niệm bằng tiếng Anh hay tiếng Việt. Lưu từ phù hợp hoặc thêm từ thủ công. |
| WordBoard và luyện tập | Theo dõi từ đã lưu, nghe phát âm qua trình duyệt, ôn các từ đã quên rồi luyện nhớ và đặt câu. Chuỗi ngày học ghi lại các ngày có hoạt động. |
| Viết | Viết theo đề, đọc phản hồi gắn với đoạn cụ thể và mở lại bản gốc cùng bản chỉnh sửa trong lịch sử. |
| Tài khoản | Đăng nhập bằng email và mật khẩu hoặc Google. Tài khoản đủ điều kiện có thể liên kết Google đã xác minh để giữ lại WordBoard. |

Bản thử nghiệm chạy ứng dụng trên một VM và dùng cơ sở dữ liệu Single-AZ riêng tư. Mục tiêu là thử luồng học và khả năng khôi phục với một nhóm nhỏ.

## Kiến trúc đã triển khai

{{< ownword-architecture alt="Luồng yêu cầu và sao lưu của Ownword. GitHub Actions đẩy image phát hành lên ECR riêng tư tại Singapore để Lightsail tải về." caption="Kiến trúc Ownword và luồng tự động phát hành ngày 24/11/2026. Chọn sơ đồ để xem ở kích thước đầy đủ." >}}

### Các dịch vụ AWS đang dùng

- **Amazon CloudFront.** Cung cấp điểm truy cập HTTPS công khai của Ownword và chuyển yêu cầu web, API tới Caddy trên Lightsail. Callback của Cognito dùng tên miền công khai của ứng dụng.
- **AWS WAF.** Áp dụng web ACL cho yêu cầu đi qua distribution CloudFront trước khi chúng đến máy chủ gốc.
- **AWS Certificate Manager (ACM).** Cấp chứng chỉ cho tên miền công khai trên CloudFront. Caddy quản lý chứng chỉ riêng cho kết nối tới máy chủ gốc.
- **Amazon Lightsail.** Chạy VM tại Singapore. Caddy nhận HTTPS từ CloudFront rồi chuyển yêu cầu tới Next.js qua mạng Docker riêng. VM cũng chạy tác vụ sao lưu và kiểm tra tình trạng bản sao.
- **Amazon RDS for PostgreSQL.** Lưu hồ sơ người học, từ trên WordBoard, kết quả luyện tập và lịch sử bài viết. Cơ sở dữ liệu Single-AZ được mã hóa, nằm trong subnet riêng tại Singapore (`ap-southeast-1a`) và chỉ nhận kết nối qua cổng 5432 từ máy Lightsail qua VPC peering. Ứng dụng kiểm tra chứng chỉ và tên máy chủ của RDS.
- **Amazon Cognito.** Quản lý mật khẩu, xác minh email và đăng nhập Google qua user pool tại Singapore. Next.js ánh xạ danh tính Cognito đã xác minh vào hồ sơ người học trong PostgreSQL.
- **AWS Lambda.** Chạy trigger Pre sign-up tại Singapore cho đăng nhập Google. Nếu lần đăng nhập đầu tiên khớp với một tài khoản đủ điều kiện, trigger có thể liên kết danh tính Google để giữ nguyên WordBoard của người học.
- **Amazon Bedrock.** Chạy Kimi K3.1 Pro cho tra cứu theo khái niệm qua inference profile tại Mỹ. Ứng dụng gọi endpoint ở Bắc Virginia và kiểm tra cấu trúc gợi ý trước khi trả về.
- **Amazon S3.** Lưu bản xuất PostgreSQL hằng ngày trong một bucket riêng tư và ghi nhật ký truy cập vào bucket riêng. Cả hai bucket dùng SSE-S3. Bản sao nằm ngoài VM và cơ sở dữ liệu đang chạy, nên nhóm có thể dùng để thử khôi phục vào một cơ sở dữ liệu riêng.
- **Amazon ECR.** Lưu image phát hành riêng tư do GitHub Actions tạo. Lightsail tải image theo digest và kiểm tra ứng dụng sau khi triển khai. [Luồng phát hành](../5-workshop/5.3-architecture/)
- **Amazon CloudWatch.** Nhận metric `BackupFresh` mỗi giờ. Alarm dựa vào giá trị đó để đánh giá bản sao mới nhất còn đủ mới và có mặt trên S3 hay không.
- **Amazon SNS.** Gửi email cho người vận hành khi CloudWatch chuyển sang trạng thái cảnh báo.
- **AWS Key Management Service (KMS).** Cung cấp khóa do nhóm quản lý để mã hóa SNS topic dùng cho cảnh báo sao lưu.
- **AWS Identity and Access Management (IAM).** Giới hạn quyền gọi Bedrock, truy cập bản sao S3, ghi metric CloudWatch và chạy Lambda liên kết tài khoản. PostgreSQL dùng role riêng cho ứng dụng và tác vụ sao lưu.

## Triển khai kỹ thuật

### Đường đi của yêu cầu và dữ liệu

1. Mở ứng dụng (bước 1-4): Trình duyệt kết nối HTTPS tới CloudFront. CloudFront kết nối TLS tới Caddy qua tên miền máy chủ gốc. Caddy chuyển yêu cầu tới Next.js. Ứng dụng đọc hoặc ghi dữ liệu người học trên RDS riêng tư qua một kết nối TLS khác.
2. Đăng nhập (bước 5-8): Yêu cầu đăng nhập bằng mật khẩu đi tới Cognito. Với Google, Cognito xử lý liên kết danh tính rồi đưa trình duyệt về callback của Ownword. Next.js đổi mã ủy quyền bằng PKCE. Lambda có thể liên kết danh tính Google ở lần đăng nhập đầu tiên đủ điều kiện.
3. Gọi mô hình (bước 9-10): Next.js gửi yêu cầu tra theo khái niệm tới Kimi trên Bedrock. Đánh giá bài viết, làm giàu từ vựng và chấm luyện tập dùng các tuyến OpenRouter riêng. Thông tin xác thực của nhà cung cấp nằm trên máy chủ.
4. Sao lưu và cảnh báo (bước 11-14): VM đọc RDS bằng role chỉ đọc, xuất cơ sở dữ liệu lên S3 riêng tư rồi kiểm tra bản sao mới nhất mỗi giờ. Nếu bản sao quá cũ hoặc thiếu tín hiệu, hệ thống gửi email qua SNS topic có mã hóa.

Workshop giải thích thêm [sơ đồ và đường đi của yêu cầu](../5-workshop/5.3-architecture/), [đăng nhập và HTTPS công khai](../5-workshop/5.5-auth/) và [cách sao lưu, khôi phục và thử cảnh báo](../5-workshop/5.6-operations/).

### Nhóm dùng Amazon Bedrock và OpenRouter như thế nào {#writing-inference-provider}

Ownword dùng Kimi K3.1 Pro trên Amazon Bedrock để tra từ theo khái niệm, một phần chính của tính năng khám phá từ vựng. Người học có thể diễn đạt ý mình muốn nói bằng tiếng Anh hoặc tiếng Việt để nhận gợi ý từ và cụm từ phù hợp. Khi người học lặp lại truy vấn, ứng dụng có thể dùng kết quả đã lưu để tránh gọi mô hình thêm một lần.

Tính năng Viết gửi bản nháp hoặc bản chỉnh sửa đến GPT-6.1 Terra Low qua OpenRouter và yêu cầu Zero Data Retention trên tuyến đã cấu hình. Phần làm giàu từ vựng và chấm luyện tập dùng Gemini 3.6 Flash qua OpenRouter vì phản hồi ngắn ổn định và chi phí thấp, còn dòng Gemini chưa có trên Bedrock. Ứng dụng kiểm tra cấu trúc phản hồi trước khi lưu. [Tình trạng truy cập mô hình](#tóm-tắt-dự-án)

## Tiến độ và các mốc

| Mốc | Việc đã làm |
| --- | --- |
| 14/09 đến 18/10 | Làm các bài AWS về tài khoản, IAM, mạng, cơ sở dữ liệu và giám sát. [Nhật ký](../1-worklog/) |
| 25/10 | Ghi nhận bản mẫu Ownword đầu tiên, có gợi ý từ bản nháp, WordBoard và luyện đặt câu. [Tuần 6](../1-worklog/1.6-week6/) |
| 28/10 | Thêm Quick Review và Full Practice để người học tập trung vào các từ đã quên. [Tuần 7](../1-worklog/1.7-week7/) |
| 05/11 | Thử khôi phục bản sao trên S3 và kiểm tra luồng cảnh báo CloudWatch, SNS trên Lightsail. [Tuần 8](../1-worklog/1.8-week8/) |
| 12/11 | Đưa màn hình tài khoản, đăng nhập Google và nút phát âm lên bản thử nghiệm. [Tuần 9](../1-worklog/1.9-week9/) |
| 20/11 | Chuyển cơ sở dữ liệu sang RDS riêng tư và phát hành tính năng chuỗi ngày học. |
| 30/11 | Chạy thử demo, ghi kết quả kiểm thử Workshop và hoàn thiện tài liệu bàn giao. |

## Dự toán và tối ưu chi phí {#dự-toán-chi-phí}

Với 10 người học hoạt động, chi phí vận hành dự toán là 43,56 USD/tháng trước thuế và tín dụng tài khoản, gồm 43,24 USD cho AWS và 0,32 USD tiền lượt gọi OpenRouter theo giá công bố. Với 100 người học và cùng cấu hình máy, dự toán tăng lên 60,98 USD/tháng.

| Chi phí hằng tháng (USD) | 10 người học | 100 người học |
| --- | ---: | ---: |
| Lightsail và RDS riêng tư | 33,01 | 33,01 |
| Phân phối, bảo mật, lưu trữ và giám sát | 8,69 | 9,33 |
| Tra theo khái niệm qua Bedrock | 1,54 | 15,40 |
| OpenRouter cho Viết, từ vựng và luyện tập | 0,32 | 3,24 |
| **Tổng** | **43,56** | **60,98** |

[Xem dự toán chi tiết trong Workshop](../5-workshop/5.7-verification/#2-lập-dự-toán-hằng-tháng) để đối chiếu thông số và kết quả AWS Pricing Calculator, giả định về lưu lượng, token và hạn mức áp dụng. Nhóm kiểm soát chi phí bằng cách dùng lại kết quả tra cứu, đặt giới hạn chi tiêu ở nhà cung cấp và giới hạn thời gian lưu bản sao cùng số image phát hành.

## Quyết định và rủi ro

| Rủi ro | Thiết kế xử lý thế nào và cần kiểm tra gì |
| --- | --- |
| VM ứng dụng ngừng chạy | RDS giữ dữ liệu ở ngoài máy chủ ứng dụng. Thử triển khai lại theo workshop và đo thời gian để đăng nhập và WordBoard hoạt động trở lại. |
| Mất cơ sở dữ liệu hoặc sao lưu quá cũ | Bản thử nghiệm dùng RDS Single-AZ. Lưu bản dump hằng ngày trên S3 riêng tư và kiểm tra `BackupFresh`. Khi thử khôi phục vào cơ sở dữ liệu cô lập, ghi lại bản sao được dùng và thời gian thực hiện. |
| Truy cập dữ liệu của người học khác | Cognito xác minh danh tính. Next.js giới hạn dữ liệu theo chủ tài khoản. Dùng tài khoản thứ hai thử mở URL chi tiết từ đã lưu của tài khoản thứ nhất. |
| Mô hình lỗi hoặc phản hồi chưa phù hợp | Kiểm tra cấu trúc phản hồi trước khi dùng. Thử tra một khái niệm mới và kiểm tra bản sửa với nội dung giả lập để nhận ra lỗi nhà cung cấp hoặc phản hồi chưa hữu ích. |
| Lượng truy cập hoặc chi phí tăng | Dùng lại kết quả cho truy vấn lặp và giới hạn lượt gọi mô hình. Theo dõi CPU, bộ nhớ, độ trễ và lỗi khi thử tải nhẹ trước khi quyết định tăng cấu hình VM. |

## Kết quả và kiểm chứng

Báo cáo có sơ đồ kiến trúc, ứng dụng đang chạy và hướng dẫn song ngữ để triển khai, dọn tài nguyên. Các lần kiểm tra trước đã ghi nhận đăng nhập Cognito, lưu từ và kết quả luyện tập, gọi mô hình thật và khôi phục bản sao RDS vào cơ sở dữ liệu tạm.

Trong buổi demo, người học cần tìm được một từ chưa quen, lưu rồi nhớ lại từ đó và dùng phản hồi để sửa bản nháp. Về phía AWS, nhóm cần tự làm lại bài lab với tài nguyên riêng, khôi phục dữ liệu và nhận cảnh báo khi bản sao quá cũ. Chương kiểm chứng trong Workshop ghi lại minh chứng gồm một yêu cầu hợp lệ và dòng dữ liệu đã lưu, log CloudWatch của luồng đăng nhập và phản hồi khi gửi dữ liệu sai định dạng. [Các bước kiểm chứng trong workshop](../5-workshop/5.7-verification/)
