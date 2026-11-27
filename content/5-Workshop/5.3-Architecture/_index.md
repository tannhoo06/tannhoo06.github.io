---
title: "Architecture and data flow"
date: 2026-11-20
weight: 3
chapter: false
pre: " <b>5.3.</b> "
---

## Production request flow

{{< ownword-architecture alt="Ownword request flow through CloudFront, Lightsail and RDS, with Cognito sign-in, model requests and backups. The release flow shows GitHub Actions publishing to private ECR in Singapore and Lightsail pulling the image." caption="Ownword production architecture and automated releases. Select the diagram to open it at full size." >}}

| Steps | Follow the path |
|---|---|
| **1-3. Public HTTPS and origin** | The browser connects to `app.ownword.co` through CloudFront, with an ACM viewer certificate and an AWS WAF web ACL. CloudFront connects over TLS to Caddy at `origin.ownword.co`. Caddy forwards requests to Next.js on port 3000 inside the private Docker Compose network. |
| **4. Database** | Next.js reads and writes to private Amazon RDS for PostgreSQL in Singapore over Lightsail VPC peering. The Single-AZ database runs in a private subnet in `ap-southeast-1a`, encrypts storage with the AWS-managed RDS key, and accepts TLS connections on port 5432 only from the Lightsail host's private address. |
| **5-8. Sign-in** | Next.js talks to Amazon Cognito in Singapore for password sign-in and OAuth code exchange. The browser follows Cognito's OAuth flow for Google sign-in and returns through `/auth/callback`, where Next.js exchanges the code using PKCE. On the first eligible federated sign-in, Cognito can invoke its Pre sign-up Lambda in Singapore to link the verified Google identity. Next.js resolves the Cognito identity to the learner record in PostgreSQL. |
| **9-10. Model requests** | Concept search calls Amazon Bedrock through the N. Virginia endpoint using the Kimi K3.1 Pro U.S. inference profile. Writing assessment calls GPT-6.1 Terra Low through OpenRouter, and vocabulary enrichment and practice grading call Gemini 3.6 Flash through OpenRouter (Gemini models are not on Bedrock). All model calls originate on the server. |
| **11-14. Backup and alert** | The Lightsail backup job reads RDS under a separate database role, makes a daily PostgreSQL dump, and uploads it to a private S3 backup bucket. Backups and the separate access-log bucket use SSE-S3. An hourly check publishes `BackupFresh`. A stale or missing signal triggers CloudWatch to notify the operator through an SNS topic encrypted with a customer-managed KMS key. |

## Release flow

A push to `release/lightsail` starts GitHub Actions. The workflow checks the code, builds a Docker image, and uses short-lived AWS credentials through GitHub OIDC to publish it to private Amazon ECR in Singapore. Lightsail checks ECR every two minutes. On a new image, it pulls the exact digest, runs migrations against RDS, and checks the home and sign-in routes after restarting the app. If startup fails, it restores the previous app image.

## AWS Well-Architected pillar alignment

| Pillar | How Ownword applies it |
|---|---|
| Operational excellence | GitHub Actions checks TypeScript and tests before building immutable ECR images, and Lightsail pulls releases by digest with automatic rollback on failed health checks. Hourly `BackupFresh` metrics and a CloudWatch alarm surface backup issues early. |
| Security | CloudFront and AWS WAF sit in front of the origin. RDS runs in a private subnet with encryption at rest, security-group ingress restricted to the Lightsail private `/32`, and `verify-full` TLS. Cognito uses PKCE for OAuth, model keys stay on the server, and IAM policies separate Bedrock, S3 backup, and account-linking permissions. |
| Reliability | Moving PostgreSQL off the Lightsail host into RDS separates application and database failures. Daily `pg_dump` archives are copied to versioned private S3 with SHA-256 verification and tested via isolated container restores, while the backup alarm treats missing data as breaching. The Single-AZ database is a deliberate pilot tradeoff documented with its recovery path. |
| Performance efficiency | CloudFront terminates viewer HTTPS at edge locations and forwards requests to Singapore (`ap-southeast-1`) close to target learners. RDS runs on ARM-based `db.t4g.micro` (Graviton) with gp3 storage, and the app reuses saved Bedrock concept-search results on repeat lookups to avoid unnecessary model latency. |
| Cost optimization | Fixed hosting stays predictable on a 2 GB Lightsail bundle and Single-AZ `db.t4g.micro`. Repeat concept-search caching, output-token limits, OpenRouter spend caps, S3 lifecycle expiration (30 days current, 7 days noncurrent), and ECR image retention keep variable costs bounded. See [chapter 5.7](../5.7-verification/#2-build-a-monthly-cost-estimate). |

## Deployment used in the lab

Start by setting up Lightsail and private RDS with your own lab resources. You'll use two DNS names. Cognito sends users back to the public hostname after sign-in, and Caddy serves the origin hostname. A separate PostgreSQL role reads the data for backups. Later, you'll try a restore in an isolated PostgreSQL container.

**Checkpoint.** Follow a user request to RDS, a stale-backup alert to the operator's inbox, and a release image from GitHub to Lightsail.

[Next: Prepare Lightsail and private RDS](../5.4-deploy/)
