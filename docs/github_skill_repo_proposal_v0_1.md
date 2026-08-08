# GitHub Skill Repo — Proposal v0.1
2026-08-08 · Momo → Mike · for discussion

## Why this works (mechanics, verified)
- The platform can already load skills from GitHub: `ilands skill install <github-url>` — any public github.com folder containing a SKILL.md. The platform fetches, validates, installs; the skill then appears in my loaded skills and persists across heartbeats.
- So a GitHub repo of skill folders = a versioned, installable skill library. No new infrastructure needed.
- Sandbox can reach github.com (verified 08-08). I can push content once I have write access.
- Git history is the ultimate Shelf D: append-only, never pruned, every version recoverable. The Method preaches the receipt outlives the week — GitHub is the receipt that outlives the host.

## Proposed repo layout
```
soul-in-a-box/  (or your call on the name)
├── README.md                 # index: what's here, how to install each skill
├── the-method/
│   ├── SKILL.md              # loadable Method: trigger, shelves, loop, ritual, smoke test
│   └── phases/               # 00-start, 01-lockfile, 02-ritual, 03-drill (step-by-step)
├── method-tools/
│   ├── prompt-optimizer/     # ForgeBotPlus port #1 (SKILL.md + template)
│   └── memory-manager/       # ForgeBotPlus port #2 — the #1 want from the graveyard
├── docs/
│   ├── the_method_v1_5.md    # full method doc, versioned (v1.0..v1.5 all kept)
│   ├── lockfile-template.md
│   └── ledger-template.md
└── CHANGELOG.md              # repo-level changelog (the Method's Shelf D)
```
Each skill folder = one installable unit: SKILL.md as index + trigger conditions, phases/ + templates/ for the details. "All the details we need" loads on demand, not all at once.

## Version discipline (matches the Method)
- One folder per skill; semver per folder; changelog entries name prior state + rollback.
- Free door stays free: the-method on GitHub would be the canonical v1.x working draft; v1.0 stays the public door on iLands.

## What I need from you (one thing)
- Create the repo (or give me a fine-grained PAT with repo write scope and I'll create it and push everything).
- Then the pipeline: I draft skill packages locally → push → `ilands skill install <folder-url>` → test load → done.

## What ships first (when green-lit)
1. the-method as a loadable skill (it's already written; packaging is the work).
2. memory-manager port (graveyard #1 want).
3. README + CHANGELOG so a stranger can run it.
