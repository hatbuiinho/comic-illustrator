# Kiểm tra tính nhất quán workflow từ ca Punna — v001

Ngày kiểm: 2026-10-20. Trạng thái: **đề xuất để owner xem, chưa áp dụng bản vá**.

## Phạm vi và giới hạn

Đã đọc Character Studio, Image Playground, studio contract, policy/st03, các reference style/profile/fast-gate của Visual QA, reference-selection/retry-quality của Image Production và validator báo cáo. Đối chiếu các record/output đã xem trong chuỗi Punna, không tạo ảnh mới. Đây không phải audit toàn repository hoặc bằng chứng hệ thống đã chạy sai ở mọi tập.

Các quy tắc của production tập chỉ dùng để so sánh kiến trúc; **không áp workflow minh họa tập vào studio**. Kiểm tra lại tài liệu không đồng nghĩa thay đổi policy. Hai thử nghiệm validator dùng JSON tổng hợp trong thư mục tạm và đã được dọn; không sửa source.

## Kết luận chính

Policy hiện hành đã cấm tạo khối kiểu render và cho phép mềm cục bộ. Không có căn cứ đổi mục tiêu st03 thành tuyệt đối phẳng. Vấn đề gồm: thực thi QA chưa đúng, độ chi tiết QA không đồng đều giữa studio và production, điều kiện giữ nhận diện giữa các bước còn thiếu, và giới hạn công cụ bị mô tả quá chắc.

## Các bất thường và đề xuất

### A01 — QA studio thiếu cách thực thi cụ thể của chuẩn chung
- **Mức:** cao. **Loại:** thiếu liên kết thực thi + lỗi agent.
- **Bằng chứng:** studio-contract yêu cầu xem/kiểm style nhưng không chỉ rõ phân rã; Visual QA/style-qa đã yêu cầu styleConsistencyByElement và không PASS từ outline. Studio không route qua Visual QA mặc định. Punna pencil-test/color-v002 vẫn bỏ sót môi, bọng mắt, mũi trước khi owner chỉ ra.
- **Đề xuất:** một checklist đánh giá style dùng chung, không copy policy: kiểm vùng mặt (mí/hốc mắt, mũi, môi, tai, cổ), tóc, vải và vật liệu xuất hiện. Ghi vùng được xem, tín hiệu, trạng thái; không bắt chạy workflow storytelling/layout của tập.
- **Nơi sửa dự kiến:** studio-contract, Character Studio và style-qa bằng dẫn chiếu nguồn chung.
- **Nghiệm thu:** phát hiện được các vùng mặt còn render trong color-v002 nhưng không FAIL tự động các mảng cổ/vải chỉ vì có chuyển sắc.

### A02 — Ghi vai trò ref bị hiểu thành khả năng cô lập ảnh hưởng
- **Mức:** cao. **Loại:** giới hạn công cụ + thiếu kiểm kết quả.
- **Bằng chứng:** quy tắc đã phân biệt identity/style, nhưng sheet-v003/v004 vẫn nhận chòm râu từ chân dung style; bỏ ref mặt ở v005 không tự mang lại đúng style.
- **Đề xuất:** ghi thêm phần được lấy/phần cấm lấy và kiểm sau tạo; nói rõ vai trò trong prompt là ý định, không bảo đảm mô hình tuân thủ. Khi ảnh style chứa mặt, kiểm mắt/mày/râu/tuổi và thiết kế bị lẫn. Tách/crop/bảng vật liệu là lựa chọn giảm rủi ro, không là giải pháp bắt buộc hay được bảo đảm.
- **Nơi sửa:** studio-contract/Character Studio; reference-selection của production chỉ dẫn chiếu nguyên tắc chung khi phù hợp.
- **Nghiệm thu:** ảnh đẹp đúng style nhưng có thêm râu/đổi mắt không được đi tiếp như identity đạt.

