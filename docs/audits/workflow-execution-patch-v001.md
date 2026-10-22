# Bản vá thực thi/kiểm tra — v001

Ngày 2026-10-20. Owner chọn phương án 1 của `punna-workflow-review-v001.md`.
Đã áp dụng bản vá; không thay định nghĩa st03, không tạo ảnh mới hoặc duyệt profile.

## Thay đổi

- `../visual-review-contract.md`: kiểm mặt/vật liệu theo vùng, dấu nhận diện trọng yếu, kiểm ref bị lẫn, điều kiện chuyển bước, giới hạn preserve/layer và cách ghi activeBrief/requirementChanges/experiment/waiver.
- `../studio-contract.md` và Character Studio: dẫn contract dùng chung; tự sửa một lượt khi lỗi rõ sửa an toàn được, giữ giới hạn hiện hành; không bắt chì→màu/storytelling/layout.
- Visual QA/style-qa và profile-qa: dùng tiêu chí chung, một lệch identity trọng yếu đủ không đạt; không ép phẳng/chặn mọi gradient hoặc highlight.
- reference-selection của Image Production: vai trò ref không là bảo đảm model giữ đúng, cần kiểm output.
- Validator/report-contract: presets check tối thiểu theo deliverable, bằng chứng PASS/FAIL, nhóm style theo vùng, waiver có nguồn/scope. Tách reportValidity, qaOutcome và eligibleForNextStep; không còn status PASS tổng mơ hồ.
- Exit code mới: 0 đủ điều kiện QA; 1 report không hợp lệ; 2 report hợp lệ nhưng có FAIL. Người dùng/caller cũ cần cập nhật theo report-contract; không tự migrate report lịch sử. Caller tìm thấy trong repo đã được kiểm qua fixture mới.
- Bộ test: thêm report-validation.test.js và nối vào bộ tích hợp hiện có.

## Xác minh đã chạy

- 14/14 ca QA report: thiếu checks; REQUIRED bị bỏ; PASS thiếu evidence; style tổng mâu thuẫn nhóm; thiếu kiểm mặt; waiver thiếu scope/nguồn; N/A sai; studio không bị bắt gate tập; report FAIL không thành QA PASS; scope page/asset; JSON lỗi và stale; performance FAIL.
- Bộ tích hợp: 27/27 kiểm tra đạt, gồm ca QA mới và các kiểm continuity/layout/delivery hiện có; thao tác test dùng thư mục tạm.
- Fixture Visual QA cập nhật: reportValidity=PASS, qaOutcome=PASS, eligibleForNextStep=true.
- Hồi quy Punna: `punna-regression-qa-v001.json` hợp lệ nhưng qaOutcome=FAIL, eligibleForNextStep=false; style và profile không đạt. Đây là audit mới, không ghi đè record cũ.
- Hai skill entrypoint thay đổi qua quick_validate: hợp lệ.
- 20 liên kết Markdown trong các tài liệu thay đổi/thêm được kiểm: không hỏng.
- git diff --check: đạt.

## Giới hạn và phần không thay

Script không xem ảnh, không xác thực bằng chứng hoặc quyền user bằng thị giác;
vẫn cần agent đọc ảnh, kiểm scope/nguồn waiver đúng thực tế. Preset là tối thiểu,
không thay toàn bộ check active của minh họa tập. PASS_WITH_WAIVERS không thành
PASS toàn ảnh và eligibleForNextStep không thay gate chọn/approved.

Chưa có generation thử mới, chưa chứng minh giảm tỷ lệ drift. Chưa làm bộ mẫu
đối chứng mới (phương án 2). Không thay brief/profile nguồn hoặc sửa hồi tố các
test Punna. Hướng dẫn activeBrief áp dụng khi lập revision/record tiếp nối;
lịch sử cũ chưa được migrate hàng loạt. Chưa commit/push.

## Bước kiểm hệ thống tiếp theo

Chạy một ca generation có brief/input cố định dưới quy trình mới, kiểm độc lập
identity và từng vùng style, chỉ sửa trong lượt cho phép; ghi regression và
không nâng output FAIL thành nguồn chuẩn. Cần phân biệt việc phát hiện lỗi tốt
hơn với việc model tạo lỗi ít hơn.
