# Phác composition bằng ImageGen — nét chì tối giản

Mặc định được người dùng chốt ngày 2026-10-13. Áp dụng cho preview composition,
không đổi phong cách artwork hoàn thiện và không tự duyệt composition.

## Mức chi tiết

- Nền trắng, nét chì mảnh và nhẹ; gần rõ hơn xa. Composition chưa cần đổ bóng:
  không tô màu, mảng tóc đen, mảng xám, shading, hatch, bóng đổ/bóng chân,
  texture giấy hoặc hiệu ứng hoàn thiện.
- Không mắt, lông mày, con ngươi, nếp biểu cảm hoặc nét mặt nhỏ. Hướng nhìn đọc
  qua góc quay/nghiêng đầu, silhouette mũi–cằm và vị trí tai, không qua mắt.
- Tóc chỉ giữ silhouette và dáng đặc trưng (búi, ngôi…) với ít đường cấu trúc;
  không vẽ từng sợi hoặc nhiều lọn nội bộ.
- Dấu hiệu identity khác (râu, đầu cạo, đạo cụ riêng…) lấy theo profile gốc của
  từng nhân vật trong đúng tập, chỉ gợi bằng nét đơn giản; không cho nhân vật phụ
  mượn dấu hiệu của nhân vật chính.
- Trang phục giữ kiểu mặc/quấn, đường bao, lớp chính và vài nếp dài cần để đọc
  pose; bỏ nếp vụn. Tay/chân đủ đọc cử chỉ, không tả từng ngón hay cơ bắp.
- Trang sức chỉ gợi nhận diện, không lặp đầy từng hạt. Nền chỉ giữ contour và
  quan hệ không gian cần cho scene; không bỏ context/active process bắt buộc.
- Đây là mức giản lược có chủ đích. Không thêm chi tiết để đáp ứng QA dung mạo
  artwork cuối; ghi giới hạn đó và kiểm lại khi production.

## Tạo và sửa

Sau khi nguồn và direction được xác nhận, dùng ImageGen qua skill `imagegen`
built-in của GPT/Codex (không nằm trong `.agents/skills/`). Đọc lại và truyền
profile gốc đúng tập trong mỗi lượt; profile chỉ giữ identity/trang phục, không
truyền màu, độ hoàn thiện của mặt, tóc hoặc shading sang phác. Hai mẫu dưới đây
chỉ dùng cho ngôn ngữ nét; không lấy nhân vật, pose, đạo cụ hay khung của mẫu:

- `../assets/pencil-style-procession.png`
- `../assets/pencil-style-over-shoulder.png`

Mẫu được người dùng cung cấp và chốt kiểu nét; không phải profile/canon của tập.
Khi sửa, truyền đúng phác làm edit target cùng profile gốc và mẫu nét. Giữ
camera, hierarchy, khoảng cách, crop và cử chỉ đã được chọn, chỉ thay phần được
phản hồi. Nếu cấu trúc cần đổi, trình preview revision trước production.

Không chỉ dùng câu “giảm chi tiết”: nói rõ bỏ loại nét nào, giữ dấu hiệu nào.
Khung prompt (điền phần `<…>`, bỏ dòng không áp dụng):

```text
Composition study, sparse pencil contours on plain white, <tỉ lệ khung theo layout/spread>.
Scene: <khoảnh khắc và context bắt buộc>. Camera: <cỡ cảnh, góc máy, độ cao, hướng nhìn của camera>.
Actors: <id – vị trí/độ sâu – hướng đầu – cử chỉ chính – dấu hiệu identity giữ lại>.
Leave clear space for text at <vùng chữ/balloon theo layout>.
References: <file profile> = identity and costume only, ignore their color and rendering;
<file mẫu nét> = line-weight reference only, ignore its subjects, props, poses and framing.
Almost blank faces, no eyes or eyebrows; facing direction through head silhouette.
Minimal hair and garment folds. No color, no shading, no hatching, no cast or contact shadows,
no grey fills, no paper texture, no text or letters.
```

## Loại và tạo lại

Không trình preview cho người dùng nếu ảnh có một trong các lỗi sau; ghi lỗi vào
reference map rồi tạo lại với prompt nhấn đúng lỗi đó:

- Có mắt, lông mày, nét biểu cảm, màu, mảng xám, hatch, bóng hoặc texture giấy.
- Có chữ, glyph, số hoặc ký hiệu giả chữ.
- Chép nhân vật, đạo cụ, pose hoặc khung của mẫu nét thay cho nội dung scene.
- Sai identity so với profile, thiếu nhân vật/context bắt buộc hoặc lệch camera
  của direction đã chọn.

Tối đa 2 lần tạo lại cho cùng một lỗi. Nếu vẫn lỗi, trình bản tốt nhất kèm ghi
rõ lỗi còn lại và hỏi người dùng, không tự hạ chuẩn.

## Chữ, artifact và cổng duyệt

- Artwork raster không chứa glyph; ghép chữ/proxy bằng overlay riêng theo
  preview contract đang áp dụng ([storyboard-schema.md](storyboard-schema.md)).
  Đánh giá toàn spread và crop cử chỉ/hướng đầu tại cỡ đọc.
- Lưu prompt, reference map (vai trò style/identity/edit target), artwork,
  preview và storyboard có card chín mục theo
  [storyboard-schema.md](storyboard-schema.md); version mới, không ghi đè.
- Raster không cần semantic actor marker hoặc renderer SVG. SVG vẫn được dùng
  làm overlay chữ và proof typography; không tự quay lại vẽ actor bằng SVG.
- Giữ proxy burden/layout/artifact binding và kiểm crop như workflow hiện có.
  Render thành công không chứng minh ý đồ kể chuyện đạt.
- Composition chỉ CONFIRMED khi người dùng duyệt rõ preview. Chốt phương pháp
  phác hoặc độ giản lược không tự động là duyệt camera/bố cục hay chọn master.
- Nếu ImageGen lỗi/không khả dụng (kể cả agent không có skill `imagegen`), báo
  giới hạn; không âm thầm chuyển sang SVG hay API khác.
