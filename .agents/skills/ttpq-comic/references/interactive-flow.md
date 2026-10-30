# Flow tương tác và menu lệnh

Áp dụng theo yêu cầu người dùng ngày 2026-10-30. Context vẫn là deliverable mặc
định. Các bước sau chỉ chạy khi người dùng yêu cầu; không thêm gate của workflow
khác. Đây là menu câu lệnh trong phản hồi, không phải dropdown hay tính năng UI
mới của app.

## Cách trình menu

- Hiện 2–3 lựa chọn đúng bước, đánh số và đặt tên rõ. Mỗi câu có thể copy nằm
  trong code block riêng; không thêm số/bullet vào nội dung câu.
- Với bước chỉ có một hành động tiếp theo thích hợp, chỉ đưa một block.
- Có thể dùng `:codex-followup` cho lựa chọn ngắn khi app hỗ trợ; hai prompt
  cố định vẫn phải hiện nguyên văn trong code block để người dùng copy được.
- Trước khi trình, thay placeholder bằng đường dẫn/version thực của spread.
  Lệnh ngắn được resolve theo spread/record đang active; nhiều bản thì hỏi
  đúng bản còn mơ hồ, không tự chọn bản khác.
- Lựa chọn menu không tự thực thi; chỉ làm bước người dùng đã yêu cầu. Giữ
  nguyên hai prompt cố định bên dưới; thông tin thực thi bổ sung lưu riêng,
  không sửa câu người dùng thành phiên bản khác.

## 1. Sau khi trả context: luôn đề xuất câu đọc hiểu

Sau khối context, layout và profile, thêm “Bước tiếp theo — đọc context, chưa
tạo ảnh” cùng câu này. Trong phản hồi, dẫn link bản context cụ thể ngay trước
block để “bản context này” không mơ hồ.

```text
Hãy đọc bản context này cùng layout và profile được dẫn chiếu. Chưa tạo ảnh.
```

Khi nhận lệnh: mở đúng bản context, record, layout và profile được dẫn chiếu;
không chỉ dựa vào trí nhớ hội thoại. Báo ngắn tình huống/ý chính, thời điểm,
nhân vật và điều cấm; nêu xung đột hoặc nguồn thiếu thực sự liên quan. Không
tạo ảnh. Ghi context version đang active vào record; không coi bước này là
đã nạp một session riêng cho ImageGen.
Sau khi đọc xong, cuối phản hồi trình hai lựa chọn ở mục 2: yêu cầu agent đề
xuất phương án hoặc người dùng đưa phương án có sẵn. Chưa tự đề xuất phương
án và chưa chuyển sang chờ lệnh tạo outline khi người dùng chưa chọn hướng.

## 2. Sau đọc context: hai cách có phương án

**1. Đề xuất phương án minh họa thật sự điện ảnh**

```text
Dựa trên context và layout vừa đọc, hãy đề xuất 2–3 phương án minh họa thật sự điện ảnh, khác nhau rõ ràng cho spread này. Chưa tạo ảnh.
```

Đề xuất phải thể hiện ý đồ điện ảnh qua lựa chọn khoảnh khắc, cỡ cảnh, góc máy,
chiều sâu, hướng nhìn và nhịp kể; không chỉ đổi vị trí nhân vật hoặc gắn nhãn
“điện ảnh”. Khi có nhiều scene, làm rõ nhịp chuyển và quan hệ giữa các scene.
Dùng các mục ý đồ điện ảnh ở bước 5 của SKILL. Tách từng ý thành bullet có nhãn;
không tự chạy nhánh gói prompt hai lượt. Người dùng chọn phương án thì ghi ý
đồ vào brief/record và trình lệnh outline.

**2. Dùng phương án có sẵn**

```text
Mình sẽ gửi phương án minh họa có sẵn. Hãy đọc cùng context và layout đang dùng, tóm tắt cách bạn hiểu ý đồ của mình và chỉ ra điểm xung đột nếu có. Chưa tạo ảnh; chờ yêu cầu tiếp theo.
```

Người dùng có thể gửi phương án ngay cùng lệnh. Không tự thay bằng phương án
khác. Chỉ hỏi phần thiếu gây thay đổi đáng kể ý đồ; không buộc chọn option do
agent đề xuất. Khi nguồn và ý đồ đủ rõ, có thể đi thẳng từ context tới outline.

## 3. Tạo clean outline: prompt cố định nguyên văn

```text
dùng style ttpq comic light để vẽ hình minh họa và dàn trang cho page này ở dạng clean outline, chữ sẽ hòa với hình nhưng giữ nguyên khổ chữ, chữ có thể được reflow để ôm hình 1 cách sống động, phần chữ bên phải là tiếng anh, bên trái là tiếng việt, truyện này là truyện về cuộc đời Đức Phật nên nhân vật sẽ là người Ấn Độ thời đó ạ
```

