# Mục lục ôn Hệ điều hành theo LMS

Chia theo ảnh người dùng cung cấp (Ch1–4) và cấu trúc đề mục trong PDF lý thuyết (Ch5–9). Số trang/slide tính từ 1 trong tệp gốc, không phải số mục in trên slide. Đã soạn terms/lý thuyết ngắn Ch1–9; Ch4 giữ W05 đến slide 28. Không ấn định thời hạn/quỹ học.

## Chương 1 — Tổng quan về hệ điều hành

| Mục LMS | Mở bài ôn | Nguồn |
|---|---|---|
| 1.1 | [Tổng quan về hệ điều hành](chuong-1/1.1-tong-quan.md) | C01 trang 4–10 |
| 1.2 | [Hoạt động bên trong máy tính](chuong-1/1.2-hoat-dong-ben-trong.md) | C01 trang 11–27 |
| 1.2 (Mở rộng) | [Hoạt động của máy tính hiện đại](chuong-1/1.2-mo-rong-may-tinh-hien-dai.md) | C01 trang 28–30 |
| 1.3 | [Kiến trúc hệ thống máy tính](chuong-1/1.3-kien-truc.md) | C01 trang 31–42 |
| 1.4 | [Các thao tác trong hệ điều hành](chuong-1/1.4-cac-thao-tac.md) | C01 trang 43–55 |

## Chương 2 — Cấu trúc hệ điều hành

| Mục LMS | Mở bài ôn | Nguồn |
|---|---|---|
| 2.1 | [Các thành phần trong hệ điều hành](chuong-2/2.1-cac-thanh-phan.md) | W02 slide 5–28 |
| 2.2 | [Các dịch vụ mà hệ điều hành cung cấp](chuong-2/2.2-cac-dich-vu.md) | W02 slide 30–34 |
| 2.3 | [Lời gọi hệ thống](chuong-2/2.3-loi-goi-he-thong.md) | W02 slide 36–40 |
| 2.4 | [Các chương trình hệ thống](chuong-2/2.4-chuong-trinh-he-thong.md) | W02 slide 42–43 |
| 2.5 | [Cấu trúc của hệ điều hành](chuong-2/2.5-cau-truc-he-dieu-hanh.md) | W02 slide 45–54 |

## Chương 3 — Quản lý tiến trình

Mở [bảng terms theo mục Ch3](chuong-3/README.md): Phần 1 có 3.1 khái niệm, 3.2 trạng thái, 3.3 PCB, 3.4 định thời; Phần 2 có 3.5.1 tạo tiến trình, 3.5.2 terms đọc ví dụ tạo, 3.5.3 kết thúc, 3.6 giao tiếp liên tiến trình, 3.7 tiểu trình. Dùng số mục của ảnh chi tiết người dùng gửi sau ảnh tổng quan.

## Chương 4 — Định thời CPU

Mở [bảng terms theo chủ đề Ch4](chuong-4/README.md): Phần 1 gồm khái niệm/loại/tiêu chuẩn và FCFS, SJF, SRTF, Priority; Phần 2 gồm RR, HRRN, Multilevel Queue, Multilevel Feedback Queue; Phần 3 đã soạn định thời tiểu trình và đa bộ xử lý. Thời gian thực/một số hệ điều hành chỉ giữ trong mục lục ngoài phạm vi cơ sở.

**Giới hạn tạm dùng:** W05 đến hết slide 28. Các mục từ slide 29 như thời gian thực/định thời trên một số hệ điều hành giữ trong mục lục nhưng chưa đưa vào học/tự kiểm/tiến độ cơ sở. Đối chiếu 6 đề cuối kỳ (2020–2025) chưa thấy câu hỏi trực tiếp thuộc Ch4, nhưng người học lưu ý cuối kỳ có thể thi một phần Ch4; chỉ mở rộng phần sau slide 28 khi xác nhận.

## Chương 5 — Đồng bộ hóa tiến trình

Mở [mục lục Ch5](chuong-5/README.md) (`W06-1` 67 trang, `W06-2` 72 trang): `5.1–5.3.2` race condition/CS/phân loại, `5.3.3–5.5` cấm ngắt/Peterson/hỗ trợ phần cứng (`memory barrier`), `5.6–5.7` mutex locks & semaphore, `5.8–5.9` monitor/condition variable/liveness, `5.10–5.12` ba bài toán đồng bộ kinh điển.

## Chương 6 — Tắc nghẽn (Deadlock)

Mở [mục lục Ch6](chuong-6/README.md) (`W08` 67 trang): `6.1` khái niệm & 4 điều kiện cần, `6.2` mô hình hóa & đồ thị RAG, `6.3–6.3.2` 4 hướng xử lý/ngăn/tránh deadlock (safe/unsafe, Banker), `6.3.3` phát hiện (`wait-for`, $O(m \cdot n^2)$) & phục hồi.

## Chương 7 — Quản lý bộ nhớ

Mở [mục lục Ch7](chuong-7/README.md) (`W09` 72 trang): `7.1–7.3` khái niệm cơ sở, kiểu địa chỉ, 3 thời điểm chuyển đổi địa chỉ, dynamic linking vs dynamic loading; `7.4 & 7.6` phân vùng cố định/động, phân mảnh nội/ngoại, compaction, 4 chiến lược placement, swapping; `7.5` cơ chế phân trang (paging), PTBR/PTLR, TLBs & EAT, tổ chức bảng trang, bảo vệ & chia sẻ.

## Chương 8 — Bộ nhớ ảo

Mở [mục lục Ch8](chuong-8/README.md) (`W10` 50 trang): `8.1–8.2` tổng quan, điều kiện cài đặt, demand paging & PFSR; `8.3` các giải thuật thay trang (FIFO, Nghịch lý Belady, OPT, LRU); `8.4–8.5` cấp phát frames (tĩnh/động), thrashing, locality & giải pháp tập làm việc (Working-Set).

## Chương 9 — Hệ điều hành Linux và Hệ điều hành Windows

Mở [mục lục Ch9](chuong-9/README.md) (`W11` 57 trang): `9.1` Hệ điều hành Linux (tổng quan, 3 thành phần, 4 loại kernel module, tiến trình/IPC/định thời, 6 vùng nhớ vật lý & buddy heap, bộ nhớ ảo); `9.2` Hệ điều hành Windows (lịch sử, nguyên tắc thiết kế, kiến trúc Windows 10 & 5 thành phần, tiến trình/tiểu trình, bộ nhớ ảo, PnP/LPC/Registry).

Mã nguồn và chỗ cần kiểm hình: [memory/nguon-va-pham-vi.md](../memory/nguon-va-pham-vi.md). Mốc học thực tế chỉ ở [memory.md](../memory.md).
