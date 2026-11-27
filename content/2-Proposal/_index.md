---
title: "Proposal"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>2.</b> "
---

## Executive summary

Ownword is an English learning app for people who recognize more words than they can use when they write. It gives learners a way to find the word they're reaching for, save it, and practice until they can recall it on their own. A separate Writing module helps them decide what to change in a draft and check how well a revision addresses that feedback.

The pilot runs on AWS. Amazon Bedrock handles concept search with Kimi K3.1 Pro, and OpenRouter gives the Writing module access to a frontier model for draft assessment and revision feedback. Readers can [watch the demo video](https://youtu.be/VEdfxhcqqCk), [try the live app](https://app.ownword.co/), or deploy their own copy with the [bilingual workshop](../5-workshop/).

At report close (30 November 2026), we are still waiting for AWS Support to resolve model access. Requests for GPT-6 Luna on Amazon Bedrock returned `AccessDeniedException` on our AWS Free Tier account even after we accepted the model agreement. We continue to access GPT-6 Luna through OpenRouter for evaluation. After several rounds of benchmarking for draft assessment and revision checks, we selected GPT-6.1 Terra with low reasoning effort through OpenRouter for production Writing because it offered the best balance of feedback quality and cost for our workload. For vocabulary enrichment and practice grading, we picked Gemini 3.6 Flash through OpenRouter because it gave reliable definitions and grading at low cost, and Gemini 3.6 Flash is not listed in the Amazon Bedrock model catalog.

## The problem

You can recognize a word in a book and still reach for a simpler one when you write. Looking up a better word helps you finish the sentence. The next time you need that word, you may have to look it up again. Revising can be just as frustrating when a sentence feels off and you can't pinpoint what to change.

Ownword starts from a learner's own draft or an idea they want to express. It connects that moment of discovery to later practice and keeps writing feedback tied to the passages the learner wrote.

## Audience and learning loop

The pilot is designed for advanced English learners working on their own. The vocabulary loop moves through six steps: write, discover, choose, practice, retrieve, and activate. On WordBoard, a saved word progresses through **New**, **Practicing**, and **Active** as the learner recalls and uses it in different contexts over time.

Imagine wanting a word for an experience that feels happy and sad at the same time. You can describe that feeling in English or Vietnamese, consider a suggestion like *bittersweet*, and save it to WordBoard. In Quick Review you can flag the word if you forget it. In Full Practice you can try recalling it and using it in a sentence on a topic of your choice.

Writing follows a separate loop. The learner picks a prompt, writes a response, reads feedback on specific passages, and revises in their own words. Keeping the original in view lets the learner see what changed and check which earlier suggestions the revision addresses.

## Pilot scope

| Feature | What the pilot supports |
| --- | --- |
| Vocabulary discovery | Find suggestions in your own writing or describe a concept in English or Vietnamese. Save useful suggestions or add a word by hand. |
| WordBoard and practice | Track saved words, listen to browser-based pronunciation, review words you forgot, and practice recall and sentence use. The learning streak tracks days of activity. |
| Writing | Draft from a prompt, review feedback on exact passages, and revisit the original and its revision in Writing history. |
| Accounts | Sign in with email and password or Google. An eligible existing account can link to a verified Google identity and keep its WordBoard. |

The pilot uses one application VM and a private Single-AZ database. Its purpose is to test the complete learning and recovery flows with a small group.

## Deployed architecture

{{< ownword-architecture alt="Ownword production request and backup paths, with GitHub Actions publishing release images through private ECR in Singapore for Lightsail to pull." caption="Ownword production architecture and automated releases, 24 November 2026. Select the diagram to open it at full size." >}}

### AWS services used

- **Amazon CloudFront.** Serves the public HTTPS entry point for Ownword and forwards web and API requests to the Caddy origin on Lightsail. Cognito callbacks use the public app hostname.
- **AWS WAF.** Applies a web ACL to requests that reach the CloudFront distribution. It operates at the public edge before those requests go to the origin.
- **AWS Certificate Manager (ACM).** Supplies the viewer certificate for the public hostname on CloudFront. Caddy handles the certificate for the separate origin connection.
- **Amazon Lightsail.** Runs the Singapore VM. Caddy accepts origin HTTPS and forwards traffic to Next.js over the private Docker network. The VM also runs the database backup and backup health jobs.
- **Amazon RDS for PostgreSQL.** Stores application records such as learner profiles, WordBoard entries, practice results, and Writing history. The encrypted Single-AZ database runs in a private subnet in Singapore (`ap-southeast-1a`) and accepts connections on port 5432 only from the Lightsail host over VPC peering. The app verifies the database certificate and hostname.
- **Amazon Cognito.** Manages passwords, verified email, and the Google sign-in flow through a user pool in Singapore. Next.js maps the verified Cognito identity to the learner's PostgreSQL record.
- **AWS Lambda.** Runs the Pre sign-up trigger for Google federation in Singapore. When the first Google sign-in matches an eligible existing account, the trigger can link the verified identity so the learner keeps their WordBoard.
- **Amazon Bedrock.** Runs Kimi K3.1 Pro for concept search through a U.S. inference profile. The application calls the Bedrock endpoint in N. Virginia and validates the suggestions before returning them.
- **Amazon S3.** Holds daily PostgreSQL exports in a private bucket and writes access logs to a separate private bucket. Both use SSE-S3. A copy outside the app VM and database gives the team an archive it can restore into a separate test database.
- **Amazon ECR.** Stores private release images built by GitHub Actions. Lightsail pulls the published image by digest and checks the app after rollout. [Release flow](../5-workshop/5.3-architecture/#release-flow)
- **Amazon CloudWatch.** Receives the hourly `BackupFresh` metric. The backup alarm evaluates whether the latest export is fresh and its S3 copy is present.
- **Amazon SNS.** Sends an email to the operator when the CloudWatch alarm changes to the alarm state.
- **AWS Key Management Service (KMS).** Provides the customer-managed key that encrypts the SNS topic used by the backup alarm.
- **AWS Identity and Access Management (IAM).** Scopes AWS permissions for Bedrock calls, S3 backup access, CloudWatch metric writes, and the account-linking Lambda. PostgreSQL has separate roles for the app and backup job.

## Technical implementation

### Request and data flow

1. Open the app (steps 1-4): The browser connects to CloudFront over HTTPS. CloudFront then connects over TLS to Caddy at the origin hostname. Caddy sends the request to Next.js, which reads or writes learner data in private RDS using a separate TLS connection.
2. Sign in (steps 5-8): A password sign-in goes to Cognito. For Google sign-in, Cognito handles federation and returns the browser to Ownword's callback. Next.js exchanges the authorization code using PKCE. The Lambda trigger can link the Google identity during the first eligible sign-in.
3. Ask a model (steps 9-10): Next.js sends concept-search requests to Kimi on Bedrock. Writing assessment, vocabulary enrichment, and practice grading use separate OpenRouter routes. Provider credentials stay on the server.
4. Back up and alert (steps 11-14): The VM reads RDS with a read-only backup role, exports the database to private S3, and checks the latest backup each hour. A stale or missing signal triggers an email through the encrypted SNS topic.

The workshop walks through [the diagram and request flow](../5-workshop/5.3-architecture/), [sign-in and public HTTPS](../5-workshop/5.5-auth/), and [backup, restore, and alarm testing](../5-workshop/5.6-operations/).

### How we use Amazon Bedrock and OpenRouter {#writing-inference-provider}

Ownword uses Kimi K3.1 Pro on Amazon Bedrock for concept search, a core part of its vocabulary discovery. Learners can describe an idea in English or Vietnamese and get suggestions for words and phrases that express it. The app can reuse a saved result for a repeat lookup, which avoids another model call.

Writing submits the draft or revision to GPT-6.1 Terra Low through OpenRouter and requests Zero Data Retention on the configured route. Vocabulary enrichment and practice grading use Gemini 3.6 Flash through OpenRouter for reliable short responses at low cost, and Gemini is not on Bedrock. The application validates the structured feedback before saving it. [Model access status](#executive-summary)

## Timeline and milestones

| Milestone | What happened |
| --- | --- |
| 14 September to 18 October | Worked through the AWS labs on accounts, IAM, networking, databases, and monitoring. [Worklog](../1-worklog/) |
| 25 October | Recorded the first Ownword prototype with draft-based vocabulary discovery, WordBoard, and sentence practice. [Week 6](../1-worklog/1.6-week6/) |
| 28 October | Added Quick Review and Full Practice so learners could focus on words they had forgotten. [Week 7](../1-worklog/1.7-week7/) |
| 5 November | Verified the backup path by restoring an S3 dump and testing the CloudWatch and SNS alert flow on the Lightsail pilot. [Week 8](../1-worklog/1.8-week8/) |
| 12 November | Deployed the custom account screens, Google sign-in, and pronunciation controls. [Week 9](../1-worklog/1.9-week9/) |
| 20 November | Moved the application database to private RDS and released the daily learning streak. |
| 30 November | Rehearsed the demo, captured the Workshop test results, and finished the handover. |

## Cost estimate and optimization {#budget-estimate}

For a 10-learner pilot, the operating budget is US$43.56/month before tax and account credits. This combines US$43.24 for AWS and US$0.32 for OpenRouter inference at published rates. At 100 learners with the same server sizes, the estimate rises to US$60.98/month.

| Monthly cost | 10 active learners | 100 active learners |
| --- | ---: | ---: |
| Lightsail and private RDS | $33.01 | $33.01 |
| Edge, security, storage and monitoring | $8.69 | $9.33 |
| Bedrock concept search | $1.54 | $15.40 |
| OpenRouter Writing, vocabulary and practice | $0.32 | $3.24 |
| **Total** | **$43.56** | **$60.98** |

The [detailed Workshop estimate](../5-workshop/5.7-verification/#2-build-a-monthly-cost-estimate) records the AWS Pricing Calculator inputs and results, request and token assumptions, and applicable allowances. We control costs by reusing concept-search results, setting provider spend limits, and limiting backup and release-image retention.

## Design choices and risks

| Risk | What the design does and what to check |
| --- | --- |
| The app VM goes down | RDS keeps the database separate from the app host. Use the workshop to rehearse redeployment and time how long it takes for sign-in and WordBoard to return. |
| Database failure or stale backup | The pilot uses Single-AZ RDS. Keep a private S3 copy of each daily dump and check `BackupFresh`. Time a restore into an isolated database and record which backup it used. |
| Access to another learner's data | Cognito establishes identity. Next.js limits access to the signed-in owner's records. Check that a second account cannot open a saved-word detail URL from the first account. |
| Model failure or unsuitable feedback | Validate response structure before using it. Test a fresh concept lookup and a revision with synthetic text so a provider error or unhelpful result is visible. |
| Higher usage or costs | Use the saved result for repeat lookups and cap model calls. Compare CPU, memory, latency, and errors under a small test load before deciding whether the VM needs more capacity. |

## Delivery and measurement

The report includes the architecture diagram, the live app, and a bilingual deployment and cleanup guide. Earlier release checks recorded Cognito sign-in, persistence of saved words and practice results, live model calls, and a restore of an RDS backup into a temporary database.

The demo is successful if a learner can find an unfamiliar word, save and recall it later, and work through feedback on a draft. The AWS side is successful if the team can repeat the lab with its own resources, restore the data, and receive an alert when the backup is stale. The Workshop verification chapter records a valid request and its saved database row, a CloudWatch log from the sign-in flow, and the response to invalid input. [Workshop acceptance checks](../5-workshop/5.7-verification/)
