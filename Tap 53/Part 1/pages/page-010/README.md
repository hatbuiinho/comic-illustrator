# Page 010 package

Page 10 là một package độc lập. Khi xử lý page này, chỉ đọc `layout.json`,
option manifest và các nguồn chung bắt buộc của Tap 53/Part 1. Không nạp
storyboard, output hoặc context của page khác trừ khi manifest ghi rõ một
`continuityInput` tóm tắt.

QA riêng cho page:

```bash
node ../../scripts/layout-frame-qa.js layout.json
```

Manifest tổng `Part 1/scripts/layout_frames.json` được giữ lại để tương thích
ngược; thay đổi mới nên thực hiện trong package page này trước.
