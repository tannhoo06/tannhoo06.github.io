---
title: "Prepare Lightsail and private RDS"
date: 2026-11-20
weight: 4
chapter: false
pre: " <b>5.4.</b> "
---

## 1. Create the Lightsail host and origin DNS

1. In **Lightsail → Instances → Create instance**, choose **Singapore**, **Linux/Unix → OS Only → Ubuntu 24.04 LTS**, and an x86-64 bundle with a public IPv4 address and at least 2 GB RAM. Name it `ownword-lab`. Save the private IPv4 from the instance page. Select an SSH key you already hold or download the matching private key from the Lightsail account's SSH keys page.
2. Create a static IPv4 in Singapore and attach it to the instance. In your DNS provider, point your origin subdomain, for example `origin-lab.example.com`, directly to that address with an A record (DNS-only if your provider offers a proxy). If you do not own a domain, skip the DNS record and use `origin-lab.<A-B-C-D>.sslip.io` (your static IPv4 with hyphens instead of dots) as the origin hostname; `sslip.io` resolves it to your instance automatically so Caddy can issue a public TLS certificate. The public app hostname is configured with CloudFront in chapter 5.5.
3. In the Lightsail networking firewall, allow TCP 80 and 443 for Caddy's public certificate validation and HTTPS. Restrict TCP 22 to your workstation's public IP. If you use Lightsail browser SSH, enable its separate access option. Leave ports 3000 and 5432 closed on the internet. Review IPv6 rules separately if enabled. [Lightsail instance creation](https://docs.aws.amazon.com/lightsail/latest/userguide/getting-started.html) · [Static IP](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-create-static-ip.html) · [Lightsail firewall](https://docs.aws.amazon.com/lightsail/latest/userguide/understanding-firewall-and-port-mappings-in-amazon-lightsail.html)

**Checkpoint.** The instance is running, your origin hostname resolves to the static IPv4, and you can connect as `ubuntu`.

## 2. Create a private PostgreSQL instance

1. In **Lightsail → Account → Advanced**, enable **VPC peering** for Singapore. The receiving VPC must be the account's default VPC in Singapore. In the VPC console, confirm that the peering connection is active and the route tables for the RDS subnets have a route to the Lightsail network through that peering connection. Use the actual routes and CIDRs shown in your account.
2. In that default VPC, use a DB subnet group covering at least two Availability Zones. Create a dedicated security group for the DB with inbound TCP 5432 from the Lightsail instance's private IPv4 /32. Attach that group to RDS and remove any broader ingress that the creation wizard added.
3. In **RDS → Databases → Create database → Standard create**, select **PostgreSQL 16**, a **Single DB instance**, `db.t4g.micro` if available, and 20 GiB encrypted gp3. Select the default VPC, DB subnet group and security group from steps 1-2. Set **Public access: No**, port 5432, at least one day of automated backup retention, and deletion protection. Use a lab administrator password stored privately. Leave the initial database name blank so you can create it with the correct owner below. [Lightsail VPC peering](https://docs.aws.amazon.com/lightsail/latest/userguide/lightsail-how-to-set-up-vpc-peering-with-aws-resources.html) · [RDS VPC and subnet groups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html) · [Create an RDS DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_CreateDBInstance.html)

**Checkpoint.** RDS is **Available**, reports **Publicly accessible: No**, and gives you its DNS endpoint. Use that endpoint for TLS hostname verification.

## 3. Transfer the source and bootstrap Ubuntu

**On your workstation.** Open a shell where you saved the archive and fill in the SSH key path and IP for your instance.

```bash
KEY="$HOME/.ssh/ownword-lab.pem"
LIGHTSAIL_IP='YOUR_LIGHTSAIL_STATIC_IPV4'
scp -i "$KEY" ownword-lab-source-c8a903e.tar.gz "ubuntu@$LIGHTSAIL_IP:~/"
ssh -i "$KEY" "ubuntu@$LIGHTSAIL_IP"
```

**In the Lightsail SSH session.** Unpack the archive into a new directory and run the setup script. Disconnect and sign back in so your user picks up its Docker group membership.

```bash
mkdir "$HOME/ownword-lab"
tar -xzf "$HOME/ownword-lab-source-c8a903e.tar.gz" -C "$HOME/ownword-lab"
cd "$HOME/ownword-lab"
bash deploy/lightsail/bootstrap-ubuntu.sh
```

After reconnecting:

```bash
cd "$HOME/ownword-lab"
docker compose version
free -h
docker pull postgres:16-alpine
install -d -m 700 deploy/lightsail/.secrets
curl -fsSL https://truststore.pki.rds.amazonaws.com/global/global-bundle.pem \
  -o deploy/lightsail/.secrets/rds-ca.pem
chmod 644 deploy/lightsail/.secrets/rds-ca.pem
```

The setup script installs Docker and Compose and adds 2 GiB of swap. The RDS CA bundle is public. Later, you'll also store private environment files in `.secrets`. [Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/) · [RDS CA bundles](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html)

## 4. Create the application and backup logins

**In the Lightsail SSH session.** Fill in your RDS endpoint and administrator name. Enter the administrator password when the container prompts you. With `verify-full`, PostgreSQL checks the certificate chain and matches the certificate to the endpoint hostname.

```bash
cd "$HOME/ownword-lab"
RDS_HOST='YOUR_RDS_ENDPOINT'
RDS_ADMIN='YOUR_RDS_MASTER_USERNAME'
docker run --rm -it \
  --mount "type=bind,source=$PWD/deploy/lightsail/.secrets/rds-ca.pem,target=/rds-ca.pem,readonly" \
  -e PGSSLMODE=verify-full -e PGSSLROOTCERT=/rds-ca.pem \
  postgres:16-alpine psql -h "$RDS_HOST" -p 5432 -U "$RDS_ADMIN" -d postgres -W
```

**Inside `psql`.** Run the statements once on the new instance. Generate two different random passwords, for example with `openssl rand -hex 32`, and enter them when prompted. The application login will own the database and run the Drizzle migrations. In chapter 5.6, you'll grant the backup login read access once the schema exists.

```text
\set ON_ERROR_STOP on
\conninfo
CREATE ROLE ownword_app LOGIN;
\password ownword_app
CREATE ROLE ownword_backup LOGIN;
\password ownword_backup
GRANT ownword_app TO CURRENT_USER WITH SET TRUE;
CREATE DATABASE ownword OWNER ownword_app;
\q
```

**Checkpoint.** Check that `\conninfo` reports SSL and that both roles and the database exist. If the connection times out, check the peering connection, subnet routes, and the private IPv4 in the security group. For a certificate error, confirm you're using the RDS endpoint and the AWS CA bundle. [RDS PostgreSQL TLS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/PostgreSQL.Concepts.General.SSL.html) · [PostgreSQL database ownership](https://www.postgresql.org/docs/16/sql-createdatabase.html)

{{< figure src="/images/workshop/production-rds-tls.png" alt="PostgreSQL session reporting SSL enabled and TLSv1.3" caption="A read-only check from the running Ownword app on Lightsail confirmed a TLS 1.3 connection to production Amazon RDS in Singapore." >}}

[Next: Configure sign-in, deploy the app and connect CloudFront](../5.5-auth/)
