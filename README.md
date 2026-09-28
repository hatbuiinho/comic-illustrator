# Comic Illustration Project

Project tổ chức workflow minh họa truyện tranh bằng các skill repo-scoped trong
`.agents/skills/`. Quy tắc chung nằm trong `AGENTS.md`; dữ liệu và ngoại lệ nằm
trong từng thư mục tập.

## Cấu trúc

```text
.agents/skills/       Workflow dùng chung
AGENTS.md             Quy tắc nền và routing
Tap 53/               Dữ liệu riêng của Tập 53
  notes.md            Dữ kiện và ngoại lệ cấp tập
  shot_notes.md       Continuity/nhịp shot riêng của tập
  characters/         Profile nhân vật
  Part 1/, Part 2/    Layout, page, output và QA theo part
```

## Các skill

| Skill | Dùng khi |
| --- | --- |
| `comic-page-guide` | Dẫn người dùng từng bước và xin xác nhận tại mỗi cổng |
| `comic-production` | Làm một page/frame hoàn chỉnh qua nhiều giai đoạn |
| `comic-source-reader` | Đọc và kiểm chứng nguồn |
| `comic-shot-design` | Lên storyboard hoặc composition |
| `comic-prompt-writer` | Viết prompt từ shot đã chọn |
| `comic-image-production` | Tạo/chỉnh/variant ảnh |
| `comic-visual-qa` | QA profile, style, context và storytelling |
| `comic-layout-qa` | QA ảnh trong layout |
| `comic-delivery` | Lưu bản đã duyệt vào `approved/` |

Codex có thể tự chọn skill theo mô tả. Có thể gọi trực tiếp bằng `$ten-skill`
khi muốn khóa workflow cụ thể.

## Ví dụ yêu cầu

```text
Mình muốn làm minh họa cho một page nhưng chưa biết bắt đầu từ đâu.
```

```text
Phân tích Tap 53, Part 2, page 11; chưa tạo ảnh.
```

```text
Đưa ra ba phương án storyboard cho frame 1 của page 11.
```

```text
Viết prompt hoàn chỉnh theo phương án 2; chưa tạo ảnh.
```

```text
Tạo ảnh theo phương án 2, không cần tránh gáy trong deliverable này.
```

## Override kiểm tra

Kiểm tra điều kiện có ba trạng thái:

- `REQUIRED`: áp dụng và có thể làm QA thất bại.
- `NOT_APPLICABLE`: không liên quan đến deliverable.
- `SKIPPED_BY_USER`: người dùng chủ động bỏ qua trong phạm vi đã nêu.

Ví dụ “không cần tránh gáy” làm check `spine` thành `SKIPPED_BY_USER`; script
vẫn có thể vẽ guide để tham khảo nhưng không đánh FAIL vì giao với gáy.

## Layout QA

```text
node .agents/skills/comic-layout-qa/scripts/layout-frame-qa.js <manifest.json> <output-directory>
```

Hoặc với page package có `layout.json`:

```text
node .agents/skills/comic-layout-qa/scripts/run-page-qa.js <page-directory>
```

Script tạo `frame-report.md`, `frame-report.json` và overlay SVG trên raster
layout gốc có text.

## Quy tắc output

Ảnh tạo mới nằm trong `outputs/` và có version riêng. Chỉ dùng
`comic-delivery` sau khi QA phù hợp đã PASS và người dùng chọn rõ output. Không
ghi đè file đã duyệt.
