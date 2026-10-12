---
name: comic-prompt-writer
description: Viết prompt tạo hoặc chỉnh ảnh từ storyboard/composition đã chọn cho project truyện tranh 2D. Dùng khi người dùng cần prompt hoàn chỉnh; không tự tạo ảnh hoặc thay đổi shot đã duyệt.
---

# Viết prompt ảnh truyện tranh

Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md) và áp dụng theo giai đoạn của skill này.

Nhận `selectedPageComposition` đã chọn cùng `generationLayoutPlan` được lập sau
khi chọn shot, rồi chuyển thành prompt render `flattenedPageCandidate`. Không tự
đổi focus, moment, camera, quan hệ, hierarchy, crop có ý nghĩa hoặc profile.
Cho phép hoàn thiện diễn xuất, nét và mảng trong ý đồ đã duyệt; không biến
tọa độ/contour preview thành khuôn. Giữ khả năng đọc của chữ–hình đã chốt.

Chỉ nhận composition có `selectedPageComposition.status: CONFIRMED`. Narrative
direction đã chọn nhưng composition còn `PROPOSED` chưa cho phép viết prompt
production.

Trước khi viết, kiểm tra composition không bị `STALE` so với dependency revision
đã ghi. Bảo toàn `mustNotChange` và `forbidden`; không biến
`writesIfApproved` thành sự kiện đã xảy ra ngoài đúng moment của shot.

Bảo toàn thứ bậc kể chuyện của composition: `readerFeeling` →
`emotionalThesis` → `emotionalAnchor`/`performanceSubtext` → vẻ đẹp và sức sống
→ `emotionalPriority` → `explicitRequired` → `implicitReadable` →
`optionalSupport`. Không chuyển mọi dữ kiện thành checklist chi tiết có độ nhấn
như nhau.

Chuyển `performanceContract` thành dấu hiệu quan sát được cho từng nhân vật:
gaze, hand gesture, posture, spacing và cách đọc sai cần tránh. Không chỉ dùng
tính từ như “gentle”, “reverent” hoặc “agreeing” nếu pose khác vẫn có thể đọc
thành ra lệnh, dò xét, khó hiểu hay cảm xúc trái direction. Giữ
`groupEmotionalCoherence` trong prompt và mọi remediation.

Prompt phải mở bằng khối `READER EXPERIENCE` mô tả cảm xúc đầu tiên, dư vị và
nhịp sống cần tạo; sau đó mới tới moment/context. Nếu prompt đọc như inventory
nhân vật–vật thể–sự việc, phải rút bớt chi tiết trước generation. Chỉ
`selectiveEvidence.mustShow` được mô tả trực diện; `canImply` đi qua nhịp, lớp
sâu, phản ứng hoặc quan hệ; `omitToProtectEmotion` không được lén đưa lại.

Luôn resolve style theo `docs/project-style-policy.md` active của project và
đọc [pure-2d-style.md](references/pure-2d-style.md). Prompt/qaLocks cũ không
được âm thầm áp lại mức shading đã thay đổi; cập nhật phần phụ thuộc policy
trước dùng lại, giữ các lựa chọn nội dung/composition còn hiệu lực. Đọc
[prompt-contract.md](references/prompt-contract.md) để cấu trúc prompt và
[negative-constraints.md](references/negative-constraints.md) để chọn điều cấm.

