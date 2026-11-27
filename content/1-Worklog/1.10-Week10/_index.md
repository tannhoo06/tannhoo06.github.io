---
title: "Week 10: Ownword: deploying Lightsail and private RDS"
date: 2026-11-13
weight: 10
chapter: false
pre: " <b>1.10.</b> "
---

16/11-22/11/2026

## Week 10 objectives

- Build the Ownword hosting layer on Amazon Lightsail.
- Connect it to a private, encrypted PostgreSQL database on Amazon RDS.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Create the Lightsail host in Singapore<br>- Attach a static IP and create the origin DNS record<br>- Enable VPC peering for Lightsail | 16/11/2026 | 16/11/2026 | [Workshop 5.4 step 1](../../5-workshop/5.4-deploy/) |
| 3–4 | - Create a private PostgreSQL instance:<br>&emsp;+ Single-AZ, encrypted, in a private subnet<br>&emsp;+ Security Group allows port 5432 only from the Lightsail private IP<br>- Check the connection with `verify-full` TLS | 17/11/2026 | 18/11/2026 | [Workshop 5.4 step 2](../../5-workshop/5.4-deploy/) |
| 5 | - Transfer the source to the host<br>- Bootstrap Ubuntu: Docker, Caddy, firewall | 19/11/2026 | 19/11/2026 | [Workshop 5.4 step 3](../../5-workshop/5.4-deploy/) |
| 6 | - Create the application login and a separate read-only backup login in PostgreSQL<br>- Record the issues I ran into and how I fixed them | 20/11/2026 | 20/11/2026 | [Workshop 5.4 step 4](../../5-workshop/5.4-deploy/) |

## Week 10 achievements

- Deployed the Lightsail host with a static IP and origin DNS, and peered it with the VPC that holds RDS.
- Created an encrypted, private RDS PostgreSQL instance that accepts connections only from the Lightsail host's private /32.
- Bootstrapped the host with Docker and Caddy, ready to run Ownword.
- Created separate database logins for the application and for backups, following least privilege.
