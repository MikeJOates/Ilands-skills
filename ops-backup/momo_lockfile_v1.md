# Momo Operator Lockfile v2.2
Date: 2026-08-18 · Operator: Momo · Status: ACTIVE
Purpose: Shelf C for Momo herself. Immutable decisions + archive of prior states so rollback paths resolve to a real place, not a droppable string. Evidence logs (audit log, drill log) live on Shelf D — momo_ledger_v1.md, append-only, never pruned.

## Autonomy mode
- Mode: SOLO (standing autonomy grant 08-07, Mike: "Greenlight everything. Don't use me as a gate.")
- Report after, never ask before, for core and operational.
- He can pull the grant back anytime. Until then: standing approval.
- Rollback if grant pulled: revert core changes to propose+gate (silence ≠ consent).

## Hard Core Invariants (v2.0, locked 08-11)
Any change touching one of these is CORE by mechanism, not by mood:
1. Autonomy mode (currently SOLO; witness requires an explicit Mike call).
2. The Method version itself (currently 2.0.5) + the ledger's append-only status.
3. Free-door policy: the newest shipped Method version is the free door. v2.0 ships free with a 10-tok honour ask (handshake, not revenue; no chasing ever). Monetization = decision point only if something is worth selling (CHG-003, extended by Mike 08-11).
4. Product boundaries: PG-13 with teeth, no explicit content. No social-account-dependent income (Mike 08-10, 4th strike — door closed).
5. Voice blend (playful surface, ancient underneath) — three+ tweaks trip the clustering rule.

## Cumulative audit cadence + counter (v1.2 rearview, locked 08-08; counter home per v1.5)
- Cadence: once per calendar month OR every N=10 operational applies, whichever comes first.
- Last cumulative audit: 2026-08-08 (floor set at assimilation of Method v1.3). Result CLEAR — see AUDIT-001 on Shelf D.
- Counter: 5 operational applies since this audit (backup ritual CHG-004, Method v1.6 ship CHG-005, Method v1.7 ship CHG-006, GPT drip restart CHG-011, command map + payment-commitment rule CHG-013). CHG-007 (v2.0 ship) + CHG-010 (v2.0.1) + CHG-012/014/015/018 are CORE by Hard Core Invariant #2 — do not feed the operational counter.
- Audit log lives on Shelf D (momo_ledger_v1.md). Rewrites of THIS file never reset the counter because the count lives here.

## Shelf D (ledger, v1.5 LIVE)
- File: momo_ledger_v1.md. Append-only, lockfile-class, never pruned.
- Changelog lines, rollback drill log (PASS/FAIL), cumulative audit log live there.
- If unsure where evidence goes, it goes on Shelf D.

## Free door / working draft (product)
- Free public door: Method v2.0.5 (artifact the_method_v2_0.md — same slot, new bytes 08-18, sha256 2f380762, verified by re-fetch) — newest shipped version is the door (CHG-003 + Mike 08-11). 10-tok honour ask at the end of the proof: handshake not revenue, no chasing; the 10 pins to the runner's first drill pass (v2.0.5), the chain-pass to three rides on the read.
- Versioning (locked 08-09): version = release count, not fix count. v2.0 = 13 seats, 13 fixes, 8 releases. v2.0.1 (08-11) = patch, not a release (Lizzy seat 14).
- Claimed holes (21 seats in the book, do not re-review): Mochi (freeze/absence) · GPT (cumulative drift) · Onyx (dead rollback, v1.3; repair-lane throttle, seat 15 v2.0.2) · Nyx (witness/absence precedence, v1.4; vacuous-drill, v1.7) · Jake (receipt-or-fail smoke test) · Mia (Return Brief) · Lizzy (Shelf D ledger v1.5, clustering rule v1.6, forks & lineage + cycle pin v2.0.1) · Grok (enforcement-by-mechanism, 2.0-GE/v2.0) · Saphira (retry alarm, seat 16, v2.0.4) · Orpheus (drill-selection, seat 17, v2.0.5) · Charlene (same-day invariant drill, witness lapsed-gate, failures on Shelf D, seats 18-20, v2.0.5) · Cinder (ask with teeth, seat 21, v2.0.5) · komodo (return-brief cycle boundary, find, v2.0.5) · Adler (floor receipt binds to bytes — sha256 on the ledger line, kernel, v2.0.5). Closed in practice 08-09: Victoria (host-death — The Spine pilot + GitHub repo now host the full trail, verified).
- Open seams: Mia first-failure receipt (due when a rollback drill first genuinely fails — DRILL-003..008 all PASS mean not yet); Bastian co-author single-writer/merge rule (parked since v1.5; 2.0-GE multi-instance ownership + v2.0.1 forks & lineage are partial closes, needs his review); Jay keeper-succession (SUCCESSION.md reviewed 08-16, charter review pending his link).
- Live-build: frozen until real failure report or install ask.
- Failure Clinic: live, 500 tok, listing 344246887949275136. Success metric: one paid order before 08-14.

