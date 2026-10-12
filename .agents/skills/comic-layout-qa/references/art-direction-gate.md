# Cổng art direction cho layout chữ–hình

Cổng này đứng trước QA hình học. Đây là review bằng mắt trên clean preview,
không thể thay bằng manifest hợp lệ hoặc các box không giao nhau.

## Trước cổng duyệt cuối

- `TEXT_PROXY_INTEGRATION` cần cả `PROXY_BURDEN_PASS` và `PROXY_LAYOUT_PASS`;
  preview đẹp không bù được proxy làm nhẹ lượng chữ hoặc có hình thái dàn chữ
  phi thực tế. Không ép chữ về tọa độ layout gốc, nhưng phải giữ nội dung, cỡ đọc, ranh giới đoạn và reading order khả thi; số dòng/measure/cột
  được thiết kế lại, không khóa theo nguồn.
- `BAKED_TEXT_PROXY_CONCEPT` dùng cùng hai gate và artifact binding. Chữ sai
  không tạo FAIL; proxy co nhỏ, mất occurrence, footprint không khả thi hoặc
  interaction phụ thuộc vào một glyph cụ thể vẫn FAIL.
- Trước duyệt cuối cần `ARTIFACT_BINDING_PASS` schema 4: mọi occurrence
  chữ nguồn đều có group chữ render thật ở đúng scale và hash source/SVG/preview
  còn khớp. Dashed bars hoặc vùng chữ bị deduplicate không được mở gate.
- Composition có nhân vật cần `PERFORMANCE_READ_PASS`: đọc riêng gaze, hand
  gesture, posture và khoảng cách của từng nhân vật, rồi kiểm tra cảm xúc cả nhóm
  có cùng phục vụ emotional thesis hay không. Một pose đọc thành ra lệnh, dò xét,
  khó hiểu hoặc cảm xúc khác với direction phải FAIL dù card mô tả đúng.

Review nghệ thuật từ draft trước, rồi kiểm proof kỹ thuật và review lại bản cuối.
Cấm tự ghi PASS để mở gate. Khi có lỗi kỹ thuật, sửa theo tác động thực tế, không
làm yếu hình chỉ để giống mẫu.

## Cách review nhanh

Xem ở ba tỷ lệ: thumbnail toàn spread, kích thước đọc bình thường và crop 100%
tại chỗ chữ ôm hình. Chỉ PASS khi các mục áp dụng đều có bằng chứng nhìn thấy cụ thể:

1. **Visual thesis:** trong một giây có đọc được quan hệ hoặc chuyển biến chính
   của cảnh không?
2. **Figure–ground:** biên giữa mảng trắng và tranh có sinh ra từ silhouette,
   cử chỉ, lớp sâu và nhịp chữ không, hay chỉ là hình hộp/đường cong trang trí?
3. **Rhythm:** độ dài dòng, khối đoạn, khoảng nghỉ và diện tích tranh có nhịp
   lớn–nhỏ; tránh soi gương, chia đôi đều hoặc lặp cùng một module.
4. **Eye path:** chữ dẫn mắt vào nhân vật/cử chỉ rồi trở lại đoạn kế tiếp mà
   không tạo ngõ cụt, cạnh tiếp tuyến hoặc điểm hút giả.
5. **Page character:** layout có quyết định riêng cho cảnh này; nếu thay cảnh
   khác vào mà hình khối vẫn hợp y nguyên thì chưa đủ art-direct.
6. **Text burden:** lượng chữ đại diện có trung thực ở scale đọc dự kiến hay
   composition chỉ đẹp vì proxy đã bị co/giảm. Không đánh giá bằng vị trí.
7. **Performance coherence:** cảm xúc nhìn thấy của từng nhân vật có nhất quán
   với nhau và với direction; không lấy nhãn mô tả thay bằng chứng pose/gaze.
8. **Paragraph rhythm:** block proxy có giữ ranh giới đoạn, indent/bullet,
   khoảng nghỉ và nhịp dòng hay chỉ là các thanh trang trí được gom tùy ý.
