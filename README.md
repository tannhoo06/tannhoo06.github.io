# Mẫu báo cáo thực tập Ownword cho các thành viên Gi Group

Thư mục này có sẵn toàn bộ mã nguồn để bạn tự tạo và đăng trang báo cáo thực tập song ngữ (tiếng Anh và tiếng Việt) lên GitHub Pages.

## Phần dùng chung của nhóm (giữ nguyên)

Ba phần dưới đây cả nhóm dùng chung nên bạn không cần viết lại:

- Đề xuất dự án (`content/2-Proposal/`)
- Ba bài blog đã đăng trên AWS Study Group (`content/3-BlogsPosted/`)
- Toàn bộ bài Workshop triển khai Ownword trên AWS (`content/5-Workshop/`), gồm sơ đồ kiến trúc, bảng chi phí và kết quả kiểm chứng

## Những việc bạn cần tự làm trước khi nộp

Các phần dưới đây bắt buộc phải là nội dung riêng của từng người. Mọi trang đều có hai bản: file `.md` cho tiếng Anh và file `.vi.md` cho tiếng Việt.

1. Điền tên và thông tin cá nhân của bạn. Đổi dòng `[YOUR FULL NAME]` trong `config.toml` thành tên bạn, sau đó điền họ tên, số điện thoại, email, trường và chuyên ngành ở trang chủ (`content/_index.md` và `content/_index.vi.md`). Nếu muốn hiển thị ảnh chân dung, thay tệp `static/images/profile-placeholder.svg` bằng ảnh của bạn.
2. Viết lại nhật ký công việc từ Tuần 1 đến Tuần 12 (`content/1-Worklog/`). Thay các ô mẫu bằng công việc bạn đã học và làm mỗi tuần, gắn ảnh chụp màn hình bài lab của riêng bạn vào thư mục `static/images/worklog/` và nhớ che Account ID hoặc thông tin riêng tư.
3. Viết lại hoàn toàn mục Sự kiện đã tham gia (`content/4-EventParticipated/`). Xóa 3 sự kiện mẫu và thay bằng 3 sự kiện bạn thực sự tham dự, kèm bài viết của chính bạn và ảnh check-in thấy rõ khuôn mặt (xóa hết các ảnh mẫu cũ trong `static/images/events/` để tránh sót ảnh thẻ tên của thành viên khác, rồi thay bằng ảnh của riêng bạn).
4. Làm phần Tự đánh giá (`content/6-Self-evaluation/`). Đổi ô `⬜` sang `✅` ở mức phù hợp với bạn, sau đó tự viết phần đóng góp của bạn trong dự án Ownword và những điểm muốn cải thiện.
5. Viết phần Chia sẻ và góp ý (`content/7-Feedback/`) theo trải nghiệm thực tập của riêng bạn.

## Xem thử báo cáo trên máy

Nếu muốn mở xem giao diện trước khi đưa lên mạng, tải [Hugo Extended 0.134.3](https://github.com/gohugoio/hugo/releases/tag/v0.134.3) rồi chạy lệnh sau ngay tại thư mục này:

```sh
hugo server --bind 127.0.0.1
```

Mở đường dẫn hiện trên terminal (thường là `http://127.0.0.1:1313/`) để kiểm tra cả bản tiếng Anh và tiếng Việt.

## Đưa báo cáo lên GitHub Pages và nộp bài

1. Tạo một kho GitHub riêng của bạn và đẩy toàn bộ thư mục này lên đó.
2. Sau khi đã thay hết các phần cá nhân và kiểm tra kỹ hai ngôn ngữ, tạo một tệp trống tên là `REPORT_READY.md` ngay tại thư mục gốc rồi commit và push lên GitHub. Tệp này là chốt kiểm tra để tránh đăng nhầm bản chưa làm xong.
3. Trong phần Settings -> Pages của kho GitHub, chọn nhánh nguồn là `gh-pages`.
4. Mở tab Actions, chọn workflow Deploy Hugo site to GitHub Pages và bấm chạy thủ công.
5. Mở link GitHub Pages của bạn kiểm tra lần cuối, rồi nộp link đó vào mục Workshop Submission trên FCAJ Portal. Link demo ứng dụng `https://app.ownword.co/` đã gắn sẵn bên trong báo cáo, không nộp link app thay cho link báo cáo.
