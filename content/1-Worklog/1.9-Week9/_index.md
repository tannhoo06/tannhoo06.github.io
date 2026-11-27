---
title: "Week 9: CI/CD with GitHub Actions and the Ownword proposal"
date: 2026-11-13
weight: 9
chapter: false
pre: " <b>1.9.</b> "
---

09/11-15/11/2026

## Week 9 objectives

- Automate building and deploying container images.
- Understand the Ownword proposal and agree on the AWS architecture with the team.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn CI/CD concepts<br>- **Practice:**<br>&emsp;+ Clone the GitHub template and push code<br>&emsp;+ Create credentials for the pipeline<br>&emsp;+ Check the GitHub Actions results | 09/11/2026 | 09/11/2026 | [CI/CD with GitHub Actions](https://000017.awsfcaj.com/4-cicd-github/) |
| 3 | - **Practice:**<br>&emsp;+ Build with CodeBuild and create a release tag<br>&emsp;+ Monitor containers with Container Insights<br>&emsp;+ Clean up ECS and ECR resources | 10/11/2026 | 10/11/2026 | [CI/CD with CodeBuild](https://000017.awsfcaj.com/5-cicd-codebuild/)<br>[Container Insights](https://000017.awsfcaj.com/6-monitoring-with-container-insights/) |
| 4 | - Read the Ownword proposal: problem, audience, pilot scope<br>- Discuss my tasks in the project with the team | 11/11/2026 | 11/11/2026 | [Ownword Proposal](../../2-proposal/) |
| 5 | - Study the Ownword architecture:<br>&emsp;+ Production request flow<br>&emsp;+ Release flow (GitHub Actions → ECR → Lightsail)<br>&emsp;+ Well-Architected pillar alignment | 12/11/2026 | 12/11/2026 | [Workshop 5.1 Overview](../../5-workshop/5.1-overview/)<br>[Workshop 5.3 Architecture](../../5-workshop/5.3-architecture/) |
| 6 | - Prepare my lab environment:<br>&emsp;+ Check AWS access and prerequisites<br>&emsp;+ Get the source and workstation tools<br>&emsp;+ Record my lab inputs | 13/11/2026 | 13/11/2026 | [Workshop 5.2 Prerequisites](../../5-workshop/5.2-prerequisites/) |

## Week 9 achievements

- Built a CI/CD pipeline that tests, builds and pushes a container image automatically.
- Understood Ownword's goal: help learners find, save and actively use new English words, plus get feedback on their writing.
- Can explain the Ownword architecture end to end: CloudFront and WAF → Caddy and Next.js on Lightsail → private RDS, with Cognito for sign-in, Bedrock for concept search and S3 for backups.
- Prepared my workstation and recorded the inputs I need for the lab.
