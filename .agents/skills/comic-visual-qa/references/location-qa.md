# Location QA

Che subject/effect/text và kiểm tra background còn đọc đúng location không.

Mức neo tham khảo:

- establishing/wide: ít nhất ba neo;
- medium: hai neo mạnh hoặc ba neo nhẹ;
- close-up/insert: một shared anchor mạnh và tín hiệu không gian đủ nhận diện.

Đây là tiêu chí theo shot size, không phải lý do đổi sang shot rộng. FAIL nếu
địa hình, horizon, quy mô hoặc shared anchor mâu thuẫn nguồn; vật liệu chung như
tường đá hoặc sàn tối không tự thành nhiều neo độc lập.

Số lượng neo chỉ là điều kiện cần. Chạy thêm bốn check:

- `contextSpecificity`: tổng thể có đọc thành đúng location cụ thể hay chỉ là
  một nền chung có vài vật thể token;
- `processEvidence`: có dấu vết quan hệ cho biết hoạt động đang/vừa diễn ra;
- `spatialContinuity`: foreground, midground và background có nối thành cùng
  một không gian;
- `topographyLock`: horizon và địa hình có đúng nguồn, không thêm núi/đồi/sông
  chỉ để làm background đẹp hơn;
- `textZoneBackgroundQuality` khi dùng `GENERATION_LAYOUT_INTEGRATION`: nền dưới chữ
  có yên để đọc và tiếp tục location trong footprint cảnh đã duyệt; ngoài cảnh
  có thể là paper tone/khoảng thở có chủ ý theo `sceneExtentPlan`.

FAIL `BACKGROUND_CONTEXT_GENERIC` khi đủ số anchor nhưng thiếu specificity hoặc
process evidence. FAIL `BACKGROUND_CONTEXT_LOSS` khi mất neo/quan hệ cần thiết
để hiểu đúng nơi chốn hoặc hoạt động, không chỉ vì nền giấy hiện diện. Kiểm
`sceneEconomy`: cảnh nhỏ đủ context tốt hơn nền trải rộng chỉ để phủ trang;
không yêu cầu thêm lớp sâu/đường chân trời ngoài phạm vi cần kể.
