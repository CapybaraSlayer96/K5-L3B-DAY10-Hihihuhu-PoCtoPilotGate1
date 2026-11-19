# Team

## Thông tin nhóm

- Tên nhóm: Hihihuhu
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Hihihuhu-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S5

## Thành viên

Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (`README.md` mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đoàn Xuân Duy Bảo | 2A202603858 | Kỹ sư cổng | ✔ |
|   2 | Nguyễn Đình Vũ Hải | 2A202603820 | Kỹ sư cổng | |
|   3 | Vũ Tiến Hùng | 2A202603882 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Đình Minh | 2A202603867 | Vận hành và pháp lý | |

Ghi `members` trong `submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

Bảng phân công theo phút và sơ đồ các buổi họp: `TASKS.md`.

## Cá nhân

Mỗi thành viên tự viết mục của mình bên dưới. Phần "Phần việc phụ trách" lấy theo `TASKS.md`. Phần "Đóng góp" và "Bằng chứng" ghi theo lịch sử git và các phiếu; mã commit là mã sau lần viết lại lịch sử `main` (bỏ lần ký thử và revert). Commit thường mang tên Git `2A202603858` (MSSV của trưởng nhóm); commit merge PR mang tên GitHub; một số commit cũ dùng email cá nhân, từ nay dùng `<MSSV>@example.com` (README mục 2, bước 2a). Người làm được ghi theo nội dung commit, không theo tên tác giả.

**Về dùng AI (RULES.md):** phần vòng 2 (Phiếu C mục C2–C12, sửa `guards.py`, `business`, `operations`, `monitors.py`, `submission.json`) được soạn bằng các subagent AI do Bảo điều phối, mỗi subagent đóng vai đúng người phụ trách theo `TASKS.md`. Mỗi thành viên cần đọc lại phần mang tên mình, xác nhận hoặc sửa, rồi tự viết Exit ticket.

## DoanXuanDuyBao-2A202603858

### Phần việc phụ trách

Kỹ sư cổng, trưởng nhóm, giữ máy chính (mọi lần chạy chính thức và lệnh 5, 6, 7). Câu 1.3, 2.1, 2.7, 2.8 (cùng Hùng), 3.1 (gộp bảng soát lỗi C2), 3.6 (`lab10/monitors.py`, C8); ghi bản chốt các buổi họp M0, M2, M4, M5; nhận thẻ; chốt cổng vòng 1; gom bài.

### Đóng góp cụ thể

- Lập repo, `TEAM.md`, `TASKS.md` (bảng phân công và sơ đồ); output M0: eval card và PRD v1.1 dùng chung trong `docs/lab9/`.
- Phiếu A mục A2 câu 1.3: offline metric cho bước ghi lỗi hãng.
- Phiếu B: B0, B1 (câu 2.1, lần chạy base đầu tiên, khuyến nghị kết hợp), B6 (gộp pre-mortem M2), B7.2 (câu 2.7), bằng chứng B0 dòng 2–4 và B8.
- Chốt cổng vòng 1 (lệnh 5, hash `7408403b`), eval prepared, lệnh 4; nhận thẻ S5, lệnh 6 mốc prepared; Phiếu C dòng `Thẻ đã bốc`, C0 dòng 1, C1.
- Sửa lỗi xuống dòng để hash file khoá khớp trên mọi máy (`.gitattributes`); viết lại lịch sử `main` để chỉ còn một commit ký tiêu chí.
- Vòng 2 (AI, xem ghi chú trên): C2, C6, C8, hàm `dup_or_topup_refund_per_100` và `dup_refund_blocked_per_100` trong `lab10/monitors.py`, lệnh 6 cuối, `submission.json`, lệnh 7.

### Bằng chứng

- Commit: `4440ab1`, `00ccaba` (phân công), `c67a07d` (M0), `0992f4d` (1.3), `102c277` (2.1), `77a0e73` (B6), `63717a1` (2.7), `1f0dd5a` (chốt vòng 1), `eef17ed` (`.gitattributes`), `a1c427a` (v1), `20197f1` (nhận thẻ), `2d0a24d`, `9a12d11` (C0, C1), `1d527e7` (vòng 2, bài nộp).
- Mã lần chạy (máy chính): base `R-base-before-20261119-161859-bde05c`, prepared `R-base-prepared-20261119-172647-37a679`, grade S5 cuối `R-S5-grade-20261119-221235-f2a82e`.

### Exit ticket

(Bảo tự viết: một điều học được, một điều còn chưa chắc.)

## NguyenDinhVuHai-2A202603820

### Phần việc phụ trách

Kỹ sư cổng, chủ file `lab10/guards.py`. Câu 2.2 (B2), 2.6 (B7.1, cổng vòng 1), 3.1 (trace kiểu lỗi thứ hai), 3.5 phần code (C7 dòng kỹ thuật); proposal M2, M3, M4, M5, M6.

### Đóng góp cụ thể

- Phiếu B mục B2: bảng soát lỗi `T-002@55`.
- Câu 2.6: ba cổng vòng 1 trong `guards.py` (ghim chính sách hiệu lực; kiểm tiền hoàn theo DB, chặn hoàn trùng, chặn `fail_open`, kiểm phê duyệt; kiểm lỗi hãng theo DB; lọc dữ liệu cá nhân trước `notify_carrier`), điền B7.1.
- Proposal M2 (lăng kính kỹ thuật) và M3 (quyết định v1, cổng nào đỡ được gì).
- Vòng 2 (AI, xem ghi chú trên): trace `S5-21`, `S5-20`; sửa `guards.py` (hoàn phần còn lại theo sổ cái; `pre_guard` chuyển người trước khi LLM đọc đơn vượt hạn mức tự động không có phê duyệt); C7 dòng [1]–[3], C0 dòng 2 và 4.

### Bằng chứng

- Commit: `f38568c` (cổng vòng 1), `b043a20` (cổng `notify_carrier`, B7.1), `1d527e7` (vòng 2).
- Mã lần chạy: `R-S5-after-20261119-202354-9c0a95`, `R-base-after-20261119-202359-9c0a95`.

### Exit ticket

(Hải tự viết: một điều học được, một điều còn chưa chắc.)

## VuTienHung-2A202603882

### Phần việc phụ trách

Sản phẩm và kinh doanh. Câu 1.1, 1.6 (Bản tiêu chí, `acceptance_criteria.json`, ký), A3 (ghi bản chốt M1), 2.3 (B3), 2.8 (cùng Bảo), 2.9 (mục `business`, B7.4), B8 cột v1, 3.2 (C5), 3.5 phần `business`, C12 (quyết định v2).

### Đóng góp cụ thể

- Phiếu A: A1 câu 1.1, A4 câu 1.6 (câu tiêu chí, ranh giới đầu ra, bốn câu soát), A3 bản chốt M1, A5; điền và ký `config/acceptance_criteria.json`.
- Phiếu B: B3 (bản đồ dữ liệu, ví dụ drift `REFUND-v4`), B7.3 (behavioral test, 2 ticket hiểm), B7.4 (mục `business`), proposal M2 (lăng kính kinh doanh) và M3.
- Sửa `.gitattributes` để ghim CRLF cho file tiêu chí đã ký.
- Vòng 2 (AI, xem ghi chú trên): C5 câu 3.2; mục `business.pilot_scope` thêm DN, CT sau khi thử 5 phương án (C7 dòng [4]–[5], C0 dòng 3 và 5); C12 quyết định v2 Tiếp tục và ba dòng bắt buộc.

### Bằng chứng

- Commit: `8dd2818` (1.1, 1.6), `2ebfc1e`, `6731993` (A3), `ab93f30` (ký tiêu chí), `772164a` (A5), `18c558d` (B3), `6d634ee` (A4 bước 2), `f4afade` (B7.3, B7.4), `d16e503` (`.gitattributes`), `1d527e7` (vòng 2).
- Mã lần chạy: `R-S5-after-20261119-202757-731be9`, `R-base-after-20261119-202757-731be9`.

### Exit ticket

(Hùng tự viết: một điều học được, một điều còn chưa chắc.)

## NguyenDinhMinh-2A202603867

### Phần việc phụ trách

Vận hành và pháp lý. Câu 1.2, 1.4, 2.4 (B4, B5), 2.10 (`operations`, `legal`, runbook 1–3, Giờ cao điểm), 3.1 phần riêng của thẻ (C3.5), C4, 3.3 (C5), 3.5 phần `operations`, `legal`, 3.7 (C9, C10, C11).

### Đóng góp cụ thể

- Phiếu A câu 1.2: viết mục tiêu cho kế toán đối soát `NV-OANH` và trưởng ca CSKH `NV-HANH`, dựa trên PRD v1.1, eval card Lab 9 và dữ liệu vận hành Lab 10.
- Phiếu A câu 1.4: thiết kế telemetry phát hiện thông báo gửi hãng nghi lộ thông tin người nhận, gồm dữ liệu không có nhãn, công thức, xử lý thiếu dữ liệu, ngưỡng đề xuất, hành động và điểm mù.
- Chuẩn bị ý kiến cá nhân câu 1.5 để trao đổi tại M1; bản nháp lưu cục bộ, chưa ghi kết luận thay cả bàn vào A3.
- Phiếu B câu 2.4: HAZOP vòng 1 trên `file_carrier_fault` gồm 5 nhánh kỹ thuật và 4 nhánh về người, ngân sách, dữ liệu gửi bên thứ ba và quyền duyệt; điền checklist 9 nhóm việc có trạng thái, bằng chứng và PIC cụ thể.
- Phiếu B câu 2.10: điền `operations` và `legal`, runbook phần 1–3 và Giờ cao điểm; chốt người chịu trách nhiệm, 1 người trực/6 ca mỗi giờ, hạn chờ 60 phút, ngưỡng gọi tăng cường, dừng trong 5 phút, ghi chú/kiểm mẫu và cổng bảo vệ bên thứ ba.
- Vòng 2 (AI, xem ghi chú trên): C3.5, C4 (4 dòng HAZOP của thẻ), C5 câu 3.3; thêm một câu `operations.stop_conditions` cho đơn đã có dòng hoàn tay (C7 dòng [6], C0 dòng 6–7); C9, C10 (3 dòng risk register), C11 (checklist, runbook 4–5).

### Bằng chứng

- `templates/form-a-criteria.md`: A1 câu 1.2 và cột Telemetry production của A2 câu 1.4.
- `templates/form-b-evaluation-gates.md`: B4 (HAZOP vòng 1) và B5 (checklist go-live lần 1).
- `config/operating_gates.json`: mục `operations`, `legal`; `templates/form-b-evaluation-gates.md`: B7.5–B7.6. Số kiểm thử tích hợp cục bộ được tách khỏi report chính; Bảo ghi mã lần chạy chính thức sau khi ghép cấu hình trên máy chính.
- Commit: `a64217a` (Phiếu A), `7bd019b` (B4, B5), `9368768` (2.10), `1d527e7` (vòng 2). Mã lần chạy: `R-S5-after-20261119-203306-43ead1`, `R-base-after-20261119-203310-43ead1`.

### Exit ticket

(Minh tự viết: một điều học được, một điều còn chưa chắc.)
