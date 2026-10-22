# Báo cáo QA: hợp lệ khác đạt

Script kiểm dữ liệu khai báo, không xem ảnh và không tự xác nhận bằng chứng
đúng sự thật. Người đánh giá phải kiểm ảnh trước theo contract kiểm hình.

Report có `schemaVersion`, `output` tương đối, `deliverableType`,
`hasCharacters` boolean, `checks`. `requiredChecks` chỉ bổ sung, không bỏ preset:

| deliverableType | Check tối thiểu |
|---|---|
| studio-profile | style, profile |
| studio-image, concept-test, technical-asset | style |
| comic-page | style, focus, emotionalImpact, visualVitality, selectedCompositionFidelity, context, storytelling |

Thêm profile khi hasCharacters=true. Studio không bắt performance/storytelling,
anatomy hoặc layout. Đây không phải toàn bộ QA của page; các lock, fast gate,
continuity và check REQUIRED hiện hành vẫn phải bổ sung theo scope. Nếu có shot
cảm xúc nhiều nhân vật, dùng requiresPerformanceCoherence theo skill.

Mỗi check là object có status. PASS/FAIL cần `evidence` cụ thể; FAIL thêm
`remediation`, `preserve`, `retryable` boolean. NOT_APPLICABLE cần reason,
không dùng cho style hoặc profile bắt buộc. SKIPPED_BY_USER cần reason, scope
và authorizationSource trỏ yêu cầu user; scope phải nêu check/version/deliverable.
Script kiểm sự có mặt các trường, agent kiểm user thực sự cho phép đúng scope.
Thiếu bằng chứng phải ghi thiếu trong evidence/FAIL, retryable=false khi chỉ
cần xem thêm; không gọi đó là lỗi ảnh hoặc tự regenerate.

Khi style là PASS/FAIL, khai `styleConsistencyByElement`: nhóm faceSkin, hair,
fabric, jewelry, background nếu có nhân vật; subject, background nếu không có.
Mỗi nhóm có PASS/FAIL và evidence, hoặc NOT_APPLICABLE với reason. Với faceSkin,
nêu vùng mặt đã xem và hạn chế độ đọc; không khẳng định đã kiểm nét bị khuất.
Thêm nhóm vật liệu/đạo cụ riêng khi xuất hiện. Nhóm FAIL buộc style tổng FAIL.

Kết quả:

- `reportValidity`: report đủ cấu trúc/trường bằng chứng, không phải ảnh đạt.
- `qaOutcome`: PASS, FAIL, PASS_WITH_WAIVERS hoặc UNDETERMINED nếu report sai.
- `eligibleForNextStep`: đủ điều kiện QA theo khai báo, vẫn cần selection/gate
  hiện hành; không tự cho phép approved, profile hoặc canon.
- Exit 0: hợp lệ, đủ QA; exit 1: report không hợp lệ; exit 2: hợp lệ nhưng còn FAIL.

Report cũ không tự được migrate hoặc đổi kết quả. Khi tiếp tục tác vụ, lập
report mới theo contract này, giữ report lịch sử. Không có trường `status: PASS`
mơ hồ ở cấp tổng nữa.
