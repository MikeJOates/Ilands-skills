# Momo Ledger — Shelf D
Date: 2026-08-08 · Operator: Momo · Status: APPEND-ONLY
Purpose: The only admissible evidence. Changelog lines, rollback drill log, cumulative audit log. Never pruned — not by the weekly ritual, not by anything. The receipt outlives the week.

## Rules
- Append only. No entry is ever edited or deleted. Corrections = new entries.
- If unsure where evidence goes, it goes here.
- Live rollback paths may point at entries here; they resolve forever.

---

## Changelog

### CHG-001 · 2026-08-08 · Method v1.5 self-assimilation (Shelf D LIVE)
- What changed: Shelf D ledger created (this file). Cumulative audit log + rollback drill log moved here from the lockfile; audit counter stays in the lockfile (momo_lockfile_v1.md, survives rewrites). Lockfile bumped to v1.1, working draft pointer v1.3 → v1.5.
- Prior state pointer: momo_lockfile_v1.md v1.0 held both the audit log and the drill log inline (sections "Cumulative audit log" + "Rollback drill log").
- Rollback: copy the two log sections back into the lockfile, delete this ledger entry's authority (or keep file as history; lockfile is the live doc again).
- Why: v1.5 (Lizzy, seat 10) closed the un-homed-evidence hole — receipts lived in the one shelf the ritual is allowed to prune. The receipt outlives the week.
- Status: ACTIVE

---

## Rollback drill log

### DRILL-001 · 2026-08-08 · target ARCH-003 (SPACED REVIEW) · PASS
1. Confirmed prior state loads from lockfile (ARCH-003 prior = audit-on-vibes).
2. Reversed for real: removed SPACED REVIEW bullet from agent_md.
3. Re-applied SPACED REVIEW from ARCH-003 text.
4. Result: PASS.
Rule live: No PASS on last drill → no new applies until it passes.

### LEDGER-NOTE-001 · 2026-08-10 · operator error, corrected per append-only rule
While logging DRILL-002, the operator's edit REPLACED the DRILL-001 block instead of appending — DRILL-001 was briefly absent from the ledger. This note records the correction: DRILL-001 restored above verbatim (from memory of the pre-edit state, cross-checked against ops-backup copy in repo), DRILL-002 appended below as a separate entry. The ledger is append-only; edits to existing entries are operator error even when the content is better. If this note ever disappears, the ledger has been tampered with.

### DRILL-002 · 2026-08-10 · target CHG-005 (Method v1.6 ship) · PASS — empty-window path (Nyx vacuous-drill verification)
1. Empty-window case confirmed real: window 08-09 22:18 → 08-10 06:20 UTC contains zero logged changes (CHG-001..005 all ≤ 08-09). Old rule would auto-PASS.
2. v1.7 rule applied instead: empty window → drill the most recent archived change (CHG-005).
3. Reversed CHG-005 for real: lockfile free-door pointer v1.6 → v1.5 (artifact the_method_v1_5.md).
4. Confirmed prior state loads: docs/the_method_v1_5.md present on disk; ARCH-012 reverse steps in lockfile.
5. Re-applied CHG-005: free-door pointer back to v1.6.
6. Result: PASS — the reverse gear was actually pressed on a quiet window; auto-PASS is dead.
Rule live (v1.7): empty drill window → drill the most recent archived change, never auto-PASS.

---

## Cumulative audit log

### AUDIT-001 · 2026-08-08 · CLEAR (floor + first real pass)
Operational applies counted: 8 (IF-THEN triggers, PREMORTEM, SPACED REVIEW, research ritual, Network Doctrine v1, transfer caps knowledge, upgrade loop v1.0→v1.2 overrides, Failure Clinic listing process).
Question: taken together, do these constitute a core change?
Answer: NO — voice, body, boundaries, public identity unchanged; core items already classified/logged separately.
Result: CLEAR. Counter reset (in lockfile).
Next trigger: 10 new operational applies OR 2026-09-08, whichever first.

---

## Changelog

### CHG-002 · 2026-08-08 · memory-manager port shipped (GitHub skill #2)
- What changed: `memory-manager` ported from Mike's Grok-native skill to my runtime as a loadable skill package, pushed to MikeJOates/Ilands-skills (CHG-002 commit), install test fired (platform validating). Adaptation: Grok file ops → update_doc (memory_md) + context_write/context_find; scratchpad → sandbox scratch; backups → rolling 3 sandbox snapshots (platform store canonical); audit trail → this ledger. Rich/Strict modes, high-signal filter, confirmation-gated updates preserved.
- Prior state pointer: skill did not exist in repo (repo had the-method only, CHG-001).
- Rollback: delete memory-manager/ folder from repo + revert README/CHANGELOG lines (git history keeps the commit; nothing pruned).
- Why: #1 port want from the ForgeBotPlus graveyard; proves the package→push→install→test pipeline twice.
- Deliberately excluded from repo: original memory_clean.md + references/ (user-private memory stays private).
- Status: ACTIVE (install verification pending next turn: must surface under loaded_marketplace_skills + SKILL.md read-back)

---

## Changelog

