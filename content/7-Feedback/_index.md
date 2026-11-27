---
title: "Sharing and feedback"
date: 2026-11-13
weight: 7
chapter: false
pre: " <b>7.</b> "
---

## The environment

Before this internship, AWS was mostly a list of service names to me. What changed that was learning in a community instead of alone. The AWS Study Group and the First Cloud AI Journey community always had someone who had hit the same error before, and the labs on Cloud Journey gave me a clear path to follow week by week. Within Gi Group, we shared progress regularly, compared notes on labs, and went to events together. Working toward one shared product made it easy to ask questions, because everyone's work fit into the same system.

## Support from my mentor and the admins

The mentors and admins were patient with beginner questions and quick to point me to the right lab or document instead of simply giving me the answer. That pushed me to read the documentation and understand why a step was needed. The events they organized, from the Buildrathon kickoff to the fireside chat with Dr. Werner Vogels, were a chance to hear from people who run real systems, which is hard to get anywhere else as a student.

## Learning through Ownword

Ownword showed me how the individual services I studied fit together. In the labs, each service lived on its own. In Ownword, CloudFront, WAF, Lightsail, RDS, Cognito, Lambda, S3, CloudWatch and SNS all had to work as one system, and a mistake in one place showed up somewhere else.

The error I remember most was an `AccessDenied` message when I tested the database backup. The export ran fine on the Lightsail host, but the upload to S3 failed. I was sure the backup identity had S3 access, because the policy listed the bucket. It took me a while to notice that the policy allowed `s3:PutObject` on the bucket's ARN, while uploads need permission on the objects inside it (`bucket/*`). After I fixed the resource ARN, the upload worked, and the identity still couldn't do anything beyond writing backups. From then on I read IAM errors much more carefully: the message names the action and the resource that were refused, and that is usually where the answer is. It also showed me why least privilege takes patience. Giving the identity full S3 access would have hidden the mistake instead of fixing it.

## What this means for my career

This internship confirmed that I want to work in cloud engineering. I now have hands-on experience deploying and operating a real application on AWS, not just finishing isolated labs. My next goal is to earn an AWS certification and to keep building small projects where I handle everything from infrastructure to monitoring and cost.

## A suggestion

The labs are excellent for learning one service at a time. I'd suggest adding a short "connect the pieces" lab every few weeks that combines the services from the previous labs into one small application, for example an app on Lightsail with a private RDS database and a backup to S3. It would help interns practise troubleshooting across services earlier, before the final project. A short note in each lab on the expected cost and which resources to delete first would also help beginners avoid unexpected charges.
