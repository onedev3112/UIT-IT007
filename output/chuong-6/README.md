# Chương 6 — Tắc nghẽn (Deadlock)

Nguồn: **W08** (`#Week08-Chapter6 2024.pdf`, 67 trang) trong `Lý thuyết/`. Số trang dưới đây tính theo trang PDF từ 1. Đã kiểm tra trực tiếp hình vẽ sơ đồ ở trang 39 (RAG avoidance) và trang 53 (RAG → wait-for graph).

Mỗi bài gồm định nghĩa ngắn tiếng Việt kèm thuật ngữ tiếng Anh, dấu hiệu nhận diện, giải thuật/công thức, điểm dễ nhầm và nguồn trang PDF. Đây là bản ôn đã soạn, không phải đáp án chính thức hay bằng chứng đã học/thành thạo.

## Mục lục bài ôn

| Mục trong slide | Bản ôn | Nguồn |
|---|---|---|
| 6.1 | [Vấn đề deadlock, định nghĩa và 4 điều kiện cần](6.1-khai-niem-va-dieu-kien-deadlock.md) | W08 trang 4–12 |
| 6.2 | [Mô hình hóa hệ thống và đồ thị cấp phát tài nguyên (RAG)](6.2-mo-hinh-hoa-va-do-thi-rag.md) | W08 trang 13–24 |
| 6.3–6.3.2 | [Bốn hướng xử lý, ngăn deadlock và tránh deadlock (Banker)](6.3-ngan-va-tranh-deadlock.md) | W08 trang 25–49 |
| 6.3.3 | [Phát hiện deadlock (Wait-for, $O(m \cdot n^2)$) và phục hồi](6.4-phat-hien-va-phuc-hoi-deadlock.md) | W08 trang 50–62 |

## Ghi chú nguồn và trọng tâm đề cuối kỳ cũ

- Chương 6 xuất hiện trong **tất cả 6 đề cuối kỳ (2020–2025)** ở cả trắc nghiệm lẫn tự luận.
- Các dạng câu hỏi lặp lại nhiều nhất: 4 điều kiện cần, quy tắc chu trình của RAG (1 thực thể vs nhiều thực thể), phân biệt Ngăn vs Tránh deadlock, quan hệ trạng thái `safe`/`unsafe` với deadlock, chạy tay **Giải thuật Banker** (kiểm tra chuỗi an toàn và xét yêu cầu `Request_i`), đồ thị `wait-for` ($O(n^2)$), giải thuật phát hiện nhiều thực thể ($O(m \cdot n^2)$), và cách phục hồi deadlock.
- Ghi chú lỗi in nhỏ ở slide gốc: `W08 trang 47` dòng chữ ghi `Need 1 = (1, 1, 2)` trong khi bảng ngay bên dưới ghi `P1 Need = (1, 2, 2)`; `W08 trang 61–62` ghi nhầm "Lấy tại tài nguyên" và nhãn chân trang 62 ghi nhầm "Chấm dứt tiến trình bị deadlock" trên slide nói về thu hồi/rollback. Bài ôn ghi đúng bản chất lý thuyết, không sao chép lỗi in.
