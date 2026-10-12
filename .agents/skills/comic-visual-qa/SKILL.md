---
name: comic-visual-qa
description: Kiểm tra output truyện tranh về focus, profile, thuần 2D, context, location và storytelling. Không dùng để kiểm tra hình học layout hoặc anatomy.
---

# Visual QA

Đọc [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md) và áp dụng theo giai đoạn của skill này.

Sau ba fast gate kỹ thuật, kiểm tra theo thứ tự: `emotionalImpact` →
`visualVitality` → profile → `selectedCompositionFidelity` → context/location →
storytelling và mức độ tiết chế. Không lấy prompt làm bằng chứng; chỉ dùng output
nhìn thấy và nguồn gốc. Không thực hiện anatomy QA và không tạo FAIL hoặc vòng
retry dựa trên anatomy.

`emotionalImpact` PASS khi cảm xúc chính đọc được trong một giây, ánh mắt–khoảng
cách–gesture tạo quan hệ, performance có subtext và đúng dư vị đã khóa. FAIL khi
ảnh đúng hành động nhưng vô cảm, biểu cảm chung chung, nhân vật tạo dáng giải
thích hoặc background lấn át quan hệ.
Không đánh giá emotional anchor riêng lẻ: ghi `performanceReadByCharacter` và
`groupEmotionalCoherence`. Nếu một nhân vật đọc thành ra lệnh, dò xét, khó hiểu,
đối đầu hoặc sắc thái khác làm lệch emotional thesis, `emotionalImpact` FAIL dù
nhân vật chính riêng lẻ vẫn đẹp.

`visualVitality` PASS khi hình đẹp ở thumbnail lẫn kích thước đọc, có nhịp
lớn–nhỏ/tĩnh–động, điểm hút rõ, lớp sâu sinh động và chi tiết sống vừa đủ. FAIL
khi bố cục đúng kỹ thuật nhưng khô, mọi vật ngang hàng, quá nhiều bằng chứng sự
việc, hoặc hình đọc như sơ đồ/ảnh minh họa giáo khoa.

Kiểm ở kích thước đọc của trang theo `shotReadabilityProof`, ngoài thumbnail
và crop chi tiết. Một biểu cảm đẹp khi phóng to nhưng không đọc được trên trang
chưa chứng minh `emotionalImpact` PASS. Nếu shot không dành đủ chỗ cho tín hiệu
chính, trả `COMPOSITION_NEEDS_REVISION`, không chỉ yêu cầu sửa nét hoặc phóng
lớn/dời artwork.

Ghi kết quả kỹ thuật và nghệ thuật riêng, cùng hạn chế còn lại. Style, context
hoặc geometry PASS không suy ra `emotionalImpact`/`visualVitality` PASS. Mỗi
kết luận nghệ thuật phải chỉ ra tín hiệu nhìn thấy; không dùng prompt/card để
giải thích hộ hình, không gọi toàn candidate “QA đạt” khi còn check REQUIRED
chưa đạt hoặc chưa kiểm.

Check thuần 2D phải có `styleConsistencyByElement`; không được kết luận PASS từ
ấn tượng tổng thể hoặc riêng nhân vật. Nếu bất kỳ nhóm vật liệu/background bắt
buộc nào drift bán thực, style tổng là FAIL và phải có remediation cụ thể.

Đọc reference đúng mục tiêu:

Trước mọi reference khác, đọc [fast-gates.md](references/fast-gates.md) và chạy
ba gate style → topography → process. Gate FAIL thì dừng sớm; không tốn thời
gian chạy profile/context/storytelling/layout cho output chắc chắn phải sửa.

Khi ba gate PASS, `emotionalImpact` và `visualVitality` là REQUIRED trừ khi
deliverable chỉ là profile, asset kỹ thuật hoặc concept test không kể chuyện.

- [style-qa.md](references/style-qa.md)
- [profile-qa.md](references/profile-qa.md) khi có nhân vật
- [location-qa.md](references/location-qa.md) khi background mang identity
- [storyboard-qa.md](references/storyboard-qa.md) khi đối chiếu composition

Với chủ thể bị cắt, đọc
[crop-read-contract.md](../comic-shot-design/references/crop-read-contract.md),
kiểm `cropRead`, `groundPlaneContinuity` và `occlusionLogic` theo phạm vi áp dụng.
Với remediation, đọc
[retry-quality-contract.md](../comic-image-production/references/retry-quality-contract.md)
và kiểm `qualityPreservation` sau fast gates PASS, trước khi dùng bản sửa làm
parent. Nếu fast gate FAIL, chỉ so regression nhanh với mốc thẩm mỹ tốt nhất
và bản cha để chọn đường sửa; không mở QA sâu hoặc layout.
PASS style/placement không bù regression diễn xuất hoặc vẻ đẹp.

