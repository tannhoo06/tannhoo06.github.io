---
title: "Week 7: Serverless and identity: AWS Lambda, Amazon Cognito and VPC Peering"
date: 2026-11-13
weight: 7
chapter: false
pre: " <b>1.7.</b> "
---

26/10-01/11/2026

## Week 7 objectives

- Automate tasks with AWS Lambda.
- Add user sign-up and sign-in with Amazon Cognito.
- Connect two VPCs privately with VPC Peering.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn about AWS Lambda<br>- **Practice:**<br>&emsp;+ Tag EC2 instances and create a role for Lambda<br>&emsp;+ Write Lambda functions to stop and start instances<br>&emsp;+ Send results to Slack | 26/10/2026 | 26/10/2026 | [Create Role for Lambda](https://000022.awsfcaj.com/4-createroleforlambda/)<br>[Create Lambda Function](https://000022.awsfcaj.com/5-createlambdafunction/) |
| 3 | - Learn about Cognito user pools and app clients<br>- **Practice:**<br>&emsp;+ Create a user pool<br>&emsp;+ Create an API and Lambda function<br>&emsp;+ Test sign-in from the front end | 27/10/2026 | 27/10/2026 | [Create User Pool](https://000081.awsfcaj.com/2-create-user-pool/)<br>[Test with Front-end](https://000081.awsfcaj.com/4-test-front-end/) |
| 4 | - **Practice:**<br>&emsp;+ Deploy Cognito across two sites<br>&emsp;+ Read the code walkthrough for the OAuth flow<br>&emsp;+ Test and clean up | 28/10/2026 | 28/10/2026 | [Code Explanation](https://000141.awsfcaj.com/3-note-code/)<br>[Deploy and Test](https://000141.awsfcaj.com/4-app-configuration/) |
| 5 | - Learn about VPC Peering<br>- **Practice:**<br>&emsp;+ Launch the CloudFormation template<br>&emsp;+ Update Network ACLs<br>&emsp;+ Create a peering connection | 29/10/2026 | 29/10/2026 | [VPC Peering Introduction](https://000019.awsfcaj.com/1-introduce/)<br>[Create Peering Connection](https://000019.awsfcaj.com/4-vpcpeering/) |
| 6 | - **Practice:**<br>&emsp;+ Update route tables on both sides<br>&emsp;+ Enable cross-peer DNS<br>&emsp;+ Clean up resources<br>- Note how Lightsail can peer with the default VPC to reach RDS | 30/10/2026 | 30/10/2026 | [Route Tables](https://000019.awsfcaj.com/5-routetables/)<br>[Cross-Peer DNS](https://000019.awsfcaj.com/6-crosspeerdns/) |

## Week 7 achievements

- Wrote Lambda functions with a least-privilege role to start and stop EC2 on a schedule.
- Created a Cognito user pool and app client, and understood the OAuth authorization code flow with PKCE.
- Connected two VPCs with VPC Peering, updated route tables and Network ACLs, and enabled cross-peer DNS.
- Understood the three building blocks Ownword uses for sign-in and database access: Cognito, a Pre sign-up Lambda trigger and Lightsail VPC peering.
