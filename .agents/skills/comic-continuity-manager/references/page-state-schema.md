# Schema page-state (schemaVersion 2)

Nguồn duy nhất cho cấu trúc `page-state`. Skill khác chỉ dẫn chiếu file này,
không định nghĩa schema riêng.

## Vị trí và định dạng

- Một page một file: `<tap>/<Part N>/pages/page-XXX/page-state.yaml`. Không dùng
  `.json` hoặc `.yml`; không tạo hai file trạng thái cho cùng page.
- Key dùng camelCase. Mọi đường dẫn tương đối từ thư mục tập (chứa
  `episode.json`), kể cả trong `artifacts` và `active`.
- Trước khi thay file bằng bản viết lại lớn (reset, migrate), lưu bản cũ vào
  `page-XXX/history/page-state-<lý-do>-<YYYYMMDD>.<ext>`.
- Validate sau mỗi lần ghi:
  `python3 .agents/skills/comic-continuity-manager/scripts/comic-context.py validate <page-state.yaml>`.

## Cấu trúc

```yaml
artifactType: page-state
schemaVersion: 2
scope:
  episode: "Tap 53"            # bắt buộc
  part: "Part 1"               # bắt buộc, đúng tên thư mục part
  page: 8                      # bắt buộc, số nguyên
  frame: null                  # id frame hoặc null nếu cả page/spread
  target: full-spread          # tùy chọn: full-page | full-spread | frame
  printedPages: [18, 19]       # tùy chọn
status: CURRENT                # CURRENT | STALE | CONFLICT
updatedAt: "2026-10-12"
stage: composition             # xem danh sách stage
confirmed:                     # chỉ true khi người dùng xác nhận rõ
  target: true
  sourceSnapshot: true
  narrativeDirection: true
  composition: false
  productionRun: false
  qaResolution: false
  selectedForLayout: false
  finalOutput: false
active:                        # lựa chọn đang hiệu lực; null khi chưa có
  direction: direction-1-trust-opens-secret
  composition: page008-d1-trust-v08
  compositionStatus: PROPOSED  # PROPOSED | CONFIRMED | null
  candidate: null              # đường dẫn candidate đang xét
  bestAestheticVersion: null   # mốc thẩm mỹ tốt nhất cho retry
  selectedVersion: null        # chỉ ghi khi SELECTED_FOR_LAYOUT
artifacts:                     # vai trò -> đường dẫn artifact hiện hành
  sourceSnapshot: Part 1/pages/page-008/source-snapshot-v05.md
candidates:                    # tùy chọn: lịch sử candidate/version
  - version: 1
    path: Part 2/pages/page-006/outputs/page006-option2-pencil-sketch-v1.png
    role: intermediate-pencil-sketch
    qa: null
    status: null               # PASS | FAIL | null
    note: "..."
superseded: []                 # artifact cũ không còn là đầu vào active
qa: {}                         # tùy chọn: kết luận QA dạng nhãn, vd exactTextCapacity
userConfirmed:                 # xác nhận rõ của người dùng
  - key: page008.narrativeDirectionV05
    value: "Hướng 1 — Lòng tin mở bí quyết"
    date: "2026-10-11"
    evidence: "1"
facts: []                      # key/value/provenance/evidence theo artifact-model
contextLocks: []
forbidden: []
generatedFrom: []              # path/kind/fingerprint
pendingQuestion: null          # câu hỏi/cổng đang chờ người dùng
nextAction: null
unresolved: []
staleReasons: []
```

Có thể thêm key riêng của page (ví dụ `layout`, `production`) khi cần, miễn
không trùng nghĩa với key chuẩn ở trên.

## Stage

Chuỗi mặc định: `scope` → `source` → `direction` → `composition` → `production`
→ `visual_qa` → `selected_for_layout` → `delivery` → `complete`.
`layer_package` và `layout_qa` là nhánh tùy chọn giữa selection và delivery khi
người dùng yêu cầu bộ layer; không cần tạo stage/artifact này cho ảnh đơn.
Các stage vẫn được validator giữ theo thứ tự cũ để tương thích artifact hiện có.

- `production` gồm viết prompt và tạo candidate.
- `visual_qa` gồm QA candidate và chờ người dùng chọn master.
- `selected_for_layout` trở đi chỉ khi người dùng đã chọn rõ một version.

## Bất biến được validator kiểm

- `stage` từ `production` trở đi cần `confirmed.composition: true` và
  `active.compositionStatus: CONFIRMED`.
- `stage` từ `selected_for_layout` trở đi cần `confirmed.selectedForLayout: true`
  và `active.selectedVersion`.
- `stage: complete` cần `confirmed.finalOutput: true`.
- `confirmed.<gate>` sau chỉ true khi gate trước đó true.
- Không dùng key schema cũ: `confirmedGates`, `activeChoice`, `active_choice`,
  `active_direction`, `pending_question`, `stale_reasons`, `next_action`,
  `selectedPageComposition` và `target` cấp gốc.
- Đường dẫn trong `artifacts`/`active`/`candidates` không tồn tại chỉ là cảnh báo.
