# Comic Project — Claude Instructions

## Ngôn ngữ
- Trả lời bằng tiếng Việt. Giữ nguyên thuật ngữ kỹ thuật và tên file.

## Quy tắc tiết kiệm token
- Trả lời trực tiếp, không viết lời mở đầu/kết thúc xã giao.
- Không tự ý đọc toàn bộ thư mục. Chỉ đọc file được chỉ định.
- Không chạy lệnh build/test toàn project trừ khi được yêu cầu.
- Khi cần ngữ cảnh nhân vật hoặc cảnh, chỉ đọc file `.md` profile, KHÔNG mở file `.png`.

## Cấu trúc project
- `AGENTS.md` — Chỉ dẫn chung và routing skill.
- `Tap XX/notes.md` — Dữ kiện và ngoại lệ theo tập.
- `Tap XX/shot_notes.md` — Continuity notes.
- `Tap XX/Part N/part-config.json` — Cấu hình từng part.
- `.agents/skills/` — 10 skill chuyên môn, chỉ đọc skill liên quan.

## Thứ tự ưu tiên
1. Yêu cầu trực tiếp của người dùng
2. `notes.md` → `shot_notes.md` của đúng tập
3. Skill phù hợp trong `.agents/skills/`
4. Quy tắc trong file này
