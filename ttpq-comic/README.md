# TTPQ Comic

Flow tạo prompt minh họa và dàn trang cho truyện về cuộc đời Đức Phật, theo
style `ttpq-comic`. Flow độc lập với `comic-illustrator/` và hai studio: không
đọc, không gọi skill hoặc quy tắc của các workflow đó.

Flow nghiên cứu kịch bản cả tập thành story bible và timeline cảnh, rồi dừng
ở **gói prompt**: đọc layout, cảnh tương ứng, nhân vật, bối cảnh và contract rồi viết prompt hai lượt:

1. **Lượt nét:** clean outline đen trắng của cả spread, chữ VI trái và chữ
   tiếng Anh giữ chỗ bên phải, ôm hình. Đính kèm `layout-ref.png` và ảnh ref.
2. **Lượt màu:** vẽ màu style ttpq comic light (mặc định), ttpq comic soft hoặc
   ttpq comic blend (khi gọi tên) từ outline đã chọn, nhân vật
   đúng profile, giữ chữ đã ôm hình.

Prompt ảnh do `build-prompt.py` ghép: khối STYLE, ảnh ref theo dòng
**Profile:** của cảnh và điều cấm được chèn tự động.

Ảnh tạo ra là nháp; chữ trong ảnh chỉ để tham khảo, chữ in dàn trong InDesign.

Gọi flow: `/ttpq-comic` (Claude Code) hoặc `$ttpq-comic` (Codex). Quy tắc của
flow nằm trong [contract.md](contract.md).

## Cấu trúc

```text
ttpq-comic/
  README.md
  contract.md                 Quy tắc flow: nguồn, version, duyệt
  book-spec.md                Khổ spread, chữ VI/EN, quy tắc chữ ôm hình
  style/
    ttpq-comic.md             Định nghĩa style, khối prompt, điều cấm
    ttpq-comic-soft.md        Style tùy chọn soft: khối STYLE và LINE ART STAGE
    ttpq-comic-blend.md       Style test blend (50 comic/25 flat/25 storybook)
    era-ancient-india.md      Trang phục, kiến trúc, cảnh vật thời Đức Phật
    refs/                     Ảnh mẫu style (bổ sung sau)
  story/<tập>/
    script.md                 Kịch bản toàn văn (nguồn)
    bible.md                  Nhân vật, địa điểm, tiến độ, đạo cụ, điểm cần quyết
    scenes.md                 Timeline cảnh: thời điểm, nơi chốn, được phép, bị cấm
  characters/<slug>/          profile.md + ảnh ref identity
  settings/<slug>/            setting.md + ảnh ref bối cảnh
  layouts/                    PDF layout đầu vào
  spreads/<layout-slug>/p<trái>-<phải>/
    layout.json, layout.png   Dữ liệu và ảnh chụp spread trích từ PDF
    brief.md                  Mode, bối cảnh truyện và ý đồ điện ảnh đã chọn
    prompts/vNNN-*            Khối bối cảnh, body và prompt đã ghép
    outputs/                  Ảnh outline/màu theo version
    record.md                 Prompt, ảnh đính kèm, comment từng lượt
```

Skill: `.agents/skills/ttpq-comic/` (SKILL.md, mẫu, `read-layout.py`, `build-prompt.py`).
