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
