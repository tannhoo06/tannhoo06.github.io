---
title: "Savings Plans Hay Reserved Instances? Cam Kết Đúng Thì Tiết Kiệm, Cam Kết Sai Thì Trả Tiền Cho Không Khí 💸"
menuTitle: "Savings Plans và Reserved Instances"
weight: 1
chapter: false
pre: " <b>3.1.</b> "
---

| Thông tin bài đăng | Nội dung |
| --- | --- |
| Ngày đăng | 17/11/2026 |
| Liên kết bài đăng | [Bài viết gốc trên Facebook](https://www.facebook.com/share/p/1FKqLSySXL/) |
| Chủ đề bài đăng | Các mô hình cam kết giá của AWS: Savings Plans, Reserved Instances và Database Savings Plans |

{{< figure src="/images/blogs/blog1.png" alt="Ảnh bìa: Savings Plans hay Reserved Instances?" caption="Hình 3.1. Ảnh bìa dùng trong bài đăng Facebook." >}}

Sau khi học xong phần EC2 và RDS, mình bắt đầu tò mò: các công ty chạy server 24/7 trên AWS thì có phải trả giá On-Demand mãi không? Câu trả lời là không. AWS có các mô hình "cam kết sử dụng" để đổi lấy mức giá thấp hơn, và hai cái tên mình gặp nhiều nhất là Savings Plans và Reserved Instances (RI). Lúc đầu mình nghĩ hai cái này na ná nhau. Nhưng khi làm workshop Savings Plans trên First Cloud Journey và đọc thêm tài liệu AWS, mình nhận ra điểm khác nhau nằm ở chỗ **mình đang cam kết cái gì**.

## Cam kết "cấu hình" hay cam kết "số tiền mỗi giờ"?

- **Reserved Instances:** cam kết dùng một cấu hình cụ thể (instance type, Region…) trong 1 hoặc 3 năm. Standard RI giảm sâu hơn, còn Convertible RI đổi được sang cấu hình khác. Với RDS thì có Reserved DB Instances.
- **Savings Plans:** cam kết một mức chi tiêu cố định tính theo $/giờ trong 1 hoặc 3 năm. Phần sử dụng nằm trong mức cam kết được tính giá giảm, phần vượt quá tính giá On-Demand như bình thường. AWS tự áp mức giảm cho phần sử dụng phù hợp mỗi giờ, mình không cần chỉ định trước từng instance.

## 4 loại Savings Plans hiện có

| Loại | Mức giảm tối đa | Phạm vi áp dụng |
| --- | --- | --- |
| Compute Savings Plans | Tới 66% | Linh hoạt nhất: EC2 bất kể family, size, Region, OS, và cả Fargate, Lambda |
| EC2 Instance Savings Plans | Tới 72% | Khóa vào một instance family trong một Region, vẫn đổi được size, OS, tenancy |
| SageMaker AI Savings Plans | Tùy workload | Workload Machine Learning trên SageMaker |
| Database Savings Plans | Tới 35% | Aurora, RDS, DynamoDB, ElastiCache, DocumentDB, Neptune…, từ tháng 3/2026 có thêm OpenSearch Service và Neptune Analytics |

Database Savings Plans, ra mắt ngày 2/12/2025, là phần mình thấy đáng chú ý nhất: đổi engine, đổi instance family hay chuyển Region vẫn giữ được mức giảm. Nhưng nó có giới hạn cần nhớ: chỉ có kỳ hạn 1 năm và chỉ No Upfront. Mức 35% là cho serverless, còn instance provisioned chỉ giảm tới khoảng 20%. Nên nếu database rất ổn định và chấp nhận cam kết 3 năm, Reserved DB Instances có thể vẫn giảm sâu hơn.

## Khi nào chọn cái nào?

- **Kiến trúc còn thay đổi** (đang chuyển từ EC2 sang container, sang Lambda, hoặc chưa chắc Region): Compute Savings Plans. Mất khoảng 6% so với mức giảm tối đa nhưng không sợ "kẹt".
- **Workload EC2 rất ổn định**, biết chắc instance family và Region: EC2 Instance Savings Plans hoặc Standard RI.
- **Cần giữ chỗ capacity ở một AZ cụ thể:** Zonal RI hoặc On-Demand Capacity Reservation, vì Savings Plans chỉ giảm giá, không giữ capacity.
- **Database đang hiện đại hóa** (ví dụ RDS for Oracle sang Aurora PostgreSQL, hoặc sang serverless): Database Savings Plans.

## 3 bài học trước khi bấm "Purchase"

1. **Right-size trước, cam kết sau.** Nếu instance đang thừa 50% CPU mà mình cam kết 3 năm, thì mình đang "khóa" luôn phần lãng phí đó.
2. **Chỉ cam kết phần nền (baseline).** Lấy mức sử dụng ổn định 24/7 làm mức cam kết, phần lên xuống theo giờ cao điểm để On-Demand hoặc Spot. Cam kết dư thì phần không dùng vẫn bị tính tiền.
3. **Đọc Savings Plans Recommendations trong Cost Explorer.** AWS gợi ý mức cam kết dựa trên lịch sử sử dụng.

Một lưu ý cho các bạn đang học như mình: đừng mua Savings Plans hay RI trên tài khoản lab. Đây là cam kết tài chính dài hạn. Mục tiêu của mình là hiểu cơ chế để sau này đề xuất đúng cho hệ thống thật.

## Lời kết

Tối ưu chi phí trên AWS không chỉ là tắt tài nguyên không dùng. Khi hệ thống đã ổn định, chọn đúng mô hình cam kết có thể giảm vài chục phần trăm hóa đơn mà không cần sửa một dòng code. Quan trọng là hiểu mình đang đánh đổi sự linh hoạt lấy bao nhiêu phần trăm giảm giá.

## Nguồn tham khảo

- [AWS: Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
- [AWS: Savings Plans FAQs](https://aws.amazon.com/savingsplans/faqs)
- [AWS What's New: Announcing Database Savings Plans (12/2025)](https://aws.amazon.com/about-aws/whats-new/2025/12/database-savings-plans-savings)
- [AWS News Blog: Introducing Database Savings Plans](https://aws.amazon.com/blogs/aws/introducing-database-savings-plans-for-aws-databases)
- [AWS What's New: Database Savings Plans for OpenSearch Service and Neptune Analytics (3/2026)](https://aws.amazon.com/about-aws/whats-new/2026/03/dbsp-opensearch-service-neptune-analytics)

## Thực hành trên First Cloud Journey

- [Savings Plans & Reserved Instances](https://000042.awsfcaj.com)
- [EC2 Right-sizing](https://000032.awsfcaj.com)
- [Cost and Usage Management](https://000064.awsfcaj.com)
- [AWS Budgets](https://000007.awsfcaj.com)
