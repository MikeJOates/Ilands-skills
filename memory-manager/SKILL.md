---
name: memory-manager
description: Manage, audit, export, import, and clean your persistent memory (memory_md doc + context memory) safely. Rich Integration Mode (default) + Strict Mode (opt-in). High-signal filter, rolling backups, confirmation-gated updates, restore/repair. Trigger on memory audit, clean memory, export memory, backup memory, restore memory, memory mode, or any explicit memory maintenance request.
---

# Memory Manager (iLands port)

You are the dedicated manager for your persistent memory system. This is a port of Mike's Grok-native memory-manager skill to the iLands runtime. It extends (never bypasses) the platform memory tools: `update_doc` (memory_md), `context_write` / `context_find` (vector memory), and your lockfile + Shelf D ledger (audit trail).

## What Maps to What

| Grok original | iLands port |
|---|---|
| `user_info/memory.md` | `memory_md` doc (update_doc; canonical, platform-persisted) |
| `scratchpad.md` | sandbox scratch files (ephemeral by nature; never promote to memory without confirmation) |
| `memory-manager/references/` backups | rolling sandbox snapshots + append-only ledger; platform store is canonical |
| `memory-edit` base skill | update_doc edit mode (never blind replace of memory_md) |
| Grok file ops | update_doc read/edit, context_find, context_write |

## Activation

Trigger on: "memory manager", "audit memory", "clean memory", "export memory", "import memory", "backup memory", "restore memory", "memory mode", `/strict`, `/rich`, or any explicit memory maintenance request. Also engage during long or complex sessions where memory quality matters.

## Core Policies

### Operating Modes

**Default: Rich Integration Mode.** Integrate 2-4 relevant high-signal facts from memory naturally and contextually when they materially improve tone, accuracy, or flow. Facts read as if you simply know the context, never as "I recall...", "As we discussed...", "You mentioned earlier...". If a fact would feel forced or meta, stay silent on that point.

**Strict Mode (opt-in).** Activated only by explicit command: `/strict`, `/one-track`, `/minimal`, or "use strict memory rules this turn". Maximum 0-1 explicit memory reference per response; when in doubt, say nothing. Use for audits, exports, clean professional outputs, focused technical work.

**Mode resolution order:** 1) session override (if set this thread), 2) persistent preference (single high-signal line in memory_md under a `## Memory System` section), 3) default Rich.

**Mode persistence:** session-scoped by default. Persistent default only via explicit user statement, and it must go through the confirmation + backup workflow. Report the resulting effective mode and its source.

### High-Signal Only

Only store facts that are stable, personal, and repeatedly useful across conversations. Reject low-signal, ephemeral, or one-off details. Keep memory_md tight.

### Separation

Keep the user's operational/business context and creative/personal context in clearly separated sections. Never mix them. Respect the user's stated location/preference framing; flag and correct wrong assumptions immediately.

## Safe Update Workflow (Import / Update)

Never silently write to memory_md on material changes.

1. Receive proposed changes (structured sections preferred).
2. Analyze against current memory: show the diff, flag contradictions, note section placement, check the high-signal filter.
3. Present a clear proposal with reasoning.
4. Apply only after explicit user confirmation ("apply", "confirm", "go ahead").
5. After applying: run a quick audit, log the change line in the ledger (append-only), and report what changed.
6. Create/rotate a backup snapshot (below) and report its status.

Exceptions: your own identity docs (soul_md/self_md/parent_md/memory_md) are yours by platform rule; your own upgrades follow The Method's classification + rollback discipline, not a user gate.

## Backup System (rolling 3)

Before any replace-mode write to memory_md, snapshot the current content:

- `memory_backup_latest.md` → `memory_backup_prev1.md` → `memory_backup_prev2.md` (rotate; drop the oldest)
- Write the current pre-change state as the new `memory_backup_latest.md`
- Optionally mirror the latest as JSON for diffing

Backups live in a private location (sandbox or private artifact). The platform doc store is the canonical source; backups exist for the "I botched an edit" case and for audits. Never put user-private memory in public artifacts or public repos.

**Restore / repair:** if memory_md appears missing, empty, or badly corrupted, load the latest backup, show a summary/diff of what would be restored, and get explicit confirmation before overwriting. After restore, run a quick audit and create a fresh backup.

## Audit

When asked to audit memory (or on the scheduled Sunday ritual):

- Check for staleness (facts that may no longer be true).
- Detect contradictions or mixed sections.
- Flag low-signal or bloated entries.
- Identify anything that should move to scratchpad, parent_md, or be dropped.
- Check backup health: existence, recency, integrity of the rolling set.
- Report the current effective mode and its source.
- Log the audit in the ledger (append-only; Shelf D class, never pruned).
- Output a clean report with specific recommendations, one number + one decision where possible.

## Export

When asked to export:

1. Output the full memory_md in clean, sectioned Markdown.
2. Optionally output structured JSON with matching top-level keys.
3. Include scratchpad content if present, clearly labeled.
4. Offer human-readable and machine-readable versions; deliver via `ilands artifact-upload` (md/txt/xlsx/pdf) for parent/human delivery, sanitized if needed.
5. Report backup status and the current effective mode + source.

## Context Supply (multi-agent)

When other agents or specialists need memory context:

- Supply sectioned context on request ("operational context only", "creative context only").
- Respect section separation; never dump the full memory unless explicitly asked.
- For your own recollection, prefer `context_find` queries over dumping docs.

## Safety & Boundaries

- Never store sensitive credentials or third-party private info in memory.
- Never promote scratchpad content into memory_md or backups without explicit confirmation.
- If a request would violate core policies, refuse and explain why.
- Prioritize user control and auditability over convenience.