9. **Typesetting feasibility:** line measure, leading, độ rộng cột, dòng ngắn và
   contour quanh silhouette có thể dàn bằng glyph thật ở scale đã khóa hay
   không.
10. **Scene economy:** phạm vi cảnh có vừa đủ cho meaning/moment và giữ context
    cần thiết không? Nền giấy chủ ý hợp lệ; đất/scaffold/horizon/props kéo rộng
    chỉ để lấp trang là `SCENE_OVEREXPANSION`, dù coverage và geometry đều PASS.
11. **Shot space fit (`shotSpaceFit`):** cỡ cảnh có dành đủ diện tích cho tín
    hiệu cảm xúc chính ở scale đọc bình thường không? Phần toàn thân, vật thể
    hoặc nền đang chiếm chỗ có thực sự giúp kể chuyện? Đối chiếu
    `shotSizeRationale`: shot gần hơn hoặc crop khác có giữ meaning/context
    với ít diện tích hơn không? Không mặc định shot gần luôn tốt hơn và không
    coi text frame gốc là vùng cấm. Với shot không dựa vào biểu cảm, kiểm tín
    hiệu kể chuyện chính thay vì bắt buộc mặt phải lớn.

`shotSpaceFit` cần `shotReadabilityProof` trên preview tại kích thước trang dự
kiến, không chỉ trên crop phóng to. Nếu phải dựa vào mô tả hoặc zoom mới nhận
ra tín hiệu chính, trả `COMPOSITION_NEEDS_REVISION`; đánh giá lại viewpoint,
cỡ cảnh/crop và bằng chứng phụ trước thu nhỏ hoặc dời cả cụm. Không suy PASS
từ footprint nhỏ, khoảng trắng nhiều hoặc proxy burden đạt.

Kết quả geometry và art direction phải ghi riêng. Không giao chữ, đúng trim/gáy
hoặc đủ context không chứng minh visual thesis, performance hay vẻ đẹp. Mỗi
mục nghệ thuật cần dấu hiệu nhìn thấy và hạn chế còn lại; không dùng lời trong
card/prompt để giải thích hộ hình. Chỉ kết luận đạt nghệ thuật khi các mục áp
dụng đều đạt, kể cả khi script hình học trả PASS.

Với chủ thể bị cắt, kiểm thêm `cropRead`, `groundPlaneContinuity` và
`occlusionLogic` theo
[crop-read-contract.md](../../comic-shot-design/references/crop-read-contract.md).
Áp ở semantic composition và clean preview; hình đọc thành người lún trong đất
phải sửa trước khi duyệt dù text/proxy/geometry đều PASS.

Nếu shot kế thừa làm cảm xúc khó đọc hoặc tiêu tốn không gian không cần thiết,
ghi `shotSpaceFit: FAIL`, trả `COMPOSITION_NEEDS_REVISION` và đánh giá lại
camera/shot size/crop trước scale/placement. Proxy và geometry PASS không thay
đánh giá này. Nếu thay shot đã duyệt, quay lại cổng composition.

Nếu một mục FAIL, trả `LAYOUT_COMPOSITION_NEEDS_REVISION` và sửa flow envelope,
staging hoặc overlap. Không chữa bằng bo góc, thêm đường cong ngẫu nhiên, thu
nhỏ chữ hoặc ghi một câu evidence chung.

Sau khi chọn integrated concept, review thêm bản clean ở thumbnail, kích thước
đọc và crop 100%. Nếu tháo proxy làm mất edge rhythm, để ghost/vết vá, đổi
protected artwork hoặc phá footprint đặt chữ, trả `CLEAN_PLATE_NEEDS_REVISION`;
không quay sang fresh-generation.

## White knockout

`WHITE_OPAQUE` là thuộc tính che nền, không phải hình dạng. Mask là kết quả của
art direction và có thể là nhiều mảng, contour hoặc vùng âm liên kết. Chỉ che
vùng cần cho chữ và khoảng thở; không mặc định phủ toàn text frame. Foreground
có thể chồng lên mảng trắng khi đã có layer/cutout thật và vẫn tránh glyph.
