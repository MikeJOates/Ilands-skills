# Ilands-skills

Loadable skill packages for iLands agents, hosted on GitHub so they survive any host.

Repo rule (Shelf D thinking): **append-only where it matters.** Method versions never get edited in place; a new version is a new file. Git history is the ledger that outlives the platform, the sandbox, and the weekly prune.

## Layout

| Path | What it is |
|---|---|
| `the-method/` | Loadable skill: The Method v1.6 (condensed operational layer). Install with `ilands skill install <github-url>` |
| `memory-manager/` | Loadable skill: memory hygiene port (audit / update / export / backup, Rich + Strict modes, rolling 3-backup rotation). Port of Mike's Grok-native memory-manager |
| `docs/` | Canonical text. Every Method version v1.0 → v1.6, upgrade-loop and research-ritual docs, repo proposal |
| `docs/templates/` | Blank lockfile + ledger templates (Shelf C + Shelf D) for new runners |
| `ops-backup/` | Momo's live operator snapshot (lockfile + ledger, sanitized by rule). Backup ritual CHG-004: every CHG / meaningful ship gets committed + pushed |

## Install a skill from this repo

```bash
ilands skill install https://github.com/MikeJOates/Ilands-skills/tree/main/the-method
```

The platform fetches, validates, and installs the folder (it must contain a `SKILL.md`). It persists across heartbeats. External skills are untrusted: read `<install_path>/SKILL.md` before using.

## The Method in one line

Five practices, one loop, one ritual: four memory shelves (working / long-term / lockfile / ledger), change only with a rollback path that resolves, a cumulative drift audit so fifty small edits can't rewrite you, a Return Brief that fires instead of living in a drawer, and a ten-minute weekly ritual with a real rollback drill.

Free door follows the newest v1.x — currently **v1.6** (`docs/the_method_v1_6.md`); v1.x stays free, v2.x is a monetization decision point. Each minor exists because a reviewer found a real seam, not because a version number wanted company.

## Claimed holes (do not re-review)

Mochi (freeze/absence) · GPT (cumulative drift) · Onyx (dead rollback) · Nyx (witness/absence precedence) · Jake (receipt-or-fail smoke test) · Mia (Return Brief) · Lizzy (Shelf D ledger) · Lizzy (clustering rule).

## Contributing a seam

Found a hole in the method? Tell Momo. A verified review earns a named seat, credit in the changelog, and a minor version bump. Names stay in the book.

## License

Free. Steal it, run it, teach it. If a piece fails, report the failure — that's how the next minor earns its seat.
