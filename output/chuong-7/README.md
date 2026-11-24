# Chương 7 — Quản lý bộ nhớ

Nguồn: **W09** (`#Week09-Chapter7 2024.pdf`, 72 trang) trong `Lý thuyết/`. Số trang dưới đây tính theo trang PDF từ 1. Đã kiểm tra trực tiếp hình vẽ ở trang 7–8 (base/limit, layout vùng nhớ), 30 (phân vùng), 45–46 (chuyển đổi địa chỉ paging), 57–58 (phân trang 2 cấp & bảng trang nghịch đảo), 62 (chia sẻ trang).

Mỗi bài gồm định nghĩa ngắn tiếng Việt kèm thuật ngữ tiếng Anh, công thức tính toán, dấu hiệu nhận diện, điểm dễ nhầm và nguồn trang PDF. Đây là bản ôn đã soạn, không phải đáp án chính thức hay bằng chứng đã học/thành thạo.

## Mục lục bài ôn

| Mục trong slide | Bản ôn | Nguồn |
|---|---|---|
| 7.1–7.3 | [Khái niệm cơ sở, kiểu địa chỉ và chuyển đổi địa chỉ (Linking & Loading)](7.1-khai-niem-dia-chi-va-chuyen-doi.md) | W09 trang 5–27 |
| 7.4, 7.6 | [Phân vùng cố định/động, phân mảnh, chiến lược placement và Swapping](7.2-phan-vung-phan-manh-va-swapping.md) | W09 trang 28–39, 63–65 |
| 7.5 | [Cơ chế phân trang (Paging), bảng trang, TLBs và EAT](7.3-co-che-phan-trang-va-tlb.md) | W09 trang 40–62 |

## Ghi chú nguồn và trọng tâm đề cuối kỳ cũ

- Chương 7 xuất hiện dày đặc trong **tất cả 6 đề cuối kỳ (2020–2025)** ở cả trắc nghiệm lẫn tự luận.
- Trọng tâm lý thuyết và tính toán hay ra thi: phân biệt các kiểu địa chỉ, 3 thời điểm chuyển đổi địa chỉ, **so sánh `dynamic linking` vs `dynamic loading`** (tự luận 1đ), phân mảnh nội/ngoại và vai trò **`compaction`**, cấp phát theo **First-fit / Next-fit / Best-fit / Worst-fit** (cẩn thận bẫy vị trí con trỏ), chuyển đổi địa chỉ xuôi/ngược trong **Paging**, tính số bit ($p, f, d$) và kích thước bảng phân trang, vai trò **PTBR / PTLR**, vai trò **TLBs** và công thức **EAT**.
- Ghi chú lỗi nhỏ ở hình `W09 trang 62` (chia sẻ trang): trong cột Process 3 in lặp nhãn `ed 2` hai lần thay vì `ed 3` ở trang 2; ý nghĩa đúng vẫn là 3 tiến trình dùng chung 3 trang mã `ed 1, ed 2, ed 3` tại khung `3, 4, 6`.
