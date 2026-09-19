# G3 — Storyboard QA, Page 3, phương án 3

## Lựa chọn đã ghi nhận

- `userAction`: `Chọn option: page003-reprocess-option3-nguoi-cho-ngoai-khung`
- `optionId`: `page003-reprocess-option3-nguoi-cho-ngoai-khung`
- Card xác nhận: `page003-reprocess-option3-confirmed-composition.svg`
- Card PNG để duyệt: `page003-reprocess-option3-confirmed-composition.png` (1622 × 1151)

## Composition được trình duyệt

### Frame trái — `h1-nalini-holds-elder-hand`

- **Focus:** bàn tay bà lão đã được Nalini giữ, đọc như một cái nắm tay không phân biệt.
- **Camera:** insert cận ngang; mặt hai người chủ động ngoài khung.
- **Chi tiết thứ hai:** miếng vá vai áo nâu xám sờn của bà lão, nằm sau cử chỉ.
- **Không gian:** áo bà lão ở lớp gần, cử chỉ ở lớp giữa, đất ướt sương và gốc cây thưa ở lớp nền; không thêm vật che khung.
- **An toàn:** hai bàn tay là `requiredComplete`; miếng vá là `requiredReadable`; mọi chi tiết trọng tâm nằm trong frame trái và cách dải gáy.

### Frame phải — `h2-nalini-warmed-by-volunteers`

- **Focus:** Nalini ở 1/3 phải, giữ cuộn bản vẽ và hướng nhìn về đoàn người chờ.
- **Camera:** medium-wide tiết chế, thấp vừa đủ để người chờ đọc như dư âm chứ không thành cảnh đông người.
- **Dư âm:** ba silhouette chờ nhỏ ở xa bên trái, không hoạt động và không tranh focus.
- **Không gian:** Nalini là lớp giữa; đất sương, gốc cây thưa và ba silhouette xa là lớp nền. Không dùng blur hay hiệu ứng máy ảnh.
- **An toàn:** mặt, turban, cuộn bản vẽ và bàn tay Nalini là `requiredComplete`; ba silhouette là `optionalSupport`, tất cả nằm trọn trong frame phải, xa dải gáy và mép xén.

## Kết quả QA trên composition card

| Gate | Kết quả | Bằng chứng |
| --- | --- | --- |
| `semanticThumbnailGate` | PASS | Ở kích thước layout, mắt đọc tay → miếng vá ở frame trái; mặt Nalini → hướng nhìn → ba người chờ ở frame phải. |
| `spatialDepthGate` | PASS | Frame trái có ba lớp có chủ đích; frame phải dùng Nalini, ba silhouette xa và nền giản lược, không cần vật che khung hoặc hiệu ứng ống kính. |
| `backgroundOnlyGate` | PASS | Khi che nhân vật, vẫn còn đất ướt sương, gốc cây thưa và ba silhouette chờ xa: đúng khoảng đất trống, không đọc thành công trường hay phong cảnh khác. |
| `anatomySilhouetteGate` | PASS | Tỷ lệ người được giữ nguyên khối theo profile; không ép thân hoặc tay để né gáy. |
| `priorityConflictGate` | PASS | Focus của từng frame xa dải gáy và còn khoảng thở; chi tiết nền không cạnh tranh với cử chỉ hay phản ứng. |
| Khóa phong cách | PASS | Card chỉ định nét viền rõ, màu phẳng, tối đa 1–2 mảng cel-shading; cấm CGI, texture thật, blur, DOF, glow và gradient tạo khối. |

## Khóa tạo ảnh khi được duyệt

- Đọc lại và truyền trực tiếp `Tap 53/characters/Bác Nalini.png` và `Tap 53/characters/bà lão.png` ở mỗi lượt tạo có nhân vật.
- Tờ mờ sáng, đất ướt sương; không công trường, dụng cụ, Visakha, Punna, xe ngựa, núi, sông hoặc rừng dày.
- Tạo riêng từng frame ngang khoảng 1,51:1; không gộp montage, không đặt chi tiết kể chuyện sát mép hoặc vào gáy.

**Trạng thái G3:** card đã PASS kiểm tra nội bộ, chờ xác nhận rõ của người dùng trước G4.
