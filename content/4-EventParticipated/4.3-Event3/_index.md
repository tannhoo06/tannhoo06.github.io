---
title: "Fireside Chat with Dr. Werner Vogels"
date: 2026-11-13
weight: 3
chapter: false
pre: " <b>4.3.</b> "
---

| Event detail | Information |
|---|---|
| Event theme | Navigating the Future of Cloud & AI in Vietnam |
| Date | Friday, 2 October 2026 |
| Location | Ho Chi Minh City |
| Guest | Dr. Werner Vogels, Chief Technology Officer at Amazon |
| My role | Attendee |

## Event overview

Dr. Werner Vogels has spent more than two decades building the infrastructure behind Amazon and AWS. In this fireside chat organized for the First Cloud AI Journey community, he shared lessons from that work and talked about what it means to be a developer when AI can write code. I came in expecting a talk about technology and left thinking mostly about habits: how to choose tools, how to talk about trade-offs and how to keep learning.

{{< event-photo file="fireside_1.jpg" alt="First Cloud AI Journey opening slide showing the event title and 2 October 2026" caption="The opening slide of the fireside chat." >}}

## What I learned

### Match the tool to the workload

Dr. Vogels described a holiday peak when an overloaded relational database cluster went down and took customer data storage offline for a day. When Amazon's engineers looked at what the applications were really doing, roughly 70% of the requests were simple key-value lookups, about 20% used a single table, and only around 10% needed full relational features. What I took from the story was not "build your own database" but "measure before you choose". It is easy to pick a familiar tool for everything. It is better to look at the actual requests first.

### Everything fails, so plan for it

One idea he returned to was that everything fails all the time. Systems should be designed so that losing a component, or even a whole data center, doesn't stop the service. Amazon runs GameDays where teams deliberately take infrastructure offline to check that failover happens automatically. For a student project this sounds far away, but the principle scales down: decide in advance what happens when each part fails, and practise it instead of hoping.

{{< event-photo file="fireside_2.jpg" alt="Dr. Werner Vogels speaking with the host during the fireside chat" caption="Dr. Werner Vogels during the conversation." >}}

### Explain trade-offs in plain language

Among the traits of what he calls the "Renaissance developer", the one I needed most was communication. His example was the cost difference between 99.9% and 99.99% uptime. That extra "9" is not a technical detail. It is a business decision, and engineers should explain it so that the people paying for it can choose. The other traits were curiosity, systems thinking, ownership and T-shaped expertise: going deep in one area while understanding enough of the neighbouring ones, such as the UI, the business logic and the database.

### AI is a fast but imprecise compiler

He described AI as a natural-language compiler that is not precise. It has cut prototyping from weeks to hours, but the output still has to be checked for security problems, edge cases and efficiency. The engineer remains responsible for what goes into production. He ended with a warning from Grace Hopper that "we've always done it this way" is a dangerous mindset. For me that means I shouldn't refuse AI tools, and I shouldn't trust them blindly either.

## How this relates to Ownword

Ownword runs on one Lightsail VM and a Single-AZ RDS database. That is a deliberate trade-off for a small pilot: lower cost in exchange for less redundancy. After this talk I can explain that choice better. If the database fails, we rely on daily exports to S3 that we have actually restored in an isolated test, and the `BackupFresh` alarm tells us if a backup goes missing. If the pilot grows, moving to Multi-AZ is the extra "9" we would discuss with the team, together with its monthly cost. I also want to keep reviewing AI-assisted code line by line, especially in sign-in and database access.

{{< event-photo file="fireside_3.jpg" alt="Group photo with other attendees at the First Cloud AI Journey event" caption="With my teammates after the fireside chat." >}}

## References

- [AWS Builder Center recap of the fireside chat](https://builder.aws.com/content/3KBSLeKsdkk6uMUPq7d9Xxa5jbS/the-invariable-lessons-of-tech-and-humanity-key-takeaways-from-amazon-cto-werner-vogels)
- [Amazon's Dynamo paper](https://www.amazon.science/publications/dynamo-amazons-highly-available-key-value-store)
- [Reliability pillar of the AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/welcome.html)