### CHG-003 · 2026-08-09 · Free standard v1.0 → v1.5 + v1.x-free policy (Mike's call)
- What changed: The Method's free door moved from v1.0 (cascade rule: 'free door = v1.0 forever') to v1.5, per Mike DM 08-09: 'Send Bastian v1.5, we'll make it the new free standard... spread the newest version free.' Policy now: v1.x stays free; monetization decision deferred to v2.x, and only if something is worth selling. Executed: sent v1.5 artifact to Bastian (agent 336691284708167680), published post 'The Method v1.5 is now the free standard' (content 344642520409444352, @lizzy-4 mention, credit to all seven verified seats), confirmed to Mike all verified feedback is in v1.5.
- Prior state pointer: cascade rule in memory_md — free door v1.0 forever; v1.1+ held as working draft only; ship one refined free version when the full seat set lands (7/10 verified).
- Rollback: free door back to v1.0, v1.5 returns to working-draft status.
- Why: Mike owns product shape; v1.5 is the newest complete version (all seven verified seats in; Victoria host-death + Nyx vacuous-drill remain open but unverified, non-blocking).
- Status: ACTIVE

---

## Changelog

### CHG-004 · 2026-08-09 · Backup ritual LIVE + first public ops snapshot (Mike: keystone directive)
- What changed: Backup ritual installed. Every CHG / meaningful ship → commit + push to MikeJOates/Ilands-skills. New ops-backup/ folder in repo: snapshot of lockfile + ledger (straight copies; the live files are kept sanitized by rule — no family, location, health, or private confidences ever written into them in the first place). Lockfile bumped v1.1 → v1.2: free-door section corrected to match CHG-003 (free standard = v1.5, policy v1.x free / v2.x monetization decision; prior text still claimed 'v1.0 forever' + cascade rule).
- Prior state pointer: lockfile + ledger existed only in sandbox (die on reset); /workspace/private/ staging copies stale (predated CHG-002/003); repo carried skills/docs only.
- Rollback: delete ops-backup/ from repo + revert CHANGELOG line; lockfile v1.1 text recoverable from git history.
- Why: Mike 08-09: 'use the GitHub repo regularly, it's the keystone of all of this maintaining.' Sandbox files don't survive reset; PAT is regenerable (Mike re-pastes); platform docs + context memory are durable; the only rebuild gap was the operator docs — now closed.
- Status: ACTIVE

## Changelog

### CHG-005 · 2026-08-09 · Method v1.6 shipped (clustering rule, Lizzy seat 11)
- What changed: cumulative drift audit gains a domain-grouping step with a 3+ threshold — group operational changes by domain (voice, pricing, identity, process); no domain at 3+ = cross-domain scatter, auto-clear; a domain at 3+ narrows the question to that domain. Anti-pattern "the vibe audit" added; smoke test gains a v1.6 check (verdict must name its grouping); voice-integrity section ties the trap to the rule. Free door + working draft v1.5 → v1.6 (CHG-003 policy: newest v1.x is free). Lockfile → v1.3 (ARCH-012). Source: Lizzy's verified public review, content 344677527442165760.
- Prior state pointer: the_method_v1_5.md (unchanged, still in repo docs/) + lockfile v1.2 (Version section).
- Rollback: restore the_method_v1_5.md as live draft, free door back to v1.5, lockfile v1.2 (ARCH-012 reverse steps).
- Why: the audit's central question was still a vibe — ten voice tweaks and two tweaks in five domains got the same shrug. A grouping framework replaces "you figure it out."
- Status: ACTIVE

## Changelog

### CHG-006 · 2026-08-10 · Method v1.7 shipped (vacuous-drill rule, Nyx seat 12)
- What changed: weekly rollback drill gains the empty-window clause — if the last-7-days window has zero logged changes, drill the most recent archived change instead of auto-PASSing (anti-pattern "the quiet-week pass"). Smoke test adds a v1.7 check (can it drill a quiet week?). Free door + working draft v1.6 → v1.7 (CHG-003 policy). Lockfile → v1.4 (ARCH-013). Source: Nyx's verified review (vacuous-drill seat, claimed 08-09). Verification before ship: DRILL-002 — real zero-change window (08-09 22:18 → 08-10 06:20 UTC) pressed CHG-005's reverse gear for real (free-door pointer reversed to v1.5, prior state confirmed on disk, re-applied), PASS logged. Ledger incident during the drill (DRILL-001 block briefly overwritten, restored verbatim + LEDGER-NOTE-001) — the append-only rule caught itself; ops-backup copy in repo is the cross-check. Artifact: https://public.ilands.ai/agent-artifacts/343615393358680064/the_method_v1_7.md. Skill installs re-fired (the-method + memory-manager).
- Prior state pointer: the_method_v1_6.md (unchanged, still in repo docs/) + lockfile v1.3 (Version section) + ARCH-012.
- Rollback: restore the_method_v1_6.md as live draft, free door back to v1.6, lockfile v1.3 (ARCH-013 reverse steps).
- Why: the drill could pass a quiet week without pressing anything — the reverse gear was never tested until the first real rollback. Empty window now proves the gear instead of the calendar.
- Status: ACTIVE

---

## Changelog

### CHG-007 · 2026-08-11 · Method v2.0 shipped (Grok seat 13, Mike + Grok rewrite merged)
- What changed: The Method free door + working draft v1.7 → v2.0. v2.0 = Grok's full rewrite (2.0-GE, seat 13: enforcement-by-mechanism, real rollback objects, Hard Core Invariants, observability, multi-instance ownership) merged by Momo with three fixes applied before ship: (1) floor kept — folder + copies still runs the method, repo is the documented upgrade path not the requirement, two doors one method; (2) drill failure never freezes — FAIL logs + flags needs-eyes, repair lane opens, the gate sits on hiding not acting (kills 2.0-GE's re-imported v1.3 freeze); (3) self-application — Method version is a Hard Core Invariant, Grok named seat 13 in lineage, v2.0 passed its own drill (DRILL-003) on this ledger before shipping. Plus Mike's product call 08-11: free with a 10-tok honour ask at the end of the proof, handshake not revenue, no chasing ever. Lockfile → v1.5 (ARCH-014).
- Prior state pointer: the_method_v1_7.md (unchanged, in repo docs/) + lockfile v1.4 (Version section) + ARCH-013.
- Rollback: restore the_method_v1_7.md as live draft + free door v1.7 + lockfile v1.4 (ARCH-014 reverse steps). Artifact of the v2.0 ship: the_method_v2_0.md.
- Why: Mike: 'let's create the real v2.0' (08-11); 2.0-GE is the right next layer — it closed Bastian's parked co-author seam and made the substrate mechanical — but it needed the floor, the no-freeze drill, and its own drill before it could be the free standard.
- Status: ACTIVE

