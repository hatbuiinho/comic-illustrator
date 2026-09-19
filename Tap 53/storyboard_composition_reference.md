# Reference bố cục storyboard — Tập 53

Đây là bộ công cụ hỗ trợ kể chuyện, không phải tiêu chuẩn đẹp độc lập hay hard
gate. Thứ tự ưu tiên luôn là:

`shot thesis → story clarity/emotion → profile/location continuity → text,
spine, trim-safe → composition tool → decorative beauty`.

Nếu guide làm yếu diễn xuất, che proof, đẩy critical khỏi safe zone hoặc khiến
shot khó đọc thì bỏ guide. `primaryTool: none` là lựa chọn hợp lệ.

## Cách chọn

Mỗi shot dùng tối đa một primary tool và hai supporting tools. Ghi tool vì tác
dụng kể chuyện cụ thể, không ghi chỉ vì “đẹp/cân”. Guide trong
`composition_guides/` là layer review bật/tắt trên composition card, không xuất
hiện trong ảnh cuối. Có thể lật ngang/dọc hoặc xoay guide nếu eye path yêu cầu.

| Công cụ | Hợp khi | Tác dụng | Tránh khi |
| --- | --- | --- | --- |
| Rule of Thirds | hội thoại, reaction, subject + context | focus rõ, có lead room/text space | placement làm mất relational focus |
| Phi Grid | khung tĩnh, reflective, chapter ending | cân bất đối xứng mềm hơn thirds | phải đẩy mặt/đạo cụ khỏi safe zone |
| Golden Spiral | một eye path có điểm đến rõ | dẫn từ context đến emotional focus | cảnh có nhiều focus ngang nhau |
| Leading Lines | kiến trúc, gaze, gesture cùng hướng | gom mắt về dramatic focus | line vô tình dẫn ra mép/trang kế |
| Triangle | ba subject hoặc ba mass | quan hệ ổn định, quyền lực, căng thẳng | nhóm đông cần nhịp/phân tầng khác |
| Centered Symmetry | nghi lễ, quyền lực, đối đầu, bất an | tĩnh, trang trọng, áp chế | shot cần chuyển động hoặc lead room |
| Frame within Frame | cô lập/quan sát/ẩn náu | khóa attention và tạo lớp nghĩa | location anchor bị che hoặc frame giả quá nặng |
| Dynamic Diagonal | hành động, mất cân bằng, xung đột | lực và hướng chuyển động mạnh | reflective pause cần tĩnh |
| Negative Space | cô đơn, chờ đợi, dư âm, chỗ text | nhịp thở và anticipation | subject nhỏ đến mức mất emotion |
| Hitchcock’s Rule | mọi shot | scale phản ánh tầm quan trọng của beat | phóng lớn chi tiết không phải focus |

## Cách ghi trong option/manifest

```json
"compositionStrategy": {
  "primaryTool": "golden-spiral",
  "supportingTools": ["leading-lines", "negative-space"],
  "storyPurpose": "dẫn mắt từ dấu vết công trình tới sự nhận ra của Nalini",
  "focusPlacement": "điểm kết spiral gần mặt Nalini",
  "eyePath": "foundation lines → shelters → Nalini",
  "guideAsset": "Tap 53/composition_guides/golden-spiral-right.svg",
  "intentionalExceptions": ["dịch focus khỏi spiral 4% để giữ spine-safe"]
}
```

## Review

Hỏi năm câu: focus có đọc ngay; eye path có chủ ý; mass/negative space có cân;
tool có phục vụ shot thesis; có dấu hiệu ép staging vào guide không. Một shot chỉ
FAIL khi composition làm sai/khó đọc câu chuyện hoặc vi phạm hard lock, không
FAIL vì điểm đặt không trùng chính xác đường vàng.
