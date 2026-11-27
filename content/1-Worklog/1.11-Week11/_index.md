---
title: "Week 11: Ownword: sign-in with Cognito, app launch and CloudFront"
date: 2026-11-13
weight: 11
chapter: false
pre: " <b>1.11.</b> "
---

23/11-29/11/2026

## Week 11 objectives

- Configure email and Google sign-in with Amazon Cognito.
- Launch Ownword and publish it through CloudFront and AWS WAF.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Create the Cognito user pool and public app client<br>- Configure the callback URL and PKCE | 23/11/2026 | 23/11/2026 | [Workshop 5.5 step 1](../../5-workshop/5.5-auth/) |
| 3 | - Configure Google as an identity provider<br>- Deploy the Pre sign-up Lambda that links a verified Google identity to an existing account<br>- Test sign-in with a new account and an existing account | 24/11/2026 | 24/11/2026 | [Workshop 5.5 step 2](../../5-workshop/5.5-auth/) |
| 4 | - Prepare model provider credentials (Amazon Bedrock and OpenRouter)<br>- Keep model keys on the server only | 25/11/2026 | 25/11/2026 | [Workshop 5.5 step 3](../../5-workshop/5.5-auth/) |
| 5 | - Build and start the app against RDS<br>- Run database migrations and check the app logs | 26/11/2026 | 26/11/2026 | [Workshop 5.5 step 4](../../5-workshop/5.5-auth/#launch-app) |
| 6 | - Request an ACM certificate for the public hostname<br>- Create the CloudFront distribution in front of the Caddy origin<br>- Attach an AWS WAF web ACL<br>- Test the app through the public URL | 27/11/2026 | 27/11/2026 | [Workshop 5.5 step 5](../../5-workshop/5.5-auth/) |

## Week 11 achievements

- Set up a Cognito user pool with email and password sign-in and Google sign-in, using the OAuth code flow with PKCE.
- Deployed the Pre sign-up Lambda so an existing learner who signs in with Google keeps their WordBoard.
- Launched Ownword on Lightsail, connected to the private RDS database.
- Published the app through CloudFront with an ACM certificate and an AWS WAF web ACL.
