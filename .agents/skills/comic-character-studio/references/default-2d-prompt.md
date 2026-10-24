# Prompt chuyển style 2D mặc định

Nguồn: người dùng chọn prompt trong hội thoại và yêu cầu tích hợp ngày
2026-10-23. Áp dụng trong Character Studio, không thay policy toàn project.
Chỉ @ skill kèm ảnh là đủ khởi động luồng chuyển style, không tự tạo sheet.

## Khối lõi

Giữ nội dung dưới đây làm nền prompt thực tế; không thay bằng một tên style
hoặc diễn giải dài. Resolve rule thiết kế trước khi gửi: với tu sĩ, bổ sung
màu/cách quấn y chuẩn và reference tương ứng; câu giữ trang phục chung bên
dưới không miễn các rule đó. Với yêu cầu giữ khác chuẩn rõ, thay phần liên
quan và ghi override. Nguồn identity luôn là ảnh gốc, không phải output cũ.

```text
Chuyển ảnh gốc sang phong cách 2D hand-drawn animation, với những nguyên tắc:

- Giữ nguyên cấu trúc khuôn mặt, biểu cảm, nụ cười nếu có, râu/ria nếu có và tỷ lệ nhân vật theo ảnh gốc.
- Không phóng to mắt, thu nhỏ mũi, làm thon mặt, kéo dài cổ, trẻ hóa hoặc tự cân chỉnh lại các bộ phận.
- Giữ nguyên kiểu tóc, trang phục, phụ kiện, tư thế và bố cục. Không tự thêm hoặc thay đổi thiết kế.

- Tóc, da, khăn/mũ đội đầu nếu có và trang phục được vẽ thành các mảng màu rõ ràng, với nét vẽ tay thanh, có chủ ý.
- Da sử dụng khoảng 3 tông: màu gốc, vùng sáng và vùng tối. Mỗi mảng có màu đồng nhất bên trong, không thêm các dải chuyển màu trung gian.
- Giữ màu da gốc, không tự tăng vàng/cam, làm trắng hoặc làm tối da.
- Giữ nguyên màu môi từ ảnh gốc, gồm sắc màu, độ sáng, độ bão hòa và sự khác biệt giữa môi trên–môi dưới nếu có. Không tự đổi sang đỏ/hồng, tăng độ rực hoặc tô hai môi cùng một màu khi nguồn khác nhau; chỉ chuyển cách thể hiện sang mảng màu 2D, không đổi hình hay độ đầy môi.
- Giữ các nét cấu trúc cần thiết ở mắt, mũi và miệng; không viền đậm toàn bộ khuôn mặt hoặc từng mảng bóng.

- Giữ nếp vải chính, hoa văn nhận diện và hình dáng trang sức; loại bỏ texture ảnh thật, vân dệt và bóng từng sợi tóc.
- Trang sức và phụ kiện cũng được diễn bằng mảng màu phẳng, không bóng cầu hoặc phản chiếu mượt.
- Background dùng cùng ngôn ngữ vẽ 2D với nhân vật.

- Không gradient, không airbrush, không hiệu ứng 3D, không texture hạt và không tạo cảm giác ảnh chụp được xử lý bằng filter.
- Chỉ áp dụng cho các thành phần thực sự có trong ảnh; không tự thêm tóc, râu/ria, khăn/mũ đội đầu hoặc phụ kiện.
```

## Bổ sung có điều kiện và QA

- Chỉ thêm dấu nhận diện dễ mất của nguồn và các khối theo checklist lắp
  prompt trong SKILL.md; gộp các câu trùng, không lặp mô tả style nhiều lần.
- Ngôn ngữ: giữ khối lõi tiếng Việt như đã chốt. Dán các khối bổ sung tiếng
  Anh nguyên văn bên dưới tiêu đề `Additional constraints:` và
  `Avoid/Negative constraints:`; không dịch lại hoặc trộn câu hai ngôn ngữ
  trong cùng một dòng.
- Giữ màu da nguồn mặc định. Khi được yêu cầu màu khác, thay dòng màu da
  bằng yêu cầu mới, giữ tuổi/tỷ lệ và ghi provenance; không mở nhánh bảng
  màu chỉ vì có mô tả màu trong yêu cầu chuyển style trực tiếp.
- Kiểm riêng màu môi trên và môi dưới trực tiếp với ảnh gốc, gồm vùng sáng
  và tối đang thấy; không lấy màu môi từ ref style hoặc output cũ. Không áp
  tên màu của một nhân vật thành công thức chung. Chỉ thay màu môi khi người
  dùng yêu cầu rõ, ghi override đúng phạm vi và giữ hình/tỷ lệ nguồn.
- Khi có y, áp dụng màu/cách quấn chuẩn và input ref theo SKILL.md; không
  coi câu “giữ màu da gốc” là yêu cầu giữ màu y nguồn. Khi có trang sức,
  xem/truyền bảng vật liệu bắt buộc, giữ thiết kế theo nguồn.
- Kiểm tỷ lệ trước: mặt/ngũ quan, đầu–cổ–vai–thân và phần chi thực sự thấy.
  Sau đó kiểm màu da, khoảng ba nhóm tông, nét mũi/miệng, tóc/vải/trang sức/nền.
  Không hiểu “khoảng 3 tông” thành đúng ba mã pixel cho cả ảnh hoặc tính nét,
  môi, mắt, anti-alias như một tông da mới; vẫn kiểm dải chuyển màu thật.
- Không PASS từ prompt: kiểm gradient/airbrush ở trán, má, mũi, cằm, cổ,
  phần da khác và từng vật liệu. Đạt nét không bù lệch tỷ lệ hoặc màu.
  Giữ giới hạn tự sửa hiện hành; không chạy ảnh kiểm chứng khi chỉ bảo trì skill.
- Lưu prompt thực tế, input/vai trò, ngoại lệ và QA theo version. Chờ người
  dùng duyệt ảnh đạt kiểm trước sheet; sheet được chọn rõ mới lưu profile.
