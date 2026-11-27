---
title: "Week 6: Edge and monitoring: CloudFront, AWS WAF and CloudWatch"
date: 2026-11-13
weight: 6
chapter: false
pre: " <b>1.6.</b> "
---

19/10-25/10/2026

## Week 6 objectives

- Put a CDN and a web application firewall in front of an application.
- Monitor resources with metrics, logs, alarms and dashboards.

## Tasks for the week

| Day | Task | Start date | Completion date | Reference material |
| --- | --- | --- | --- | --- |
| 2 | - Learn about Amazon CloudFront: distributions, origins, caching<br>- **Practice:**<br>&emsp;+ Create an S3 origin and upload index.html<br>&emsp;+ Configure a CloudFront distribution | 19/10/2026 | 19/10/2026 | [Create S3 bucket](https://000094.awsfcaj.com/1.1-t%E1%BA%A1o-nh%C3%B3m-s3/)<br>[Configure CloudFront](https://000094.awsfcaj.com/1.3-c%E1%BA%A5u-h%C3%ACnh-amazon-cloudfront/) |
| 3 | - Learn about AWS WAF<br>- **Practice:**<br>&emsp;+ Deploy the sample web application<br>&emsp;+ Create a web ACL with managed rules | 20/10/2026 | 20/10/2026 | [WAF Introduction](https://000026.awsfcaj.com/1-introduction/)<br>[Web ACLs with managed rules](https://000026.awsfcaj.com/3-useawswaf/3.1-createswebacl/) |
| 4 | - **Practice:**<br>&emsp;+ Write custom and advanced custom rules<br>&emsp;+ Test the new rules<br>&emsp;+ Enable request logging<br>&emsp;+ Clean up resources | 21/10/2026 | 21/10/2026 | [Custom Rule](https://000026.awsfcaj.com/3-useawswaf/3.2-createcustomrule/)<br>[Request Logging](https://000026.awsfcaj.com/3-useawswaf/3.5-logging/) |
| 5 | - Learn CloudWatch metrics<br>- **Practice:**<br>&emsp;+ View metrics<br>&emsp;+ Use search and math expressions<br>&emsp;+ Use log groups, Logs Insights and metric filters | 22/10/2026 | 22/10/2026 | [CloudWatch Metrics](https://000008.awsfcaj.com/3-cloud-watch-metric/)<br>[CloudWatch Logs](https://000008.awsfcaj.com/4-cloud-watch-logs/) |
| 6 | - **Practice:**<br>&emsp;+ Create CloudWatch alarms<br>&emsp;+ Build a CloudWatch dashboard<br>&emsp;+ Clean up resources | 23/10/2026 | 23/10/2026 | [CloudWatch Alarms](https://000008.awsfcaj.com/5-cloud-watch-alarm/)<br>[CloudWatch Dashboards](https://000008.awsfcaj.com/6-cloud-watch-dashboard/) |

## Week 6 achievements

- Configured a CloudFront distribution and understood how caching and origin settings affect requests.
- Protected an application with an AWS WAF web ACL using managed rules, custom rules and request logging.
- Used CloudWatch metrics, Logs Insights and metric filters to understand what an application is doing.
- Created alarms and dashboards. Ownword later uses the same pattern: a CloudWatch alarm on a custom backup metric.
