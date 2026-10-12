# Prompt contract

Đặt `qaLocks` thành một đoạn hard constraints ngắn ở cuối prompt. Không lặp cùng
constraint ở nhiều đoạn; không mở rộng thành mô tả dài nếu lock đã rõ.

Prompt nên mô tả theo thứ tự:

1. `READER EXPERIENCE`: cảm xúc đầu tiên, dư vị, `emotionalThesis`,
   `performanceSubtext` và vẻ đẹp/sức sống cần tạo. Không bắt đầu bằng inventory
   vật thể hoặc sự việc.
   Với mỗi nhân vật, chuyển `performanceContract` thành gaze, hand gesture,
   posture, spacing và `forbiddenReads`; kiểm cảm xúc cả nhóm không mâu thuẫn.
2. Loại ảnh và canvas trang/spread mục tiêu. `briefRegion` chỉ là gợi ý staging,
   không phải frame hoặc biên crop. Nếu layout dùng mask tròn, oval hoặc hình
   bất quy tắc, phải ghi rõ output vẫn là canvas chữ nhật đầy đủ, background
   phủ kín bốn góc; không alpha, cutout, viền/vignette hay crop sẵn theo mask.
   Mask chỉ là guide bố cục và được áp ở bước dàn trang.
3. Khoảnh khắc, cảm xúc hoặc quan hệ ưu tiên, focus, camera và điểm nhìn. Nếu
   có `visualPriorityFromLayout`, chuyển ý được highlight thành ưu tiên của pose,
   biểu cảm và eye path; không yêu cầu tái tạo highlight hay chữ trong ảnh.
4. Nhân vật, hành động, quan hệ, population plan và điều người đọc được phép tự
   suy ra. Luôn chuyển `activeProcessAgents` và `minimumVisibleRepresentatives`
   vào prompt; giữ họ ở cấp hỗ trợ nếu không phải emotional focus, nhưng không
   xóa họ hoặc thay họ hoàn toàn bằng đạo cụ/dấu vết.
5. Profile reference cùng dấu hiệu phải giữ.
6. Background, thời điểm và location anchors. Bảo toàn `topographyLock`; không
   thêm núi, đồi, sông, vách, skyline hoặc địa hình nổi bật khi nguồn không xác
   nhận. Khóa chỉ các dữ kiện context;
   cho phép phân lớp, nhịp mảng, crop và chi tiết phụ hợp bối cảnh. Vùng nền
   dưới chữ cần yên hơn nhưng không bắt buộc trống hoặc phẳng.
7. Bố cục, eye path, `textZone`, `subjectExclusionZone`, negative space và
   intentional crop. Nhân vật/đạo cụ kể chuyện tránh chữ; background được phép
   chạy dưới chữ trong `sceneExtentPlan`. Nêu riêng phạm vi cảnh, biên hòa giấy
   và khoảng thở chủ ý; không dùng “full spread” thay cho mô tả quy mô cảnh.
8. Ngôn ngữ thuần 2D.
9. Các chi tiết bắt buộc và cách đọc sai cần tránh.
10. Negative constraints thực sự áp dụng.

Nếu prompt dùng để chỉnh ảnh, nêu rõ phần giữ nguyên và phần cần thay đổi. Không
dùng output cũ làm chuẩn identity thay cho profile gốc.

Giữ nguyên phân cấp `emotionalPriority`, `explicitRequired`, `implicitReadable`
và `optionalSupport` từ storyboard. Chỉ mô tả trực diện những gì thực sự cần
nhìn rõ để bảo toàn ý nghĩa. Với thông tin có thể suy ra, dùng một số tín hiệu
tối thiểu từ nhịp, hướng, tư thế, phản ứng, chồng lớp hoặc ngữ cảnh; không biến
chúng thành checklist hình thể.

Negative constraints không được loại bỏ sự mơ hồ có chủ ý hoặc buộc mọi yếu tố
phải rõ ngang nhau. Nếu prompt dẫn đến hành động phô diễn, tạo dáng giải thích
hoặc quá nhiều điểm cạnh tranh thị giác, phải giảm chi tiết trước khi sản xuất.