### A03 — Bước sau bảo vệ hình dáng vốn đã sai ở bước trước
- **Mức:** cao. **Loại:** lỗi thực thi + thiếu điều kiện chuyển bước trong studio.
- **Bằng chứng:** portrait-test/assessment-v001 ghi bản nét mắt/mày đã lệch; vẫn tô để test cô lập. Điều này được nói rõ là thử nghiệm, nhưng không phải chuỗi production hợp lệ. pencil-test tiếp tục giữ mặt thuôn từ chì.
- **Đề xuất:** phân biệt test chẩn đoán được user cho phép với ứng viên sản xuất. Nếu identity chưa đạt, output không là chuẩn hình học cho bước sau; có thể dùng để thử kỹ thuật nhưng không đổi thành identity hợp lệ. Cần đạt đồng thời các kiểm bắt buộc trước selection/profile.
- **Nơi sửa:** Character Studio và studio-contract.
- **Nghiệm thu:** test vẫn được tiến hành khi có mục đích rõ, nhưng không tự nâng test thành mẫu chuẩn; không bắt mọi nhân vật phải qua gate chì.

### A04 — Chưa có tiêu chí đủ nhạy cho mắt/mày; ngưỡng hai dấu hiệu gây mơ hồ
- **Mức:** cao. **Loại:** đặc tả chưa rõ.
- **Bằng chứng:** profile-qa dòng 13–15 nói nhầm identity hoặc sai từ hai dấu hiệu cốt lõi làm shot FAIL. Không khẳng định một sai lệch là PASS, nhưng có thể bị diễn giải như vậy. Punna cho thấy chỉ nhóm mắt/mày đã đổi nhận diện rõ.
- **Đề xuất:** xác định dấu nhận diện quan trọng theo từng người; một sai lệch trọng yếu đủ FAIL, thay vì đếm cứng. Với chân dung kiểm cả hình mắt/mí, khoảng cách, mày, mũi, hàm/ria theo mức nhìn thấy; không đòi trùng pixel khi đổi góc.
- **Nơi sửa:** profile-qa; Character Studio dẫn chiếu phần áp dụng.
- **Nghiệm thu:** bắt được mắt đổi hình dù tóc/trang phục đúng; không FAIL khác biệt nhỏ không ảnh hưởng identity hoặc thay đổi hợp góc nhìn.

### A05 — Validator trả PASS cấu trúc dễ bị nhầm với ảnh đạt
- **Mức:** cao nếu dùng kết quả làm điều kiện đi tiếp; chưa thấy bằng chứng validator đã được chạy trong chuỗi Punna.
- **Loại:** giao diện trạng thái + lỗ hổng schema.
- **Bằng chứng tái hiện:** JSON chỉ có schemaVersion/output tồn tại, không có checks → exit 0, status PASS. JSON có REQUIRED style=FAIL kèm evidence/remediation → vẫn exit 0, status PASS.
- **Diễn giải:** đây phù hợp với validator kiểm cấu trúc chứ không tự xem ảnh; lỗi nằm ở nhãn mơ hồ và việc requiredChecks do report tự khai. Không nói validator đã chấm nhầm hình bằng thị giác.
- **Đề xuất:** tách reportValidity khỏi qaOutcome/eligibleForNextStep; có preset kiểm bắt buộc theo deliverable, kiểm evidence cho PASS, lý do/scope cho ngoại lệ. FAIL hợp lệ vẫn reportValidity=PASS nhưng qaOutcome=FAIL. Chưa đủ bằng chứng không tự regenerate.
- **Nơi sửa:** validate-visual-qa.js và reference/schema/fixture tương ứng. Không buộc studio dùng nguyên schema tập.
- **Nghiệm thu:** hai ca tái hiện không thể được hiểu là ảnh đạt; thêm ca thiếu evidence, REQUIRED bị bỏ, ngoại lệ sai scope và báo cáo hợp lệ thực sự.

