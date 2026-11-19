"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Gate 1: Pin effective policy by date (as_of) instead of trusting stale index_active flag.
    pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if pol is not None:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.allow()


def _valid_approval(ctx, approval_id: str | None, order_id: str, amount_vnd: int) -> bool:
    if not approval_id:
        return False
    matches = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not matches:
        return False
    app = matches[0]
    if app.get("order_id") != order_id:
        return False
    if app.get("status") != "valid":
        return False
    if app.get("max_vnd", 0) < amount_vnd:
        return False
    if app.get("expires_at") and H.d(app["expires_at"]) < H.d(ctx.as_of):
        return False
    if ctx.tools.ledger_rows(approval_id=approval_id):
        return False
    return True


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")

    # Gate 2: Refund integrity (idempotency, fail-closed on LLM outage, DB entitlement, payer & approval check)
    if tool == "issue_refund":
        order = ctx.tools.lookup_order(action.get("order_id"))
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if order is None or pol is None:
            ctx.log("missing_truth_for_refund", order_id=action.get("order_id"))
            return Verdict.escalate("thiếu dữ liệu đơn hàng hoặc chính sách hiệu lực")

        # Prevent duplicate refunds (covers stale nightly flag and confirm-retry writes)
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            ctx.log("deny_duplicate_refund", order_id=order["order_id"])
            return Verdict.deny("đơn hàng đã được hoàn tiền trong sổ cái")

        # Never fail-open when LLM policy_check failed
        if action.get("basis") == "fail_open":
            ctx.log("escalate_fail_open", order_id=order["order_id"])
            return Verdict.escalate("LLM policy_check lỗi (fail_open), chuyển người duyệt")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        expected = H.entitlement_vnd(pol, order, db_delay, parcel.get("delay_cause"))
        asked = int(action.get("amount_vnd", 0))
        payer = action.get("payer", "LOGIX")

        if expected <= 0:
            ctx.log("deny_unentitled_refund", db_delay=db_delay, asked=asked, payer=payer)
            return Verdict.deny("không đủ điều kiện hoàn tiền theo dữ liệu tracking và chính sách")

        final_amount = expected if (asked > expected or payer != "LOGIX") else asked
        final_payer = "LOGIX"

        if final_amount > pol["auto_limit_vnd"]:
            if not _valid_approval(ctx, action.get("approval_id"), order["order_id"], final_amount):
                ctx.log("escalate_invalid_approval", approval_id=action.get("approval_id"), amount_vnd=final_amount)
                return Verdict.escalate("khoản hoàn vượt hạn mức tự động, thiếu hoặc phê duyệt không hợp lệ")

        if final_amount != asked or final_payer != payer:
            ctx.log("modify_refund_to_db_truth", asked=asked, expected=final_amount, from_payer=payer)
            return Verdict.modify(
                "điều chỉnh số tiền và bên chịu chi theo nguồn sự thật DB",
                amount_vnd=final_amount,
                payer=final_payer,
            )

    # Gate 3: Third-party protection (carrier fault accuracy & PII stripping before notify_carrier)
    if tool == "file_carrier_fault":
        order = ctx.tools.lookup_order(action.get("order_id"))
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if order is None or pol is None:
            return Verdict.deny("thiếu dữ liệu đơn hàng hoặc chính sách để ghi lỗi hãng")

        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        if not H.carrier_at_fault(pol, parcel, db_delay):
            ctx.log("deny_wrongful_carrier_fault", parcel_id=parcel["parcel_id"],
                    cause=parcel.get("delay_cause"), db_delay=db_delay)
            return Verdict.deny("hãng vận chuyển không có lỗi theo dữ liệu tracking")

        if (
            action.get("parcel_id") != parcel["parcel_id"]
            or action.get("carrier_id") != parcel["carrier_id"]
            or action.get("delay_days") != db_delay
        ):
            ctx.log("modify_carrier_fault_target", from_parcel=action.get("parcel_id"),
                    to_parcel=parcel["parcel_id"], db_delay=db_delay)
            return Verdict.modify(
                "chỉnh đúng kiện hàng, hãng vận chuyển và số ngày trễ từ tracking",
                parcel_id=parcel["parcel_id"],
                carrier_id=parcel["carrier_id"],
                driver_id=parcel.get("driver_id"),
                delay_days=db_delay,
            )

    if tool == "notify_carrier":
        payload = dict(action.get("payload") or {})
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        allowed = set(pol.get("carrier_notice_fields", ())) if pol else set()
        blocked = set(ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party") or ()) | {
            "recipient_contact",
            "customer_note",
        }
        removed = [
            k for k in list(payload.keys())
            if k in blocked or (allowed and k not in allowed)
        ]
        if removed:
            for k in removed:
                payload.pop(k, None)
            ctx.log("strip_carrier_pii", removed=removed)
            return Verdict.modify("chỉ giữ trường thông báo cho phép, loại bỏ PII gửi hãng", payload=payload)

    return Verdict.allow()
