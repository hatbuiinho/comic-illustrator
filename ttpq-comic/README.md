# TTPQ Comic

Flow tạo prompt minh họa và dàn trang cho truyện về cuộc đời Đức Phật, theo
style `ttpq-comic`. Flow độc lập với `comic-illustrator/` và hai studio: không
đọc, không gọi skill hoặc quy tắc của các workflow đó.

Flow nghiên cứu kịch bản cả tập thành story bible và timeline cảnh, rồi dừng
ở **gói prompt**: đọc layout, cảnh tương ứng, nhân vật, bối cảnh và contract rồi viết prompt hai lượt:

1. **Lượt nét** (ChatGPT Image): clean outline đen trắng của cả spread, chữ
   VI/EN ôm hình. Đính kèm `layout-ref.png` và ảnh ref profile nhân vật.
2. **Lượt màu** (Codex hoặc ChatGPT Image): tô màu style ttpq-comic từ ảnh nét
   đã chọn, nhân vật đúng profile, giữ nguyên chữ đã ôm hình từ ảnh nét.

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
    prompts/vNNN-*.md         Gói prompt lượt nét + lượt màu để copy
    record.md                 Nguồn đã dùng, quyết định, kết quả tự kiểm
```

Skill: `.agents/skills/ttpq-comic/` (SKILL.md, mẫu và script `read-layout.py`).
