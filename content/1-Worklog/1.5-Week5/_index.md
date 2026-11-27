---
title: "Week 5: Containers: Docker, Amazon ECR and Lightsail Containers"
date: 2026-11-13
weight: 5
chapter: false
pre: " <b>1.5.</b> "
---

12/10-18/10/2026

## Week 5 objectives

- Package an application as a Docker image and run it with Docker Compose.
- Push images to Amazon ECR and run containers on AWS.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn about containers, images and Dockerfiles<br>- **Practice:**<br>&emsp;+ Install dependencies and run the app locally<br>&emsp;+ Test the application | 12/10/2026 | 12/10/2026 | [Docker Introduction](https://000015.awsfcaj.com/1-introduction/)<br>[Deploy on Local](https://000015.awsfcaj.com/2-deploy-local/) |
| 3 | - **Practice:**<br>&emsp;+ Prepare the VPC, Security Group and IAM role for ECR<br>&emsp;+ Launch an RDS instance<br>&emsp;+ Configure the EC2 host | 13/10/2026 | 13/10/2026 | [Preparation](https://000015.awsfcaj.com/3-preparation/)<br>[Launch RDS Instance](https://000015.awsfcaj.com/4-configure-rds/)<br>[Configuring EC2](https://000015.awsfcaj.com/5-configure-ec2/) |
| 4 | - **Practice:**<br>&emsp;+ Deploy with a single Docker image<br>&emsp;+ Deploy with Docker Compose<br>&emsp;+ Push the image to Amazon ECR | 14/10/2026 | 14/10/2026 | [Deploy with Docker Image](https://000015.awsfcaj.com/6-docker-image/)<br>[Deploy with Docker Compose](https://000015.awsfcaj.com/7-docker-compose/)<br>[Push image to ECR](https://000015.awsfcaj.com/8-push-image/8.1-use-ecr/) |
| 5 | - **Practice:**<br>&emsp;+ Create a Lightsail container service<br>&emsp;+ Deploy a public image | 15/10/2026 | 15/10/2026 | [Create a container service](https://000046.awsfcaj.com/1-create-container-service/)<br>[Deploy a public image](https://000046.awsfcaj.com/2-deploy-public-image/) |
| 6 | - **Practice:**<br>&emsp;+ Build and push my own image<br>&emsp;+ Deploy my image and clean up<br>- Compare Lightsail containers with Docker on a Lightsail VM | 16/10/2026 | 16/10/2026 | [Build and push your image](https://000046.awsfcaj.com/3-build-and-push-image/)<br>[Deploy your image](https://000046.awsfcaj.com/4-deploy-your-image/) |

## Week 5 achievements

- Wrote a Dockerfile and a Docker Compose file, and ran a multi-container app with a database.
- Pushed images to a private Amazon ECR repository using an IAM role instead of access keys.
- Deployed containers on Lightsail and understood the trade-offs. Ownword ended up running Docker on a Lightsail VM and pulling images from ECR.
