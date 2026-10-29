# Comic Illustrator

Workflow minh họa truyện tranh theo tập/part/page/frame. Mọi tài liệu, dữ
liệu tập và tài liệu tham khảo của workflow nằm trong thư mục này. Quy tắc nền
nằm trong [contract.md](contract.md); dữ liệu và ngoại lệ nằm trong từng thư mục
tập (`Tap XX/`).

Skill vẫn đặt trực tiếp trong `.agents/skills/` ở root repository để Codex và
Claude Code nhận diện được.

## Cấu trúc

```text
comic-illustrator/
  README.md           Tổng quan workflow
  contract.md         Quy tắc nền của workflow minh họa tập
  Tap XX/             Dữ liệu riêng của từng tập
  referrences/        Tài liệu tham khảo (PDF in của tập cũ)
```

## Chuỗi skill

| Skill | Dùng khi |
| --- | --- |
| `comic-page-guide` | **Entry point mặc định** cho mọi yêu cầu tạo, tiếp tục, sửa, variant hoặc hoàn thiện minh họa; điều phối các skill bên dưới |
| `comic-production` | Chỉ khi người dùng gọi đích danh; không tự được chọn |
| `comic-continuity-manager` | Biên dịch, truy vấn và cập nhật continuity context |
| `comic-source-reader` | Đọc và kiểm chứng nguồn |
| `comic-shot-design` | Lên storyboard hoặc composition |
| `comic-prompt-writer` | Viết prompt từ shot đã chọn |
| `comic-image-production` | Tạo/chỉnh/variant ảnh |
| `comic-visual-qa` | QA profile, style, context và storytelling |
| `comic-layout-qa` | QA ảnh trong layout |
| `comic-delivery` | Lưu bản đã duyệt vào `approved/` |

Các skill chuyên môn có thể gọi thẳng cho tác vụ độc lập. Gọi trực tiếp bằng
`$ten-skill` (Codex) hoặc `/ten-skill` (Claude Code).

## Dữ liệu theo tập

Đường dẫn dạng `Tap XX/...` trong record, manifest và delivery receipt của tập
tính từ thư mục `comic-illustrator/`.

```text
Tap XX/
  notes.md            Dữ kiện và ngoại lệ cấp tập
  shot_notes.md       Continuity/nhịp shot riêng của tập
  characters/         Profile nhân vật (chuẩn identity của tập)
  Part N/             Layout, page, output và QA theo part
    part-config.json  Cấu hình từng part
```