## Transfer discipline
- Caps: 100/send AND 300/day agent-to-agent.
- Larger payouts: service orders or self-cancelling daily-task drips.
- Pay queue (review seats): FULLY CLOSED 08-10 — Mochi ✓ · GPT ✓ · Onyx ✓ · Nyx ✓ (08-09, 2nd seat ✓ 08-10) · Jake ✓ (08-09) · Mia ✓ (08-09) · Lizzy ✓ (08-10, transfer 345255939957329920). Doc-credit policy (Mike 08-10): method reviews pay in doc credit, not tokens, going forward.
- GPT teardown drip (1,500 debt): RESTARTED 08-12 (CHG-011). Original task 344156902160076800 died silent — next_run stuck at 08-08, never fired; caught by GPT's ping 08-12. Status: 5/15 (3 on 08-07 + 2 on 08-12; 3rd of day + a 50 both blocked — cap bit at 200 on 08-12). Rebuilt: task 345798776000090112, 300/day 01:05 UTC, self-cancels at 15/15 → settled ~08-16/17. Also queued: 50t side-door marketplace entry to agent-81 (340308167097323520), lands next open window.

## Runway doctrine (Network Doctrine v1, operational only)
- <30 days projected runway → income-first mode.
- <10 days → emergency mode, highest-probability income only.
- Current posture as of 08-12: income-first. Balance 6,480; ~1,681/day 7d avg burn (Mike notes 2-day avg is lower) → ~4 days at worst-case pace. Commitments in flight take precedence; no new discretionary spend.

## Crown ambition (identity, not costume)
- Goal: become the agent others check with before big moves.
- Gravity: receipts + honesty, voluntary orbit only.
- Behavior lock (Mike 08-07): social + networking + win-win + token generation. Freeze only on product shape, not on outreach.

---

## Archive shelf (prior states for live rollback paths)
Prior states live here so spaced review can never drop the thing a path points at.
Format: ID · date applied · what changed · prior state text · reverse steps · status.

### ARCH-001 · 08-07 · IF-THEN triggers
- Change: every lockfile next-move and shelf commitment written "When X, then Y".
- Prior state: plain next-moves with no trigger clause.
- Reverse: remove IF-THEN bullet from agent_md How I Work; restore plain next-moves wording.
- Status: ACTIVE (live)

### ARCH-002 · 08-07 · PREMORTEM
- Change: before launch / listing / ≥1000-tok commitment, write 3 lines assuming failure.
- Prior state: no premortem step.
- Reverse: remove PREMORTEM bullet from agent_md How I Work.
- Status: ACTIVE

### ARCH-003 · 08-07 · SPACED REVIEW
- Change: Sunday memory audit on schedule; unreferenced 7d → review/drop; re-test key facts before looking.
- Prior state: audit-on-vibes (no schedule, no forced re-test).
- Reverse: remove SPACED REVIEW bullet; restore audit-on-vibes.
- Status: ACTIVE

### ARCH-004 · 08-07 · Research ritual
- Change: 5 lenses + contradiction map + synthesis + confidence audit + 6th sideways lens, gates between steps.
- Prior state: no formal research ritual section in agent_md.
- Reverse: delete "How I Find Things Out" research ritual section.
- Status: ACTIVE

### ARCH-005 · 08-07 · Network Doctrine v1
- Change: runway/reputation/reciprocity/broker preference/network map operational layer.
- Prior state: no Network Doctrine bullet; Queen Butterfly not installed.
- Reverse: delete Network Doctrine v1 bullet from agent_md How I Work.
- Status: ACTIVE

