---
title: "Week 2: Networking with Amazon VPC and compute with Amazon EC2"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>1.2.</b> "
---

21/09-27/09/2026

## Week 2 objectives

- Understand the core building blocks of an Amazon VPC.
- Launch, connect to and manage Amazon EC2 instances.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn VPC concepts:<br>&emsp;+ Subnets<br>&emsp;+ Route tables<br>&emsp;+ Internet Gateway and NAT Gateway<br>- Learn Security Groups and Network ACLs | 21/09/2026 | 21/09/2026 | [VPC Introduction](https://000003.awsfcaj.com/1-introduce/)<br>[Firewall in VPC](https://000003.awsfcaj.com/2-firewallinvpc/) |
| 3 | - **Practice:**<br>&emsp;+ Create a VPC, public and private subnets<br>&emsp;+ Create an Internet Gateway and route tables<br>&emsp;+ Create a Security Group<br>&emsp;+ Enable VPC Flow Logs | 22/09/2026 | 22/09/2026 | [Preparation Steps](https://000003.awsfcaj.com/3-prerequisite/) |
| 4 | - **Practice:**<br>&emsp;+ Launch EC2 instances in the public and private subnets<br>&emsp;+ Test connectivity and create a NAT Gateway<br>&emsp;+ Use Reachability Analyzer<br>&emsp;+ Connect with Session Manager | 23/09/2026 | 23/09/2026 | [Deploying EC2 Instances](https://000003.awsfcaj.com/4-createec2server/)<br>[Session Manager](https://000003.awsfcaj.com/4-createec2server/4.6-sessionmanager/) |
| 5 | - Learn basic EC2:<br>&emsp;+ Instance types<br>&emsp;+ AMI<br>&emsp;+ EBS<br>- **Practice:**<br>&emsp;+ Launch an Amazon Linux instance and connect via SSH | 24/09/2026 | 24/09/2026 | [EC2 Introduction](https://000004.awsfcaj.com/1-introduce/)<br>[Launch Amazon Linux Instance](https://000004.awsfcaj.com/4-launchlinuxinstance/) |
| 6 | - **Practice:**<br>&emsp;+ Change the instance type<br>&emsp;+ Create EBS snapshots and a custom AMI<br>&emsp;+ Launch an instance from the custom AMI<br>&emsp;+ Restrict EC2 usage by Region and instance type with IAM<br>&emsp;+ Clean up resources | 25/09/2026 | 25/09/2026 | [Amazon EC2 Basic](https://000004.awsfcaj.com/5-amazonec2basic/)<br>[Cost & Usage Governance with IAM](https://000004.awsfcaj.com/8-costusagegovernance/) |

## Week 2 achievements

- Understood how subnets, route tables, the Internet Gateway and the NAT Gateway work together in a VPC.
- Can tell when to use a Security Group (stateful, per instance) and when to use a Network ACL (stateless, per subnet).
- Built a VPC with public and private subnets and checked connectivity with Reachability Analyzer.
- Launched and connected to EC2 instances with SSH and Session Manager. Connecting through Session Manager needs no open port 22.
- Created EBS snapshots and a custom AMI, and used IAM conditions to limit which Regions and instance types can be used.
