---
title: "Week 4: Databases with Amazon RDS and simple hosting with Amazon Lightsail"
date: 2026-11-13
weight: 4
chapter: false
pre: " <b>1.4.</b> "
---

05/10-11/10/2026

## Week 4 objectives

- Run a managed relational database in a private subnet.
- Learn Amazon Lightsail, the hosting option we later chose for Ownword.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn about Amazon RDS: engines, Multi-AZ, backups<br>- **Practice:**<br>&emsp;+ Create a VPC and Security Groups<br>&emsp;+ Create a DB subnet group | 05/10/2026 | 05/10/2026 | [RDS Introduction](https://000005.awsfcaj.com/1-introduce/)<br>[Prerequisite steps](https://000005.awsfcaj.com/2-prerequiste/) |
| 3 | - **Practice:**<br>&emsp;+ Create an RDS database instance<br>&emsp;+ Launch an EC2 instance and deploy the sample app<br>&emsp;+ Connect the app to RDS | 06/10/2026 | 06/10/2026 | [Create RDS instance](https://000005.awsfcaj.com/3-create-rds/)<br>[Application deployment](https://000005.awsfcaj.com/5-deploy-app/) |
| 4 | - **Practice:**<br>&emsp;+ Take a snapshot and restore the database<br>&emsp;+ Clean up resources<br>- Note the RDS settings to reuse in the project (encryption, private subnet) | 07/10/2026 | 07/10/2026 | [Backup and restore](https://000005.awsfcaj.com/6-backup/) |
| 5 | - Learn about Amazon Lightsail<br>- **Practice:**<br>&emsp;+ Create a Lightsail database<br>&emsp;+ Deploy WordPress and attach a static IP | 08/10/2026 | 08/10/2026 | [Create a Lightsail database](https://000045.awsfcaj.com/1-create-database/)<br>[Deploy WordPress](https://000045.awsfcaj.com/2-wordpress-instance/) |
| 6 | - **Practice:**<br>&emsp;+ Secure the applications<br>&emsp;+ Create snapshots<br>&emsp;+ Migrate to a larger instance<br>&emsp;+ Create alarms<br>&emsp;+ Clean up resources | 09/10/2026 | 09/10/2026 | [Secure the applications](https://000045.awsfcaj.com/4-secure-the-applications/)<br>[Create snapshots](https://000045.awsfcaj.com/5-create-snapshots/)<br>[Create alarms](https://000045.awsfcaj.com/7-create-alarms/) |

## Week 4 achievements

- Created an RDS instance in a private subnet that only accepts connections from the application's Security Group.
- Deployed a sample application on EC2 that reads and writes to RDS, then practiced snapshot and restore.
- Learned how Lightsail bundles compute, storage, a static IP and networking at a fixed monthly price, which suits a small pilot like Ownword.
- Practiced Lightsail snapshots, scaling up to a larger instance and setting alarms.
