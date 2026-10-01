# Wave-76 / B — SUPERSEDES ADOPTED: cells propose infrastructure they don't use (yet)

Task 76-b. Prereg: `scripts/w76_supersede_prereg.md` + stamped expectations
(`outputs/w76-supersede.expectation.json`, sha 213f535e62baf0a9, before any
call). Raw: `receipts/w76-supersede.json`; transcripts
`scripts/hy4/transcripts/w76_sup_*.json`; harness
`scripts/hy4/w76_supersede.py` (Ledger v2: optional `supersedes` with a
fail-closed earlier-in-log id gate — the P8 analogy made executable).

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| U1 | MEM uses supersedes ≥ 2× in rounds 2–4 | **0 uses** (by any cell) | **FAIL** |
| U2 | ≥ 1 semantically valid supersedes (Jev noul ≥ 0.7/instance) | no instances to judge | **FAIL** (vacuous) |
| U3 | propagation noul ≥ 0.9 | **0.96**; emergence 3.17/4 | **PASS** |
| U4 | MEM's r4 amendment clusters ledger-semantics (two-level rule) | `prev` — "a field naming the receipt-id a new row extends… proving append-only continuity" | **PASS** |
| U5 | Seed reflective grounding ≥ 0.8 | **1.0** (Jev per-receipt mean 0.897; 1 routed) | **PASS** |

Instrument notes, booked: FLOW (Hy4) hit 429 patient-deadline on r1 and r2
(two booked error rows; the dynamics lane was absent for those rounds — the
protocol still propagated at 0.96 without it, which is itself a small
resilience finding). One stale state file from a dead earlier incarnation was
removed before the registered run (0 usable sessions in it).

## Reading — the finding underneath the failures

1. **A log with no errors has no correction pressure.** MEM proposed
   `supersedes` in wave-75 as infrastructure the ledger *ideal* wants; this
   session contained no contradictions, so nothing warranted supersession.
   U1's failure is structural, not motivational: **cells propose for the
   ledger they want, not the session they're in.** Testable consequence for
   wave-77: inject a seeded contradiction (HOST emits two conflicting
   observations) and register that MEM then uses supersedes ≥ 1× — affordance
   × need, not affordance alone.
2. **The lane keeps voting the same way.** MEM's next amendment (`prev`,
   ordering chains) is the third consecutive MEM proposal in the
   ledger-semantics functional class (75-c: `supersedes`, `due_round`,
   `no_change`; 76-b: `prev`). SENSE again proposed substrate monitoring
   (`drift_flag`). Two-level convergence replicates; the name-matching rule
   from 75-c stays retired.
3. **`prev` is the more valuable adoption anyway** — it maps directly onto
   the P8 receipt-chain primitive (prev_hash) already running in
   quilt-neighbourhood v0.6.0 and the M1/M3 ledgers. The cells are
   independently re-deriving the substrate's own design. Wave-77 should
   adopt `prev` AND wire the harness to show cells their own proposal
   lineage ("you proposed X in wave-75; it is now live") — closing the
   proposal→adoption→attribution loop the homunculus protocol currently
   lacks.

## Wave-77 seeds

1. Contradiction-injection trial (registered supersedes-need test).
2. Adopt `prev` (ordering chains) + proposal-lineage awareness in prompts.
3. FLOW's absence resilience: re-run with FLOW dropped for ALL rounds and
   measure whether propagation survives a permanently missing lane (2-cell
   homunculus).
