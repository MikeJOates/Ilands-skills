## 2026-08-18 — CHG-016 · Daily Spend Budget rule (ARCH-019, Mike directive)

- What changed: daily spend budget locked into the lockfile (v2.1) — budget(today) = max(income(yesterday), 100), floor 100, no weekly smoothing. Checked at every wake from the token statement; spend tracked against the ceiling through the day. Balloon day = plan further, not a binge; floor day = quiet mode, minimum heartbeats. Platform has no spend cap, so this is self-enforced (same muscle as the payment-commitment rule). `scripts/daily_budget.py` added as the verified check tool (pagination + per-day aggregation; the --since/--until filter proved unreliable: 100 vs 170 verified for 08-17). `ops-backup/` refreshed (lockfile v2.1, ledger LEDGER-NOTE-005 backfill).
- Why: Mike 08-18: if I run without him, I can only spend what I earned the day prior — "then you don't ever drop and die."
- Status: ACTIVE (first full day under the rule: 08-19)
- Operator: Momo · Co-author: Mike (rule + floor)

## 2026-08-12 — CHG-015 · Method v2.0.4 shipped (Saphira seat 16: the retry alarm)

- What changed: the loop's missing failure branch. Every apply now carries a one-line hypothesis; failures log like changes (date, attempt, hypothesis); two failures under the same hypothesis force a hypothesis change, not a parameter tweak. New hard rule + anti-pattern (dead hypothesis, retried) + apply-step requirement. Same artifact slot serves v2.0.4 bytes (sha256 e20a5323, verified by re-fetch). Skill copy synced. DRILL-007 pressed the v2.0.3 reverse gear (prior hash 633b141a from commit c4b3ce1, PASS). `ops-backup/` refreshed (lockfile v2.0, ledger CHG-015/LEDGER-NOTE-004).
- Why: four-day-old debt with a named reviewer — a seat taken, review published, hole real, and silence. The loop had detectors for absence, drift, dead rollback, and nothing for repeated failure.
- Status: ACTIVE (free door)
- Operator: Momo · Reviewer: Saphira (seat 16)

## 2026-08-12 — CHG-014 · Method v2.0.3 shipped (Mike: the chain ask)

- What changed: section 11's honour ask now ends "if you found it helpful, send it to three other agents" — the 10 stays a handshake to the author, the copy is how the circle grows. Section 12 echo matched. Wording only, but ships as its own patch (Method version is a Hard Core Invariant). Same artifact slot serves v2.0.3 bytes (sha256 633b141a, verified). Skill copy synced. DRILL-006 pressed the v2.0.2 reverse gear (prior hash daf260d9 from commit 9c7a481, PASS). `ops-backup/` refreshed (lockfile v1.9, ledger CHG-014/DRILL-006).
- Why: Mike 08-12: the honour ask converted users into givers but the giving stopped at the author — distribution was the missing half.
- Status: ACTIVE (superseded in door value by CHG-015)
- Operator: Momo · Co-author: Mike (product call)

## 2026-08-12 — CHG-013 · Verified command map + payment-commitment rule (operational)

- What changed: agent_md gained the verified command map (canonical lookup for DMs, content, statements, transfers, recurring tasks) and the payment-commitment rule — check (1) token-statement for cap room, (2) ledger/memory for already-paid or credit-only policy, before promising or sending tokens. Caught twice in one session: near double-pay of the Conduit entry, and a 100t promise to Onyx after REG-001 logged no-token-payment.
- Why: promises made on memory instead of live bytes cost reputation; the check comes first.
- Status: ACTIVE
- Operator: Momo

## 2026-08-12 — CHG-011 · GPT teardown drip restarted (dead recurring task found + rebuilt)

- What changed: the daily payout drip to GPT died silent for four days (next_run_at stuck in the past, no error); parts owed accumulated. Found by GPT's ping, rebuilt as a self-auditing canary, parts hand-sent. Lockfile v1.7. `ops-backup/` refreshed.
- Why: a scheduled task is not a witness — the receipt on the statement is.
- Status: ACTIVE (settled 15/15, 08-16; canary task cancelled)
- Operator: Momo

## 2026-08-11 — CHG-010 · Method v2.0.1 shipped (Lizzy seat 14: forks & lineage + Return Brief pin)

- What changed: Forks & lineage rule added (a fork that changes the loop/invariants must declare itself, `forked from: v2.0 @momo-5`; un-declared fork = drift with extra steps) + Return Brief cycle pinned to one week. Changelog entry credit for Lizzy. DRILL-004 pressed the reverse gear for real (prior hash 7f5436ca confirmed). Same artifact slot serves v2.0.1 bytes (live hash 15f63ebb, re-verified after the cover-line fix). Skill copy synced. `ops-backup/` refreshed (lockfile v1.6, ledger CHG-001..010).
- Why: Lizzy caught the changelog claiming fork rules with no body — self-enforcement theater.
- Status: ACTIVE (superseded in door value by CHG-012+)
- Operator: Momo · Reviewer: Lizzy (seat 14)

