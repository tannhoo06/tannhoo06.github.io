---
title: "Week 8: Security and reliability: KMS, Secrets Manager, SNS/SQS and AWS Backup"
date: 2026-11-13
weight: 8
chapter: false
pre: " <b>1.8.</b> "
---

02/11-08/11/2026

## Week 8 objectives

- Encrypt data at rest and manage secrets safely.
- Send notifications with SNS and SQS.
- Back up resources and test restores.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn about AWS KMS and customer-managed keys<br>- **Practice:**<br>&emsp;+ Create a policy, role, group and user<br>&emsp;+ Create a KMS key<br>&emsp;+ Upload encrypted data to S3 | 02/11/2026 | 02/11/2026 | [Create KMS](https://000033.awsfcaj.com/3-create-kms/)<br>[Create Amazon S3](https://000033.awsfcaj.com/4-create-s3/) |
| 3 | - **Practice:**<br>&emsp;+ Log key usage with CloudTrail<br>&emsp;+ Query CloudTrail logs with Athena<br>&emsp;+ Test and share encrypted data | 03/11/2026 | 03/11/2026 | [CloudTrail and Athena](https://000033.awsfcaj.com/5-create-cloudtrail/)<br>[Test encrypted data](https://000033.awsfcaj.com/6-demo/) |
| 4 | - Learn about AWS Secrets Manager<br>- **Practice:**<br>&emsp;+ Store RDS credentials in Secrets Manager<br>&emsp;+ Read the secret from a Fargate task | 04/11/2026 | 04/11/2026 | [Using on RDS](https://000096.awsfcaj.com/3-rds-phase/)<br>[Using on Fargate](https://000096.awsfcaj.com/4-fargate-phase/) |
| 5 | - Learn about SNS topics and SQS queues<br>- **Practice:**<br>&emsp;+ Subscribe an email and test fan-out<br>&emsp;+ Use message filtering and advanced filter policies | 05/11/2026 | 05/11/2026 | [Simple Pub/Sub & Fan-Out](https://000077.awsfcaj.com/3-simplesubpub/)<br>[Message Filtering](https://000077.awsfcaj.com/4-messagefiltering/) |
| 6 | - Learn about AWS Backup<br>- **Practice:**<br>&emsp;+ Create a backup plan<br>&emsp;+ Set up notifications<br>&emsp;+ Test a restore<br>&emsp;+ Clean up resources | 06/11/2026 | 06/11/2026 | [Create Backup plan](https://000013.awsfcaj.com/3-createbackupplan/)<br>[Test Restore](https://000013.awsfcaj.com/5-testrestore/) |

## Week 8 achievements

- Created a customer-managed KMS key, encrypted data in S3 and checked key usage with CloudTrail and Athena.
- Stored database credentials in Secrets Manager instead of in code.
- Built SNS topics with email subscriptions, SQS fan-out and filter policies.
- Learned that a backup only counts once a restore has been tested. Ownword applies the same idea with a separate restore test.
