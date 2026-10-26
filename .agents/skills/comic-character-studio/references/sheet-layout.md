# Bố cục sheet và độ phân giải

Một phần của [SKILL.md](../SKILL.md) Character Studio. Đọc khi dựng sheet tổng hợp.

## Bố cục sheet tổng hợp mặc định

- Một ảnh tổng hợp ngang trên nền trắng.
- Vùng trái khoảng 35–40% ngang: một chân dung chính diện từ ngực lên thật
  lớn, thông tin cơ bản bên dưới. Vùng phải khoảng 60–65%: bốn góc đứng
  một hàng, gồm chính diện, 3/4, nghiêng và sau lưng.
- Điều chỉnh hai vùng theo silhouette và độ dài chữ. Giữ khoảng cách rõ;
  tránh chỗ trống lớn trong khi vùng khác chen chúc.
- Kích thước canvas và tỷ lệ chia vùng trên là điểm khởi đầu, không phải
  khung cố định. Khi thiếu không gian, agent tự mở rộng chiều ngang và/hoặc
  chiều cao của sheet để chứa đủ chân dung, các góc đứng và thông tin;
  không cần hỏi lại chỉ để tăng canvas. Ưu tiên tăng ngang khi các góc chen
  nhau, tăng cao khi thiếu chỗ cho đầu/chân hoặc thông tin.
- Mỗi góc có vùng riêng và khoảng trắng rõ giữa silhouette, kể cả phần
  nhô ra như khăn, tóc, tay, vạt áo hoặc mũi giày. Không chạm, chồng lấn,
  cắt mất bộ phận hoặc bóp nhân vật để vừa ô. Giữ tỷ lệ nội bộ và tương quan
  đầu–cổ–vai–thân–tay–chân theo nguồn; không kéo/nén riêng một trục,
  thu hẹp vai, rút ngắn chân hoặc đổi chi tiết để tiết kiệm chỗ.
- Khi cần đổi kích thước hiển thị, chỉ scale đồng đều toàn nhân vật và
  giữ cùng tỷ lệ giữa các góc. Không thu nhỏ đến mức mất khả năng đọc mặt
  hoặc chi tiết nhận diện để tránh mở rộng canvas. Khi dàn nhiều ảnh,
  được crop phần khung trắng dư nhưng không cắt silhouette.
- Prompt thực tế khi dựng góc/sheet phải nêu rõ: mở rộng canvas khi cần,
  mỗi góc có khoảng trắng riêng, giữ nguyên tỷ lệ nguồn; cấm ép, bóp hoặc
  rút ngắn nhân vật để khớp bố cục. QA kiểm trọn đầu/chân, khoảng cách giữa
  các silhouette và tỷ lệ từng góc trước khi coi sheet đạt.
- Chân dung thấy trọn đầu, tóc hoặc khăn, vai và ngực; đủ lớn để nhận diện mặt.
- Các góc đứng cùng tỷ lệ, đường chân và chiều cao tương ứng; thấy trọn đầu/chân.
- Thông tin gồm tên, tuổi, giới tính, chiều cao, vai trò và xuất thân theo
  brief/nguồn; chỉ in trường có dữ kiện, không tự thêm tuổi, chiều cao,
  quê quán, tầng lớp hoặc tiểu sử.
- Không mặc định thêm biểu cảm, bảng màu, đạo cụ hoặc ô chi tiết.
- Khi brief có chiều cao, mặc định in trường `Chiều cao` trong phần thông tin
  trên ảnh profile/sheet, ví dụ `Chiều cao: 1,65 m`; giữ đúng giá trị người
  dùng cung cấp và đồng bộ với brief hiện hành. Nếu chưa có thì bỏ trường,
  không suy từ hình hoặc tự đặt số. Không thêm thước đo/vạch chiều cao nếu
  chưa được yêu cầu. Người dùng yêu cầu ẩn chiều cao thì giữ nội bộ và không in.
- Giữ bố cục đã chốt. Việc nhắc lại danh sách thành phần không tự là yêu cầu
  đổi bố cục; chỉ đổi khi người dùng yêu cầu rõ. Tự mở rộng canvas và nới
  khoảng cách để chứa đủ hình theo quy tắc trên không phải đổi bố cục:
  giữ thứ tự góc, số lượng hình và nội dung đã chốt. Nếu người dùng khóa
  kích thước/tỷ lệ khung cụ thể, tuân ràng buộc đó và báo xung đột khi không
  thể chứa đủ hình mà vẫn giữ tỷ lệ và độ đọc; không âm thầm bóp hình.

## Độ phân giải

- Sheet ngang ưu tiên mục tiêu khởi đầu 3840 × 2560 px hoặc tương đương khi
  công cụ hỗ trợ; đây không phải kích thước tối đa. Được tự tăng kích thước
  và đổi tỷ lệ canvas để chứa đủ hình theo quy tắc trên. Nếu công cụ tạo
  ảnh giới hạn canvas, tạo các góc từ cùng nguồn rồi dàn trên canvas rộng
  hơn; không ép anatomy để khớp giới hạn công cụ. Ghi riêng kích thước
  dàn trang và độ phân giải gốc của ảnh thành phần, không gọi upscale là
  chi tiết native mới.
- Kiểm khả năng trước khi cam kết, xác minh pixel file sau tạo; ghi riêng mục tiêu/thực tế.
- Kích thước trong prompt không chứng minh output đạt; upscale không tạo chi tiết gốc.
- Chưa đạt thì báo giới hạn, không tuyên bố hoàn tất yêu cầu độ phân giải.
