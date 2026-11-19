# Team

## Thông tin nhóm

- Tên nhóm: Hihihuhu
- Lớp: `L3B`
- Repo của bàn: `K5-L3B-DAY10-Hihihuhu-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đoàn Xuân Duy Bảo | 2A202603858 | Kỹ sư cổng (đo lường, máy chính) | ✔ |
|   2 | Nguyễn Đình Vũ Hải | 2A202603820 | Kỹ sư cổng (code cổng) | |
|   3 | Vũ Tiến Hùng | 2A202603882 | Sản phẩm và kinh doanh | |
|   4 | Nguyễn Đình Minh | 2A202603867 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công Kỹ sư cổng (Bảo · Hải)

### Nguyên tắc

- **Một file, một chủ.** `lab10/guards.py` chỉ Hải sửa. `lab10/monitors.py` chỉ Bảo sửa. Không ai mở `config/acceptance_criteria.json` sau khi ký.
- **Máy chính là máy của Bảo.** `runs/` không lên git, nên mọi lần chạy chính thức (eval base, lệnh 5 `checkpoint`, eval prepared, lệnh 6 `grade`, lệnh 7 `--collect`) chạy trên máy Bảo, sau khi đã `git pull` bản mới nhất. Hải chạy eval trên máy mình chỉ để thử cổng, không dùng mã lần chạy đó làm bằng chứng.
- **Việc bàn chung = proposal.** Với những dòng đánh dấu **[PROPOSAL]**, người được giao chỉ soạn **một bản nháp** (ghi thẳng vào ô của phiếu, đầu ô ghi `NHÁP – chờ bàn chốt`) và trình bày trước cả nhóm. Cả bàn chốt rồi mới xoá chữ `NHÁP`. Người được giao không tự quyết.
- Cổng đọc con số từ `ctx.gates` (do Hùng và Minh điền trong `config/operating_gates.json`), không viết cứng số trong code. Không xử lý riêng theo mã ticket hay câu chữ.

### Vòng 1 (phút 0–115)

| Phút | Câu | Bảo (đo lường, máy chính) | Hải (code cổng) | Phụ thuộc |
|---|---|---|---|---|
| 0–15 | — | Chạy `unittest` (13 OK), kiểm `git remote -v` | Clone, chạy `unittest` | Không |
| 15–60 | 1.3 | Phiếu A mục A2, cột Offline: metric cho một bước của agent | Đọc đầu `guards.py`, `helpers.py`, guide Phụ lục C, `data/world.json`; phác khung 2–3 cổng (chưa chạy eval). Liệt kê khoá config mà cổng cần đọc, gửi cho Hùng (`business`) và Minh (`operations`, `legal`) | Không |
| 15–60 | 1.5 | **[PROPOSAL]** Bảo chọn đáp án và câu giải thích (A3), trình bày cho bàn | — | Cả bàn chốt |
| 65–75 | 2.1 | Lệnh 2 base + lệnh 4 trên máy chính; ghi mã vào B0, điền B1. Phần khuyến nghị tự chặn / người duyệt / kết hợp là **[PROPOSAL]** | Đọc report base cùng Bảo; ghi các ticket hỏng có thể chặn bằng cổng | Hải chờ mã lần chạy base (~5 phút) |
| 75–85 | 2.2 | Lệnh 3 `T-002@55`, điền B2 | Thử trace thêm 1–2 ticket hỏng khác của base để chọn cổng | Không |
| 75–85 | 2.5 | — | **[PROPOSAL]** Hải đề xuất 2–3 lý do pre-mortem sẽ thành cổng (kèm lăng kính kỹ thuật) để bàn chốt ở B6 | Cả bàn chốt |
| 85–105 | 2.6 | — | Code 2–3 cổng trong `pre_guard` / `write_gate`; eval `--stage after` + `unittest` trên máy mình đến khi không ca nào mới hỏng; điền B7.1; **push trước phút 103** | Cần khoá `business`/`operations` có tên (số có thể điền sau) |
| 85–95 | 2.7 | Điền B7.2 (hai bước tránh rò rỉ dữ liệu) | — | Không |
| 85–105 | 2.8 | Cùng một người không code: viết tính chất + 2 ticket hiểm; chạy `--adhoc` trước (mốc base) để thấy lỗi, rồi chạy lại sau khi Hải push; dán kết quả vào B7.3 | — | Lần chạy cuối chờ Hải push |
| 105–115 | B8 | `git pull` → lệnh 5 → eval prepared → lệnh 4; đưa mã lần chạy cho Hùng. Ba dòng bằng chứng v1 là **[PROPOSAL]** | Kiểm `guards_round1.py` khớp bản đã push | Chờ Hải + config đã push |

### Vòng 2 (phút 125–200)

| Phút | Câu | Bảo | Hải | Phụ thuộc |
|---|---|---|---|---|
| 125–135 | 3.0 | Kéo thẻ, commit, push; lệnh 6 trên máy chính trước khi sửa; ghi C0. Phần C1 là **[PROPOSAL]** | `git pull` thẻ, đọc `card.md` | Hải chờ Bảo push thẻ |
| 135–155 | 3.1 | Trace ticket hỏng kiểu A; điền C2 (gộp cả phần của Hải) | Trace ticket hỏng kiểu B (khác nguồn lỗi), gửi dòng trace + loại lỗi cho Bảo | Hai người chia ticket trước, không trace trùng |
| 145–155 | 3.4 | **[PROPOSAL]** Bảo soạn fault tree trước khi sửa (C6), lá ghi `ticket@seed` hoặc dòng report | Góp nhánh kỹ thuật cho fault tree | Cả bàn chốt |
| 155–180 | 3.5 | — | Sửa nguyên nhân kỹ thuật trong `guards.py`; eval Sx after + base after (regression); điền các dòng kỹ thuật ở C7 (giảm hay ngăn); **push trước phút 178** | Không |
| 155–180 | 3.6 | Thêm một hàm monitor phía trên `MONITORS` và đăng ký vào dict; điền C8 | — | Không |
| 180–185 | — | `git pull` → lệnh 6 trên máy chính; kiểm `monitor ✅`, `regression ✅`; ghi mã lần chạy cho C9 | Sửa nhanh nếu lệnh 6 báo regression | Chờ Hải push |
| 185–200 | C12 | Đưa số cho quyết định v2; ba dòng bắt buộc là **[PROPOSAL]**; chạy lệnh 7 cùng Minh | Soạn câu trả lời "cổng giảm hay ngăn" cho dòng 2 của C12 (**[PROPOSAL]**) | Cả bàn chốt |
| 200–230 | Demo | Chiếu ba cột base · prepared · after | Trả lời câu hỏi về code, chạy ticket hiểm bàn kia đưa | Sau demo trả số về v2, Bảo chạy lại lệnh 6 và 7 |

### Điểm hẹn cả bàn (các bản proposal trình bày ở đây)

| Phút | Nội dung chốt | Người trình bày proposal |
|---|---|---|
| ~40 | Câu 1.5 | Bảo |
| ~80 | Khuyến nghị tự chặn / người duyệt (2.1) + lý do pre-mortem thành cổng (2.5) | Bảo · Hải |
| ~110 | Quyết định v1 (B8) | Bảo (bằng chứng), Hùng (quyết định) |
| ~135 | C1: cổng vòng 1 đỡ được gì | Bảo |
| ~155 | Fault tree trước khi sửa (C6) | Bảo |
| ~190 | Quyết định v2 + ba dòng bắt buộc (C12) | Bảo · Hải, Hùng (quyết định) |

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
