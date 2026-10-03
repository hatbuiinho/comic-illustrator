---
name: comic-shot-design
description: Thiết kế storyboard, shot và phương án composition cho truyện tranh từ nguồn đã kiểm chứng. Dùng khi cần focus, khoảnh khắc, camera, emotional flow hoặc composition card; không dùng để tạo ảnh cuối.
---

# Thiết kế shot

Đi theo thứ tự: ý nghĩa kịch bản → trải nghiệm và cảm xúc người đọc → trọng tâm
thị giác → thông tin cần hiểu → cách kể và bố cục → chi tiết hỗ trợ → số người
trong khung.

Không mặc định mọi dữ kiện trong nguồn đều phải được thể hiện trực diện. Phân
biệt điều bắt buộc nhìn rõ, điều có thể suy ra từ tổng thể và điều chỉ hỗ trợ.
Ưu tiên diễn xuất, quan hệ, nhịp điệu và khoảng trống diễn giải; nếu việc làm rõ
một thông tin phụ khiến focus hoặc cảm xúc suy yếu, phải giản lược thông tin phụ.

Đọc các reference theo nhu cầu:

- [cinematic-language.md](references/cinematic-language.md) cho shot và nhịp.
- [emotional-flow.md](references/emotional-flow.md) cho chuỗi nhiều frame.
- [composition-strategy.md](references/composition-strategy.md) khi lên bố cục.
- [semantic-preview.md](references/semantic-preview.md) trước khi dựng preview.
- [storyboard-schema.md](references/storyboard-schema.md) khi cần artifact có cấu
  trúc hoặc bàn giao sang prompt.

Mỗi ảnh là một shot, một khoảnh khắc và một focus thị giác chính. Focus có thể
là cá nhân, quan hệ, tập thể, hoạt động, không gian hoặc dấu vết.

Chuyển động, bối cảnh và hành động phụ có thể được gợi bằng hướng, nhịp, chồng
lớp, crop, phản ứng hoặc quan hệ không gian. Không phóng đại hành động, mở rộng
khuôn hình hay thêm chi tiết chỉ để chứng minh một dữ kiện mà người đọc đã có
thể suy ra đúng.

Khi có nhiều hướng kể hợp lệ, đưa 2–3 phương án đánh số; mỗi phương án nêu kết
quả và đánh đổi trong một dòng. Không khóa số người tùy ý trước khi xác định ý
nghĩa và bằng chứng cần thấy.

Mỗi option phải có một composition preview PNG riêng để người dùng so sánh
trước khi chọn. Preview là sơ đồ/thumbnail bố cục, không phải ảnh minh họa cuối:

- dùng đúng aspect ratio và hình học frame/mask của layout khi có;
- biểu diễn vị trí, tỷ lệ và crop của chủ thể chính; foreground/midground/
  background; hướng nhìn, hướng chuyển động và eye path;
- đánh dấu vùng chữ, safe zone hoặc phần dễ bị mask che khi chúng ảnh hưởng;
- dùng nhãn ngắn hoặc legend nếu silhouette chưa đủ rõ, tránh chữ dài;
- lưu từng option thành file PNG ổn định, có `optionId` trong tên, không ghi đè;
- hiển thị đủ các PNG cùng mô tả và đánh đổi tại cổng lựa chọn.

Preview chính phải là SVG semantic do Codex dựng riêng theo shot: silhouette đọc
được đầu, thân, pose, hướng mặt/ánh nhìn, interaction và location anchor; dùng
bảng màu lấy từ profile gốc đúng tập để phân biệt nhân vật. Sau đó chạy
`scripts/render-composition-preview.js <semantic.svg> <composition.json>
[output.png]` để kiểm contract và rasterize.

Rectangle/bounding-box chỉ được dùng trong ảnh debug tạo bởi
`scripts/render-composition-debug.js`; không trình bày debug-box như option cho
người dùng chọn. Nếu semantic quality gate không đạt, bổ sung/customize SVG,
không hạ xuống preview hình chữ nhật.
Không dùng preview làm identity reference, style reference hoặc output sản xuất.
Nếu không thể tạo PNG, nêu blocker thay vì cho người dùng chọn chỉ từ mô tả chữ.

Đầu ra phải đủ để `comic-prompt-writer` viết prompt mà không cần phát minh lại
shot. Mỗi option khai báo continuity fact đã đọc, trạng thái không được đổi,
chi tiết bị cấm và thay đổi dự kiến chỉ khi approved theo
[storyboard-schema.md](references/storyboard-schema.md). Không coi composition
card sơ bộ là phê duyệt cuối và không tự ghi ledger.
