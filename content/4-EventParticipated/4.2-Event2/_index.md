---
title: "AWS Cloud and AI Day Hanoi 2026"
date: 2026-11-13
weight: 2
chapter: false
pre: " <b>4.2.</b> "
---

| Event detail | Information |
|---|---|
| Date | Tuesday, 29 September 2026 |
| Main conference | JW Marriott Hotel Hanoi |
| Where I joined | Ho Chi Minh City watch party |
| Session I followed | DVT205, watch party for "Building software like never before with agentic AI" |
| My role | Attendee |

## Event overview

The main event took place in Hanoi with a keynote in the morning and parallel tracks from 11:00 on AI, data and analytics, migration and modern applications. Sessions on the agenda included an internal developer platform on Amazon EKS from VPBank, taking agentic AI from demo to deployment with Katalon, building an AI-ready data foundation, and large-scale migration with AWS Transform. Our team followed the event from the Ho Chi Minh City watch party, where the 11:00 session was about building software with agentic AI.

{{< event-photo file="cloud_day_1.jpg" alt="Group photo in the watch-party room with conference video on the screens" caption="At the Ho Chi Minh City watch party." >}}

## What I learned

### The community behind the event

One keynote slide stayed with me more than any product announcement. It counted more than 157,000 people trained in cloud and AI, more than 54,000 members of the AWS Study Group and more than 15,000 participants in the First Cloud AI Journey ecosystem. I am one of those 15,000. It made me see the labs and blogs I use every week as part of something much larger, and it is a reason to share what I learn back with the group.

### Agents write code, but someone still owns it

The watch-party session was about using AI agents across the software lifecycle, not only to autocomplete code but to plan, change and test larger pieces of work. The theme I kept hearing during the day was that once an agent can call APIs, modify code or trigger a deployment, it raises the same questions as any new team member: which identity does it use, what is it allowed to do, who approves its changes and where can we see what it did. Faster code generation doesn't remove the need for review. It moves the effort from writing code to reading and checking it.

{{< event-photo file="cloud_day_2.jpg" alt="Slide shown on the watch-party screens" caption="A slide from the sessions we followed at the watch party." >}}

### More automation needs more guardrails, not fewer

Platform engineering came up as a foundation for AI rather than a separate topic. When teams automate more, they rely more on shared deployment patterns, secure defaults and policy checks, because nobody manually inspects every change anymore. I connected this to what I learned in the CI/CD labs: a pipeline is only as safe as the checks it runs before something reaches production.

### Identities that aren't people are a security boundary

Workloads, pipelines, services and AI agents all call AWS APIs, and each of them needs an identity. The advice I noted was to prefer short-lived credentials and federation over long-lived keys, to design trust policies carefully and to keep verifying which identity is actually in use. This was the same lesson as my week 3 lab on IAM roles for EC2, seen at a much larger scale.

## How this relates to Ownword

Ownword has several non-human identities: the Lightsail host calling Amazon Bedrock, the backup job writing to S3, the Pre sign-up Lambda in Cognito and GitHub Actions pushing images to ECR. Our architecture already gives Bedrock access, S3 backups and account linking separate IAM policies, so one identity can't quietly do another's job. After this event I would like to go one step further and replace any remaining long-lived access key with temporary credentials, and write down for each identity who owns it and what it is allowed to do.

{{< event-photo file="cloud_day_3.jpg" alt="Conference attendance badge" caption="My attendance badge for AWS Cloud and AI Day Hanoi 2026." >}}

## References

- [Conference overview](https://aws.amazon.com/events/cloud-day-hanoi/)
- [Official agenda](https://aws.amazon.com/events/cloud-day-hanoi/agenda/)
- [Conference recap on AWS Builder Center](https://builder.aws.com/content/3KMpKxUhRFeSlclpmwu5ZxBQBYL/aws-cloud-and-ai-day-hanoi-2026-building-for-the-next-phase-of-cloud-and-ai)
- [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)
