# Chuyển style giữ nguồn

> Cập nhật người dùng 2026-10-29 — `SKIPPED_BY_USER`, toàn dự án:
> style duy nhất là **ttpq comic light** (`docs/style-ttpq-comic-light.md`,
> đường dẫn từ root). Các yêu cầu rendering, bảng trang sức/ref style cũ,
> override st03 và khối prompt style cũ bên dưới đã được thay thế; không
> copy các phần đó vào prompt mới. Workflow, identity và QA fidelity vẫn giữ.
> Chỉ khi ảnh có tu sĩ mới đọc `docs/monastic-robes.md` cho màu/cách quấn y.


Phương án người dùng tạm chốt ngày 2026-10-22 sau test Punna v004.
Áp dụng cho chuyển style ảnh có yêu cầu giữ chi tiết trong Image Playground;
không mở rộng thành thay đổi thiết kế, nguồn sáng hoặc policy chung của project.

## Phân vai nguồn

- Ảnh/profile gốc: chuẩn duy nhất cho identity, tuổi, cấu trúc mặt, thiết kế,
  pose, bố cục, màu và vị trí/hình dạng các vùng sáng–tối. Xem lại trước mỗi lượt.
- [Ref đen trắng v002](../../../../studios/playground/outputs/chan-dung-den-trang/portrait-v002.png):
  lấy nét cấu trúc đen thanh, rõ và vuốt đầu nét; cách xử lý rìa mảng tiết chế.
  Không lấy khuôn mặt, tuổi, nếp nhăn, y phục hoặc bản đồ ánh sáng của ref.
- Khi có trang sức, dùng
  [bảng trang sức v003](../../comic-image-production/references/style-st03/jewelry-board-v003.png)
  cho cách diễn vật liệu giảm bóng. Không lấy hình phụ kiện, connector, motif,
  số hàng hạt, độ rộng/số vòng tay từ bảng; chúng còn sai khác với nguồn Punna.
  Không áp trang sức hoặc ref này vào vùng không có trang sức.
- Màu vàng/đá/ngọc vẫn theo nguồn từng nhân vật; ref đen trắng không yêu cầu
  output grayscale. Yêu cầu grayscale riêng phải ghi đúng phạm vi.

## Khóa trong prompt thực tế

Nêu rõ vai trò từng input và các điều cấm phù hợp trước khi gửi. Dùng các khóa
dưới đây, điều chỉnh tên/vùng theo ảnh thực; không chỉ ghi “giữ nguyên chi tiết”.

```text
Ảnh gốc quyết định toàn bộ identity, thiết kế, màu, bố cục và bản đồ sáng–tối.
Giữ vị trí, hình dạng, diện tích và hướng của các vùng sáng–tối có trong nguồn.
Không tự thêm, tách, gộp, mở rộng hoặc dịch mảng. Vùng không có ranh giới mảng
trong nguồn không được thêm ranh giới mới, đặc biệt trên trán, hai bên đầu và má.
Không lấy hình dạng/vị trí mảng từ ref style, suy diễn thêm giải phẫu hoặc tạo
nguồn sáng mới. Không viền đen quanh ranh giới bóng.
Chỉ làm rõ nét cấu trúc đã có, làm sạch texture/hạt và xử lý rìa mảng sẵn có.
Giữ độ đầy má, hàm, tuổi, biểu cảm; không thêm rãnh má/nếp nhăn hoặc tăng độ dày
mày theo khuôn mặt ref. Không giảm chi tiết thiết kế chỉ để làm phẳng hình.
Nếu hiệu ứng style cần thêm/đổi chi tiết hoặc mảng, ưu tiên nguồn và bỏ hiệu ứng
đó tại vùng ấy. Không tự ép mọi vùng trơn thành thêm các ô cel-shading.
```

Giữ tổ chức nét/mảng 2D theo policy ở toàn bộ vật liệu đang có. Với nguồn có
rendering liên tục không thể chuyển đạt cả style lẫn khóa mảng, báo rõ xung đột
và giới hạn kết quả; không âm thầm thêm mảng rồi ghi đạt fidelity.

## Trang sức giảm bóng

- Kim loại: nền màu chủ đạo chắc, bóng ở mép/chỗ chồng bằng mảng thiết kế dịu;
  chỉ ít điểm sáng nhỏ, giảm tương phản. Vẫn đọc được chất liệu, không tô lì
  toàn bộ một màu hoặc đổi vàng thành xám trong output màu.
- Đá: màu nguồn đậm hơn nền kim loại khi phù hợp; mảng sáng nhỏ tiết chế,
  không đốm trắng bầu dục lớn, bóng vòm hoặc dải phản chiếu liên tục.
- Ngọc/hạt sáng: nền sáng với mảng bóng nhỏ; không chấm trắng chói lặp trên
  mọi hạt, không chuyển sắc cầu mượt.
- Cấm bóng cầu/trụ chuyển mượt, airbrush tạo khối, phản chiếu gương/chrome,
  bóng nhựa ướt, sparkle/glow và texture vi mô. Không thêm hạt, nét khắc,
  hoa văn hay phụ kiện để bù việc giảm bóng. Giới hạn 2D còn lại theo policy.

## QA và trạng thái tạm chốt

- So trực tiếp nguồn gốc: mặt/tuổi/mày, mảng đầu–má–cổ, nếp vải, silhouette,
  hình/số lượng/bố trí trang sức; không dùng ref vật liệu làm chuẩn thiết kế.
- Kiểm riêng độ bóng: đốm trắng, dải phản chiếu, bóng cầu/trụ và điểm sáng lặp;
  đồng thời kiểm có làm mất chất liệu hoặc mất chi tiết không.
- Ref vật liệu v003 và
  [test Punna v004](../../../../studios/playground/outputs/truong-gia-punna-st03/punna-v004.png)
  được tạm chọn làm hướng xử lý giảm bóng, không phải duyệt mọi chi tiết của ảnh.
  Test còn bóng cầu ở vài hạt và lệch thiết kế/mảng; giữ các giới hạn đó trong QA,
  không coi là đặc điểm style hoặc waiver fidelity.
- ImageGen vẽ lại, prompt không chứng minh pixel-lock. Ghi lỗi quan sát được,
  không kết luận “giữ nguyên toàn bộ” khi chưa có bằng chứng. Số lượt sửa và
  điều kiện dừng theo contract studio; không tự lặp vô hạn.
- Lưu prompt đầy đủ, input/vai trò, activeBrief, parent/attempt và QA theo
  version. Nếu dùng thử ref chưa đạt để chẩn đoán theo yêu cầu, ghi experiment;
  không nâng nó thành chuẩn identity/profile/canon hay ref toàn project.
