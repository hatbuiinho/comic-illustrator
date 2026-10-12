# Toolchain của project

Agent tự chuẩn bị công cụ; người dùng không cần chạy lệnh chuẩn bị. Trước tác
vụ đầu tiên trong phiên có dùng script, PDF, composition preview, QA hoặc
delivery, chạy bootstrap đúng hệ điều hành. Đọc/sửa Markdown và trao đổi nội
dung đơn thuần không cần bootstrap.

## Windows

Bootstrap:

```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\bootstrap-windows.ps1
```

Với lệnh workflow thủ công, ưu tiên wrapper
`powershell -ExecutionPolicy Bypass -File .\scripts\run-with-tools.ps1 -- <lệnh> <tham-số>`.
Bootstrap phải idempotent: chỉ cài tool còn thiếu, đồng bộ `.venv` khi
`requirements-tools.txt` đổi và lưu snapshot version vào `.tools/state.windows.json`.

## macOS

Bootstrap:

```sh
./scripts/bootstrap-macos.sh
```

Với lệnh workflow thủ công, ưu tiên wrapper
`./scripts/run-with-tools.sh <lệnh> <tham-số>`.
Bootstrap dùng Homebrew, chỉ cài formula còn thiếu, đồng bộ `.venv` khi
`requirements-tools.txt` đổi và lưu snapshot version vào `.tools/state.macos.json`.
Nếu thiếu Homebrew, bootstrap tự chạy installer chính thức; macOS có thể yêu
cầu người dùng nhập mật khẩu quản trị. Không ghi state READY nếu cài thất bại.

## Kiểm tra môi trường

Không coi state là bằng chứng duy nhất; kiểm tra command thực tế vì tool có
thể đã bị gỡ hoặc PATH đã đổi. Không commit `.venv/` hay state theo máy.
Thực hiện cài đặt theo quyền truy cập và cơ chế phê duyệt của môi trường hiện tại.
