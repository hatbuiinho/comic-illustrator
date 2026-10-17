---
name: comic-production
description: Điều phối trực tiếp quy trình minh họa truyện tranh nhiều giai đoạn từ đọc nguồn đến bàn giao. Chỉ dùng khi người dùng gọi đích danh skill này ($comic-production hoặc /comic-production) hoặc yêu cầu rõ dùng skill này; mọi yêu cầu tạo hình minh họa thông thường phải route qua comic-page-guide.
---

# Điều phối sản xuất truyện tranh

Áp [quy tắc nghệ thuật](../comic-shot-design/references/art-first-policy.md).
Chỉ dùng skill này khi được gọi đích danh; không thay entry point comic-page-guide.

Skill này là explicit-only. Không tự động chọn, đọc hoặc gọi skill này chỉ vì
người dùng yêu cầu làm hoàn chỉnh một page, frame hoặc chuỗi shot. Trong trường
hợp đó, dùng `comic-page-guide`. Chỉ tiếp tục ở đây khi người dùng gọi đích danh
`$comic-production` (Codex), `/comic-production` (Claude Code) hoặc yêu cầu rõ
dùng skill này.

Xác định deliverable và chỉ thực hiện các giai đoạn cần thiết. Yêu cầu trực tiếp
mới nhất của người dùng luôn được ưu tiên hơn mặc định của workflow.

## Routing

1. Resolve context tối thiểu: dùng `comic-continuity-manager`; nếu chưa có
   artifact biên dịch thì để `comic-source-reader` mở cửa sổ nguồn cần thiết.
2. Đọc và kiểm chứng nguồn: dùng `comic-source-reader`.
3. Thiết kế shot/storyboard: dùng `comic-shot-design`.
4. Viết prompt: dùng `comic-prompt-writer`.
5. Tạo, chỉnh hoặc tạo variant ảnh: dùng `comic-image-production`.
6. Kiểm tra nội dung nhìn thấy: dùng `comic-visual-qa`.
7. Kiểm tra master trong layout có chữ: dùng `comic-layout-qa` khi deliverable
   gắn với layout; coi vùng brief là guide, không phải frame cứng.
8. Khi người dùng chọn đúng master và QA áp dụng đạt, dùng `comic-delivery`
   chuyển đúng hình đã tạo vào `approved/`, rồi commit continuity event đã được
   xác nhận và invalidate đúng dependency downstream. Không tự tách layer.
9. Sau bàn giao, đề xuất tách nhân vật/background bằng ImageGen hoặc chuẩn bị
   bộ InDesign. Chỉ khi người dùng yêu cầu rõ mới gọi production hậu kỳ và QA
   tương ứng. Không chạy anatomy QA.

Không chạy lại giai đoạn đã được người dùng chốt nếu dependency của giai đoạn
đó không thay đổi. Nếu input stale, chỉ chạy lại consumer chịu ảnh hưởng; không
chạy lại cả tập. Không tự biến một tác vụ độc lập thành toàn bộ pipeline.

Sau khi sửa script dùng chung, chạy
`scripts/test-comic-skills.js` cùng validator skill trước khi bàn giao.

## Trạng thái kiểm tra

Mỗi kiểm tra điều kiện phải là một trong ba trạng thái:

- `REQUIRED`: áp dụng và có thể làm deliverable FAIL.
- `NOT_APPLICABLE`: không liên quan đến loại deliverable.
- `SKIPPED_BY_USER`: người dùng chủ động bỏ qua; ghi lý do và phạm vi, không
  tính là FAIL.

Nếu người dùng không nêu phạm vi override, chỉ áp dụng cho deliverable hiện tại.

## Điểm dừng

Chỉ yêu cầu quyết định khi lựa chọn làm thay đổi đáng kể nội dung, composition
hoặc output active. Khi có 2–3 lựa chọn thực tế, trình bày thành danh sách đánh
số ngắn. Không chuyển file sang `approved/` nếu chưa có xác nhận rõ.
