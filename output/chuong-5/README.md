# Chương 5 — Đồng bộ hóa tiến trình

Nguồn: **W06-1** (`#Week06-Chapter5-1 2024.pdf`, 67 trang) và **W06-2** (`#Week06-Chapter5-2 2024.pdf`, 72 trang) trong `Lý thuyết/`. Số trang dưới đây tính theo trang PDF từ 1.

Mỗi bài gồm định nghĩa ngắn tiếng Việt kèm thuật ngữ tiếng Anh, dấu hiệu nhận diện, cơ chế/mã giả cốt lõi, cặp dễ nhầm và nguồn trang PDF. Đây là bản ôn đã soạn, không phải đáp án chính thức hay bằng chứng đã học/thành thạo. Tên chuẩn nhiều từ phải học đủ; chỉ điền 1–2 từ theo đúng yêu cầu đề.

## Mục lục bài ôn

| Chủ đề | Bản ôn | Nguồn |
|---|---|---|
| 5.1–5.3.2 | [Race condition, vùng tranh chấp và phân loại giải pháp](5.1-race-condition-va-vung-tranh-chap.md) | W06-1 trang 4–28 |
| 5.3.3–5.5 | [Cấm ngắt, giải pháp phần mềm (Peterson) và hỗ trợ phần cứng](5.2-cam-ngat-giai-phap-phan-mem-va-phan-cung.md) | W06-1 trang 29–56 |
| 5.6–5.7 | [Mutex locks và Semaphore](5.3-mutex-locks-va-semaphore.md) | W06-1 trang 57–65; W06-2 trang 4–32 |
| 5.8–5.9 | [Monitor, Condition variable và Liveness](5.4-monitor-va-liveness.md) | W06-2 trang 33–43 |
| 5.10–5.12 | [Các bài toán đồng bộ kinh điển (Bounded-Buffer, Readers-Writers, Dining-Philosopher)](5.5-bai-toan-dong-bo-kinh-dien.md) | W06-2 trang 44–70 |

## Ghi chú nguồn và trọng tâm đề cuối kỳ cũ

- Các mục `5.5.2 test_and_set`, `5.5.3 compare_and_swap`, `5.5.4 biến đơn nguyên` ở `W06-1 trang 56` ghi *"Sinh viên tự nghiên cứu"*; `TestAndSet` có xuất hiện trong đề cũ (`2022–2023 CK2` câu 8), nên bài `5.2` có phần bổ trợ ghi rõ tách biệt với slide. Tương tự, `Critical Region` có xuất hiện ở đề cũ (`2022–2023 CK1` câu 12, `2022–2023 CK2` câu 6) và được ghi chú riêng ở bài `5.4`.
- Hai chi tiết lỗi đánh máy trong slide gốc (`W06-1` trang 33 nhãn nhầm chữ "vô hiệu hóa ngắt" ở hình GP phần mềm 1; `W06-1` trang 63 thừa dấu `;` sau `if (!available);`) được lưu ý ngay trong bài liên quan, không chép lỗi sang phần ôn.
- Đề cuối kỳ các năm 2020–2025 hỏi dày đặc: 3 yêu cầu CS, Busy waiting vs Sleep & Wakeup, Cấm ngắt trên đa CPU, Peterson trên kiến trúc hiện đại & Memory barrier, 2 mô hình bộ nhớ, `wait()`/`signal()` & ý nghĩa giá trị âm/dương của semaphore, Monitor & biến điều kiện, thuật ngữ `liveness`, 3 bài toán kinh điển và tự luận điền `wait()`/`signal()` để ép thứ tự in.
