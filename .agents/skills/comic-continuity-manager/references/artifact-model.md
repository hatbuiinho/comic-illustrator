# Mô hình artifact continuity

Chỉ tạo artifact có ích cho việc tiếp tục qua nhiều page hoặc nhiều phiên.
Không tạo file rỗng, placeholder hoặc bản sao dài của kịch bản.

## Vị trí đề xuất

```text
<tap>/continuity/episode-canon.yaml
<tap>/continuity/ledger.yaml
<tap>/continuity/scenes/<scene-id>.yaml
<tap>/<part>/<page>/page-state.yaml
```

Nếu project đã có manifest tương đương, mở rộng manifest đó thay vì tạo nguồn
trạng thái song song.

## Trường chung

Mỗi artifact có:

- `schemaVersion`;
- `scope`: episode, part, scene, page, frame khi áp dụng;
- `generatedFrom`: dependency với đường dẫn tương đối, loại nguồn và fingerprint;
- `updatedAt` khi project đang dùng timestamp;
- `facts` hoặc dữ liệu theo loại artifact;
- `unresolved`: điều chưa đủ bằng chứng;
- `status`: `CURRENT`, `STALE` hoặc `CONFLICT`.

Mọi `generatedFrom.path` được tính tương đối từ thư mục tập chứa
`episode.json`, không phải từ thư mục của chính artifact. Nếu project chưa có
`episode.json`, đường dẫn được tính từ thư mục artifact và không được đi ra ngoài
namespace đó.

Mỗi fact ảnh hưởng tới hình có `key`, `value`, `provenance`, `evidence`, khoảng
hiệu lực khi cần và `confidence` nếu là suy luận. `confidence` không nâng
suy luận thành hard lock.

Fingerprint là content hash khi công cụ hỗ trợ; nếu không, dùng revision/mtime
kèm size và ghi rõ phương pháp. Không dùng tên file đơn thuần làm freshness.

## Episode canon

Chỉ chứa dữ kiện ổn định và chỉ mục tới nguồn: character/profile registry,
location/geography registry, style locks cấp tập, timeline/scene index, global
forbidden/future facts và authority/ngoại lệ đang hiệu lực. Không nhúng toàn bộ
profile hoặc script.

## Scene packet

Là đơn vị context mặc định: phạm vi page/frame; thời gian, địa điểm và người
hiện diện; mục tiêu kể chuyện/emotional arc; `continuityIn`/`continuityOut` dự
kiến; physical/knowledge/relationship state; background/geography locks; chi
tiết tương lai bị cấm; cửa sổ nguồn trước/current/sau; unresolved/inference.
`continuityOut` dự kiến không tự động trở thành ledger event.

## Page state

Kết hợp target/stage, cổng đã xác nhận, active choice, dependency revision,
context locks, forbidden facts, đường dẫn artifact hiện hành, pending question
và stale reasons. Page state ghi nhớ quyết định, không thay thế artifact chuyên
môn và không ghi output là canonical trước delivery.

## Continuity ledger

Lưu event theo trật tự truyện. Mỗi event có `eventId`, `effectiveAfter`, scope,
thay đổi before/after, provenance/evidence, output approved liên quan và trạng
thái `CONFIRMED` hoặc `REVOKED`.

Chỉ ghi event từ source fact, xác nhận rõ của người dùng, hoặc delivery đáp ứng
policy. Khi sửa sai, thêm event điều chỉnh/revoke; không âm thầm viết lại lịch
sử nếu artifact downstream đã tham chiếu event cũ.
