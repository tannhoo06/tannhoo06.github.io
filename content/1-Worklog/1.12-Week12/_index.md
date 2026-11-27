---
title: "Week 12: Ownword: backups, monitoring, verification and the report"
date: 2026-11-13
weight: 12
chapter: false
pre: " <b>1.12.</b> "
---

30/11-06/12/2026

## Week 12 objectives

- Back up the database to S3 and alert when backups go stale.
- Verify the deployment, estimate monthly cost and finish the internship report.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Give the backup role read access to RDS<br>- Create the private S3 backup bucket, the access-log bucket and a dedicated backup identity | 30/11/2026 | 30/11/2026 | [Workshop 5.6 steps 1–2](../../5-workshop/5.6-operations/) |
| 3 | - Verify the S3 copy<br>- Restore the export into an isolated PostgreSQL container | 01/12/2026 | 01/12/2026 | [Workshop 5.6 step 3](../../5-workshop/5.6-operations/) |
| 4 | - Publish the hourly `BackupFresh` metric<br>- Create the CloudWatch alarm and an SNS topic encrypted with KMS<br>- Verify that the alarm email arrives | 02/12/2026 | 02/12/2026 | [Workshop 5.6 steps 4–5](../../5-workshop/5.6-operations/) |
| 5 | - Run the acceptance checks:<br>&emsp;+ Valid request saved to the database<br>&emsp;+ CloudWatch Logs<br>&emsp;+ Invalid request rejected<br>- Build the monthly cost estimate in AWS Pricing Calculator | 03/12/2026 | 03/12/2026 | [Workshop 5.7 Verification](../../5-workshop/5.7-verification/) |
| 6 | - Clean up lab resources and verify with the AWS CLI<br>- Complete the internship report: worklog, events, self-evaluation and feedback | 04/12/2026 | 04/12/2026 | [Workshop 5.7 Clean up](../../5-workshop/5.7-verification/) |

## Week 12 achievements

- Set up daily PostgreSQL exports to an encrypted private S3 bucket and tested restoring them into an isolated database.
- Configured a `BackupFresh` CloudWatch alarm that emails the operator through an SNS topic encrypted with KMS.
- Passed the acceptance checks for valid requests, logging and invalid requests, and estimated the monthly cost of the pilot.
- Cleaned up all lab resources and completed my bilingual internship report.
