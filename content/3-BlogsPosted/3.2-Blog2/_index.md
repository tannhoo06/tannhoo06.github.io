---
title: "Close Port 22! Accessing EC2 in a Private Subnet with Session Manager"
menuTitle: "Session Manager instead of SSH"
weight: 2
chapter: false
pre: " <b>3.2.</b> "
---

| Publication detail | Information |
| --- | --- |
| Publication date | 18 November 2026 |
| Publication link | [Original Vietnamese post on Facebook](https://www.facebook.com/share/p/1CmPTgzM4j/) |
| Publication topic | Secure access to EC2 with AWS Systems Manager Session Manager, without SSH keys, open ports or a bastion host |

{{< figure src="/images/blogs/blog2.png" alt="Cover image: Close port 22!" caption="Figure 3.2. Cover image used in the Facebook post." >}}

When I first learned EC2, I connected the "traditional" way: create a key pair, download the `.pem` file, open port 22 in the Security Group (honestly, with source `0.0.0.0/0` to save time), then `ssh -i key.pem ec2-user@...`. When I moved on to VPC and put an instance in a private subnet, I got stuck: no public IP, no Internet access, so how do I get in? The usual answer is a bastion host in a public subnet. That works, but after the Session Manager workshop on First Cloud Journey I found a cleaner and safer way.

## The problems with SSH and a bastion host

- Port 22 has to be open to the outside, where bots scan constantly.
- `.pem` files have to be created, shared and revoked for every team member. Someone who leaves and keeps a key is a risk.
- The bastion is one more server to patch, monitor and pay for.
- Knowing who logged in and what they typed requires setting up logging yourself.

## How Session Manager solves them

Session Manager is a capability of AWS Systems Manager. Instead of you connecting into the instance, the SSM Agent on the instance connects out to Systems Manager over HTTPS (443). When you start a session from the console or the CLI, your commands travel over that channel. As a result:

- **No inbound rules** in the Security Group. Ports 22 and 3389 stay closed.
- **No SSH keys.** Access is controlled by IAM, for example who may call `ssm:StartSession` on which instance.
- **No bastion host.**
- **Built-in auditing.** API calls are recorded in CloudTrail, and session content can be sent to S3 or CloudWatch Logs.

## What you need (following FCJ workshop 000058)

1. **SSM Agent on the instance.** AWS-provided Amazon Linux and Windows AMIs usually have it installed.
2. **An IAM role for EC2** with the managed policy `AmazonSSMManagedInstanceCore`, which grants the minimum permissions Session Manager needs.
3. **A network path to the `ssm`, `ssmmessages` and `ec2messages` endpoints over HTTPS 443.**
   - An instance in a public subnet can reach them through the Internet Gateway.
   - An instance in a private subnet without NAT needs VPC interface endpoints for all three services, and the VPC must have **DNS hostnames and DNS resolution** enabled. I forgot this at first, and my instance never showed up in Fleet Manager 😅
4. **(Optional) Session logs in S3.** Allow the IAM role to write to the bucket and create an S3 gateway endpoint so a private instance can upload logs without Internet access.

The workshop also covers **port forwarding**: opening a tunnel from your machine to a port on the instance, for example RDP 3389 on a private Windows server, still without any inbound rule.

## A few more things I noticed

- Interface endpoints are billed per hour in each AZ and per GB of data. Delete them when you clean up a lab. For a real system they are often still cheaper than running a NAT Gateway and a bastion just for administration.
- According to the AWS documentation, newer SSM Agent versions use `ssmmessages`, and in Regions launched from 2024 `ec2messages` is no longer used for this. The workshop still creates all three endpoints so it works in every Region.
- Session Manager doesn't replace access control. Limit who can open sessions to which instances (with tags and IAM conditions) instead of giving the whole team `ssm:*`.

## Takeaway

What I learned isn't just "one more way into a server". It's a change in mindset: don't open a port unless you need it, and let IAM manage identity instead of key files scattered across everyone's laptops. Now, whenever I'm about to add a port 22 rule to a Security Group, I ask myself whether I really need it.

## References

- [AWS Systems Manager: Session Manager prerequisites](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-prerequisites.html)
- [AWS: Using AWS PrivateLink (VPC endpoints) for Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started-privatelink.html)
- [AWS Cloud Operations Blog: Session Manager without an Internet Gateway](https://aws.amazon.com/blogs/mt/automated-configuration-of-session-manager-without-an-internet-gateway)

## Hands-on labs on First Cloud Journey

- [Session Manager](https://000058.awsfcaj.com)
- [Systems Manager](https://000031.awsfcaj.com)
- [IAM Role for EC2](https://000048.awsfcaj.com)
- [VPC](https://000003.awsfcaj.com)