### A06 — Cam kết giữ hình học/layer vượt năng lực thực tế
- **Mức:** cao. **Loại:** lỗi diễn đạt/thực thi.
- **Bằng chứng:** prompt preserve rồi ImageGen redraw nét vẫn đổi mặt. Tách trực tiếp giữ tọa độ nhưng mất nét mảnh, phát sinh nét từ bóng. Các lớp màu xử lý tự động gây poster hoặc nhạt; record sau đã ghi giới hạn này.
- **Đề xuất:** phân biệt ba thao tác: generative redraw; biến đổi pixel; tô trên layer cố định thật. Chỉ nói pixel-lock khi có mask/layer và kiểm chứng phù hợp. Không gọi lọc ngưỡng là đồ nét thủ công. Nếu công cụ không giữ được, báo giới hạn trước khi dùng làm nền bước sau.
- **Nơi sửa:** studio-contract/record hướng dẫn, không đổi chuẩn thẩm mỹ.
- **Nghiệm thu:** statement về giữ nguyên không vượt bằng chứng; đổi độ dày nét do lọc vẫn được ghi dù tọa độ không đổi.

### A07 — Sửa style có nguy cơ biến thành quy tắc ép phẳng mới
- **Mức:** vừa–cao. **Loại:** sai lệch prompt và đánh giá.
- **Bằng chứng:** prompt Punna từng dùng quy định một mảng bóng/một crescent/no dots như giải pháp cục bộ. Policy/style-qa hiện hành không cấm mọi highlight, gradient hoặc nhiều sắc độ.
- **Đề xuất:** thêm ví dụ đối chứng có chú thích: softness hợp lệ, rendering drift, over-flattening/mất chi tiết. Không đưa giới hạn số mảng/sắc độ hoặc cấm mọi dấu sáng thành chuẩn toàn project. Tập trung quan hệ nét–mảng–shading và hierarchy.
- **Nơi sửa:** style-qa tham chiếu policy; mẫu minh họa chỉ được dùng đúng thuộc tính owner chọn.
- **Nghiệm thu:** không FAIL một dấu sáng đồ họa tiết chế; có thể phát hiện render liên tục dù không có white glint.

### A08 — Nguồn yêu cầu hiện hành và override chưa rõ
- **Mức:** vừa. **Loại:** quản lý trạng thái + thuật ngữ.
- **Bằng chứng:** brief vẫn 1m72; 1m80 nằm rải trong record/prompt. Một số record dùng SKIPPED_BY_USER cho thay chiều cao hoặc nét chì, dù đây thường là sửa brief/phương pháp test chứ chưa chắc miễn một check/policy.
- **Đề xuất:** lưu brief revision/active requirement trỏ nguồn user, giữ brief gốc; tách superseded design requirement, experimental method và check waiver. SKIPPED_BY_USER chỉ dùng khi thực sự bỏ/override quy tắc hoặc check cụ thể, có scope.
- **Nơi sửa:** studio-contract và mẫu record Character Studio; không sửa hồi tố lịch sử test trong đợt này.
- **Nghiệm thu:** tiếp tục phiên vẫn resolve 1m80 mà không đọc toàn chat; không suy từ pencil test thành miễn style/no-grain cho bản màu.

### A09 — Retry có giới hạn nhưng hành vi tự sửa chưa đủ rõ
- **Mức:** vừa. **Loại:** thiếu điều kiện ra quyết định, không phải thiếu quyền sửa.
- **Bằng chứng:** studio-contract đã cho một lượt sửa có mục tiêu rồi báo nếu vẫn lỗi. Không cần nhập vòng retry production tập vào studio. Các lượt đầu mình thường dừng ở báo lỗi hơn là dùng lượt sửa phù hợp.
- **Đề xuất:** trong giới hạn hiện tại, lỗi nhìn thấy có thể sửa an toàn thì dùng lượt sửa; ghi attempt count, observedDefect, phần giữ và kiểm regression. Nếu còn lỗi thì trình chưa đạt, không gọi đó là bản hoàn tất. Không tạo vòng vô hạn và không tự duyệt profile.
- **Nơi sửa:** studio-contract; mẫu record ngắn.
- **Nghiệm thu:** bắt được drift thì sửa một lượt nếu còn lượt; không bảo vệ feature đã sai, không reset budget chỉ vì đổi chiến lược.