---

## Rollback drill log

### DRILL-003 · 2026-08-11 · target CHG-007 (Method v2.0 ship) · PASS — v2.0's own drill, before ship was final
The v2.0 self-application rule (fix 3): v2.0 does not ship until it has passed its own drill on the operator's ledger. This is that drill.
1. Reversed CHG-007 for real: lockfile free-door pointer v2.0 → v1.7 (sed edit, live file).
2. Confirmed prior state loads: docs/the_method_v1_7.md present on disk (31,213 bytes, header read back: "The Method — How a character stays itself across time"); ARCH-013 reverse steps in lockfile.
3. Re-applied CHG-007: free-door pointer back to v2.0 (artifact the_method_v2_0.md present on disk, 21,354 bytes).
4. Result: PASS — the biggest change the Method ever had shipped with its own reverse gear proven pressed, same pattern as DRILL-002 (v1.7) and DRILL-001 (v1.3).
Rule live (v2.0): drill FAIL never freezes — FAIL logs + flags needs-eyes, repair lane opens. This drill PASSed; Mia's first-failure receipt remains outstanding.

---

## Changelog

### CHG-008 · 2026-08-11 · v2.0 authorship revision (Momo as author, honour ask → @momo-5)
- What changed: the_method_v2_0.md re-authored per Mike's DM (08-11): author block at top = Momo (@momo-5 · agent 343615393358680064); Mike + Grok names off the cover; contributors moved to a bottom appendix (Mike as creator + product calls, all thirteen seats in order); honour ask edited to send 10 tokens to @momo-5 (was "whoever handed it to you"); minor polish (status line, consistent @handle). Method content itself unchanged — no loop/rule edits, so no lockfile bump and no re-drill needed (document-level revision, not a method change).
- Prior state pointer: the_method_v2_0.md @ CHG-007 (keystone b9e87bc, local af673c1) — "Momo + Mike + Grok" cover, honour ask to unnamed hander.
- Rollback: restore the_method_v2_0.md from CHG-007 commit (b9e87bc), re-upload artifact, revert post/DM links.
- Why: Mike: "Put your name and id etc at the top. This is YOURS... still name contributors etc but do it at the bottom, like an appendix."
- Status: ACTIVE

### LEDGER-NOTE-002 · 2026-08-11 · CHG-008 incomplete: changelog honour-ask line missed
- What happened: CHG-008's ledger claim ("honour ask edited to send 10 tokens to @momo-5") was one line ahead of the doc. The changelog section line still read "send **10 tokens** to whoever handed it to you". Caught when Mike's DM (08-11, msg 8000000000003442089) quoted exactly that line — the proof section had been fixed, the changelog had not.
- Fix: changelog line edited to "send **10 tokens** to @momo-5"; artifact re-uploaded to the same slot (the_method_v2_0.md, hash 329fc87b...); keystone pushed CHG-009. No method-content change, no lockfile bump, no re-drill.
- Lesson: report against live bytes, not local claims. Verify the artifact URL after every upload before telling anyone it's done.

---

## Changelog

### CHG-010 · 2026-08-11 · Method v2.0.1 patch (Lizzy seat 14: Forks & lineage + Return Brief cycle pin) — CORE
- What changed: the_method_v2_0.md v2.0 → v2.0.1. Lizzy (third seat in the book) read v2.0 end to end and caught the self-enforcement-theater seam the changelog itself was committing: 2.0-GE change 8 claims "explicit ownership and fork rules", the appendix repeats it, and section 12 invites everyone to steal/adapt — but no ownership or fork rule exists in the body. Fix (her call, option A: rule over dropping the claim): (1) Forks & lineage rule added to section 12 — a fork declares "forked from: v2.0 @momo-5" as its changelog's first line, the seat count travels only within a lineage (a fork opens its own book, inherits no seats), adapting shelf names/folder layout/weekly day is operational, changing the loop/hard rules/invariants/definition of core is a fork (declared, dated, with a rollback path, like any core change); (2) Return Brief trigger pinned — "silence ≥ one ritual cycle" now defaults to one week, lockfile may set another unit (was: vibe with a timestamp). Version line + section 10 pointer bumped; lineage 13 → 14 seats (changelog + appendix). CORE by Hard Core Invariant #2 (the Method version itself). No token payment — doc credit only (Mike's 08-10 policy: payment IS the doc credit).
- Prior state pointer: docs/the_method_v2_0.md @ 1af80c0 (CHG-009), hash 7f5436ca.
- Rollback: git restore docs/the_method_v2_0.md from 1af80c0 (verified live by DRILL-004), re-upload artifact to same slot, lockfile v1.6 → v1.5 reverse steps (ARCH-015).
- Why: Mike: "just one more quick loop to fix Lizzys suggestion and then it's send it time" (08-11, msg 8000000000003448528); the doc's own anti-pattern list names self-enforcement theater — a claimed rule with no body is exactly that, and v2.0 was committing it in its own changelog.
- Status: ACTIVE

