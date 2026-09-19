# Page 24 — 2D relock storyboard options

## Trạng thái

- Process mới: `storyboard-pending`; chưa có option nào được người dùng chọn.
- Các output và option cũ của page 24 chỉ là lịch sử tham chiếu; không tự được
  xem là đã đạt `visualComponentLock` mới.
- Không tạo ảnh ở giai đoạn này.

## Nguồn đã đọc

- `Tap 53/notes.md`, `Tap 53/shot_notes.md`, `Tap 53/workflow.md`
- `Part 1/scripts/chapter3.md` (toàn chương; scene cuối chương)
- `tmp/pdf_pages/page_24.png`
- Năm profile: `Lao dao truong.png`, `Dao si tre gay go.png`,
  `Ga dao si xoa man suon.png`, `Dao si cao to tho kech.png`,
  `Dao si ngoi gan cua.png`.

## Frame map đề xuất

| Frame | Box chuẩn hóa | Tỷ lệ | Vai trò | Spine / safe zone |
| --- | --- | --- | --- | --- |
| H1 | `x=0–0.43, y=0.7639–0.9988` | 2.57:1 | reaction | Gáy `x=0.47–0.53`; mép phải H1 `x=0.38–0.43` chỉ là đá tối giản. |
| H2 | `x=0.57–1, y=0.7639–0.9988` | 2.57:1 | transition cutaway | Gáy `x=0.47–0.53`; mép trái H2 `x=0.57–0.62` chỉ là đá tối giản. |

## Context lock và narrative inference

- **Explicit:** trong điện thờ đá cổ khuất rừng có đúng năm đạo sĩ; sau đề nghị
  cuối, lão đạo trưởng nắm chặt tay, tất cả im bặt; gió qua tường đá đổ nát làm
  đèn dầu vụt tắt.
- **Strongly implied:** H1 là sự im lặng bị ép chặt, chưa ai thực hiện kế hoạch;
  H2 là dư âm vật lý trực tiếp, không phải một cảnh trang trí về ngọn đèn.
- **Unknown / không được tự thêm:** nội dung kế hoạch ngoài lời thoại, vũ khí,
  nạn nhân, cung điện, tinh xá, phụ nữ trong mưu kế, người Phật giáo hoặc người
  thứ sáu.
- **H1:** trước gió; đèn dầu còn cháy rất nhỏ. **H2:** ngay sau gió; không lửa,
  không người, không ngoại cảnh.

## Visual component lock — bắt buộc cho mọi option

| Thành phần | Class / tỷ lệ / silhouette | Style treatment 2D | Cấm đọc sai |
| --- | --- | --- | --- |
| Lão đạo trưởng | Lão tóc-râu trắng, búi cao, khăn cam; mặt và nắm tay là hai neo lớn nhất H1. | Nét viền đậm đều, da/vải mảng phẳng, 1–2 cel-shadow cạnh cứng. | Không trẻ hóa, không photoreal beard/hair, không nắm tay kiểu siêu anh hùng. |
| Bốn đạo sĩ phụ | B gầy lo âu; C ria dày và tay trái xoa sườn; D vai/thân lớn nhất sau lão; E ngồi sát cửa, dải kem chéo. Mỗi người phải còn ít nhất hai dấu hiệu nhận dạng ở kích thước strip. | Cùng nét, palette đất nâu/cam/xám và mức cel-shading với lão; chi tiết giảm theo lớp sâu. | Không clone, không hoán đổi profile, không ai đang nói hay hành động mưu kế. |
| Điện thờ đá | Nội thất đá cũ, sàn tối, 1–2 mảng tường đổ/nứt lớn; nền phải lùi hoàn toàn. | Các mặt đá là mảng phẳng, cạnh góc cạnh có line art; shadow theo mảng cứng. | Không texture đá thật, displacement/CGI, ruin fantasy, ánh sáng tia/ray. |
| Đèn dầu H1 | Đèn đất nung nhỏ, lửa còn cháy là dấu hiệu timeline, không phải focus. | Flame 2–3 mảng màu phẳng nhỏ, sáng cục bộ cạnh cứng. | Không glow/bloom, volumetric light hay lửa quá lớn. |
| Đèn dầu H2 | Đèn đất nung cận cảnh; tim đen là focus, khói kéo ngang sang khe nứt. | Gốm và tường cùng line art/mảng phẳng; khói là 1–2 dải cel-shaded đồ họa. | Không lửa, khói ảnh thật/soft, blur, gradient, bokeh. |
| Ánh sáng / gió | H1 tối, chỉ có sáng cục bộ từ đèn; H2 tối hơn sau khi tắt. Gió chỉ hiện qua hướng khói. | Không thành một hiệu ứng riêng; mọi sáng/tối là các mảng cel-shading. | Không god ray, haze, ánh trăng điện ảnh hay motion blur. |

