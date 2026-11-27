---
title: "Savings Plans or Reserved Instances? Commit Right and Save, Commit Wrong and Pay for Nothing"
menuTitle: "Savings Plans vs Reserved Instances"
weight: 1
chapter: false
pre: " <b>3.1.</b> "
---

| Publication detail | Information |
| --- | --- |
| Publication date | 17 November 2026 |
| Publication link | [Original Vietnamese post on Facebook](https://www.facebook.com/share/p/1FKqLSySXL/) |
| Publication topic | AWS commitment pricing models: Savings Plans, Reserved Instances and the new Database Savings Plans |

{{< figure src="/images/blogs/blog1.png" alt="Cover image: Savings Plans or Reserved Instances?" caption="Figure 3.1. Cover image used in the Facebook post." >}}

After finishing EC2 and RDS, I wondered whether companies that run servers 24/7 keep paying On-Demand prices forever. They don't. AWS offers commitment models that trade a usage commitment for a lower price, and the two names I kept seeing were Savings Plans and Reserved Instances (RI). At first they looked the same to me. After the Savings Plans workshop on First Cloud Journey and some AWS documentation, I realized the real difference is **what you commit to**.

## Committing to a configuration or to an hourly spend

- **Reserved Instances** commit you to a specific configuration (instance type, Region and so on) for one or three years. Standard RIs give a deeper discount, while Convertible RIs let you exchange for a different configuration. RDS has its own Reserved DB Instances.
- **Savings Plans** commit you to a fixed spend in dollars per hour for one or three years. Usage within the commitment gets the discounted rate, and anything above it is billed On-Demand. AWS applies the discount to matching usage every hour, so you don't have to pick instances in advance.

## The four types of Savings Plans

| Type | Maximum discount | What it covers |
| --- | --- | --- |
| Compute Savings Plans | Up to 66% | The most flexible. Any EC2 family, size, Region or OS, plus Fargate and Lambda |
| EC2 Instance Savings Plans | Up to 72% | One instance family in one Region. Size, OS and tenancy can still change |
| SageMaker AI Savings Plans | Varies | Machine learning workloads on SageMaker |
| Database Savings Plans | Up to 35% | Aurora, RDS, DynamoDB, ElastiCache, DocumentDB, Neptune and more, with OpenSearch Service and Neptune Analytics added in March 2026 |

Database Savings Plans, launched on 2 December 2025, were the part I found most interesting. You keep the discount even if you change engine, instance family or Region. They do have limits: only a one-year term with No Upfront payment, and the 35% applies to serverless, while provisioned instances get around 20%. For a very stable database where a three-year commitment is acceptable, Reserved DB Instances can still be cheaper.

## Which one to choose

- **The architecture is still changing** (moving from EC2 to containers or Lambda, or the Region isn't decided yet): Compute Savings Plans. You give up about 6% compared with the maximum discount, but you can't get stuck.
- **A very stable EC2 workload** with a known instance family and Region: EC2 Instance Savings Plans or Standard RIs.
- **You need reserved capacity in a specific Availability Zone**: a zonal RI or an On-Demand Capacity Reservation, because Savings Plans only lower the price and don't reserve capacity.
- **A database that is being modernized** (for example RDS for Oracle to Aurora PostgreSQL, or moving to serverless): Database Savings Plans.

## Three lessons before clicking "Purchase"

1. **Right-size first, commit later.** If an instance is 50% idle and you commit for three years, you lock in that waste too.
2. **Commit only to the baseline.** Use the steady 24/7 usage as your commitment and cover peaks with On-Demand or Spot. Any commitment you don't use is still billed.
3. **Read the Savings Plans recommendations in Cost Explorer.** AWS suggests a commitment level based on your usage history.

One note for fellow learners: don't buy Savings Plans or RIs on a lab account. They are long-term financial commitments. The goal is to understand how they work so you can recommend the right option for a real system later.

## Takeaway

Cost optimization on AWS is more than switching off unused resources. Once a system is stable, the right commitment model can cut the bill by tens of percent without changing a line of code. The key is knowing how much flexibility you are trading for each percentage point of discount.

## References

- [AWS: Savings Plans types](https://docs.aws.amazon.com/savingsplans/latest/userguide/plan-types.html)
- [AWS: Savings Plans FAQs](https://aws.amazon.com/savingsplans/faqs)
- [AWS What's New: Announcing Database Savings Plans (12/2025)](https://aws.amazon.com/about-aws/whats-new/2025/12/database-savings-plans-savings)
- [AWS News Blog: Introducing Database Savings Plans](https://aws.amazon.com/blogs/aws/introducing-database-savings-plans-for-aws-databases)
- [AWS What's New: Database Savings Plans for OpenSearch Service and Neptune Analytics (3/2026)](https://aws.amazon.com/about-aws/whats-new/2026/03/dbsp-opensearch-service-neptune-analytics)

## Hands-on labs on First Cloud Journey

- [Savings Plans & Reserved Instances](https://000042.awsfcaj.com)
- [EC2 Right-sizing](https://000032.awsfcaj.com)
- [Cost and Usage Management](https://000064.awsfcaj.com)
- [AWS Budgets](https://000007.awsfcaj.com)
