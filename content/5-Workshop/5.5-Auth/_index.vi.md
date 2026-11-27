---
title: "Cấu hình đăng nhập, triển khai Ownword và kết nối CloudFront"
date: 2026-11-20
weight: 5
chapter: false
pre: " <b>5.5.</b> "
---

## 1. Tạo user pool Cognito và app client công khai {#base-cognito}

1. Trong **Amazon Cognito tại Singapore**, tạo user pool cho lab. Bật đăng nhập bằng email, xác thực bằng mật khẩu, tự đăng ký và xác minh email. Chỉ đặt email là thuộc tính bắt buộc để biểu mẫu Ownword có thể đăng ký tài khoản. Tạo app client công khai không có secret, ví dụ loại **Single-page application**. Dùng email đã xác minh để khôi phục tài khoản.
2. Trong cài đặt đăng nhập, bật nhà cung cấp **Cognito user pool**, **Authorization code grant** và scope `openid email profile`. Dùng tên miền công khai của lab cho callback `https://app-lab.example.com/auth/callback` và URL đăng xuất `https://app-lab.example.com/`. Tạo tên miền prefix Cognito và gán giao diện managed login nếu cần.
3. Trong **Authentication flows**, bật đăng nhập bằng tên người dùng và mật khẩu (`ALLOW_USER_PASSWORD_AUTH`). Máy chủ Ownword dùng `USER_PASSWORD_AUTH` cho biểu mẫu riêng và OAuth code grant với PKCE khi dùng managed login. Ghi lại pool ID, client ID và tên miền Cognito. [App client Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html) · [OAuth và PKCE](https://docs.aws.amazon.com/cognito/latest/developerguide/authorization-endpoint.html) · [Luồng xác thực qua API](https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_CreateUserPoolClient.html)

## 2. Cấu hình Google và liên kết tài khoản đã xác minh

1. Trong Google Auth Platform, cấu hình **Branding** và **Audience** cho dự án lab. Với tên miền prefix của Cognito, thêm `amazoncognito.com` vào authorized domains. Yêu cầu các scope OpenID, email và profile cơ bản. Tạo OAuth client loại **Web application**. Nếu dự án Google đang ở chế độ kiểm thử, thêm các tài khoản lab vào danh sách test users.
2. Đặt **Authorized JavaScript origins** thành `https://YOUR_PREFIX.auth.ap-southeast-1.amazoncognito.com` và thêm `/oauth2/idpresponse` vào tên miền đó cho **Authorized redirect URIs**. Thêm **Google** vào Cognito với client ID và secret của Google, yêu cầu `openid email profile` và ánh xạ `email`, `email_verified` vào thuộc tính tương ứng. Bật **Google** cùng **Cognito user pool** trên app client và cho phép ghi các thuộc tính được ánh xạ. [Cấu hình đăng nhập Google](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-social-idp-google.html) · [Ánh xạ thuộc tính Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-specifying-attribute-mapping.html)
3. Tải {{< workshop-download "downloads/google-linker-cloudshell.py" "script liên kết tài khoản tại Singapore" >}} rồi đưa tệp lên thư mục home trong **CloudShell tại Singapore**. Chạy kiểm tra trước và đối chiếu tài khoản, pool và ánh xạ. Chỉ dùng `--apply` với pool lab. Ghi lại tên hàm và role được tạo. Chờ ít nhất 70 giây để cấu hình có hiệu lực trước khi thử đăng nhập Google lần đầu. [Trigger Pre sign-up](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-sign-up.html) · [Liên kết danh tính bên ngoài](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-federation-consolidate-users.html)

```bash
POOL_ID='ap-southeast-1_YOUR_LAB_POOL_SUFFIX'
python3 ~/google-linker-cloudshell.py --pool-id "$POOL_ID"
python3 ~/google-linker-cloudshell.py --pool-id "$POOL_ID" --apply
aws cognito-idp describe-user-pool --region ap-southeast-1 --user-pool-id "$POOL_ID" \
  --query 'UserPool.LambdaConfig.PreSignUp' --output text
```

Nếu lệnh `--apply` dừng giữa chừng, dùng phần sau dấu gạch dưới trong pool ID để tìm các tài nguyên lab đã tạo. Tên Lambda là `ownword-google-link-<suffix>`, role là `ownword-google-link-role-<suffix>` và log group là `/aws/lambda/ownword-google-link-<suffix>`. Kiểm tra cấu hình trigger trước khi thử lại. Nếu cần làm lại bước này, gỡ trigger mới nếu đã được gắn rồi xóa đúng Lambda, role và log group của lần chạy lỗi. Giữ pool và OAuth client để dùng lại.

## 3. Chuẩn bị thông tin xác thực cho dịch vụ mô hình

1. Kiểm tra tài khoản có gọi được inference profile Kimi K3.1 Pro U.S. từ **Bắc Virginia** không. Nếu AWS yêu cầu cấp quyền hoặc đăng ký với nhà cung cấp, hoàn tất bước đó. Dù profile báo Active, bạn vẫn cần thử quyền gọi mô hình. Chạy các lệnh trong **CloudShell tại Bắc Virginia** bằng tài khoản quản trị có quyền đọc profile. Policy tạo ra sẽ dùng ARN của profile và của từng mô hình đích. Kiểm tra cả hai kết quả trước khi gắn policy. [Quyền truy cập Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) · [Quyền IAM cho inference profile](https://docs.aws.amazon.com/bedrock/latest/userguide/inference-profiles-prereq.html) · [GetInferenceProfile CLI](https://docs.aws.amazon.com/cli/latest/reference/bedrock/get-inference-profile.html)

```bash
aws bedrock get-inference-profile --region us-east-1 \
  --inference-profile-identifier us.moonshotai.kimi-k3.1 > ownword-lab-profile.json
jq -e '.status == "ACTIVE" and (.models | length > 0)' ownword-lab-profile.json
jq '{
  Version: "2012-10-17",
  Statement: [
    {Effect:"Allow", Action:"bedrock:InvokeModel", Resource:.inferenceProfileArn},
    {Effect:"Allow", Action:"bedrock:InvokeModel", Resource:[.models[].modelArn],
     Condition:{StringEquals:{"bedrock:InferenceProfileArn":.inferenceProfileArn}}}
  ]
}' ownword-lab-profile.json > ownword-lab-bedrock-policy.json
```

2. Gắn inline policy vào một danh tính dành riêng cho ứng dụng lab, chẳng hạn IAM user `ownword-lab-bedrock` chỉ truy cập qua API. Giữ riêng thông tin xác thực của ứng dụng, tài khoản quản trị và IAM user sao lưu. Nếu dùng thông tin xác thực tạm thời, nhớ nhập session token và cập nhật trước khi hết hạn. [Khóa truy cập IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html) · [Quyền gọi Bedrock Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html)
3. Tạo hai khóa OpenRouter cho lab. Dùng một khóa cho từ vựng và chấm bài luyện tập. Khóa còn lại cần gọi được tuyến GPT-6.1 Terra Low với đầu ra có cấu trúc nghiêm ngặt và không lưu dữ liệu. Đặt giới hạn chi tiêu tại nhà cung cấp. Nếu lượt gọi bị từ chối, ghi lại lỗi và xác nhận quyền truy cập trước khi đánh dấu bước này đã xong.

## 4. Build và chạy ứng dụng với RDS {#launch-app}

Bước này build container ứng dụng trên Lightsail, chạy các migration PostgreSQL lên RDS và khởi động Caddy cùng Next.js.

**Trong phiên SSH trên Lightsail.** Tạo hai tệp môi trường trong thư mục vừa giải nén. Nhập thông tin bí mật qua trình soạn thảo. Dùng một mật khẩu hex ngẫu nhiên riêng cho mỗi role cơ sở dữ liệu để dễ điền vào tệp.

```bash
cd "$HOME/ownword-lab"
umask 077
cp deploy/lightsail/.env.example deploy/lightsail/.env
chmod 600 deploy/lightsail/.env
nano deploy/lightsail/.env
nano deploy/lightsail/.secrets/app-rds.env
```

Điền các giá trị sau trong `deploy/lightsail/.env`:

| Biến | Giá trị lab |
|---|---|
| `APP_DOMAIN` | Chỉ tên máy chủ gốc, ví dụ `origin-lab.example.com` |
| `APP_PUBLIC_ORIGIN` | URL công khai, ví dụ `https://app-lab.example.com` |
| `COGNITO_ISSUER` | `https://cognito-idp.ap-southeast-1.amazonaws.com/YOUR_POOL_ID` |
| `COGNITO_DOMAIN` và `COGNITO_CLIENT_ID` | URL đầy đủ của tên miền prefix Cognito và ID client công khai ở bước 1 |
| `CUSTOM_AUTH_ENABLED` và `GOOGLE_SIGN_IN_ENABLED` | Cả hai là `true` sau bước 1 và 2 |
| `POSTGRES_PASSWORD` | Giá trị ngẫu nhiên riêng cho dịch vụ DB cục bộ trong Compose gốc. Tệp ghi đè RDS cung cấp mật khẩu ứng dụng thực tế. |
| `OPENROUTER_API_KEY` và `OPENROUTER_MODEL` | Khóa từ vựng của lab và mô hình tương thích đã kiểm tra. Gói mã mặc định là `google/gemini-3.6-flash`. |
| `BEDROCK_CONCEPT_MODEL` | `us.moonshotai.kimi-k3.1` |
| `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN` | Thông tin xác thực Bedrock từ bước 3. Nếu dùng khóa IAM dài hạn, để trống token. |
| `WRITING_MODULE_ENABLED` và `WRITING_TERRA_ENABLED` | Cả hai là `true` |
| `WRITING_TERRA_OPENROUTER_API_KEY`, `WRITING_TRENDS_ENABLED` | Khóa đánh giá bài viết riêng và `false` cho tính năng xu hướng |

Nhập vào `deploy/lightsail/.secrets/app-rds.env`:

```dotenv
OWNWORD_RDS_HOST=YOUR_RDS_ENDPOINT
OWNWORD_RDS_DATABASE=ownword
OWNWORD_RDS_USER=ownword_app
OWNWORD_RDS_PASSWORD=YOUR_APP_ROLE_PASSWORD
OWNWORD_RDS_CA_FILE=/home/ubuntu/ownword-lab/deploy/lightsail/.secrets/rds-ca.pem
```

Lưu hàm bên dưới để các lệnh migration và ứng dụng dùng cùng hai tệp môi trường và cấu hình RDS. Khi mở phiên SSH mới, nạp lại hàm bằng `source` rồi dùng `ownword_compose` cho lab. Cờ `--no-deps` giữ dịch vụ `db` cục bộ trong tệp Compose gốc ở trạng thái tắt.

```bash
cat > "$HOME/ownword-lab/compose-lab.sh" <<'EOF'
ownword_compose() {
  local app_root="$HOME/ownword-lab"
  docker compose --project-name ownword \
    --env-file "$app_root/deploy/lightsail/.env" \
    --env-file "$app_root/deploy/lightsail/.secrets/app-rds.env" \
    -f "$app_root/deploy/lightsail/compose.yaml" \
    -f "$app_root/deploy/lightsail/compose.rds.yaml" "$@"
}
EOF
source "$HOME/ownword-lab/compose-lab.sh"
ownword_compose config --quiet &&
  ownword_compose build app &&
  ownword_compose --profile tools run --rm --no-deps migrate &&
  ownword_compose up -d --no-deps app web &&
  ownword_compose ps
```

**Điểm kiểm tra.** Migration chạy thành công, Compose báo `app` và `web` đang chạy. Từ máy cá nhân, `curl -fsS https://origin-lab.example.com/ -o /dev/null` thành công với chứng chỉ máy chủ gốc hợp lệ. Nếu lỗi, kiểm tra bản ghi A, cổng Lightsail và `ownword_compose logs --tail=60 web app`.

## 5. Đưa ứng dụng ra Internet qua CloudFront và AWS WAF

{{% notice tip %}}
Nếu không có tên miền riêng, bạn không cần thuê tên miền cho bài lab này. Bỏ qua bước 1 (ACM) và bước 5 (DNS CNAME), để trống **Alternate domain names** ở bước 2 để CloudFront dùng chứng chỉ mặc định `*.cloudfront.net`, rồi dùng `https://<distribution>.cloudfront.net` cho `APP_PUBLIC_ORIGIN` trong `deploy/lightsail/.env` và cho URL callback, đăng xuất của Cognito ở mục 1.
{{% /notice %}}

1. Trong **ACM tại Bắc Virginia**, yêu cầu chứng chỉ công khai cho tên miền công khai. Thêm CNAME do ACM cung cấp vào DNS và chờ **Issued**. Giữ bản ghi để gia hạn. Caddy phục vụ chứng chỉ riêng cho máy chủ gốc. [Yêu cầu chứng chỉ CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cnames-and-https-requirements.html) · [Xác thực DNS của ACM](https://docs.aws.amazon.com/acm/latest/userguide/dns-validation.html)
2. Tạo standard CloudFront distribution với custom origin. Dùng tên máy chủ gốc, để trống origin path, chọn **HTTPS only** qua cổng 443 cho origin và **Redirect HTTP to HTTPS** cho người dùng. Thêm tên miền công khai vào alternate domain names và chọn chứng chỉ ACM. Chọn trả theo mức sử dụng để có thể xóa distribution sau bài lab. [Cài đặt origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesOrigin.html) · [Cài đặt distribution](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html)
3. Trong behavior mặc định, cho phép tất cả phương thức HTTP để ứng dụng xử lý POST và các thao tác ghi khác. Chọn **CachingDisabled** và origin request policy **AllViewerExceptHostHeader**. Cookie, chuỗi truy vấn và header người dùng được chuyển tiếp. CloudFront dùng tên máy chủ gốc trong `Host` để khớp cấu hình Caddy và chứng chỉ. Điều này giữ nguyên callback OAuth, cookie phiên và kiểm tra cùng nguồn. Chọn thời gian chờ origin phù hợp với lượt gọi AI rồi kiểm chứng bằng yêu cầu thử nghiệm. [Cài đặt cache behavior](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/DownloadDistValuesCacheBehavior.html) · [Cache policy có sẵn](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-cache-policies.html) · [Origin request policy có sẵn](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-managed-origin-request-policies.html)
4. Gắn AWS WAF web ACL phạm vi CloudFront. Trong lab, thêm nhóm quy tắc như **AWSManagedRulesCommonRuleSet** và đặt hành động từng quy tắc thành Count. Sau bước cấu hình DNS, thử đăng nhập và đánh giá bài viết bình thường, rồi xem yêu cầu mẫu trước khi chuyển sang chặn. Web ACL bảo vệ lưu lượng đi qua CloudFront. [Gắn web ACL](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-associating-aws-resource.html) · [Thử nghiệm quy tắc WAF](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html)
5. Khi distribution báo **Deployed**, tạo CNAME DNS trỏ tên miền công khai của lab tới tên distribution, hoặc dùng alias trong Route 53. Giữ bản ghi A của máy chủ gốc trỏ tới Lightsail. Chạy lệnh sau tại máy cá nhân với tên miền công khai của lab. [Tên miền thay thế CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/CNAMEs.html)

```bash
LAB_HOST='app-lab.example.com'
curl -fsS -D - -o /dev/null "https://$LAB_HOST/"
curl -fsS -D - -o /dev/null "https://$LAB_HOST/auth/signin?hosted=1"
```

**Điểm kiểm tra.** Trang chủ trả 200 qua CloudFront, còn URL managed login chuyển bạn sang Cognito với callback công khai. Dùng biểu mẫu Ownword để đăng ký và xác minh email thử. Đăng nhập, lưu một từ rồi đăng xuất. Dùng Google với cùng email đó để đăng nhập lần đầu vào pool. Bạn sẽ thấy lại WordBoard cũ. Thử thêm một tài khoản Google khác để kiểm tra bảng từ riêng. Nếu CloudFront trả 502, xem DNS, TLS máy chủ gốc và header Host. Nếu Cognito từ chối chuyển hướng, đối chiếu từng ký tự của URL callback và đăng xuất.

{{< figure src="/images/workshop/production-wordboard.png" alt="WordBoard hiển thị các từ đã lưu tại app.ownword.co qua HTTPS" caption="Sau khi đăng nhập, người học mở WordBoard qua HTTPS trên ứng dụng đang vận hành và xem các từ đã lưu." >}}

[Tiếp theo: Sao lưu RDS và cấu hình giám sát](../5.6-operations/)
