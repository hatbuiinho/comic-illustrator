# Comic Project — Claude Instructions

Chỉ dẫn chung, routing workflow và khóa phong cách nằm trong `AGENTS.md`
(dùng chung cho mọi agent):

@AGENTS.md

## Ngôn ngữ
- Trả lời bằng tiếng Việt. Giữ nguyên thuật ngữ kỹ thuật và tên file.

## Quy tắc tiết kiệm token
- Trả lời trực tiếp, không viết lời mở đầu/kết thúc xã giao.
- Không tự ý đọc toàn bộ thư mục. Chỉ đọc file được chỉ định.
- Không chạy lệnh build/test toàn project trừ khi được yêu cầu.
- Khi cần ngữ cảnh nhân vật hoặc cảnh, chỉ đọc file `.md` profile, KHÔNG mở file `.png`.

## Skill trong Claude Code
- `.claude/skills` là symlink tới `.agents/skills/`; chỉ sửa skill tại `.agents/skills/`.
- Gọi skill bằng `/<ten-skill>` (ví dụ `/comic-page-guide`). `comic-production`
  chỉ dùng khi người dùng gọi đích danh, theo `comic-illustrator/contract.md`.
- `agents/openai.yaml` trong mỗi skill là cấu hình riêng của Codex; Claude bỏ qua.

## Cấu trúc project
- `AGENTS.md` — Chỉ dẫn chung và routing workflow.
- `comic-illustrator/` — Workflow minh họa tập: contract, dữ liệu tập, tham khảo.
- `comic-illustrator/Tap XX/notes.md` — Dữ kiện và ngoại lệ theo tập.
- `comic-illustrator/Tap XX/shot_notes.md` — Continuity notes.
- `comic-illustrator/Tap XX/Part N/part-config.json` — Cấu hình từng part.
- `.agents/skills/` — 10 skill chuyên môn, chỉ đọc skill liên quan.

## Thứ tự ưu tiên
Theo mục **Thứ tự ưu tiên trong project** của `AGENTS.md`; với minh họa tập,
theo bản chi tiết trong `comic-illustrator/contract.md`.