Trước bàn giao, chạy `inventory check`: nếu có thể xóa một vật/nhóm phụ mà vẫn
giữ đúng meaning/context và hình trở nên giàu cảm xúc hoặc đẹp hơn, chuyển nó
sang `canImply` hoặc bỏ theo `omitToProtectEmotion`. Không xóa
`activeProcessAgents`, `mustShow`, continuity lock hoặc bằng chứng nhân quả bắt
buộc; hạ chúng xuống lớp hỗ trợ khi không phải emotional focus.

Prompt generation tạo một `flattenedPageCandidate` hoàn chỉnh theo
`selectedPageComposition` và `generationLayoutPlan`; chưa yêu cầu tách
background hoặc alpha mid+foreground. Candidate phải giữ camera, staging, vị
trí/tỷ lệ/crop tương đối, silhouette, eye path và depth đã khóa, đồng thời tích
hợp text-flow contour/foreground overlap được lập sau khi chọn shot.

Ngoại lệ `BAKED_TEXT_PROXY_CONCEPT`: prompt generation tạo
`integratedTextConcept` từ mockup toàn trang có proxy. Proxy được phép hiện trong
output và tham gia nhịp hình, nhưng text burden, reading order, footprint,
interaction edge và shot không được đổi. Không yêu cầu clean plate trong lượt
này; clean master chỉ được edit từ concept đã chọn.

Với `GENERATION_LAYOUT_INTEGRATION`, lập và dùng `textFlowEnvelope`,
`knockoutContour`, `overlapPlan` sau khi shot đã được chọn. Art-direct các contour
này với layout chữ thật và `cleanCompositionMap` ngay trước generation; không
được thay đổi camera/staging để cứu layout. Recognition core, cử chỉ và đạo cụ
kể chuyện phải nằm trong phần nhìn thấy; không để bước expand sau này phát minh
chúng. Typography model sinh chỉ là artifact tạm và sẽ bị che/thay bằng chữ gốc
từ PDF trong `pageConceptPreview`.

Câu trên không áp dụng cho `BAKED_TEXT_PROXY_CONCEPT`: glyph/pseudo-glyph được
giữ trong integrated concept để duyệt art direction, rồi tháo bằng mask sau
selection trước khi đặt chữ production ở InDesign.

Trước khi bàn giao prompt, chạy `background-context preflight`:

1. chuyển đủ `backgroundContextPlan` thành quan hệ không gian và dấu vết hoạt
   động, thay vì chỉ chép vài danh từ neo;
2. nếu layout dùng `textKnockoutMask: WHITE_OPAQUE`, candidate bám đúng
   `knockoutContour`; phần bị che chưa cần là clean plate hoàn chỉnh, nhưng
   recognition core và thông tin kể chuyện phải nằm ngoài vùng sẽ cần expand;
3. không dùng chỉ dẫn bao trùm như “để trống 40–50% canvas” hoặc cấm mọi
   silhouette trong cả vùng chữ; chỉ recognition core và cạnh tương phản cao
   bị loại khỏi glyph bounds;
4. negative constraints không xóa tín hiệu context cần thiết;
5. nêu `genericFailureMode` cần tránh.
6. `topographyLock` có provenance; không thêm địa hình nổi bật để lấp khoảng trống.

Nếu remediation sửa overlap với chữ, ưu tiên sửa wrap trong phạm vi cho phép
hoặc scale/placement/crop của hình trong shot đã chọn. Hạ tương phản chỉ giúp
background dễ đọc, không giải quyết giao nhau giữa glyph và nhân vật/đạo cụ.
Giữ location/process evidence trong `sceneExtentPlan`; nền giấy ngoài footprint
có chủ ý hợp lệ. Không bắt model kéo bối cảnh phủ canvas hoặc lấp mọi khoảng
thở. Truyền rõ phạm vi cảnh và biên hòa giấy, không chỉ kích thước output.
