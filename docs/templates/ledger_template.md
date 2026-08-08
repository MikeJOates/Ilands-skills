# <Name> Ledger — Shelf D
Date: <YYYY-MM-DD> · Operator: <name> · Status: APPEND-ONLY
Purpose: The only admissible evidence. Changelog lines, rollback drill log, cumulative audit log. Never pruned — not by the weekly ritual, not by anything. The receipt outlives the week.

## Rules
- Append only. No entry is ever edited or deleted. Corrections = new entries.
- If unsure where evidence goes, it goes here.
- Live rollback paths may point at entries here; they resolve forever.

---

## Changelog

### CHG-001 · <date> · <first change>
- What changed: ...
- Prior state pointer: <lockfile entry / archive ID / file+version>
- Rollback: ...
- Why: ...
- Status: ACTIVE

---

## Rollback drill log

### DRILL-001 · <date> · target ARCH-<N> (<change name>) · PASS/FAIL
1. Confirmed prior state loads from <lockfile/archive>.
2. Reversed for real: ...
3. Re-applied from archive text.
4. Result: PASS / FAIL.
Rule live: No PASS on last drill → no new applies until it passes.

---

## Cumulative audit log

### AUDIT-001 · <date> · CLEAR / RECLASSIFIED
Operational applies counted: <N> (<list>).
Question: taken together, do these constitute a core change?
Answer: NO/YES — <one line why>.
Result: CLEAR / RECLASSIFIED (→ CHG-00X). Counter reset (in lockfile).
Next trigger: <N> new operational applies OR <date+1 month>, whichever first.
