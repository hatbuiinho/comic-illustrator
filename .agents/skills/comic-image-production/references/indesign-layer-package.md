# Bộ layer cho InDesign

Đây là hậu kỳ tùy chọn, không phải bước delivery mặc định. Chỉ chạy khi người
dùng yêu cầu rõ bộ layer InDesign, đã chọn đích danh master và trạng thái là
`SELECTED_FOR_LAYOUT`. Không chạy cho option, variant hoặc master chưa được
chọn. Chọn master hoặc yêu cầu “bàn giao” không tự cấp phép tạo bộ layer.

Tạo từ candidate đã chọn. Trước tiên lưu `visible-art-lock-mask` và chỉ expand
phần bị chữ/knockout che; pixel trong vùng đã duyệt phải bất biến. Từ full-page
master đã expand, tách background và chủ thể trong cùng bộ version. Mỗi asset
dùng cùng canvas, kích thước pixel, điểm gốc và profile màu:

- `<base>-master.<ext>`: ảnh đã được chọn, bất biến trong bước tách;
- `<base>-bg.<ext>`: background full-bleed, opaque, đã phục hồi sạch vùng từng
  bị chủ thể che;
- `<base>-mgfg.png`: midground + foreground có alpha, gồm nhân vật, đạo cụ,
  hiệu ứng và vật/bóng cần di chuyển cùng chủ thể;
- `<base>-wrap.svg`: silhouette text wrap đơn giản hóa, bỏ khe vụn và có khoảng
  đệm quanh chủ thể;
- `<base>-visible-art-lock-mask.png`: vùng pixel đã được người dùng nhìn thấy;
- `<base>-expand-mask.png`: chỉ vùng được phép phục dựng sau selection;
- `<base>-layout-preview.png`: bản ghép sạch với knockout và chữ thật để duyệt.

Với `BAKED_TEXT_PROXY_CONCEPT`, candidate được chọn là provenance và bản duyệt
nghệ thuật; `<base>-master` phải là `cleanArtworkMaster` đã đạt
`CLEAN_PLATE_PASS`. Lưu thêm `proxy-removal-mask`, `repair-context-ring` và
`protected-artwork-mask`; không đưa integrated concept có glyph vào bộ artwork
đặt trong InDesign.

Với `AUTO_LAYOUT`, lưu kèm layout plan chứa `textFlowEnvelope`,
`knockoutContour`, `overlapPlan`, `readingOrder`, các text element cố định và
thiết lập wrap tương ứng. Đây là
chỉ dẫn reflow cho InDesign; không được sửa nội dung chữ.

Vật vẫn đứng yên khi di chuyển chủ thể thuộc `bg`; vật phải đi cùng chủ thể
thuộc `mgfg`. Bóng tiếp xúc hoặc hiệu ứng gắn trực tiếp với chủ thể nằm trong
`mgfg`; bóng môi trường cố định nằm trong `bg`.

Không dùng alpha chi tiết của tóc, ngón tay hoặc vạt áo làm wrap path trực tiếp.
Wrap path phải theo silhouette tổng, không tạo dòng chữ ngắn hoặc khe chữ vụn.

QA hậu kỳ chỉ kiểm: vùng visible-art lock không đổi; expand nối line art, mảng
màu/shading của master đã chọn, perspective và continuity; clean plate không lỗ/bóng ma; alpha
không viền/sót nền; `bg + mgfg` khớp master; mọi asset cùng canvas/điểm gốc;
nhân vật và chi tiết kể chuyện không đè glyph; wrap path tự nhiên. Không mở lại
visual QA hoặc tạo lại candidate đã duyệt vì lỗi tách lớp.
