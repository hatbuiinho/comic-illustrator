# Fast QA gates

Nhận trực tiếp `qaLocks` từ source snapshot; không đọc lại toàn bộ script khi
lock còn fresh.

```json
{
  "style2D": {
    "required": true,
    "groups": ["characters", "materials", "vehicles", "background"]
  },
  "topography": { "type": "FLAT", "provenance": "user" },
  "activeProcess": { "agents": "workers-moving-stone", "minVisible": 2 }
}
```

Chạy theo thứ tự và dừng sớm:

1. `STYLE_GATE`: nhìn bốn nhóm theo policy phong cách active: nét và mảng màu
   thiết kế dẫn hình, shading/chi tiết cùng ngôn ngữ 2D, không texture ảnh hoặc
   tạo khối kiểu render. Chuyển sắc mềm nhẹ được policy cho phép không tự tạo
   FAIL. Một nhóm drift rõ thì trả `STYLE_2D_DRIFT`; chỉ rõ dấu hiệu và vùng
   cần sửa, không ép phẳng toàn ảnh. Không chạy QA sâu sau FAIL.
2. `TOPOGRAPHY_GATE`: so silhouette đường chân trời với lock. Sai thì trả
   `TOPOGRAPHY_MISMATCH` ngay.
3. `PROCESS_GATE`: đếm đại diện process agent nhìn thấy. Thiếu thì trả
   `PROCESS_AGENT_MISSING` ngay.
4. Chỉ khi ba gate PASS mới chạy focus, profile, context, storytelling và layout.

Output tối thiểu:

```json
{
  "fastGates": {
    "style": "PASS|FAIL",
    "topography": "PASS|FAIL",
    "process": "PASS|FAIL"
  },
  "stopReason": null,
  "remediationDelta": null
}
```

Không mô tả dài khi PASS. Với FAIL, chỉ ghi dấu hiệu nhìn thấy, phần cần giữ và
một delta sửa cụ thể.
