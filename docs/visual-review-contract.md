# Kiểm hình và điều kiện chuyển bước

Đọc cùng [policy phong cách](project-style-policy.md). Tài liệu này quy định
cách kiểm, không tạo style mới. Dùng cho hai studio và phần kiểm áp dụng của
minh họa tập; không đưa gate storyboard, storytelling hoặc layout vào studio.

## Reference và nhận diện

Với mỗi ảnh đầu vào, ghi nguồn, vai trò, thuộc tính được lấy và thuộc tính
không được lấy. Vai trò trong prompt là yêu cầu, không bảo đảm mô hình cô lập
được ảnh hưởng. Sau tạo, kiểm cả phần cần giữ và dấu hiệu lẫn từ ref khác.
Ref style có mặt cần kiểm riêng mắt/mày, tóc/râu, tuổi và thiết kế trang phục.
Crop hoặc bảng vật liệu là lựa chọn giảm ảnh hưởng, không phải giải pháp bảo đảm.

So trực tiếp với identity gốc. Tùy nhân vật, xác định dấu hiệu quan trọng như
hình mắt/mí, khoảng cách mắt, hình/dày/hướng mày, mũi, hàm, ria. Một sai lệch
trọng yếu đủ làm identity không đạt; không đếm cứng số lỗi. Đổi góc/biểu cảm
không đòi trùng pixel; phần khuất hoặc thiếu độ phân giải phải ghi giới hạn.

## Style theo vùng đang có

Xem toàn hình ở kích thước sử dụng và crop vùng cần xác minh. Với mỗi nhóm,
ghi bằng chứng nhìn thấy, kết quả và vùng cần sửa; không PASS từ outline,
prompt hoặc tên st03. Nhóm không xuất hiện ghi không áp dụng, không tạo thêm.

| Nhóm | Cần quan sát |
|---|---|
| Mặt/da | Mí/hốc mắt, mũi, môi, tai, má, hàm/cổ: nét và mảng có dẫn hình hay bóng nối tiếp đang mô phỏng thể tích thật? Giữ tuổi và dấu riêng. |
| Tóc/râu | Cụm và nét có chủ ý hay bóng từng sợi/lọn lấn át thiết kế? |
| Vải | Mảng/nếp chính có rõ, còn chi tiết cần thiết hay mỗi nếp thành khối render? |
| Trang sức/đá/ngọc | Nét/mảng gợi vật liệu hay phản chiếu, bóng cầu, độ trong mô phỏng vật liệu thật? Có tự thêm hoa văn/hạt/nét khắc, tăng mật độ so với nguồn hoặc lấn trọng tâm mặt ở kích thước sử dụng không? |
| Đạo cụ/background | Cùng ngôn ngữ với nhân vật, đúng mức chi tiết và ánh sáng theo policy? |

Mềm cục bộ, nhiều sắc độ hoặc một dấu sáng đồ họa không tự là lỗi. Cũng không
PASS vì đã bỏ hết highlight: shading có thể vẫn render. Không đặt số mảng,
sắc độ hay cấm mọi dấu sáng; không làm mất nếp, hoa văn, tóc, tuổi hoặc khiến
hình khô/nhạt để đạt nhãn 2D. Delta chỉ nhắm dấu hiệu drift đã thấy và giữ phần
đúng policy. Mỗi nhận xét phân biệt lỗi chắc chắn và phần chưa đủ bằng chứng.

## Bước sau, sửa và thử nghiệm

- Tách kết quả style, identity và các kiểm bắt buộc khác. Đạt một nhóm không
  bù nhóm chưa đạt. Thiếu bằng chứng không đồng nghĩa ảnh có lỗi và không tự
  tạo lại; phải kiểm thêm hoặc ghi chưa đủ bằng chứng.
- Chỉ dùng bản làm nền sản xuất bước sau khi các thuộc tính bước đó phụ thuộc
  đã đạt. Không khóa feature sai chỉ vì nó nằm trong bản cha. Output FAIL có
  thể là ảnh đích sửa phần lỗi, không trở thành nguồn identity/style mới.
- Test chẩn đoán được người dùng yêu cầu có thể dùng bản chưa đạt để cô lập
  nguyên nhân; ghi mục tiêu test và lỗi kế thừa, không nâng thành mẫu chuẩn.
  Khi so phương pháp, giữ brief/pose/input ổn định và ghi biến đã thay, thay vì
  kết luận nhân quả từ một ảnh đẹp. Không bắt mọi tác vụ qua chì rồi tô.
- Trong giới hạn tự sửa của workflow đang dùng, lỗi nhìn thấy sửa an toàn được
  thì dùng lượt sửa có mục tiêu. Ghi attempt count, parent, lỗi, delta, phần
  giữ và kết quả regression so với nguồn gốc/bản cha. Hết lượt mà còn lỗi thì
  trình chưa đạt và chờ hướng tiếp; không reset lượt bằng đổi chiến lược.
- Chọn phương pháp hoặc duyệt một bộ phận không phải duyệt toàn ảnh/profile.
  Chỉ miễn check khi user cho phép rõ, ghi check, version và phạm vi.

## Giới hạn công cụ và record

Phân biệt vẽ lại bằng model, xử lý pixel và tô dưới lớp nét cố định thật.
Lệnh preserve không chứng minh pixel-lock. Lọc giữ tọa độ vẫn có thể mất nét
hoặc đổi độ dày; tách lớp tự động không phải đồ nét thủ công. Chỉ khẳng định
bất biến theo mức công cụ/bằng chứng thực sự hỗ trợ; nếu không đạt phải báo
trước khi coi output là nền hợp lệ cho bước sau.

Record dùng nguồn tương đối và trỏ tới brief revision hiện hành, gồm yêu cầu
đã thay cùng provenance user, không sửa brief gốc/QA cũ. Tách rõ:

Khi yêu cầu thiết kế đổi, tạo brief revision có version mới và ghi `activeBrief`
trong record hiện hành. Khi tiếp tục, resolve con trỏ này và nguồn user thay
vì chỉ đọc brief gốc hoặc suy từ ảnh gần nhất. Nếu chưa có con trỏ, đối chiếu
revision và yêu cầu trực tiếp mới nhất rồi ghi lại; không tự coi số version ảnh
lớn nhất là nguồn brief đã duyệt.

- `requirementChanges`: thay đổi thiết kế, như chiều cao mới thay số cũ;
- `experiment`: phương pháp thử và biến thay đổi, không mặc định là waiver;
- `SKIPPED_BY_USER`: miễn/override quy tắc hay check cụ thể, có scope/version.

Không có waiver thì tiêu chí hiện hành vẫn áp dụng. Record ngắn cần đủ nguồn,
input thực tế, parent/attempt, QA theo phần áp dụng, hạn chế và điều kiện đi tiếp.