## Semantic thumbnail gate

- H1 ở kích thước dàn trang phải đọc lần lượt: nắm tay / mặt lão → sự im lặng
  của bốn profile → đèn còn cháy nhỏ; không được đọc thành cuộc họp đông người
  hay tranh luận.
- H2 phải đọc: tim đèn đen → khói ngang → khe nứt → tối; không cần chữ để biết
  đèn đã tắt.
- Khi che nhân vật, H1 vẫn là nội thất điện thờ đá cũ; khi che đèn ở H2, tường
  vẫn là mảng đá 2D, không được chuyển thành background bán thực.

## Option A — nắm tay ép cả vòng họp

- **Focus / khoảnh khắc:** nắm tay lão ở foreground trái vừa siết lại sau lời
  đề nghị cuối; sự im lặng lan qua bốn người còn lại.
- **Camera / người thấy:** low medium-wide từ trong vòng họp; đủ năm đạo sĩ.
  Lão trái-trung, B/C sâu sau lão, D là vai lớn nền phải, E sát mảng cửa nứt.
- **Placement:** fist `x=0.07–0.19`; mặt lão `x=0.18–0.27`; B–E chạy theo lớp
  sâu `x=0.22–0.37`; đèn còn cháy nhỏ `x=0.29–0.33`, thấp; `x=0.38–0.43` là
  tường đá tối giản, safe zone trước gáy.
- **Critical cần bảo vệ:** fist, mặt lão, hai dấu hiệu profile của từng B–E,
  flame nhỏ H1; ở H2 là tim đen, khói ngang, khe tường.
- **Điểm mạnh / đánh đổi:** lực kịch tính mạnh nhất và eye path rõ; đổi lại,
  phải kiểm profile rất nghiêm vì strip hẹp dễ làm B/C bị che hoặc thành clone.

## Option B — nửa vòng mở, nắm tay ở tâm

- **Focus / khoảnh khắc:** năm người cùng nén lại trong khoảng lặng; nắm tay
  lão trên gối là điểm tối/đặc nhất ở tâm vòng.
- **Camera / người thấy:** high-angle medium-wide, nửa vòng mở về phía người
  đọc; thấy rõ đúng năm đạo sĩ, không ai bị che.
- **Placement:** vòng người `x=0.05–0.35`; lão tâm-trái, B–E xếp theo cung;
  nắm tay `x=0.17–0.23`; đèn cháy nhỏ sâu ở giữa; `x=0.35–0.43` là đá phẳng.
- **Critical cần bảo vệ:** năm mặt/silhouette profile, nắm tay, đèn còn cháy;
  H2 cố định như Option A.
- **Điểm mạnh / đánh đổi:** đúng “ngồi co cụm thành vòng” và profile dễ QA
  nhất; đổi lại, lực của nắm tay và áp lực tâm lý yếu hơn A.

## Option C — qua vai đạo sĩ trẻ, nhìn vào quyết tâm của lão

- **Focus / khoảnh khắc:** vai co lại của B dẫn vào nắm tay và gương mặt lạnh
  của lão; ba người còn lại là những phản ứng im lặng lùi sâu.
- **Camera / người thấy:** over-the-shoulder medium shot từ B; đủ năm đạo sĩ,
  nhưng B chỉ là điểm nhìn chứ không là chủ thể chính.
- **Placement:** vai B `x=0.05–0.13`; fist `x=0.16–0.25`; mặt lão
  `x=0.23–0.31`; C/D/E theo lớp sâu `x=0.29–0.37`; đèn nhỏ ở thấp-trung;
  `x=0.38–0.43` là đá tối giản.
- **Critical cần bảo vệ:** vai/mặt lo âu B, fist và mặt lão, dấu hiệu C/D/E,
  flame; H2 cố định như Option A.
- **Điểm mạnh / đánh đổi:** bất đối xứng tâm lý rõ nhất, tạo nhịp thay đổi so
  với cảnh nhóm; đổi lại, phần vai B có nguy cơ thu hẹp không gian cho C/D/E.

## H2 cố định sau khi chọn H1

Extreme close-up ngang 2.57:1: tim đèn đen ở phải-trung → khói đồ họa mảnh kéo
ngang sang khe tường đá nứt; trái frame chỉ là đá tối phẳng để thở cạnh gáy.
Không người, không lửa, không thêm côn trùng nhìn thấy.
