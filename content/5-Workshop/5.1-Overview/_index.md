---
title: "Overview and learning flow"
date: 2026-11-20
weight: 1
chapter: false
pre: " <b>5.1.</b> "
---

## What you will build

Once your copy of Ownword is running, sign in and try it as a learner. Use Bedrock to search by concept, save one of the suggestions to WordBoard, and practice recalling it. You can also submit a made-up writing sample and see what feedback comes back. WordBoard tracks New, Practicing, and Active words, and your streak shows the days you've been active.

Model routing note: concept search runs on Amazon Bedrock with Kimi K3.1 Pro. The Writing module uses GPT-6.1 Terra with low reasoning effort through OpenRouter because requests for GPT-6 Luna on Bedrock returned `AccessDeniedException` on an AWS Free Tier account even after accepting the model agreement. Vocabulary enrichment and practice grading use Gemini 3.6 Flash through OpenRouter for reliable grading at low cost, and Gemini models are not on Amazon Bedrock.

## What you will practice

1. Create the Singapore Lightsail host and a separate private RDS PostgreSQL instance. Connect them by Lightsail VPC peering and verify database TLS.
2. Configure Cognito in Singapore and verify both password sign-in and Google account linking. Publish the application over CloudFront HTTPS with a WAF web ACL.
3. Use Bedrock through N. Virginia for concept search and OpenRouter for the vocabulary and Writing routes.
4. Back up RDS to private S3, restore in a disposable container, and verify that CloudWatch can notify the operator through encrypted SNS.
5. Check that the app works, estimate what a month would cost, and remove the resources you created.

[Start: Prepare your lab environment](../5.2-prerequisites/)
