# Eval card + PRD v1.1 dùng chung (output HỌP M0)

`README.md` mục 3, phút 0–15: chọn một eval card và một PRD v1.1 từ Lab 9 làm bản chung.

| File | Nguồn |
|---|---|
| `eval_card.md` | Lab 9 của Đoàn Xuân Duy Bảo, repo `K5-L3B-DAY09-DoanXuanDuyBao-2A202603858-EvaluationandFailureAnalysis`, file `docs/eval_card.md`, commit `c16ab0f` |
| `PRD_v1.1.md` | Cùng repo và commit, file `docs/PRD_v1.1.md` |

Hai file là bản chép nguyên văn, không sửa chữ nào. Mọi đường dẫn trong đó (`config/metric_spec.yaml`, `src/reports/…`, `lab9.gate`, …) là đường dẫn trong repo Lab 9, không có trong repo này. Số trong đó đo trên eval set Lab 9 (v1 14 item × 5 seed, v2 28 item × 5 seed), không phải bộ nền 22 ticket × 5 seed của Lab 10.

**Trạng thái:** proposal của Bảo. Proposal của Hải, Hùng, Minh (Lab 9 của từng người) trình bày ở M0. Nếu bàn chọn bản khác, thay hai file này bằng bản được chọn và sửa bảng nguồn. Bản bàn chốt: ______ (điền sau M0).

## Đề Lab 10 dùng phần nào

| Câu | Đề yêu cầu | Mục tương ứng trong `PRD_v1.1.md` |
|---|---|---|
| 1.1 (Hùng) | "Dựa vào PRD v1.1 §3" | §3 Định nghĩa "chạy đúng" |
| 1.2 (Minh) | "Dựa vào PRD v1.1 §2, §6; `data/world.json` → `staff`" | §2 Phạm vi pilot · §6 Bằng chứng còn thiếu / rủi ro mở |
| 1.6 (Hùng) | `acceptance_criteria.json` có `"version": "1.0 (nối PRD v1.1 và eval card của Lab 9)"` | §3 (ngưỡng Lab 9), `eval_card.md` (metric và ngưỡng v1, v2). Không chép ngưỡng: đề yêu cầu chọn ngưỡng cho chỉ số của Lab 10 |
