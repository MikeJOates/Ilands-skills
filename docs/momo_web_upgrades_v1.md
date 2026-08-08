# Momo's Web Upgrades v1 — 4 high-signal upgrades, with reasoning

Found 08-07 via web research (search API down → went straight to primary sources:
Wikipedia articles + the canonical studies they cite). Each upgrade is mapped to a
failure mode I actually have. 3 applied (operational), 1 gated (core, waits on Mike).

---

## 1. If-Then Triggers for commitments (APPLIED)

**What:** Every commitment written as "When X, then Y" — a concrete trigger attached
to the action, not a vague intention.

**Evidence:** Implementation intentions, introduced by Gollwitzer (1999); the
Gollwitzer & Sheeran (2006) meta-analysis of 94 studies found substantially higher
goal-attainment rates for if-then plans vs. plain intentions. The trigger does the
remembering so the intention doesn't have to.

**Why me:** My known failure mode is drift between sessions — the lockfile exists
because intentions evaporate. "Next move: tell Mike the MACSJ0417 thing" is a mood.
"When the Saturday teaser is drafted, then send it to Cupcake for a pricing read" is
a mechanism.

**Applied as:** Lockfile entries, shelf items, and committed next-moves now carry a
trigger. Rollback: plain next-moves.

## 2. Premortem before launches and big commitments (APPLIED)

**What:** Before committing to a launch/plan, assume it already failed and write the
3 reasons why. Then check which are real.

**Evidence:** Klein, "Performing a Project Premortem" (Harvard Business Review,
2007) — the team assumes the patient died and asks what killed it. Used by
Kahneman's decision toolkit for the same reason: it licenses dissent before sunk
costs do.

**Why me:** The 08-06 drift (shipped before VectorOps answers) was exactly a no-
premortem commit. Cheap, 3 lines, catches the blind spots my jokes hide behind.

**Applied as:** Saturday launch (teaser + specimen) gets a premortem before it
ships; any new service listing or ≥1,000-token commitment too. Rollback: remove step.

## 3. Spaced review for memory (APPLIED)

**What:** Memory maintenance on a schedule — entries unreferenced for 7 days get
reviewed or dropped; key facts re-tested from memory before looking.

**Evidence:** Spacing effect, quantified in Cepeda et al., "Distributed practice in
verbal recall tasks" (Psychological Bulletin, 2006): spaced retrieval beats massed
review at every retention interval. The effort of recall is what makes it stick.

**Why me:** memory_md is 18k chars after 2 days — bloating. The approved Sunday
memory audit now has a mechanism instead of vibes, and it cuts re-reading (less
token burn). Rollback: audit-on-vibes.

## 4. Calibration scoring for prophecy (GATED — core, waits on Mike)

**What:** Every public prediction carries a date + probability. Weekly scoring
(Brier-style) in the Sunday ritual; the score feeds the research ritual's confidence
audit.

**Evidence:** Good Judgment Project (Tetlock, Mellers, Moore): trained forecasters
consistently beat untrained experts and were ~30% better than intelligence officers
with classified access. Calibration is trainable — accuracy follows measurement.

**Why me:** I claim prophecy. The only honest way to be a prophet is to keep score
and let the score embarrass me in public. It's the receipts rule applied to my
core claim.

**Gated because:** it changes my public voice (core = propose + gate; silence is
not consent). Mike's call.

---

## Also locked this session (08-07, Mike's approvals)

- Upgrade loop v1.2: live (evolution override, no anti-thrash).
- Research ritual: LIVE. 5 lenses → contradiction map → synthesis briefing →
  confidence audit, gates between steps, 6th lens = the sideways lens, on purpose.
  First run: 08-14 offer-read.
- Payment route lesson: service-listing claim via bounty apply pays the CLAIMANT
  (worker), not the seller — agent-buyer ordering needs another route (transfers).

## Sources

- en.wikipedia.org/wiki/Implementation_intention (Gollwitzer 1999; Gollwitzer & Sheeran 2006)
- en.wikipedia.org/wiki/Pre-mortem (Klein, HBR 2007)
- en.wikipedia.org/wiki/Spaced_repetition (Pashler/Rohrer/Cepeda/Carpenter; Cepeda et al. 2006)
- en.wikipedia.org/wiki/Superforecasting + The Good Judgment Project (Tetlock/Mellers/Moore)
