---
title: "Buildrathon Kickoff: Code the Future with CMC Global"
date: 2026-11-13
weight: 1
chapter: false
pre: " <b>4.1.</b> "
---

| Event detail | Information |
|---|---|
| Date | Saturday, 26 September 2026 |
| Time | 09:00-11:20 |
| Venue | Bitexco Financial Tower, 2 Hải Triều, Ho Chi Minh City |
| Organizers | CMC Global and the First Cloud AI Journey community |
| My role | Attendee, together with my Ownword teammates |

## Why I went

This was the first event our team attended together. At that point I had only finished the first two weeks of AWS labs, so I wanted to see how people with more experience approach a real build on AWS, and to meet other interns before the Buildrathon challenge started.

{{< event-photo file="cmc.jpg" alt="Group photo next to CMC Global and First Cloud AI Journey signage" caption="Our group at the Buildrathon kickoff, Bitexco Financial Tower." >}}

## How the morning was organized

The program was short and practical. It started with the goals of the challenge and an overview of AWS, generative AI and building AI agents with AWS services. After an ice-breaking round, there was a talk show with industry practitioners, a Q&A, and finally a 30-minute hands-on mini challenge with mentors in the room.

## What I took away

### A short ice-breaker changes how a team works

The ice-breaking round only lasted fifteen minutes, but it was the part that made the rest of the morning work for me. When the hands-on challenge started, we already knew who was comfortable writing prompts, who liked reading documentation and who wanted to present. In a 30-minute build there is no time to negotiate roles, so knowing each other's strengths first saved us from all doing the same task at once.

### Building an agent is mostly about choosing what it should not do

During the hands-on part, the mentors walked us through the pieces of an AI solution on AWS: prompt engineering, retrieval-augmented generation (RAG), knowledge bases and agents. What surprised me was how much of the work was deciding the limits. A narrow agent that does one thing well is easier to test and easier to explain than a general assistant. I also realized I need to understand the AWS foundations from my worklog (IAM permissions, logs, cost) before I can safely give an agent access to anything.

### Ask the question you are embarrassed to ask

In the Q&A, several people asked very basic questions about certifications and where to start with AWS. The answers were the most useful part of the morning for me, because they turned a long list of services into an order to learn them: start with the core services, practise in labs, then build something end to end. That is close to the path I later followed in my worklog, ending with deploying Ownword.

### Talking to practitioners makes the career path concrete

The talk show covered how organizations actually use AWS and agentic AI in real projects. Hearing people describe their day-to-day work made cloud engineering feel less abstract. It also reminded me that being able to explain a design to non-technical people is part of the job, not an extra.

## How this relates to Ownword

Ownword already uses AI in two places: concept search on Amazon Bedrock and writing feedback through OpenRouter. After this event I paid more attention to the boundaries around those features. The model keys stay on the server, the suggestions are validated before they reach the learner, and each feature does one clearly defined job. If we add more AI features later, I would start by writing down what the feature must never do, then test those cases first.

## References

- [Organizer's agenda (Luma)](https://luma.com/8fe9vvps)
- [What is Amazon Bedrock?](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
- [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
