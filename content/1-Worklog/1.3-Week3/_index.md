---
title: "Week 3: IAM roles for EC2, AWS CLI and Amazon S3"
date: 2026-11-13
weight: 3
chapter: false
pre: " <b>1.3.</b> "
---

28/09-04/10/2026

## Week 3 objectives

- Let applications call AWS services without hard-coded access keys.
- Manage AWS resources from the command line.
- Store and serve files with Amazon S3.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - **Practice:**<br>&emsp;+ Access S3 from EC2 with an IAM user access key<br>&emsp;+ Replace the access key with an IAM role attached to EC2<br>- Compare the two approaches | 28/09/2026 | 28/09/2026 | [Use access key](https://000048.awsfcaj.com/2-accesskey/)<br>[IAM role on EC2](https://000048.awsfcaj.com/3-iamroleec2/) |
| 3 | - Install and configure AWS CLI<br>&emsp;+ Access Key, Secret Key, default Region<br>- **Practice:**<br>&emsp;+ Check resources via CLI<br>&emsp;+ Work with S3, SNS and IAM via CLI | 29/09/2026 | 29/09/2026 | [Install AWS CLI](https://000011.awsfcaj.com/3-installcli/)<br>[AWS CLI with Amazon S3](https://000011.awsfcaj.com/5-s3/)<br>[AWS CLI with IAM](https://000011.awsfcaj.com/7-iam/) |
| 4 | - **Practice:**<br>&emsp;+ Create a VPC, subnet, Internet Gateway and route table via CLI<br>&emsp;+ Launch an EC2 instance via CLI<br>&emsp;+ Troubleshoot common CLI errors | 30/09/2026 | 30/09/2026 | [AWS CLI with Networking](https://000011.awsfcaj.com/8-network/)<br>[Create EC2 using AWS CLI](https://000011.awsfcaj.com/9-ec2/) |
| 5 | - Learn about Amazon S3: buckets, objects, storage classes<br>- **Practice:**<br>&emsp;+ Create a bucket and enable static website hosting<br>&emsp;+ Configure Block Public Access and public objects | 01/10/2026 | 01/10/2026 | [S3 Introduction](https://000057.awsfcaj.com/1-introduce/)<br>[Enable static website](https://000057.awsfcaj.com/3-staticwebsite/) |
| 6 | - **Practice:**<br>&emsp;+ Block all public access and serve the site through CloudFront<br>&emsp;+ Enable bucket versioning<br>&emsp;+ Replicate objects to another Region<br>- Read S3 notes and best practices | 02/10/2026 | 02/10/2026 | [Accelerate with CloudFront](https://000057.awsfcaj.com/7-cloudfront/)<br>[Bucket Versioning](https://000057.awsfcaj.com/8-versioning/)<br>[Notes & Best Practices](https://000057.awsfcaj.com/12-notes/) |

## Week 3 achievements

- Understood why an IAM role is safer than an access key stored on a server: the credentials are temporary and rotate automatically.
- Installed and configured AWS CLI, then used it to check resources and to create a VPC, a subnet and an EC2 instance.
- Hosted a static website on S3, then made the bucket private and served it through CloudFront.
- Used versioning and cross-Region replication to protect data in S3.