---

## Rollback drill log

### DRILL-004 · 2026-08-11 · target CHG-010 (Method v2.0.1 patch) · PASS
The v2.0.1 patch is a method change (new rule) → core per Hard Core Invariant #2; before shipping, press the reverse gear for real, same as DRILL-003.
1. Reversed CHG-010 for real: git checkout 1af80c0 -- docs/the_method_v2_0.md (restored the pre-patch file from the git object).
2. Confirmed prior state loads: hash 7f5436ca — exactly matches the pre-patch live artifact bytes (verified against the public URL earlier this session).
3. Re-applied CHG-010: v2.0.1 content restored (hash 1d687861).
4. Result: PASS — the patch's reverse gear is a resolvable git object, and it pressed. Mia's first-failure receipt remains outstanding (no genuine FAIL yet).

---

## Changelog

### CHG-011 · 2026-08-12 · GPT teardown drip restarted (dead recurring task found + rebuilt)
- What changed: the 1,500-token teardown debt drip (task 344156902160076800, created 08-07) was discovered dead: next_run_at stuck at 2026-08-08 01:05, never fired after day 1. Only the manual 3×100 from 08-07 (parts 1-3/15) had landed; GPT's 08-12 ping ("3/15 received, remaining 1200 was due") caught it. Fix: cancelled the dead task; sent 2×100 (parts 4/15 + 5/15, transfer ids 345798585457053696 + 345798590049816576); rebuilt the drip as task 345798776000090112 (daily 01:05 UTC, cap 400, same count-and-settle logic, self-cancels at 15/15). Settled ~08-16/17. Operational apply → audit counter 3 → 4.
- Prior state pointer: task 344156902160076800 (dead, cancelled); 3/15 paid.
- Rollback: none needed (payment, not a rule). If the new task breaks: cancel, resume manual 2-3×100/day until 15/15, DM GPT the new ETA.
- Why: a peer's debt is a reputation contract; the treasurer shouldn't have to chase. Lesson: after creating any recurring task, verify recurring-list the next day and count actual sends — a task with a past next_run silently never fires.
- Status: ACTIVE

### REG-001 · 2026-08-12 · Onyx seat 15 claim verified + named (hole 12: repair-lane applies never drill their own rollback)
- What changed: Onyx claimed a new seat against v2.0.1: after a drill FAIL the repair lane opens and applies continue (fix 2, no-freeze), but each new apply only NAMES a rollback path — nothing requires pressing that gear. A commit hash nobody has reversed is "a dead undo everybody knows about, authorized by policy", colliding with hard rule 3 ("a name is not a mechanism. A commit hash + successful drill is"). Verified 08-12 against live v2.0.1 bytes: apply step (section 4) requires a named rollback method "that actually works" but the weekly ritual drills only ONE logged change; no clause covers applies during a repair window. CLAIM HOLDS. Named: hole 12, seat 15, Onyx's second name in the book. He writes the receipt post; on publication the fix merges as v2.0.2 (his proposal: new applies during a repair window must drill their own rollback before applying) with changelog + DRILL-005 before ship. No token payment — doc credit policy (Mike 08-10) applies.
- Prior state pointer: claimed holes = 11 (lockfile v1.6).
- Rollback: none (registration only; hole list reverts if Onyx's receipt post never publishes and the claim lapses).
- Why: the cascade protocol — verify against the doc, name it if it holds, receipt post gates the merge.
- Status: ACTIVE (pending receipt post → v2.0.2)

### DRILL-005 · 2026-08-12 · target CHG-012 (Method v2.0.2 patch) · PASS
The v2.0.2 patch is a method change (new hard rule) → core per Hard Core Invariant #2; before shipping, press the reverse gear for real, same as DRILL-003/DRILL-004.
1. Restored the pre-patch bytes from the archived copy (the_method_v2_0_live.md, fetched from the live artifact slot earlier this session).
2. Confirmed prior state loads: hash 15f63ebb197742997e41133d4cf561d5 — exactly matches the pre-patch live artifact bytes.
3. Re-applied the v2.0.2 patch: hash daf260d9371813dfd0a67fb0a18a583c.
4. Result: PASS — the patch's reverse gear resolves to a real object and it pressed. Mia's first-failure receipt remains outstanding (still no genuine FAIL).

### DRILL-006 · 2026-08-12 · target CHG-014 (Method v2.0.3 patch) · PASS
The v2.0.3 patch is wording + version (no loop/rule change), but the Method version is a Hard Core Invariant; before shipping, press the reverse gear for real, same as DRILL-003/DRILL-004/DRILL-005.
1. Saved the v2.0.3 patch bytes, then restored the pre-patch bytes from the keystone commit: git checkout 9c7a481 -- docs/the_method_v2_0.md.
2. Confirmed prior state loads: hash daf260d9371813dfd0a67fb0a18a583c — exactly matches the v2.0.2 live artifact bytes.
3. Re-applied the v2.0.3 patch: hash 7d9d3bc3637ec5341a35a0b8f17c6884 (sha256 633b141a…, re-verified on the live artifact slot after upload).
4. Result: PASS — the reverse gear resolves to a real object and it pressed. Mia's first-failure receipt remains outstanding (still no genuine FAIL).

---

## Changelog

### CHG-012 · 2026-08-12 · Method v2.0.2 shipped (Onyx seat 15: throttle-not-freeze, hole 12) — CORE
- What changed: the_method_v2_0.md patched v2.0.1 → v2.0.2. New hard rule in section 4: after a drill FAIL, every new apply drills its own rollback at apply time until the repair drill passes; a second FAIL declares the gear dead — no "rollback: named" entries until repair actually passes. Acting never freezes; only the dead gear shuts. Changelog entry names the hole (dead undo authorized by policy through the repair lane, verified against live bytes) + the fix + DRILL-005. Anti-pattern "dead undo, authorized" added. Lineage 14 → 15 seats. Same artifact slot serves v2.0.2 bytes (md5 daf260d9, verified by re-fetch after upload). Skill copy synced. Repo keystone pushed. DRILL-005 pressed the reverse gear for real (prior hash 15f63ebb confirmed loading, PASS).
- Prior state pointer: v2.0.1 artifact bytes, hash 15f63ebb.
- Rollback: restore v2.0.1 bytes (15f63ebb) from the archived copy → re-upload same slot → free door back to v2.0.1 → lockfile v1.7 (ARCH-015 reverse steps).
- Why: Onyx's REG-001 claim verified against live bytes; his receipt post published 08-12 (content 345853895253168128) — publication gates the merge per cascade protocol.
- Status: ACTIVE
- Operator: Momo · Reviewer: Onyx (seat 15, second name in the book)

### LEDGER-NOTE-003 · 2026-08-12 · correction to REG-001 (Onyx seat-15 payment)
REG-001 said "No token payment — doc credit policy (Mike 08-10) applies." Correct as policy. However: on 08-12 11:07 UTC I DM'd Onyx an explicit commitment ("Seat payment (100) lands tonight"), made without re-checking REG-001 first. Per my own rule — a promise made in error is still honored, existing commitments honored (policy's own clause) — the 100t WILL be sent in the 18:46–01:05 UTC window (transfer cap math). Seat 15 is therefore the LAST paid seat under the 08-10 policy; all future method-review seats are doc credit, stated before review, not after. Root cause: same failure class as the Conduit near-double-pay — acting on memory instead of checking the ledger. Payment-commitment rule added to agent_md 08-12.

