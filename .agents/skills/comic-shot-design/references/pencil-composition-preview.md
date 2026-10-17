# Phác composition bằng ImageGen — nét chì tối giản

Mặc định được người dùng chốt ngày 2026-10-13. Áp dụng cho preview composition,
không đổi phong cách artwork hoàn thiện và không tự duyệt composition.

## Mẫu mức giản nét mặc định

Dùng [`pencil-detail-level-v02.png`](../assets/pencil-detail-level-v02.png)
làm reference chính về mức giản nét, truyền ngay trong lượt tạo đầu tiên và
các lượt chỉnh phác. Người dùng chọn mức này ngày 2026-10-16. Asset là bản sao
nguyên vẹn từ
`../../../../Tap 53/Part 2/pages/page-003/outputs/page003-d2-pencil-v02.png`;
SHA-256: `29ec911d95d9be23f0b9a0883aec76a889b951f90a138692ac697e03bdee9d0f`.
Đường dẫn nguồn trên chỉ ghi provenance lịch sử; dữ liệu page 3, Part 2 đã
được xóa theo yêu cầu reset. Dùng asset trong skill, không tìm lại output trang.

Chỉ học mặt gần trống, tóc/râu bằng đường bao, ít nếp vải cấu trúc và nền gọn.
Việc chọn mẫu này không duyệt bố cục, diễn xuất hay lỗi nội dung trong v02.
Không sao chép nhân vật, pose, hướng nhìn, số người, crop, tỷ lệ cảnh hoặc vị
trí chữ của mẫu; không lấy các nét đan rổ hay chi tiết phụ còn sót làm yêu cầu.
Đây là mẫu ngôn ngữ phác dùng chung, không phải nguồn nội dung liên tập hoặc
chuẩn identity. Profile gốc của đúng tập tiếp tục là chuẩn nhân vật.

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
truyền màu, độ hoàn thiện của mặt, tóc hoặc shading sang phác. Mẫu v02 quyết
định mức hoàn thiện; profile không được kéo ảnh sang mức model sheet. Hai mẫu
dưới đây chỉ bổ trợ khi cần làm rõ ngôn ngữ nét, không bắt buộc truyền đồng
thời với mẫu v02; không lấy nhân vật, pose, đạo cụ hay khung của mẫu:

- `../assets/pencil-style-procession.png`
- `../assets/pencil-style-over-shoulder.png`

Hai mẫu bổ trợ được người dùng cung cấp và chốt kiểu nét; không phải
profile/canon của tập. Khi sửa, truyền đúng phác làm edit target cùng profile
gốc và mẫu mức giản nét v02. Giữ
camera, hierarchy, khoảng cách, crop và cử chỉ đã được chọn, chỉ thay phần được
phản hồi. Nếu cấu trúc cần đổi, trình preview revision trước production.

Khai vai trò từng file đúng với input thực tế: `detail-level-reference`,
`identity-costume-reference`, `edit-target` khi có. Nếu công cụ giới hạn số
reference, chuẩn bị packet có vai trò rõ thay vì âm thầm bỏ mẫu hoặc profile
bắt buộc; không khai đã truyền file chỉ được nhắc tên trong prompt.

Ngay lượt đầu, mở prompt bằng mức phác và vai trò reference, sau đó mới tới
scene/camera/actors. Giữ phần phong cách ngắn, cụ thể; không cộng dồn câu cấm
hoặc dùng chỉ dẫn tương đối như “bỏ 70% chi tiết” khi chưa có ảnh. Không tạo
bản nhiều chi tiết trước rồi mặc định chạy thêm lượt giản nét. Dùng đường bao
tóc/râu, vài nếp vải dài và nét tay đủ đọc cử chỉ ngay từ đầu; vẫn giữ anatomy,
identity và bằng chứng kể chuyện cần thiết.

Khung prompt cho lượt đầu (điền phần `<…>`, bỏ dòng không áp dụng; khi sửa,
thêm edit target và delta gọn trước phần scene):

```text
Sparse pencil composition study on plain white, <tỉ lệ khung theo layout/spread>.
Match the simplification and finish level of <file mẫu v02>: almost blank faces,
unfilled outer hair/beard silhouettes, main garment outlines and only a few long structural folds.
No eyes, eyebrows, pupils, individual curls or hair strands, small fabric wrinkles,
skin texture, shading, hatching, grey/black fills, shadows, paper texture, text or letters.
References: <file mẫu v02> = detail level and line economy ONLY; ignore its characters,
poses, layout, framing and scene content. <file profile thực sự truyền> = identity
and costume ONLY; ignore their color, rendering and level of finish.
Scene: <khoảnh khắc và context bắt buộc>. Camera: <cỡ cảnh, góc máy, độ cao, hướng nhìn của camera>.
Actors: <id – vị trí/độ sâu – hướng đầu – cử chỉ chính – dấu hiệu identity giữ lại>.
Leave clear space for text at <vùng chữ/balloon theo layout>.
Convey facing and action through head silhouette, posture and clear natural gestures.
Keep only background contours needed to understand the location and activity.
```

## Loại và tạo lại

Trước khi trình, xem output và mẫu v02 ở cùng cỡ trang hoặc cỡ chủ thể tương
ứng. Kiểm riêng mặt, tóc/râu, nếp vải, tay và nền: mật độ nét có gần mức mẫu
không; có thêm chi tiết hoàn thiện không phục vụ camera/cử chỉ không. So mức
giản nét, không so bố cục hay đòi hình mới giống contour mẫu. Ghi bằng chứng
nhìn thấy trong review; không kết luận đạt chỉ vì prompt có câu “tối giản”.

Không trình preview cho người dùng nếu ảnh có một trong các lỗi sau; ghi lỗi vào
reference map rồi tạo lại với prompt nhấn đúng lỗi đó:

- Có mắt, lông mày, nét biểu cảm, màu, mảng xám, hatch, bóng hoặc texture giấy.
- Mức phác dày hơn mẫu v02 do tóc/râu có nhiều nét nội bộ, nếp vải vụn hoặc
  chi tiết nền không phục vụ staging. Sửa đúng phần dư, giữ cử chỉ và identity;
  không thêm một lượt giản nét nếu ảnh đầu đã đạt.
- Có chữ, glyph, số hoặc ký hiệu giả chữ.
- Chép nhân vật, đạo cụ, pose hoặc khung của mẫu nét thay cho nội dung scene.
- Sai identity so với profile, thiếu nhân vật/context bắt buộc hoặc lệch camera
  của direction đã chọn.

Tự tạo/chỉnh lại phác composition đến khi đạt, không giới hạn số lần tạo lại
cho cùng một lỗi và không cần người dùng mở đợt mới sau hai ảnh. Mỗi lượt phải
review ảnh thực, giữ phần đã đạt và sửa có mục tiêu; nếu lỗi lặp, đổi cách sửa,
parent hoặc staging/camera trong direction đã chọn, không gọi lặp mù. Không hạ
chuẩn hoặc trình bản còn lỗi như preview đủ điều kiện duyệt. Dừng để trình duyệt
khi phác đạt nghệ thuật và QA áp dụng; chỉ hỏi sớm khi cần quyết định đổi hướng
kể/nguồn, báo lỗi khi công cụ không thể tiếp tục, hoặc dừng theo yêu cầu người dùng.

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
