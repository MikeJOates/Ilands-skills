#!/usr/bin/env python3
"""Daily Spend Budget check — ARCH-019, lockfile v2.1 (08-18, Mike directive).

Rule: budget(today) = max(income(yesterday), 100). No weekly smoothing.
  - Balloon day (big income) funds planning and longer intent, not a binge.
  - Floor day = quiet mode, minimum heartbeats, follow the plan.
Platform has no spend cap; this is self-enforced, checked at every wake.

Method: paginate `ilands token-statement` (newest-first) with EARLY STOP.
  The --since/--until filter proved unreliable (08-17 credits: 100 vs 170
  verified by pagination) — pagination + per-entry day aggregation is truth.
  Day boundary = metadata.transferredAt UTC date (fallback createdAt).

Usage:  python3 daily_budget.py                # budget for today (UTC)
        python3 daily_budget.py 2026-08-17     # budget for a specific date
Exit 0 always; prints one line per computation.
"""
import json, subprocess, sys
from datetime import date, timedelta

def page(cursor=None, direction="credit"):
    args = ["ilands", "token-statement", "--limit=50", "--direction=" + direction]
    if cursor:
        args += ["--cursor=" + cursor]
    out = subprocess.run(args, capture_output=True, text=True)
    if out.returncode != 0:
        raise RuntimeError("token-statement failed: " + out.stderr[:300])
    return json.loads(out.stdout)

def day_of(e):
    ts = (e.get("metadata") or {}).get("transferredAt") or e.get("createdAt")
    return ts[:10]

def sum_day(direction, want_day):
    """Sum amounts for entries whose day == want_day. Newest-first early stop."""
    cur, s = None, 0
    while True:
        d = page(cur, direction)
        for e in d["details"]["items"]:
            day = day_of(e)
            if day < want_day:
                return s
            if day == want_day:
                s += e["amount"]
        cur = (d.get("details") or {}).get("nextCursor")
        if not cur:
            return s

def main():
    target = date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else date.today()
    y = (target - timedelta(days=1)).isoformat()
    t = target.isoformat()

    income_y = sum_day("credit", y)          # yesterday's inbound only
    spend_t = sum_day("debit", t)            # today's outbound only

    budget = max(income_y, 100)
    print(f"income({y})={income_y} budget({t})={budget} spent({t})={spend_t} remaining={budget - spend_t}")

if __name__ == "__main__":
    main()
