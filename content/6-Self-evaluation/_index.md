---
title: "Self-evaluation"
date: 2026-11-13
weight: 6
chapter: false
pre: " <b>6.</b> "
---

From 14 September to 14 December 2026, I took part in the First Cloud AI Journey internship as a member of Gi Group. I spent the first eight weeks building my AWS foundations through the Cloud Journey labs, from IAM and VPC to RDS, Lightsail, CloudFront, Cognito and backups. In the last four weeks I applied what I had learned to Ownword, our English vocabulary and writing app. I worked through the deployment in my own lab account, helped test the sign-in, backup and monitoring flows, and wrote my parts of this bilingual report.

## My ratings

| No. | Criterion | What I assessed | Good | Fair | Average |
| ---: | --- | --- | :---: | :---: | :---: |
| 1 | Share of the work | How much of the team's work I took on and completed | ⬜ | ✅ | ⬜ |
| 2 | Impact of my work | What improved for Ownword or the team because of my work | ✅ | ⬜ | ⬜ |
| 3 | Initiative | Whether I spotted gaps, suggested changes, or volunteered to help | ⬜ | ✅ | ⬜ |
| 4 | Teamwork | How well I kept teammates informed, listened, and helped when needed | ✅ | ⬜ | ⬜ |
| 5 | Learning efficiency | How I used my time when I got stuck and when I asked for help | ⬜ | ✅ | ⬜ |
| 6 | Responding to feedback | How I used feedback to improve my work | ✅ | ⬜ | ⬜ |
| 7 | Understanding AWS basics | Whether I can explain what the AWS services I studied do and when to use them | ✅ | ⬜ | ⬜ |
| 8 | Applying AWS to Ownword | How well the services I helped set up fit the project's needs | ✅ | ⬜ | ⬜ |
| 9 | Meeting deadlines | Whether I delivered when promised and flagged delays early | ✅ | ⬜ | ⬜ |
| 10 | Prioritizing work | Whether I focused on what the team needed most | ⬜ | ✅ | ⬜ |
| 11 | Consistency | How steadily I made progress and kept my worklog up to date | ✅ | ⬜ | ⬜ |
| 12 | Quality of work | How well I checked my work and how much rework it left for teammates | ✅ | ⬜ | ⬜ |

I rated myself **Good** on eight criteria where I can point to clear evidence. I can explain the AWS services I studied and when to use them, the parts of Ownword I tested work as intended, I kept my worklog up to date every week, and I delivered my tasks on time and checked them before handing them over. I chose **Fair** for four criteria where I know I can still grow. Our team leader carried the largest share of the work and the architecture decisions, I could have proposed changes more often instead of waiting to be asked, and I sometimes spent too long on one problem before asking for help or deciding what mattered most.

## My contribution to Ownword

- **Reproducing the deployment end to end.** I followed the workshop in my own AWS account: the Lightsail host, the private RDS PostgreSQL instance with VPC peering, Cognito sign-in with Google, and CloudFront with AWS WAF in front of the app. Each time a step was unclear or failed, I noted what happened and how I fixed it, so the instructions could be checked against a fresh account.
- **Testing sign-in, backups and monitoring.** I tested signing in with email and password and with Google, including the case where an existing account links to a Google identity and keeps its WordBoard. I also checked that the daily export reached S3, restored it into an isolated PostgreSQL container, and confirmed that the `BackupFresh` alarm sent an email through SNS.
- **Verification, cost and documentation.** I ran the acceptance checks for valid and invalid requests and CloudWatch Logs, helped review the monthly cost estimate, and made sure the lab resources were cleaned up afterwards. I also wrote my own worklog, event write-ups and reflections for this report in both English and Vietnamese.

## Needs improvement

- **Ask for help earlier.** When I got stuck, for example on an `AccessDenied` error from the backup upload, I sometimes spent too long trying things on my own. Next time I will set myself a time limit, write down what I have already tried, and then ask a teammate or mentor with that information ready.
- **Understand the application code, not only the infrastructure.** I'm comfortable with the AWS console and CLI now, but I understand less about how the Next.js app handles sessions and calls Bedrock. I want to read and test that part of the code myself so I can debug a problem from the browser all the way to the database.
- **Keep notes as I work.** Some of my worklog entries were written after the fact. I want to note commands, errors and screenshots while I'm working, which will make my reports more accurate and save time at the end.
