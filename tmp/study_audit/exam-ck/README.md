# Audit đề thi cuối kỳ IT007 (6 đề: 2020–2025)

Nguồn kiểm tra: `Cuối Kỳ/Đề thi/` (6 tệp PDF: `2020-2021 CK1`, `2022-2023 CK1`, `2022-2023 CK2`, `2023-2024 CK1`, `2023-2024 CK2`, `2024-2025 CK1`). Không đọc đáp án riêng; bỏ qua nét bút viết tay trên bản scan (`2020-2021 CK1`). Cache văn bản lưu cùng thư mục (`manifest.json`); 2 đề dạng ảnh scan đã render tạm trong `scans/`.

## Cấu trúc đề (xu hướng mới 2023–2024 CK2 & 2024–2025 CK1)

- **Phần 1 — Trắc nghiệm (6.0đ):** 15–20 câu (trước đó 20–25 câu = 7.5–8.0đ).
- **Phần 2 — Tự luận (4.0đ ở đề mới; 2.0–2.5đ ở đề cũ):**
  - Câu Đúng/Sai (4 ý, phủ Ch5–Ch8).
  - Câu trả lời ngắn tiếng Anh tối đa 2 từ (ví dụ: `virtual memory`, `wait-for`, `liveness`, `thrashing`).
  - Câu giải thích/so sánh ngắn (`TLBs`, `dynamic linking` vs `dynamic loading`, `compaction`, phân mảnh trong paging).
  - Bài tính/đồng bộ lớn: thay trang (`FIFO`/`OPT`/`LRU`), giải thuật `Banker`, phân vùng cố định (`first-fit`/`best-fit`), chuyển đổi địa chỉ/bảng phân trang, đồng bộ tiểu trình bằng `semaphore`.

## Phân bố nội dung xuất hiện trong 6 đề cũ

- **Chương 4:** Chưa thấy câu hỏi trực tiếp trong 6 đề CK cũ đã kiểm. Tuy nhiên người dùng lưu ý cuối kỳ có thể thi một phần Chương 4 (giữ theo dõi riêng, không tự loại bỏ).
- **Chương 5 (Đồng bộ hóa tiến trình):** Race condition, Critical section, 3 yêu cầu, Busy waiting vs Sleep & Wakeup, Cấm ngắt (lỗi trên đa CPU), Peterson/Bakery, instruction reordering & Memory barrier, 2 mô hình bộ nhớ, TestAndSet, Mutex locks, Semaphore (`wait`/`signal`, giá trị âm/dương, hàng đợi PCB, thứ tự gọi), Monitor & Condition variable, Critical Region, Liveness, Bounded-Buffer, Readers-Writers, Dining-Philosopher, tự luận điền `wait()`/`signal()`.
- **Chương 6 (Deadlock):** Định nghĩa, 4 điều kiện cần, RAG & quy tắc chu trình (1 thực thể vs nhiều thực thể), 4 hướng xử lý (bỏ qua, ngăn, tránh, phát hiện & phục hồi), trạng thái safe/unsafe, trạng thái cấp phát tài nguyên, Banker's Algorithm (an toàn + yêu cầu cấp phát), Wait-for graph ($O(n^2)$), phát hiện nhiều thực thể ($O(m \cdot n^2)$), phục hồi (chấm dứt tiến trình, thu hồi tài nguyên).
- **Chương 7 (Quản lý bộ nhớ chính):** Địa chỉ luận lý/ảo vs vật lý/thực/tuyệt đối, 3 thời điểm address binding, Dynamic loading vs Dynamic linking, Fixed vs Dynamic partitioning, phân mảnh nội/ngoại, Compaction, First-fit/Next-fit/Best-fit/Worst-fit (chú ý quy ước con trỏ trong đề), Paging (frame/page, PTBR/PTLR, chuyển đổi địa chỉ xuôi/ngược, tính số bit & kích thước bảng trang, phân mảnh nội), TLBs & công thức EAT.
- **Chương 8 (Bộ nhớ ảo):** Điều kiện cần & lợi ích bộ nhớ ảo, Demand paging, 3 bước PFSR, thay trang FIFO (Belady's anomaly), OPT, LRU, cấp phát frame tĩnh vs động, Thrashing, Locality, Working-set.
- **Chương 9 (Linux & Windows):** Xuất hiện 1–2 câu/đề từ 2023–2024 trở đi: số vùng bộ nhớ vật lý Linux, số loại kernel module Linux, công cụ IPC truyền dữ liệu trên Linux (`Pipe`/`Network`/`Shared memory` vs `Signal`), `Hyper-V Hypervisor` và `Registry` trên Windows.

Lưu ý: Đây là kết quả kiểm 6 đề cũ để định hướng ôn tập, không phải khẳng định giới hạn thi chính thức của học kỳ hiện tại.
