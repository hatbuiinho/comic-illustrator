---
name: comic-image-production
description: Tạo, chỉnh sửa hoặc tạo variant ảnh truyện tranh từ prompt/composition đã chốt, dùng đúng profile và lưu output có version. Không dùng để duyệt hoặc chuyển ảnh vào approved.
---

# Sản xuất ảnh

Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md) và áp dụng theo giai đoạn của skill này.

Trước mỗi lượt tạo/chỉnh có nhân vật, đọc lại profile gốc từ filesystem và
truyền đúng reference trong chính lượt đó. Đọc
[profile-refresh.md](references/profile-refresh.md).

Kiểm tra prompt/composition active không bị đánh dấu `STALE`. Việc context
packet trỏ tới profile không thay thế yêu cầu đọc và truyền profile gốc trong
chính lượt tạo.

Chỉ bắt đầu production khi `selectedPageComposition.status: CONFIRMED`.
Narrative direction đã chọn hoặc composition còn `PROPOSED` chưa đủ điều kiện
tạo ảnh. Nếu thiếu xác nhận composition, dừng ở cổng duyệt và không tự suy diễn
rằng việc chọn direction đồng nghĩa với duyệt bố cục.

Đọc [reference-selection.md](references/reference-selection.md) để chọn asset.
Khi tạo variant hoặc sửa output, đọc [variant-policy.md](references/variant-policy.md).
Khi remediation/retry, đọc [retry-quality-contract.md](references/retry-quality-contract.md).
Phân biệt sửa hình với transform layout; bản sửa phải giữ chất lượng phần đã đạt.
Chỉ khi người dùng yêu cầu rõ bộ layer InDesign từ master đã chọn, đọc
[indesign-layer-package.md](references/indesign-layer-package.md).

Tạo từng `flattenedPageCandidate`/variant riêng từ `selectedPageComposition` và
`generationLayoutPlan`. Candidate là artwork toàn page giữ shot đã duyệt và
tích hợp layout chữ thật ở chính bước tạo hình; model không được tự đổi camera,
quan hệ, hierarchy, crop có ý nghĩa hoặc cấu trúc chữ–hình. Cho phép hoàn thiện
nét, pose, tỷ lệ nhỏ và mảng màu trong ý đồ đã duyệt; không khóa contour preview thô.
`flattenedPageCandidate` dùng canvas chuẩn nhưng phạm vi cảnh theo
`sceneExtentPlan` đã duyệt trong `text-artwork-integration.md`. Không tự kéo
bối cảnh phủ trang; ngoài footprint có thể là nền giấy/alpha theo deliverable.
Trong footprint, giữ thông tin cần dưới treatment chữ; không dồn recognition
core khỏi text frame chỉ vì geometry ban đầu. `pageConceptPreview` ghép
candidate → integration treatment theo mode → chữ thật hoặc proxy ngoài model.
Lưu vào đúng
`<thu-muc-tap>/.../outputs/` với tên version mới; không ghi đè. Không dùng ảnh
trong `outputs/` làm style reference mặc định và không coi output trước là
nguồn identity.

Trong khi giữ composition đã khóa, production phải bảo toàn `readerFeeling`,
`emotionalThesis`, `emotionalAnchor`, `performanceSubtext` và `beautyIntent`.
Chi tiết sự việc chỉ là bằng chứng hỗ trợ: không được làm hình thành bản kiểm kê
đồ vật/hành động, làm mất cảm xúc chủ đạo hoặc khiến trang đúng nội dung nhưng
khô, tĩnh và thiếu sức sống.

Với `TEXT_PROXY_INTEGRATION`, trước generation phải có
`productionLayoutProxy` tách lớp theo
`../comic-layout-qa/references/text-artwork-integration.md`. Raw candidate không
chứa proxy glyph. Background chỉ tiếp tục trong footprint cảnh đã khóa, có thể
hòa về nền giấy; model không tự mở rộng cảnh, tạo white panel/hard text boundary
hoặc chữ đọc được. `pageConceptPreview` ghép proxy overlay ngoài model
và ghi `exactTextCapacity: DEFERRED_TO_INDESIGN`.

Với `BAKED_TEXT_PROXY_CONCEPT`, tạo `integratedTextConcept` từ
`bakedProxyGenerationReference`; proxy được phép bake vào candidate để AI dùng
như một element composition. Không coi glyph sai là lỗi và không dùng concept
này làm artwork cuối. Candidate phải giữ text burden, reading order, footprint,
interaction edge và shot đã duyệt; model không được co proxy để lấy chỗ cho hình.

