# Workflow compatibility

Workflow dùng chung đã chuyển sang `.agents/skills/`; routing theo `AGENTS.md`.

- Entry point mặc định cho mọi yêu cầu minh họa: `comic-page-guide`.
- Đọc nguồn: `comic-source-reader`.
- Storyboard: `comic-shot-design`.
- Prompt và tạo ảnh: `comic-prompt-writer`, `comic-image-production`.
- QA: `comic-visual-qa`, `comic-layout-qa`.
- Bàn giao: `comic-delivery`.
- `comic-production`: chỉ khi người dùng gọi đích danh.

File này chỉ giữ đường dẫn tương thích cho manifest và tài liệu lịch sử. Không
thêm quy tắc workflow mới tại đây.