Chỉ đưa vào prompt các kiểm tra `REQUIRED`. Không thêm constraint thuộc
`NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. Nếu người dùng nói “không cần tránh
gáy”, prompt không được lén dịch focus khỏi gáy.

Đưa prompt hoàn chỉnh trong một code block, không dùng dấu ba chấm thay nội dung.

Prompt phải khai báo bộ input: layout PDF raster có chữ, composition preview
không chữ đã chọn, clean composition map, `generationLayoutPlan`, text/knockout
mask, overlap mask, profile và source snapshot. Layout có chữ được đưa vào ở
chính bước tạo hình để art-direct quan hệ chữ–hình; chữ model sinh không được
dùng làm typography cuối.

Nếu contract active là `TEXT_PROXY_INTEGRATION`, thay layout chữ thật/mask bằng
`productionLayoutProxy`, `backgroundValueMap`, `detailDensityMap`,
`integrationEdgeMap` và `glyphPressureMap`. Proxy text chỉ là overlay art
direction, không được model vẽ vào raw candidate. Prompt không yêu cầu text
chính xác, không yêu cầu để trống vùng chữ và không tuyên bố capacity PASS.

Nếu contract active là `BAKED_TEXT_PROXY_CONCEPT`, dùng
`bakedProxyGenerationReference` làm reference toàn trang chính. Prompt cho phép
model render glyph/pseudo-glyph như material concept và yêu cầu hình tổ chức
quanh text mass đã khóa; không yêu cầu chữ chính xác. Truyền kèm
`proxyRemovalMask`, `repairContextRing`, `protectedArtworkMask` và
`indesignTextFootprint`. Không yêu cầu model tạo clean plate trong cùng lượt và
không mô tả vùng chữ như vùng trống.

Raw candidate dùng canvas chuẩn; mô tả riêng `sceneExtentPlan` theo contract
`text-artwork-integration.md`: phạm vi cảnh, context tối thiểu, biên hòa giấy và
khoảng thở chủ ý. Không dùng canvas lớn làm lý do bắt background xuyên full
spread, không reserve một tỷ lệ trống tùy ý. Giữ footprint và composition đã
duyệt; nền chỉ tiếp tục dưới chữ nơi cảnh hiện diện. Nền giấy ngoài footprint
hợp lệ. Mặt, mắt, tay và gesture tránh glyph; không tự dàn chữ hoặc tạo panel trắng.

Prompt phải tách hai khối: `NON-NEGOTIABLE CONTEXT` chứa `contextLocks` và
`forbidden`; `CREATIVE ART DIRECTION` chứa `creativeFreedom`. Nói rõ mọi phần
không bị khóa có thể được thiết kế tự do nếu không tạo event, landmark,
identity hoặc causal state mới. Không biến creative freedom thành checklist có
độ nhấn ngang emotional focus.

Với thông tin `implicitReadable`, mô tả ấn tượng tổng thể và các tín hiệu tối
thiểu thay vì liệt kê dày đặc dấu hiệu cơ học. Không tự yêu cầu toàn thân, hành
động cường điệu, biểu cảm lớn hoặc thêm vật thể chỉ để tăng độ rõ. Nếu prompt
khiến thông tin phụ cạnh tranh với cảm xúc hoặc focus, phải giản lược trước khi
tạo ảnh.

Ưu tiên cử chỉ tự nhiên có subtext và khoảng lặng; tránh pose trình diễn chỉ để
giải thích câu chữ. Background và active process có thể sinh động bằng nhịp,
overlap và chi tiết sống có chọn lọc, nhưng phải giữ vai trò hỗ trợ emotional
anchor thay vì biến hình thành bản tường thuật đủ sự việc.

Mô tả pose, cử chỉ và silhouette khi chúng mang ý nghĩa kể chuyện, nhưng không
thêm anatomy checklist hoặc negative constraint về anatomy.

Khi nhận remediation từ QA, viết prompt delta chỉ sửa các check FAIL, nhắc lại
những gì phải giữ và không đổi composition đã duyệt. Với lỗi style, nêu đúng
dấu hiệu sai đang thấy và ngôn ngữ đồ họa thay thế; không chỉ ghi “thuần 2D”.

Với chủ thể bị cắt, chuyển nguyên `cropReadPlan` theo
[crop-read-contract.md](../comic-shot-design/references/crop-read-contract.md);
không ghép waist crop với fade thân vào đất. Khi retry, áp
[retry-quality-contract.md](../comic-image-production/references/retry-quality-contract.md):
viết prompt sửa gọn, không cộng dồn lệnh; khai báo input đúng file thực truyền
và không biến contour semantic thô thành khuôn artwork.

## Contract chữ–hình

Luôn resolve mode qua
[text-artwork-integration.md](../comic-layout-qa/references/text-artwork-integration.md).
Khi deliverable dùng `FINAL_TEXT_REFLOW`, đọc [text-reflow-contract.md](../comic-layout-qa/references/text-reflow-contract.md). Đây là
nguồn chung cho text chuẩn, presentation mode, cấu trúc cột, reference role và
bằng chứng reflow; không áp chế độ này cho concept/profile hoặc hard frame độc lập.