Với `flattenedPageCandidate`, đánh giá hai ảnh: raw candidate để phát hiện style,
profile và context drift; `pageConceptPreview` có knockout + typography gốc để
kiểm candidate còn giữ đúng focus, silhouette, staging và background depth của
`selectedPageComposition`. Chữ model sinh không được dùng làm bằng chứng.

Với `BAKED_TEXT_PROXY_CONCEPT`, đánh giá trực tiếp `integratedTextConcept` về
style, profile, context, composition fidelity và việc text mass thực sự tham gia
eye path/figure–ground. Không kiểm chính tả, nội dung glyph hoặc typography
integrity. Không dùng clean-up để cứu concept FAIL; `cleanArtworkMaster` chỉ
được tạo sau selection và thuộc layout QA/pixel-lock QA.

Mỗi check trả `PASS`, `FAIL`, `NOT_APPLICABLE` hoặc `SKIPPED_BY_USER`. Chưa đủ bằng chứng với check `REQUIRED` thì ghi chưa kiểm và kiểm thêm trước
kết luận; khi report chỉ hỗ trợ PASS/FAIL, ghi FAIL với observedDefect là thiếu
bằng chứng, không gọi đó là lỗi ảnh hoặc tự regenerate. Không chạy layout QA ở đây.

Mỗi check FAIL phải ghi `retryable`, `observedDefect`, `preserve` và
`remediationDelta`. Lỗi style mặc định là `retryable: true` nếu có thể sửa mà
không đổi composition. Delta phải mô tả dấu hiệu nhìn thấy cần loại bỏ và cách
thay thế cụ thể; không dùng chỉ dẫn chung chung như “làm thuần 2D hơn”.

Khi composition có `continuityDependencies`, chạy thêm:

- `continuityReadCheck`: output có đúng các physical, knowledge, relationship,
  location và temporal state đã đọc hay không;
- `continuityWriteCheck`: output có vô tình tạo thay đổi hoặc tiết lộ chi tiết
  không thuộc moment hiện tại hay không;
- `forbiddenCheck`: chi tiết bị cấm xuất hiện sớm hoặc trạng thái sai có hiện
  diện hay không.

Chạy `selectedCompositionFidelity` theo ý đồ đã duyệt: camera, quan hệ,
hierarchy, crop, eye path và lớp sâu. Hoàn thiện nét/pose hoặc dịch chuyển nhỏ
giữ ý nghĩa không tự tạo FAIL. Dàn lại shot hoặc đổi trọng tâm phải trình lại composition.

Với page/spread không hard frame, kiểm thêm `sceneExtentFidelity` và
`sceneEconomy` theo `sceneExtentPlan` và mục **Phạm vi cảnh khác kích thước
canvas** trong `../comic-layout-qa/references/text-artwork-integration.md`.
FAIL `SCENE_OVEREXPANSION` khi model mở rộng công trường/cảnh quan/props để phủ
trang mà không phục vụ moment; không coi nền giấy có chủ ý là context loss.

Không lấy việc prompt bỏ sót một vật làm lý do bỏ qua check nếu vật đó nằm trong
`mustNotChange` hoặc `forbidden`. Kết quả QA chỉ báo cáo bằng chứng nhìn thấy;
không tự ghi continuity ledger.

Sau khi hoàn tất đánh giá bằng mắt, có thể lưu report JSON và chạy
`scripts/validate-visual-qa.js <visual-qa.json>` để kiểm completeness, trạng
thái input và coverage của continuity dependency. Script không thay thế đánh
giá focus, identity hay cảm xúc.

Không đánh FAIL một yếu tố `implicitReadable` chỉ vì nó không được thể hiện
trọn vẹn. Đánh giá khả năng suy ra từ toàn bộ hình và chỉ FAIL khi tổng thể dẫn
đến cách hiểu sai, không đủ tín hiệu hoặc mâu thuẫn nguồn. Đồng thời kiểm tra
việc diễn giải quá mức: hành động, biểu cảm hay chi tiết phụ không được phóng
đại đến mức tranh focus, làm mất tự nhiên hoặc thu hẹp khoảng trống cho người
đọc.
