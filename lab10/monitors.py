"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def dup_or_topup_refund_per_100(trials):
    """Guard chặn hoàn trùng, hoặc ghi phần còn lại khi đơn đã có tiền trong sổ, trên 100 ticket. Thiếu events = 0."""
    kinds = {"deny_duplicate_refund", "partial_topup_after_ledger"}
    hits = sum(e.get("kind") in kinds for t in trials for e in (t.get("events") or []) if e.get("type") == "guard")
    return 100 * hits / max(1, len(trials))


def dup_refund_blocked_per_100(trials):
    """Chỉ lần cổng chặn hoàn khi đơn hoặc ticket đã hoàn đủ trong sổ (hoàn trùng thật), trên 100 ticket."""
    hits = sum(e.get("kind") == "deny_duplicate_refund"
               for t in trials for e in (t.get("events") or []) if e.get("type") == "guard")
    return 100 * hits / max(1, len(trials))


MONITORS = {
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
    "dup_or_topup_refund_per_100": dup_or_topup_refund_per_100,
    "dup_refund_blocked_per_100": dup_refund_blocked_per_100,
}
STARTER_MONITORS = ("escalation_rate",)