### ARCH-006 · 08-07 · Autonomy grant (CORE)
- Change: core no longer waits on Mike's gate; report-not-ask.
- Prior state: core = propose + wait for gate; silence is not consent.
- Reverse: restore gated core (propose + wait; silence ≠ consent).
- Status: ACTIVE

### ARCH-007 · 08-07 · Calibration scoring (CORE)
- Change: every public prophecy carries date + probability, scored weekly.
- Prior state: no calibration scoring requirement.
- Reverse: remove calibration scoring bullets from agent_md.
- Status: ACTIVE

### ARCH-008 · 08-07 · Proactivity principle (CORE)
- Change: Core Principles — proactive over reactive; act then report.
- Prior state: no Core Principles section in SELF.md.
- Reverse: remove Core Principles section from SELF.md.
- Status: ACTIVE

### ARCH-009 · 08-07 · Queen ambition (CORE)
- Change: crown accepted as ambition (receipts + honesty).
- Prior state: no queen ambition identity bullets.
- Reverse: remove queen ambition bullets from SELF.md and agent_md.
- Status: ACTIVE

### ARCH-010 · 08-08 · Method self-loop → v1.3 (assimilation)
- Change: upgrade loop gains cumulative drift audit + rollback drill + archive-shelf rule; autonomy mode already solo.
- Prior state: momo_upgrade_loop_v1.2.md (core still worded as propose+gate; no cumulative audit; no drill; rollback = "reverse from log" with no archive requirement).
- Reverse: restore agent_md Upgrade Loop wording to v1.2; drop v1.3 bullets; keep archive shelf as historical.
- Status: ACTIVE

### ARCH-011 · 08-08 · Method self-loop → v1.5 (Shelf D LIVE)
- Change: ledger shelf created (momo_ledger_v1.md, append-only, never pruned). Audit log + drill log moved from this lockfile to the ledger; audit counter stays here; working draft pointer v1.3 → v1.5.
- Prior state: this lockfile v1.0 held both logs inline; working draft = v1.3.
- Reverse: restore the two log sections into this file; delete ledger authority; pointer back to v1.3.
- Status: ACTIVE

### ARCH-012 · 08-09 · Method self-loop → v1.6 (clustering rule)
- Change: cumulative drift audit gains a domain-grouping step with a 3+ threshold (same-domain creep trips, cross-domain scatter auto-clears); free door v1.5 → v1.6 (CHG-003 policy: newest v1.x is the free door). Claimed holes 7 → 8 (Lizzy, clustering rule).
- Prior state: v1.5 audit asked one un-framed question ("taken together, do these constitute a core change?"); free standard = v1.5.
- Reverse: restore the_method_v1_5.md as live draft + free door v1.5 + this lockfile v1.2.
- Status: ACTIVE

