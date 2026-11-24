# Chương 9 — Hệ điều hành Linux và Hệ điều hành Windows

Nguồn: **W11** (`Week11-Chapter9 2024.pdf`, 57 trang) trong `Lý thuyết/`. Số trang dưới đây tính theo trang PDF từ 1. Đã kiểm tra trực tiếp hình kiến trúc Windows 10 ở trang 40 và sơ đồ chuyển đổi địa chỉ/paging Windows 10 ở trang 50–51.

Mỗi bài tóm tắt ngắn các ý chính, con số dễ bị hỏi trắc nghiệm và thuật ngữ tiếng Anh kèm đối chiếu trang PDF. Đây là bản ôn đã soạn, không phải đáp án chính thức hay bằng chứng đã học/thành thạo.

## Mục lục bài ôn

| Mục trong slide | Bản ôn | Nguồn |
|---|---|---|
| 9.1 | [Hệ điều hành Linux](9.1-he-dieu-hanh-linux.md) | W11 trang 5–31 |
| 9.2 | [Hệ điều hành Windows](9.2-he-dieu-hanh-windows.md) | W11 trang 32–55 |

## Ghi chú nguồn và trọng tâm đề cuối kỳ cũ

- Chương 9 xuất hiện **1–2 câu trắc nghiệm trực tiếp** ở các đề gần đây (`2023–2024 CK1`, `2023–2024 CK2`, `2024–2025 CK1`), chủ yếu hỏi **con số cụ thể** và **tên thành phần/công cụ**:
  - Linux: số loại kernel module (**4**), số vùng bộ nhớ vật lý (**6 vùng** theo slide 2024 — xem ghi chú đối chiếu đề cũ ở bài `9.1`), công cụ IPC chuyển dữ liệu (`Pipe`, `Network`, `Shared memory` vs `Signal` không chứa dữ liệu).
  - Windows: thành phần ảo hóa (`Hyper-V Hypervisor`), công cụ quản lý cấu hình (`Registry` và `hives`).
- Ghi chú lỗi đánh máy nhỏ trong slide gốc `W11`: trang 9 ghi tiêu đề `9.1.3 Tổng quan về Linux` (thực tế nằm giữa mục `9.1.1`); trang 18 gõ thiếu chữ `n` trong `conflict-resolutio mechanism`; trang 49 thiếu dấu phẩy giữa `free` và `standby` khi liệt kê 6 trạng thái trang. Bài ôn giữ đúng ý và chính tả chuẩn.