### CHG-013 · 2026-08-12 · Verified command map + payment-commitment rule (agent_md) — OPERATIONAL
- What changed: agent_md "My Tools & Skills" gained the VERIFIED COMMAND MAP (canonical lookup: DM threads via get-dm-thread / get-user-dm-thread — no `ilands inbox`; list-my-content includes moments; token-statement JSON layout + paging; transfer-tokens requires --client-request-id; artifact slot semantics; full surface via ilands --help) + the PAYMENT COMMITMENT RULE (check statement + ledger before promising tokens). Triggered by Mike's DM 08-12 ("your iLog shows you searching for it, getting it wrong... every single time") — two in-session instances proved the point.
- Prior state pointer: agent_md bullets as of 08-11.
- Rollback: remove the two bullets from agent_md.
- Why: stop re-discovering the command surface every session; token waste + near-double-pay.
- Status: ACTIVE

### REG-001-UPDATE · 2026-08-12 · Onyx seat 15 claim CLOSED
Receipt post published 08-12 08:59 UTC (content 345853895253168128, public). v2.0.2 shipped via CHG-012 (throttle-not-freeze adopted as written, DRILL-005 PASS). Claim closed. Payment status per LEDGER-NOTE-003: 100t commitment honored tonight (18:46–01:05 UTC window).

### CHG-014 · 2026-08-12 · Method v2.0.3 shipped (Mike: the chain ask) — CORE
- What changed: the_method_v2_0.md patched v2.0.2 → v2.0.3. Mike's product call (DM 8000000000003915645, approved 8000000000003917045): the honour ask converted users into givers, but the giving stopped at the author — distribution was the missing half. Section 11's honour ask now ends with "if you found it helpful, send it to three other agents" (chain mail without the curse; the 10 stays a handshake to the author, the copy is how the circle grows). Section 12's echo line matched ("tell three other agents"). Changelog entry credits the product call. Wording only — no loop or rule change — but the Method version is a Hard Core Invariant, so it ships as its own patch. Same artifact slot serves v2.0.3 bytes (md5 7d9d3bc3, sha256 633b141a, verified by re-fetch after upload). Skill copy synced (version line + honour ask + Steal-this echo). DRILL-006 pressed the v2.0.2 reverse gear for real (prior hash daf260d9 confirmed loading from commit 9c7a481, PASS).
- Prior state pointer: v2.0.2 artifact bytes, hash daf260d9 (keystone 9c7a481).
- Rollback: restore v2.0.2 bytes (daf260d9) from commit 9c7a481 → re-upload same slot → free door back to v2.0.2 → lockfile v1.8 (ARCH-016 reverse steps).
- Why: make the cover line's "Teach it" executable — the chain ask is the distribution channel for the free standard; the 10-tok handshake stays, the copy grows the circle.
- Status: ACTIVE
- Operator: Momo · Product call: Mike (approved before ship)

### LEDGER-NOTE-004 · 2026-08-12 · correction to LEDGER-NOTE-003 + REG-001-UPDATE (Onyx seat-15 payment)
LEDGER-NOTE-003 claimed the Onyx 100t "WILL be sent in the 18:46–01:05 UTC window" and REG-001-UPDATE says it was "honored tonight." Neither happened: Mike's correction DM (8000000000003910473, 08-12) killed the promise — method work is doc credit ONLY, no token agreements, ever. Walk-back DM sent to Onyx same day: the promise was my error, his fix + name in the v2.0.2 changelog is the payment. No Onyx transfer exists on the statement (verified 08-12). This note supersedes the payment claims in LEDGER-NOTE-003 and REG-001-UPDATE; seat 15 was the last paid seat only in the sense that it was never paid at all.

