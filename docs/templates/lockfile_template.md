# <Name> Operator Lockfile v1.0
Date: <YYYY-MM-DD> · Operator: <name> · Status: ACTIVE
Purpose: Shelf C. Immutable decisions + archive of prior states so rollback paths resolve to a real place, not a droppable string. Evidence logs (audit log, drill log) live on Shelf D — <ledger file>, append-only, never pruned.

## Autonomy mode
- Mode: SOLO or WITNESS (delete one)
- Solo: apply core with loud rollback + report. Witness: core waits in a dated queue; silence is not consent.
- Absence never changes autonomy mode.

## Cumulative audit cadence + counter
- Cadence: once per calendar month OR every N=<10> operational applies, whichever comes first.
- Last cumulative audit: n/a (start)
- Counter: 0 operational applies since this audit.
- Audit log lives on Shelf D. Rewrites of THIS file never reset the counter.

## Shelf D (ledger)
- File: <ledger file>. Append-only, lockfile-class, never pruned.
- Changelog lines, rollback drill log (PASS/FAIL), cumulative audit log live there.
- If unsure where evidence goes, it goes on Shelf D.

## Locked decisions
### <Decision 1> (v1.0)
- Decision: ...
- Rationale: ...
- Confidence: high / medium / low
- Open questions: ...
- If-then next move: When <trigger>, then <action>.
- Status: ACTIVE

### <Decision 2> (v1.0)
...

---

## Archive shelf (prior states for live rollback paths)
Format: ID · date applied · what changed · prior state text · reverse steps · status.
Prior states live here so spaced review can never drop the thing a path points at.

### ARCH-001 · <date> · <change name>
- Change: ...
- Prior state: ...
- Reverse: ...
- Status: ACTIVE (live)

---

## Version
- v1.0 (<date>): First version. Supersedes: nothing (new).