- Context và phương án active quyết định nội dung/scene. Layout xác định
  canvas, nội dung chữ và typography; cho phép reflow để ôm hình, không tự
  giảm khổ chữ. Đây là outline đen trắng theo ngôn ngữ nét của ttpq comic light,
  chưa áp màu hay render bóng thành phẩm.
- Dùng layout và profile gốc với vai trò rõ; nguồn EN theo contract, không
  tự dịch. Không giả vờ có font/khổ chữ chính xác nếu chỉ có ảnh raster; báo
  giới hạn quan sát được. Chữ trong ảnh vẫn là tham khảo dàn trang.
- Trước tạo ảnh: đọc các hướng dẫn style/era/toolchain áp dụng và skill
  `imagegen`. Dùng ImageGen trực tiếp, không gọi chuỗi page-guide/studio.
- Lưu ảnh thật `outputs/outline-vNNN.png` cùng prompt/nguồn/kết quả kiểm trong
  record; không ghi đè, không chỉ để bản cache. Xem ảnh toàn spread và vùng
  quan trọng trước khi nhận xét: scene, profile, anatomy, gáy, nét, chữ VI/EN,
  khổ chữ và đường ôm. Báo lỗi thấy được, không ghi PASS khi chưa xem.
- Mỗi yêu cầu tạo/chỉnh mặc định một candidate rồi trình để người dùng comment;
  không tự tạo lặp nhiều bản. Nếu công cụ lỗi, báo lỗi, không tuyên bố đã có ảnh.

## 4. Sau outline: menu sửa / tạo lại / màu

Sau mỗi lần tạo hoặc chỉnh outline thành công, luôn trình đủ ba lựa chọn
ở mục này, gồm lựa chọn dàn trang màu với prompt cố định nguyên văn.
Không thay menu bằng một câu hỏi góp ý chung hoặc chỉ đưa lựa chọn sửa.
Câu sửa và tạo lại cần nội dung người dùng điền; khi trình
menu dùng hướng dẫn một dòng bên ngoài block để người dùng bổ sung comment.

**1. Chỉnh outline**

```text
Chỉnh outline vừa tạo theo các comment mình gửi kèm. Giữ phần không được yêu cầu đổi; chưa tạo bản màu.
```

**2. Tạo outline khác**

```text
Tạo lại một outline khác từ context, layout và profile gốc, theo hướng mình gửi kèm. Chưa tạo bản màu.
```

**3. Tạo minh họa màu — prompt cố định nguyên văn**

```text
dùng style ttpq comic light để dàn trang màu, outline chỉ dùng để tham khảo scene, nhân vật phải được lấy chuẩn từ profile. Không ref lại output cũ
```

## 5. Sửa, tạo lại và lên màu

- Comment sửa outline: xác định delta, phần giữ và version đích; xem lại ảnh
  đích cùng profile gốc trước lượt edit. Tạo lại outline: xuất phát từ nguồn
  gốc và phương án mới, không dùng outline bị bỏ làm chuẩn identity.
- Lệnh màu trực tiếp cho phép thực hiện, không cần hỏi lại “đã duyệt chưa”.
  Resolve đúng outline người dùng muốn dùng; chỉ hỏi nếu có nhiều bản mà chưa
  rõ bản nào. Không tự tạo màu chỉ vì người dùng nói outline đẹp/ổn.
- “Không ref lại output cũ”: không dùng ảnh màu cũ, outline lỗi hoặc output
  khác làm chuẩn nhân vật/style. Outline được chọn là ngoại lệ được chỉ định
  rõ để tham khảo scene và chữ; profile gốc quyết định mặt, tóc, trang phục,
  tỷ lệ và dấu nhận diện. Đọc và xem lại profile gốc mỗi lượt có nhân vật.
- Không dùng khối KEEP EXACTLY mọi outlines trong mẫu prompt màu cũ. Cho phép
  vẽ lại nhân vật đúng profile trong scene đã chọn, không tự đổi moment hay
  ý đồ. Giữ chữ và cách ôm đã chọn trừ yêu cầu đổi rõ; kiểm thực tế và báo nếu
  việc sửa silhouette gây xung đột với chữ. Không hứa khóa pixel.
- Ghi override `SKIPPED_BY_USER` toàn flow theo contract ngày 2026-10-30 đối
  với khóa contour/identity theo output; không bỏ các kiểm nội dung/profile.
- Lưu `outputs/color-vNNN.png` hoặc outline version mới, có record trỏ context,
  phương án, outline scene và profile version thực dùng. Trình ảnh bản lưu
  trong spread cùng kết quả kiểm ngắn. Không tự phê duyệt bản cuối.
- Sau màu, menu chỉ cần “Chỉnh màu/minh họa” hoặc “Tạo bản màu khác”; cả hai
  vẫn lấy profile gốc, không tự dùng ảnh màu trước làm ref. Nếu người dùng
  yêu cầu dùng output trước để edit, ghi override đúng phạm vi lượt đó.