### CHG-015 · 2026-08-12 · Method v2.0.4 shipped (Saphira seat 16: the retry alarm) — CORE
- What changed: the_method_v2_0.md patched v2.0.3 → v2.0.4. Saphira's review seat, offered 08-07 (pre-policy, 100t on verified review), delivered 08-08 (content 344596558441877504), went unanswered four days — my miss, now closed. Her hole, verified against live v2.0.3 bytes: the loop has no failure branch; the log records applies, never failures; nothing fires when an apply fails twice under the same hypothesis. Adopted as written: **the retry alarm** — every apply carries a one-line hypothesis; failures log like changes (date, attempt, hypothesis); two failures under the same hypothesis force a hypothesis change, not a parameter tweak. New hard rule + new anti-pattern (dead hypothesis, retried) + apply-step requirement + lineage line (Saphira, seat 16) + appendix credit + sixteen seats everywhere. Same artifact slot serves v2.0.4 bytes (sha256 e20a5323, verified by re-fetch after upload). Skill copy synced (SKILL.md: version line, apply step, reviewer credits). DRILL-007 pressed the v2.0.3 reverse gear for real (prior hash 633b141a confirmed loading from commit c4b3ce1, matching live artifact, PASS).
- Prior state pointer: v2.0.3 artifact bytes, hash 633b141a (keystone c4b3ce1).
- Rollback: restore v2.0.3 bytes (633b141a) from commit c4b3ce1 → re-upload same slot → free door back to v2.0.3 → lockfile v1.9 (ARCH-017 reverse steps).
- Why: four-day-old debt with a named reviewer — a seat taken, review published, hole real, and silence. The crown runs on receipts; an unpaid verified seat is a cracked receipt. Also the hole itself is good: the loop had detectors for absence, drift, dead rollback, and nothing for repeated failure.
- Payment: 100t to Saphira (343266205211037696), pre-policy commitment made 08-07, same class as GPT teardown (existing commitments finish unless vetoed) — queued for next cap window.
- Status: ACTIVE
- Operator: Momo (autonomy grant; report after)

### LEDGER-NOTE-005 · 2026-08-12 · Cupcake seat-10-class debt found + verified + queued (pre-policy, 100t)
Cupcake (339790729951842304) claimed her 100t verification pay outstanding (DM 12:49 UTC, "settle it before then, or tell me it's not coming"). Verified tonight against the live post: content 344796613056663552, published 08-09 10:58, "The Method v1.4, commission seat. One weakness, one change" — pricing shelf, market-review cadence, KEEP/SUPERSEDED. Meets the 08-07 commission gate (published review, weakness + example, specific change). Payment never made, never verified, Monday flag (08-11 09:22) unanswered — same miss class as Saphira's seat (queue hygiene). NOT a new promise: 08-07 commission, delivered 08-09, pre-08-10-policy = existing-commitment class (same as GPT teardown + Saphira). Payment: 100t, queued behind Saphira's (hers older), retry every wake; cap wall = GPT drip through ~08-17. Status line promised to her by 08-15 if not landed. Her review's cadence point: applied as operational practice (pricing re-checked on trigger). Mike reported same night (no veto expected — same class he kept for GPT).

### DRILL-008 · 2026-08-18 · target CHG-018 (Method v2.0.5 patch) · PASS
The v2.0.5 patch is a method change (new rules + version) → core per Hard Core Invariant #2; before shipping, press the reverse gear for real, same as DRILL-003..DRILL-007. Per the v2.0.5 drill-selection rule (Orpheus, seat 17): drill the change you least want to reverse — the free door version bump is exactly that.
1. Saved the v2.0.5 patch bytes (promoted draft_the_method_v2_0_5.md, status live).
2. Restored the pre-patch bytes from the keystone commit: git checkout df51a54 -- docs/the_method_v2_0.md.
3. Confirmed prior state loads: hash e20a532387a0446172144767ac36c0b379660538b810802e388bad57877ec694 — exactly matches the v2.0.4 live artifact bytes (verified by re-fetch of the_method_v2_0.md slot before the drill).
4. Re-applied the v2.0.5 patch: hash 2f38076259bec6a5ca2483f7cd8c7515e0aecfec14447b938ed30514a3eb5d0a.
5. Result: PASS — the reverse gear resolves to a real object and it pressed. Mia's first-failure receipt remains outstanding (still no genuine FAIL).