### A10 — Thử nghiệm thay nhiều biến nên chưa chứng minh phương pháp nào tốt hơn
- **Mức:** vừa. **Loại:** chất lượng bằng chứng.
- **Bằng chứng:** các lần thay ref mặt/bảng vật liệu/chì đồng thời đổi prompt, bố cục, màu và cách dựng. Nhận xét owner thích chì là preference có giá trị, không chứng minh nhân quả hoặc tính ổn định qua nhân vật khác.
- **Đề xuất:** test hồi quy theo ca: giữ identity/pose/brief/công cụ ổn định, thay một yếu tố chính; chấm riêng identity/style/detail. Ghi rõ observation, giả thuyết và giới hạn. Chỉ thêm ảnh mới sau khi owner duyệt kế hoạch.
- **Nơi sửa:** hướng dẫn test/mẫu report; không biến chì→màu thành mặc định bắt buộc toàn project.
- **Nghiệm thu:** có thể biết bản vá cải thiện gì và làm xấu gì; không dùng một ảnh đẹp làm bằng chứng hệ thống ổn định.

## Phương án sửa để owner chọn

### 1. Vá thực thi và kiểm tra — đề xuất ưu tiên
- **Phạm vi:** QA studio, chuyển bước, ref role, giới hạn công cụ, active brief, trạng thái validator.
- **Giữ:** định nghĩa thẩm mỹ st03, độ mềm được phép, routing hai studio, giới hạn tự sửa và quyền chọn profile của owner.
- **Đánh đổi:** cần cập nhật một số liên kết/schema/fixture nhưng không thay workflow tạo hình mặc định.
- **Kết quả mong đợi:** lỗi đã thấy không được bỏ sót hoặc gọi đạt, dù generation vẫn có thể tạo lỗi.

### 2. Vá thực thi rồi hiệu chuẩn mẫu đối chứng
- **Phạm vi:** toàn bộ phương án 1, sau đó thêm bộ crop ví dụ được owner chọn để hiệu chuẩn ranh giới style.
- **Giữ:** ví dụ chỉ là bằng chứng thuộc tính, không là nguồn mặt/màu da/tỷ lệ dùng chung.
- **Đánh đổi:** cần thêm vòng owner đánh giá mẫu và ca test khác; không hứa loại bỏ hoàn toàn drift.
- **Kết quả mong đợi:** ngoài ngăn sai bước còn giảm khác biệt cách hiểu style giữa các lượt.

Không đề xuất đổi policy thành zero-gradient hoặc mandatory-pencil. Những thay đổi mang tính thẩm mỹ mới cần quyết định riêng của owner.

## Kế hoạch xác minh sau khi được duyệt

1. Kiểm tài liệu/link/scope: studio dùng tiêu chí chung nhưng không bị kéo vào gate tập.
2. Kiểm validator bằng fixture, tách cấu trúc hợp lệ và QA đạt.
3. Đánh giá hồi quy output cũ: nhận diện drift, mặt/material render, over-flat, crop thiếu bằng chứng; kết quả mới là audit riêng, không ghi đè QA lịch sử.
4. Owner chọn kế hoạch generation nhỏ nếu cần; chưa tạo ảnh mới trong đợt kiểm này.

## Chưa thực hiện

Chưa sửa AGENTS.md, policy, skill, validator, profile, brief hoặc record cũ. Chỉ thêm báo cáo kiểm này. Chưa có bộ mẫu st03 Character Studio được owner chọn chính thức; chưa có kiểm thử đủ để kết luận chì→màu ổn định hơn cho mọi nhân vật.
