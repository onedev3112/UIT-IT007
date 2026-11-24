# Chương 8 — Bộ nhớ ảo (Virtual Memory)

Nguồn: **W10** (`#Week10-Chapter8 2024.pdf`, 50 trang) trong `Lý thuyết/`. Số trang dưới đây tính theo trang PDF từ 1. Đã kiểm tra trực tiếp hình vẽ ở trang 14 (6 bước xử lý lỗi trang), 33 (so sánh LRU và FIFO), và 37 (công thức cấp phát tĩnh theo tỉ lệ).

Mỗi bài gồm định nghĩa ngắn tiếng Việt kèm thuật ngữ tiếng Anh, công thức, dấu hiệu nhận diện, điểm dễ nhầm và nguồn trang PDF. Đây là bản ôn đã soạn, không phải đáp án chính thức hay bằng chứng đã học/thành thạo.

## Mục lục bài ôn

| Mục trong slide | Bản ôn | Nguồn |
|---|---|---|
| 8.1–8.2 | [Tổng quan bộ nhớ ảo, Demand Paging và xử lý lỗi trang (PFSR)](8.1-tong-quan-va-demand-paging.md) | W10 trang 5–20 |
| 8.3 | [Các giải thuật thay trang (FIFO, Nghịch lý Belady, OPT, LRU)](8.2-cac-giai-thuat-thay-trang.md) | W10 trang 21–33 |
| 8.4–8.5 | [Cấp phát Frames, Thrashing, Locality và giải pháp tập làm việc (Working-Set)](8.3-cap-phat-frames-va-thrashing.md) | W10 trang 34–47 |

## Ghi chú nguồn và trọng tâm đề cuối kỳ cũ

- Chương 8 là một trong những chương có **tỉ trọng điểm cao nhất** trong 6 đề cuối kỳ (2020–2025): xuất hiện cả ở trắc nghiệm, Đúng/Sai, trả lời ngắn tiếng Anh (`virtual memory`, `thrashing`), và bài tự luận lớn 1.5đ vẽ bảng thay trang.
- Trọng tâm hay ra thi: định nghĩa & lợi ích bộ nhớ ảo, 2 điều kiện cần cài đặt, thứ tự 3 bước `PFSR`, chạy tay **FIFO / OPT / LRU** (tìm *victim page* tại lần truy cập đầu tiên của một trang và đếm *page faults*), **Nghịch lý Belady**, chiến lược cấp phát frame tĩnh vs động, **Thrashing**, **Locality**, và **Working-Set** ($D > m$).
- Trang `W10 trang 47` liệt kê 3 chủ đề "Đọc thêm" (Hệ thống tập tin, Hệ thống nhập xuất, Hệ thống phân tán) không có nội dung trong slide; không đưa vào phần tóm tắt cơ sở.
