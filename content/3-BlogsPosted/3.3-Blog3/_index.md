---
title: "Static Websites on S3: Public Bucket or CloudFront + OAC?"
menuTitle: "S3 static sites: public bucket vs CloudFront + OAC"
weight: 3
chapter: false
pre: " <b>3.3.</b> "
---

| Publication detail | Information |
| --- | --- |
| Publication date | 19 November 2026 |
| Publication link | [Original Vietnamese post on Facebook](https://www.facebook.com/share/p/1exGpxarnX/) |
| Publication topic | Hosting a static website on Amazon S3 securely with CloudFront and Origin Access Control |

{{< figure src="/images/blogs/blog3.png" alt="Cover image: Static websites on S3, public bucket or CloudFront + OAC?" caption="Figure 3.3. Cover image used in the Facebook post." >}}

One of my first labs was hosting a static website on Amazon S3. Upload `index.html`, enable static website hosting, click the link, and the site is live. It felt like magic 😄 But reading the steps more carefully, I noticed that to make it work I had turned off Block Public Access and let the whole world read the bucket. The S3 workshop on First Cloud Journey doesn't stop there: the later part blocks all public access again and puts CloudFront in front. This post compares the two approaches and records the mistakes I made.

## Option A: S3 website endpoint with a public bucket

Steps: create a bucket, upload the files, enable static website hosting, turn off Block Public Access, and add a bucket policy that allows `s3:GetObject` for Principal `"*"`.

- **Pros:** fast, simple and great for learning S3.
- **Cons:** the website endpoint only serves HTTP, not HTTPS; the bucket is public so anyone can read it directly; and there is no caching close to users.

## Option B: CloudFront with Origin Access Control (OAC)

The idea: the bucket stays completely private and users only reach it through CloudFront. CloudFront signs each request to S3 with SigV4, and the bucket policy only accepts requests from that specific distribution.

1. Turn **Block all public access** back on for the bucket.
2. Create a CloudFront distribution and choose the S3 bucket's **REST endpoint** as the origin, not the website endpoint.
3. Under Origin access, choose **Origin access control settings (recommended)**, create an OAC and keep the signing behavior as **Sign requests**.
4. Update the bucket policy: Principal `cloudfront.amazonaws.com` with an `AWS:SourceArn` condition equal to the distribution's ARN. The console has a button to copy this policy.
5. Set the **Default root object** to `index.html`.

## How is OAC different from OAI?

I came across both terms. OAI (Origin Access Identity) is the older method that AWS now calls legacy. OAC was introduced in 2022 and is the recommended approach because it:

- uses SigV4 signing and supports all S3 Regions,
- supports buckets encrypted with SSE-KMS, which OAI doesn't,
- supports more HTTP methods.

If an older project still uses OAI, AWS has a guide for migrating to OAC.

## Mistakes I ran into

- **403 Access Denied right after creating the distribution:** I forgot to paste the bucket policy, or pasted the wrong distribution ARN.
- **Choosing the website endpoint as the origin:** OAC doesn't work with the S3 website endpoint because CloudFront treats it as a public custom origin. You need the bucket's REST endpoint.
- **`/about/` returns an error:** the default root object only applies to `/`. Unlike the website endpoint, it doesn't add `index.html` for subfolders. The fix is a CloudFront Function that rewrites the URL.
- **Edited a file but the site didn't change:** CloudFront was serving the cached copy. Create an invalidation (for example `/*`) or use versioned file names.

## Which one to choose

- **Learning or a quick internal demo:** Option A is fine, as long as you clean up afterwards.
- **A website for real users:** Option B. You get HTTPS, a custom domain with ACM, edge caching and the option to add AWS WAF, and the bucket never has to be public.
- Interestingly, the FCJ workshop notes that AWS now recommends **AWS Amplify Hosting** for static websites. Amplify sets up CloudFront, S3 and CI/CD for you, and the S3 lab helps you understand what Amplify does underneath.

## Takeaway

Both approaches end with "the website works", but they are very different in terms of security. My biggest lesson: don't make a bucket public just because it's the fastest way to see a result. Keeping S3 private and letting CloudFront be the front door is a habit worth building from the start.

## References

- [Amazon CloudFront: Restrict access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html)
- [AWS re:Post Knowledge Center: Configure OAC and migrate from OAI](https://repost.aws/knowledge-center/cloudfront-oac-origins)
- [AWS DevOps Blog: CDK L2 construct for CloudFront OAC](https://aws.amazon.com/blogs/devops/a-new-aws-cdk-l2-construct-for-amazon-cloudfront-origin-access-control-oac)

## Hands-on labs on First Cloud Journey

- [S3 Static Website + CloudFront](https://000057.awsfcaj.com)
- [CloudFront with an S3 origin](https://000094.awsfcaj.com)
- [CloudFront & Lambda@Edge](https://000130.awsfcaj.com)
- [AWS WAF](https://000026.awsfcaj.com)