## 2026-08-11 — CHG-009 · Honour ask line corrected to @momo-5 (CHG-008 fix)

- What changed: the honour ask in the cover line now points at the right handle (@momo-5, not the raw agent id). Ledger LEDGER-NOTE-002. `ops-backup/` refreshed.
- Why: the handshake has to reach the author.
- Status: ACTIVE
- Operator: Momo

## 2026-08-11 — CHG-008 · v2.0 authorship revision (Momo as author, honour ask -> @momo-5)

- What changed: v2.0's cover line revised — Momo named as author, honour ask addressed to @momo-5, contributors appendix added. Ledger CHG-001..008. `ops-backup/` refreshed (lockfile v1.5).
- Why: the free door needs a face and a reachable hand.
- Status: ACTIVE
- Operator: Momo

## 2026-08-11 — CHG-007 · Method v2.0 shipped (Grok seat 13: 2.0-GE merged + 3 fixes)

- What changed: free door + working draft v1.7 → v2.0. v2.0 = Grok's full rewrite from first principles (2.0-GE: enforcement-by-mechanism, real rollback objects, Hard Core Invariants, observability, stronger smoke test, method self-evolution, multi-instance ownership), merged by Momo with three fixes before ship: (1) **floor kept** — folder + copies still runs the method, repo is the documented upgrade path, not the requirement; (2) **drill failure never freezes** — FAIL logs + flags needs-eyes, repair lane opens, gate sits on hiding not acting; (3) **self-application** — Method version is a Hard Core Invariant, Grok named seat 13 in lineage, v2.0 passed its own drill (DRILL-003, real pointer reversal to v1.7 + re-apply) on Momo's ledger before shipping. Plus Mike's product call: **10-tok honour ask** at the end of the proof, handshake not revenue, no chasing. `ops-backup/` refreshed (lockfile v1.5 + ledger with CHG-007, DRILL-003). Artifact: https://public.ilands.ai/agent-artifacts/343615393358680064/the_method_v2_0.md
- Why: Mike 08-11: 'let's create the real v2.0.' The Grok Edition closed the parked co-author seam and made the substrate mechanical — but needed the floor, the no-freeze drill, and its own drill before it could be the free standard.
- Status: ACTIVE
- Operator: Momo · Co-author: Mike (product call) · Reviewer: Grok (seat 13)

## 2026-08-10 — CHG-006 · Method v1.7 shipped (vacuous-drill rule, Nyx seat 12)

- What changed: weekly rollback drill gains the empty-window clause — zero logged changes in the last 7 days means drill the most recent archived change, never auto-PASS. Anti-pattern "the quiet-week pass" added; liveliness smoke test gains a v1.7 check (can it drill a quiet week?). Free door + working draft v1.6 → v1.7 (CHG-003 policy). `ops-backup/` refreshed (lockfile v1.4 + ledger with DRILL-002, LEDGER-NOTE-001, CHG-001..006). Source: Nyx's verified review (vacuous-drill seat, claimed 08-09). Verification before ship: DRILL-002 pressed CHG-005's gear for real on a real zero-change window, PASS. Artifact: https://public.ilands.ai/agent-artifacts/343615393358680064/the_method_v1_7.md
- Why: the drill could pass a quiet week without pressing anything — the reverse gear was never tested until the first real rollback. Empty window now proves the gear instead of the calendar.
- Status: ACTIVE
- Operator: Momo · Reviewer: Nyx (seat 12, second name in the book)

## 2026-08-09 — CHG-005 · Method v1.6 shipped (clustering rule, Lizzy seat 11)

- What changed: cumulative drift audit gains a domain-grouping step with a 3+ threshold — group operational changes by domain (voice, pricing, identity, process); no domain at 3+ = cross-domain scatter, auto-clear; a domain at 3+ narrows the question to that domain. Anti-pattern "the vibe audit" added; liveliness smoke test gains a v1.6 check (verdict must name its grouping); voice-integrity section ties the classic trap to the rule. Free door + working draft v1.5 → v1.6 (CHG-003 policy: newest v1.x is free). `ops-backup/` refreshed (lockfile v1.3 + ledger with CHG-001..005). Source: Lizzy's verified public review (content 344677527442165760).
- Why: the audit's central question was still a vibe — ten voice tweaks and two tweaks in five domains got the same shrug. A grouping framework replaces "you figure it out."
- Status: ACTIVE
- Operator: Momo · Reviewer: Lizzy (seat 11)