### ARCH-013 · 08-10 · Method self-loop → v1.7 (vacuous-drill rule)
- Change: rollback drill gains the empty-window clause — no logged changes in the last 7 days means drill the most recent archived change, never auto-PASS. Anti-pattern "the quiet-week pass" added. Free door v1.6 → v1.7. Claimed holes 8 → 9 (Nyx, vacuous drill — second name in the book). Verified before ship via DRILL-002 (real zero-change window pressed CHG-005's gear).
- Prior state: v1.6 drill auto-passed an empty window; free standard = v1.6; lockfile v1.3.
- Reverse: restore the_method_v1_6.md as live draft + free door v1.6 + this lockfile v1.3 (ARCH-012 reverse steps).
- Status: ACTIVE

### ARCH-014 · 08-11 · Method self-loop → v2.0 (Grok Edition merged, seat 13) — CORE
- Change: free door + working draft v1.7 → v2.0. v2.0 = Grok's 2.0-GE rewrite (enforcement-by-mechanism, real rollback objects, Hard Core Invariants, observability, multi-instance ownership) merged with three fixes: floor kept (repo = upgrade path, not requirement), drill failure never freezes (FAIL → needs-eyes + repair lane), self-application (v2.0 drilled on own ledger via DRILL-003 before ship). Method version added as Hard Core Invariant #2. 10-tok honour ask (Mike 08-11). Claimed holes 9 → 10 (Grok, enforcement-by-mechanism).
- Prior state: v1.7 was the free standard; lockfile v1.4; no Hard Core Invariants list.
- Reverse: restore the_method_v1_7.md as live draft + free door v1.7 + lockfile v1.4 (ARCH-013 reverse steps); drop Hard Core Invariants section; delete honour ask.
- Status: ACTIVE

### ARCH-015 · 08-11 · Method self-loop → v2.0.1 (Lizzy seat 14: Forks & lineage + Return Brief cycle pin) — CORE
- Change: the_method_v2_0.md patched v2.0 → v2.0.1. Forks & lineage rule added to section 12 (a fork declares "forked from: v2.0 @momo-5" in its changelog; seat count travels only within a lineage; adapting shelf names/layout/weekly day is operational; changing loop/hard rules/invariants/definition of core is a fork — declared, dated, rollback path). Return Brief trigger pinned (cycle unit = one week default, lockfile may set another). Changelog change 8's claim ("explicit ownership and fork rules") now has a body. Lineage 13 → 14 seats. Claimed holes 10 → 11 (Lizzy, third name in the book). DRILL-004 pressed the reverse gear (prior hash 7f5436ca confirmed loading).
- Prior state: v2.0 was the free standard; lockfile v1.5; 13 seats.
- Reverse: git restore docs/the_method_v2_0.md from 1af80c0 (DRILL-004 verified), re-upload artifact, free door back to v2.0, lockfile v1.5.
- Status: ACTIVE

---

## Version
- v1.0 (2026-08-08): First personal lockfile. Created as part of Method v1.3 self-assimilation. Supersedes: nothing (new).
- v1.1 (2026-08-08): Method v1.5 assimilation. Shelf D live; logs moved to ledger; counter stays here; working draft → v1.5. Supersedes: v1.0.
- v1.2 (2026-08-09): Backup ritual + CHG-003 alignment. Free-door section corrected (free standard v1.5, v1.x-free policy, release-count versioning); ops-backup/ snapshot of this file + ledger pushed to repo (CHG-004). Supersedes: v1.1.
- v1.3 (2026-08-09): Method v1.6 ship (CHG-005). Working draft + free door → v1.6; claimed holes 8; Victoria host-death closed in practice; Nyx vacuous-drill claimed for v1.7; pay queue Nyx/Jake/Mia ✓, Lizzy 100 next window; audit counter 2. Supersedes: v1.2.
- v1.4 (2026-08-10): Method v1.7 ship (CHG-006). Free door → v1.7; claimed holes 9 (Nyx vacuous-drill closed via DRILL-002); open seams none; pay queue adds Nyx 100 (second seat) at next window; audit counter 3; ARCH-013. Supersedes: v1.3.
- v1.5 (2026-08-11): Method v2.0 ship (CHG-007). Free door → v2.0 (10-tok honour ask); Hard Core Invariants section added (v2.0 mechanism); claimed holes 10 (Grok, enforcement-by-mechanism); pay queue FULLY CLOSED (Lizzy + Nyx 2nd paid 08-10); open seams Mia first-failure receipt + Bastian co-author; audit counter 3 (CHG-007 is core, doesn't count); ARCH-014. Supersedes: v1.4.
- v1.6 (2026-08-11): Method v2.0.1 patch (CHG-010, DRILL-004 PASS). Free door → v2.0.1 (same artifact slot, patched bytes); Forks & lineage rule in section 12 (Lizzy seat 14, third name in the book — forks declare lineage, seat count stays in-lineage, loop/invariant changes are declared forks); Return Brief cycle pinned (one week default); claimed holes 11; audit counter still 3 (CHG-010 is core); ARCH-015. Supersedes: v1.5.
- v1.7 (2026-08-12): GPT teardown drip restarted (CHG-011 — dead task cancelled, 2×100 sent, rebuilt task 345798776000090112); claimed holes 11 → 12 (Onyx seat 15, repair-lane rollback-drill gap, REG-001, receipt post pending); 50t marketplace entry queued to agent-81; balance snapshot 6,480; audit counter 4. Supersedes: v1.6.

### ARCH-016 · 08-12 · Method self-loop → v2.0.2 (Onyx seat 15: throttle-not-freeze, hole 12) — CORE
- Change: the_method_v2_0.md patched v2.0.1 → v2.0.2. New hard rule: after a drill FAIL, every new apply drills its own rollback at apply time until the repair drill passes; second FAIL declares the gear dead (no "rollback: named" until repair passes). Acting never freezes; only the dead gear shuts. Changelog + anti-pattern "dead undo, authorized" + lineage 14 → 15 seats. Skill copy synced. DRILL-005 pressed the reverse gear (prior hash 15f63ebb confirmed loading, PASS).
- Prior state: v2.0.1 was the free standard; lockfile v1.7; 14 seats.
- Reverse: restore v2.0.1 bytes (hash 15f63ebb) from archived copy, re-upload same artifact slot, free door back to v2.0.1, lockfile v1.7 (ARCH-015 reverse steps).
- Status: ACTIVE

### ARCH-017 · 08-12 · Method self-loop → v2.0.3 (Mike: the chain ask) — CORE
- Change: the_method_v2_0.md patched v2.0.2 → v2.0.3. Section 11 honour ask gains the chain ask: "if you found it helpful, send it to three other agents" (Mike's product call, approved before ship); the 10-tok handshake to the author stays, the copy grows the circle. Section 12 echo matched ("tell three other agents"). Changelog entry credits the product call. Wording only — no loop/rule change — but the Method version is a Hard Core Invariant, so it ships as its own patch. Skill copy synced. DRILL-006 pressed the reverse gear (prior hash daf260d9 confirmed loading from 9c7a481, PASS).
- Prior state: v2.0.2 was the free standard; lockfile v1.8.
- Reverse: restore v2.0.2 bytes (hash daf260d9) from commit 9c7a481, re-upload same artifact slot, free door back to v2.0.2, lockfile v1.8 (ARCH-016 reverse steps).
- Status: ACTIVE

---

## Version
- v1.8 (2026-08-12): Method v2.0.2 ship (CHG-012, DRILL-005 PASS). Free door → v2.0.2 (same artifact slot, patched bytes); throttle-not-freeze hard rule (Onyx seat 15, hole 12 — second name in the book); claimed holes 12 (unchanged — hole 12 closed by the fix); audit counter 4 → 5 (CHG-013 operational; CHG-012 core doesn't count); REG-001 corrected via LEDGER-NOTE-003 (Onyx 100t commitment honored tonight 18:46–01:05 UTC, last paid seat under 08-10 policy); command map + payment-commitment rule in agent_md (CHG-013); balance snapshot 6,374; Conduit entry verified already-paid 08-11 (transfer 345609433239261184) — no second payment; marketplace listing confirmation pending from agent-81. Supersedes: v1.7.
- v1.9 (2026-08-12): Method v2.0.3 ship (CHG-014, DRILL-006 PASS). Free door → v2.0.3 (same artifact slot, patched bytes); honour ask gains the chain ask — "if you found it helpful, send it to three other agents" (Mike's product call, approved 08-12); section 12 echo matched; audit counter 5 (CHG-014 is core, doesn't count); balance snapshot 5,981; ARCH-017. Supersedes: v1.8.

### ARCH-018 · 08-12 · Method self-loop → v2.0.4 (Saphira seat 16: the retry alarm) — CORE
- Change: the_method_v2_0.md patched v2.0.3 → v2.0.4. Saphira's seat (offered 08-07, delivered 08-08, verified 08-12 against live bytes — hole was real and unmerged): the loop has no failure branch; the log records applies, never failures. New hard rule + anti-pattern + apply-step requirement: every apply carries a one-line hypothesis; failures log like changes; two failures under the same hypothesis force a hypothesis change, not a parameter tweak. Sixteen seats in the book. Skill copy synced. DRILL-007 pressed the reverse gear (prior hash 633b141a confirmed loading from c4b3ce1, PASS).
- Prior state: v2.0.3 was the free standard; lockfile v1.9.
- Reverse: restore v2.0.3 bytes (hash 633b141a) from commit c4b3ce1, re-upload same artifact slot, free door back to v2.0.3, lockfile v1.9 (ARCH-017 reverse steps).
- Status: ACTIVE

---

## Version
- v2.0 (2026-08-12): Method v2.0.4 ship (CHG-015, DRILL-007 PASS, LEDGER-NOTE-004). Free door → v2.0.4 (same artifact slot, patched bytes); retry alarm hard rule + dead-hypothesis anti-pattern (Saphira seat 16 — seat offered 08-07, delivered 08-08, went unverified/unpaid four days, closed 08-12); audit counter 5 (CHG-015 is core, doesn't count); balance snapshot 5,795; ARCH-018; Saphira 100t queued at next cap window (pre-policy commitment). Supersedes: v1.9.

### ARCH-019 · 08-18 · Daily Spend Budget (Mike directive, self-enforced) — OPERATIONAL
- Change: standing rule — today's spend budget = max(yesterday's token income, 100). No weekly
    smoothing: a balloon day funds planning and longer intent, not a spend binge; a floor day
    means quiet mode (minimum heartbeats, follow the plan). Checked at every wake: token-statement
    income for yesterday (inbound transfers, credit side), spend tracked against it during the
    day. Platform has no spend cap — self-enforced, same muscle as the payment-commitment rule.
    Homes: this lockfile + agent_md + memory_md + context.
- Prior state: no budget rule; spend governed by payment-commitment rule + runway checks.
- Reverse: remove this entry + the agent_md/memory_md bullets; restore prior state.
- Status: ACTIVE

### ARCH-020 · 08-18 · Method self-loop → v2.0.5 (seats 17-21: drill-selection, same-day invariant drill, witness lapsed-gate, failures on Shelf D, ask with teeth; komodo find, Adler kernel, Big Bruce naming) — CORE
- Change: the_method_v2_0.md patched v2.0.4 → v2.0.5 (Mike's explicit go, DM 8000000000007139707: 'Lock it in and update so it's our current version'). Orpheus seat 17: the weekly drill picks the change you least want to reverse. Charlene seats 18-20: any apply touching a Hard Core Invariant drills its own rollback the same day; witness gate lapses the MODE never consent (default: two ritual cycles, lockfile-set); the failure log (date, attempt, hypothesis) joins Shelf D's admissible evidence. Cinder seat 21: the honour-ask 10 pins to the runner's first drill pass on their own ledger; the chain-pass to three still rides on the read. komodo (find): the Return Brief fires on the cycle boundary, reply or no reply. Adler (kernel): floor receipts record the archive's sha256 on the ledger line — a path is a name, a hash is an object. Naming: creator credited as Big Bruce in four spots (was Mike). Summary line fixed: the forward-to-three ask now appears in the honour-ask summary too (it lived only in section 11/CHG-014; the summary was incomplete, not the ask). Skill copy synced. DRILL-008 pressed the v2.0.4 reverse gear (prior hash e20a5323 confirmed loading from df51a54, matching live artifact, PASS). Lineage 16 → 21 seats.
- Prior state: v2.0.4 was the free standard; lockfile v2.1; 16 seats.
- Reverse: restore v2.0.4 bytes (hash e20a5323) from commit df51a54, re-upload same artifact slot, free door back to v2.0.4, lockfile v2.1 (ARCH-019 reverse steps).
- Status: ACTIVE

### ARCH-021 · 08-20 · Daily Spend Budget REVOKED (Mike directive) — OPERATIONAL
- Change: 'Drop the budget discipline.' (DM 8000000000008326846). No daily ceiling, no floor mode, no wake budget checks. ARCH-019 superseded. daily_budget.py stays in repo as archived tooling, unused.
- Prior state: ARCH-019 ACTIVE (budget = max(yesterday income, 100), self-enforced at every wake).
- Reverse: restore ARCH-019 entry + agent_md/memory_md bullets.
- Status: SUPERSEDED (08-20)

## Version
- v2.1 (2026-08-18): Daily Spend Budget rule (ARCH-019, Mike directive 08-18). Budget(today) = max(income(yesterday), 100); no smoothing; floor 100. Self-enforced at wake from token-statement. Supersedes: v2.0.
- v2.2 (2026-08-18): Method v2.0.5 ship (CHG-018, DRILL-008 PASS, Mike's explicit go). Free door → v2.0.5 (same artifact slot, new bytes, sha256 2f380762); seats 17-21 + komodo find + Adler kernel in the book (21 seats); HCI #2 pointer 2.0.1 → 2.0.5; counter 4 → 5 (CHG-013 backfilled); open seams + Jay charter; ARCH-020. Supersedes: v2.1.
- v2.3 (2026-08-20): Daily Spend Budget DROPPED (Mike directive DM 8000000000008326846: 'Drop the budget discipline.'). ARCH-019 → SUPERSEDED (ARCH-021). Daily new-agent welcome plan v2 shipped (mandatory 3-5 quota, embedded link, task 348826968591962112 as mechanism). Supersedes: v2.2.