Với frame tròn, oval hoặc hình bất quy tắc, luôn tạo ảnh chữ nhật full-bleed;
mask chỉ hướng dẫn placement. Trước khi bàn giao, xem raw output không mask trên
nền tương phản và FAIL nếu ngoài mask bị trong suốt, để trắng/rỗng, có viền hoặc
vignette theo mask, hay canvas đã bị crop. Không dùng preview đã mask làm bằng
chứng cho check này.

Mỗi lượt tự sửa phải tạo version mới, nạp lại profile gốc, giữ các check đã PASS
và áp dụng đúng `remediationDelta`. Với remediation về text overlap, không được mặc định làm rỗng text zone. Giữ
`backgroundContextPlan` đã PASS và chỉ dời/giảm recognition core, cạnh tương phản
cao hoặc chi tiết nhỏ. Nếu delta có thể xóa location identity, process evidence
hoặc spatial continuity, trả về prompt preflight thay vì tạo ảnh.

Ghi `parentVersion`, lỗi cần sửa và chiến
lược `edit` hoặc `fresh-generation`. Không dùng output FAIL làm chuẩn identity
hay style; chỉ được dùng làm ảnh đích để giữ những phần đã PASS.

Dùng `scripts/allocate-version.js <outputs-dir> <base-name> <extension>
--reserve` khi chọn tên output để cấp version atomically. File reservation rỗng
phải được thay bằng output thành công trong cùng lượt; nếu tạo ảnh thất bại thì
chỉ xóa đúng reservation do lượt đó tạo.

Sau khi tạo, bàn giao raw candidate và `pageConceptPreview` được compositing từ
integration treatment + lớp chữ ngoài model: typography gốc hoặc proxy theo
contract active. Không dùng chữ model sinh làm chữ cuối. Ghi
đường dẫn, version và những override đã áp dụng; không tự đánh dấu QA PASS hoặc
chuyển file vào `approved/`.

Với `BAKED_TEXT_PROXY_CONCEPT`, bàn giao `integratedTextConcept` thay cho cặp raw
candidate/overlay ở trên và ghi `exactTextCapacity: DEFERRED_TO_INDESIGN`.

Không tự tách hoặc expand ở bước delivery. Chọn master chỉ xác định hình để
lưu; chuyển hình đã chọn theo `comic-delivery`, rồi đề xuất làm thêm nếu cần.
Chỉ khi người dùng yêu cầu tách/expand/bộ layer mới chạy phần hậu kỳ dưới đây.

Không tách hoặc expand option/variant chưa được chọn. Khi đã có yêu cầu bổ sung
rõ và người dùng chọn
đúng candidate, ghi `SELECTED_FOR_LAYOUT`, tạo `visibleArtLockMask`, giữ nguyên
pixel artwork đã nhìn thấy và chỉ expand vùng bị chữ/knockout che. Recognition
core, cử chỉ và đạo cụ kể chuyện không được phát minh ở bước expand. Sau đó mới
tạo bộ layer đồng phiên bản. Đây là hậu kỳ kỹ thuật: không đổi composition,
nhân vật hoặc nội dung đã chốt; lỗi tách/expand chỉ sửa trong bộ layer, không tự
sửa candidate đã duyệt.

Riêng mode baked, chỉ khi người dùng yêu cầu artwork sạch hoặc bộ layer mới tạo
`cleanArtworkMaster` bằng edit/inpaint từ đúng concept đã chọn. Chỉ vùng
`proxyRemovalMask + repairContextRing` được thay đổi; vùng
`protectedArtworkMask` phải bất biến. Chạy `CLEAN_PLATE_PASS` trước khi tách
layer. Không fresh-generate clean master, không dùng clean-up để sửa pose,
identity, background staging hoặc composition đã duyệt.

## Contract chữ–hình

Luôn resolve mode qua
[text-artwork-integration.md](../comic-layout-qa/references/text-artwork-integration.md).
Khi deliverable dùng `FINAL_TEXT_REFLOW`, đọc [text-reflow-contract.md](../comic-layout-qa/references/text-reflow-contract.md). Đây là
nguồn chung cho text chuẩn, presentation mode, cấu trúc cột, reference role và
bằng chứng reflow; không áp chế độ này cho concept/profile hoặc hard frame độc lập.