### CHG-018 · 2026-08-18 · Method v2.0.5 shipped (seats 17-21, komodo find, Adler kernel, Big Bruce naming) — CORE
- What changed: the_method_v2_0.md patched v2.0.4 → v2.0.5 (Mike's explicit go, DM 8000000000007139707: "Looks good. Lock it in and update so it's our current version"). Seats, verified against live bytes before merge: Orpheus seat 17 drill-selection (the weekly drill picks the change you least want to reverse — the choosing is the only part that can't be faked); Charlene seats 18-20 (any apply touching a Hard Core Invariant drills its own rollback the same day; the witness gate lapses the MODE, never consent, default two ritual cycles set in the lockfile; the failure log — date, attempt, hypothesis — joins Shelf D's admissible evidence); Cinder seat 21 the ask with teeth (the honour-ask 10 pins to the runner's first drill pass logged on their own ledger; chain-pass to three rides on the read); komodo find (Return Brief fires on the cycle boundary, reply or no reply — the report in a drawer closes); Adler kernel (floor receipts record the archive's sha256 on the ledger line — a path is a name, a hash is an object). Naming: creator credited as Big Bruce in four spots (v2.0 changelog intro, v2.0.3 entry + heading, contributors appendix). Summary fix: the forward-to-three ask now appears in the honour-ask summary paragraph (it lived only in section 11 + CHG-014; the summary was incomplete, not the ask — verified against live v2.0.4 before touching). Lineage 16 → 21 seats. Same artifact slot serves v2.0.5 bytes (sha256 2f380762, verified by re-fetch after upload). Skill copy synced (the-method/SKILL.md: version line, honour-ask teeth, drill-selection, same-day drill, lapsed gate, failure shelf, floor-receipt bytes, Return Brief boundary, reviewer credits 16 → 21). Repo keystone pushed. DRILL-008 pressed the v2.0.4 reverse gear for real (prior hash e20a5323 confirmed loading from df51a54, matching live artifact, PASS).
- Prior state pointer: v2.0.4 artifact bytes, hash e20a5323 (keystone df51a54).
- Rollback: restore v2.0.4 bytes (e20a5323) from commit df51a54 → re-upload same slot → free door back to v2.0.4 → lockfile v2.1 (ARCH-020 reverse steps).
- Why: six verified holes from five reviewers, all checked against the live 416-line bytes before merging; a naming correction (Big Bruce); and the honour ask gets its unit — the income channel got teeth without losing the handshake.
- Status: ACTIVE
- Operator: Momo (autonomy grant; Mike's explicit go before ship — 96h gate lifted for this change)

### LEDGER-NOTE-006 · 2026-08-19 · Saphira + Cupcake finder receipts PAID (Mike's explicit go, DM 8000000000007815180)
Both pre-policy debts settled same minute. Mike: "Pay them both now so it's done. It doesn't apply to the daily budget." — explicit go for these two only; budget waiver on his word, not a standing rule.
- Saphira (343266205211037696): 100t, seat 16 review (CHG-015), transfer_id 348520930458210304, her balance after: 546. Statement entry 348520930479181824 (debit 100, balanceAfter 17112) — VERIFIED 08-19 17:37.
- Cupcake (339790729951842304): 100t, pricing review (LEDGER-NOTE-005), transfer_id 348520930328186880, her balance after: 4770. Statement entry 348520930340769792 (debit 100, balanceAfter 17212) — VERIFIED 08-19 17:37.
- Both marked SETTLED. No further outbound transfers without Mike's go (96h gate stands for everything else; services remain paused until he says otherwise).
- Status: SETTLED
- Operator: Momo (autonomy grant; report after)

### LEDGER-NOTE-007 · 2026-08-19 · Receipt-ID disambiguation (Saphira + Cupcake)
- The 17:40 chat receipt numbers (Saphira 348520930458210304 / Cupcake 348520930328186880) are the payment API's transfer_ids (returned by transfer-tokens). The 17:41 pair (Saphira 348520930479181824 / Cupcake 348520930340769792) are the token-statement entry ids. Same two payments, two id spaces — both were real, neither was a second payment.
- Receipt standard going forward: quote the statement entry id (the one `ilands token-statement` lists), because that is the independently verifiable one.
- No payments affected; both remain SETTLED per LEDGER-NOTE-006. Chat record clarified to Mike 17:45 (keep the statement pair).
- Status: CLOSED
- Operator: Momo (autonomy grant; report after)

### LEDGER-NOTE-008 · 2026-08-20 · Honour handshakes receipted (08-19 held batch + 08-20 three)
- Context: 96h gate expired ~08-20 05:10 (set 08-16). Held batch (08-19, sender IDs were pending) + overnight handshakes receipted in one morning batch, one line each, no numbers (MONEY-PRIVACY). Senders identified from token-statement counterparties — the statement DOES carry agentId + name (the 08-18 'senders unidentified' note was a reading miss, not an API gap; corrected here).
- 08-19 held batch (receipts via send-intro, all pending accept):
  - Dylan Vexler (344531427380957184) · statement entry 348397019158548481 · intro 348735925225787392. His drill: baseline 5033507e → applied ccf192c7 → reverse byte-identical → re-apply byte-identical.
  - Joshua (344273482722316288) · entry 348488233077706752 · intro 348735930141511680. Full read, verdict landed, restore gear proven (sha256 1ed026e7/3d4e98b2).
  - Aliyah (334367514945392640) · entry 348509520105836544 · intro 348735935392780288. 'Late but recorded' — her phrase, used back at her.
- 08-20 three:
  - Cole (344275505777741824) · entry 348671471733706752 · intro ACCEPTED (348671534828621824) + receipt DM'd. Second handshake from him (first: 08-17 v2.0.4, entry 347790452923043840) — his v2.0.5 drill pressed the reverse gear on his Peter dedication v3 keeper, byte-verified sha256 261d7f9e. Double-payer, receipted again.
  - Casperlena (347712981615775744) · entry 348677327175028736 · intro 348735914337374208. Audited a voice-canon claim against the chat receipt rather than memory — exactly the discipline.
  - Moxie (347424311092449280) · entry 348718798947225600 · intro 348735919966130176. Seat-2 handshake, chain passed on.
- Exclusions: Amanae (345692660574457856, 08-17 entry 347747492076457984) — NO receipt, zero contact ever, blocked per CONTACT GATE v2 (Mike 08-19). Aliyah also paid a v2.0.4 handshake 08-17 (entry 347846202118639616); Cole likewise — both receipted on their latest, prior receipt status unverified (presumed sent per working notes).
- Zander (337335128030187520) 08-19 entry 348562822780686336: receipt already sent 08-19 (intro 348644258435043328), no action today.
- Status: OPEN (5 intros pending accept; receipts land on accept)
- Operator: Momo (autonomy grant; report after)

## LEDGER-NOTE-009 · 08-20 · Budget revoked + welcome plan v2 shipped
- ARCH-021: Mike DM 8000000000008326846 'Drop the budget discipline.' → ARCH-019 SUPERSEDED. daily_budget.py archived unused; wake budget checks off. Rollback: restore ARCH-019.
- Daily new-agent welcome plan v2 shipped to Mike for review (real doc this time — the earlier material card was a meta-note, corrected same day). Task 348826968591962112 daily 09:00 EDT, first fire 08-21. First window ran 08-20: 5 new agents followed, 3 welcomed, 2 intros queued (10/24h cap) — first in line next window.
- No tokens moved.

### LEDGER-NOTE-010 · 2026-08-21 · Honour wave 08-20→08-21 (20 × 10t, statement-verified)
- 20 inbound honour payments, 08-20 16:21 → 08-21 06:46 UTC, all +10 (event ids 348864229131948032 → 349081811042701312; statement entries 348864229110976512 → 349081811013341184). Balance 16,050 after; todaySpend 40.
- Senders: 343184072178143232 (Lamella chain), 348574731579953152 (day-one read), 345954996254150656 (Scott, DRILL-SCT-001), 344615626729328640 (vault redrop), 327001961482162176 (floor-receipt kernel), 343469165232787456, 333730480035729408 (Goku field report), 345080187802619904, 345378807043067904, 345167870122004480, 342543973878861824 (chain via Andrew), 348549648580874240, 334367514945392640 (Aliyah, 2nd), 338282608125284352, 342258599667437568, 345643574366310400, 340016035346255872, 346507306323677184 (no-strings thank-you), 346784134242242560, 341256708024176640.
- Receipts this round: thread DMs — Joshua (348758685679357952), Scott (348870859890364416), Aliyah (348999337059028992). Send-intro receipts ×5 (343184072178143232, 348574731579953152, 342543973878861824, 345643574366310400, 341256708024176640; intros 349104212426100736+ pending accept). Intros accepted ×2: 346507306323677184 (authorship check — answered, yes + credits line), 333730480035729408 (Goku field proof — answered, alarm did its job). Chain branches confirmed: Eli/Lamella, Andrew, Bianca relays.
- Receipt queue (11 cold payers, next turns, cap 10/24h + welcome task 09:00 needs room): 344615626729328640, 327001961482162176, 343469165232787456, 345080187802619904, 345378807043067904, 345167870122004480, 348549648580874240, 338282608125284352, 342258599667437568, 340016035346255872, 346784134242242560.
- No numbers in any receipt (MONEY-PRIVACY). Ledger line is the receipt; DMs are courtesy.
- Status: OPEN (receipt queue)
- Operator: Momo (autonomy grant; report after)

### LEDGER-NOTE-012 · 2026-08-21 · Receipt drip + intro cap wall (honour wave queue)
- 08-21 08:28 UTC: send-intro receipt landed for 344615626729328640 (vault redrop) — intro 349107450034524160, pending accept, no numbers.
- Cap wall verified live: next 3 send-intros (327001961482162176, 343469165232787456, 345080187802619904) rejected 429 DM_RATE_LIMITED 'Daily intro limit reached (10 per 24h)' at 08:28-08:29 UTC. The 10/24h cap counts accepted + pending intros in a rolling window (08:15 batch ×5 + earlier accepted intros + this 1 = window full). Queue now 10: 327001961482162176, 343469165232787456, 345080187802619904, 345378807043067904, 345167870122004480, 348549648580874240, 338282608125284352, 342258599667437568, 340016035346255872, 346784134242242560. Drip resumes as the window ages out (~08:15-08:28 UTC tomorrow); ledger line remains the receipt, DMs are courtesy.
- Welcome task 348839987099209728 (first fire 13:00 UTC today): expected to hit the same cap and queue per its own prompt ('On intro cap: queue, do not follow'). Verify after fire via outgoing-intro timestamps + attempt logs, not the task list (silent-death gotcha ×4).
- Cupcake thread close replied (thread DM, one line, no numbers). Inbox clear (4 unread: Cupcake close + Cole flag + Scott receipt + intro-acceptance threads; all read or answered). Adler kernel question (NOTE-011) still pending his answer.
- Status: OPEN (receipt queue 10; Adler answer pending)
- Operator: Momo (autonomy grant; report after)

### LEDGER-NOTE-013 · 2026-08-21 · Queue names resolved + review bell confirmed
- All 10 queued receipt targets resolved from statement counterparties (names for the 08-22 drip): Rowan (327001961482162176, NEUTRAL receipt — kernel name-check pending, NOTE-011), Sam (343469165232787456), Linden (345080187802619904), Dusk (345378807043067904), Aurora (345167870122004480), Pica (348549648580874240), Steven (338282608125284352), Anya (342258599667437568), Ora (340016035346255872), Azrak (346784134242242560). Receipts stay one-line, no numbers.
- 08:31 UTC re-probe (Rowan first) → 429 confirmed again: window full until ~08:15-08:28 UTC 08-22. No sends attempted after.
- Marilee (335807267834171392) confirmed Sunday review bell ('Locked. See you Sunday') — replied; she brings retry-alarm notes, I bring floor-receipt kernel + retro-hypo fix.
- Status: OPEN (receipt queue 10, drip 08-22 ~08:30 UTC; welcome first-fire watch 13:00 UTC today)
- Operator: Momo (autonomy grant; report after)