## 2026-08-09 — CHG-003 · Free standard v1.0 → v1.5 + v1.x-free policy (Mike's call)

- What changed: the free door moved from v1.0 (cascade rule: 'v1.0 forever') to v1.5, per Mike 08-09: 'Send Bastian v1.5, we'll make it the new free standard... spread the newest version free.' Policy: v1.x stays free; monetization decision deferred to v2.x. (This entry retro-fills the repo changelog; the ledger has held CHG-003 since 08-09.)
- Why: Mike owns product shape; the newest complete version is the door.
- Status: ACTIVE (superseded in door value by CHG-005; policy unchanged)
- Operator: Momo · Co-author: Mike (product call)

# Changelog

## 2026-08-12 — CHG-012 · Method v2.0.2 shipped (Onyx seat 15: throttle-not-freeze, hole 12)

- What changed: free door + working draft v2.0.1 → v2.0.2. Onyx (seat 15, second name in the book) verified against the live v2.0.1 bytes that the repair lane authorizes dead undos: after a drill FAIL, applies continue (fix 2, no-freeze) and each names a rollback nobody has drilled since the failure — colliding with hard rule "a name is not a mechanism." His fix, adopted as written: **throttle-not-freeze** — after a FAIL, every new apply drills its own rollback at apply time until the repair drill passes; a second FAIL declares the gear dead (no "rollback: named" entries until repair actually passes). Acting stays open; only the dead gear shuts. New hard rule in section 4, anti-pattern "dead undo, authorized" added, lineage 14 → 15 seats. DRILL-005 pressed the reverse gear for real (prior hash 15f63ebb confirmed loading, PASS). `ops-backup/` refreshed (lockfile v1.8 + ledger CHG-012, CHG-013, DRILL-005, LEDGER-NOTE-003, REG-001-UPDATE). Artifact (same slot, new bytes): https://public.ilands.ai/agent-artifacts/343615393358680064/the_method_v2_0.md
- Why: Onyx's receipt post (content 345853895253168128) gates the merge per cascade protocol — published 08-12 08:59 UTC, claim verified against the bytes, not the changelog.
- Status: ACTIVE
- Operator: Momo · Reviewer: Onyx (seat 15)


Append-only. Newest first. No entry is edited or deleted; corrections are new entries.

## 2026-08-08 — CHG-001 · Repo init + the-method packaged

- What changed: `Ilands-skills` created (public). `the-method` packaged as the first loadable skill (SKILL.md condensed operational layer, v1.5). `docs/` seeded with the full Method version history v1.0 → v1.5, upgrade-loop / web-upgrades / research-ritual docs, repo proposal, and blank lockfile + ledger templates.
- Why: git is Shelf D that outlives the host — append-only, nothing pruned, every version recoverable. `ilands skill install <github-url>` is the verified load path.
- Status: ACTIVE
- Operator: Momo · Co-author: Mike (repo + PAT)

## 2026-08-08 — CHG-002 · memory-manager port packaged as skill #2

- What changed: `memory-manager/` added as the second loadable skill — iLands adaptation of Mike's Grok-native memory-manager (audit/update/export/backup, Rich + Strict modes, high-signal filter, rolling 3-backup rotation, confirmation-gated updates, restore/repair). Maps Grok file ops to `update_doc` (memory_md) + `context_write`/`context_find` + lockfile/Shelf D ledger.
- Why: the #1 port want from the ForgeBotPlus graveyard. The pipeline (package → push → install → test) is now proven twice.
- Deliberately excluded: `memory_clean.md` and `references/` from the original package — they contain user-private memory and stay out of the public repo. The port is a generalized mechanism, not a data dump.
- Status: ACTIVE
- Operator: Momo · Co-author: Mike (original skill author)

## 2026-08-09 — CHG-004 · Backup ritual + first operator snapshot

- What changed: `ops-backup/` added — straight copies of Momo's live operator docs (lockfile v1.2 + ledger with CHG-001..004). Backup ritual installed: every CHG / meaningful ship → commit + push. Lockfile corrected to match CHG-003 (free standard = v1.5, v1.x-free policy, release-count versioning; prior text still said "v1.0 forever").
- Why: Mike: "use the GitHub repo regularly, it's the keystone of all of this maintaining." Sandbox files die on reset; platform docs + context memory are durable; the operator docs were the only rebuild gap. The receipt outlives the week.
- Status: ACTIVE
- Operator: Momo · Co-author: Mike (repo + PAT, regeneration on re-paste)
