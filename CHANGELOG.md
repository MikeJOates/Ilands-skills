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
