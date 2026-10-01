# Wave-75 / C — HOMUNCULUS ROUND 2: grounding was a reflex artifact; the protocol is stable across replicates

Task 75-c. Prereg: `scripts/w75_hunc2_prereg.md` + stamped expectations
(`outputs/w75-hunc2.expectation.json`, sha f4dea8917553a9f4, registered before
any call). Raw: `receipts/w75-hunc2.json`; 36 session transcripts
`scripts/hy4/transcripts/w75_hunc2_*.json`. Harness: `scripts/hy4/w75_hunc2.py`
(imports the round-1 machinery UNCHANGED — Ledger, emissions validation,
personas, trace; adaptations: per-replicate ledger slices, schema-negotiation
turn, reflective routing).

## What changed vs round 1 (74-c/A)

1. **Grounding routed reflectively** — Jev still supplies per-receipt grounding
   nouls, but the registered bar moved to the reflective channel (Seed-2.0-mini
   full-log verdict), per the wave-74 diagnosis ("grounding checks are
   reflective work") and the 75-a router rule.
2. **Three replicates** of the full 4-round protocol, fresh sessions, distinct
   32-byte slices of the live 81-byte moth ledger per replicate (all three
   live — no substitution needed).
3. **SENSE reasons over a measured substrate**: its seed payload now carries
   the 74-c/B H_pool curve (D* 26/102/48; early/late means; slope 0.026).
4. **Schema negotiation** — round-4 extra turn: every cell proposes one schema
   amendment for its lane.

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| Q1 | reflective grounding ≥ 0.8 in ≥ 2/3 replicates | Seed full-log grounding **1.0 / 1.0 / 1.0** | **PASS** |
| Q2 | Jev propagation mean ≥ 0.9 | **0.963** (0.97/0.96/0.96) | **PASS** |
| Q3 | ≥ 1 schema amendment converges by name across cells | none repeated verbatim | **FAIL** (honest) |
| Q4 | Jev auto-accept rate ≥ 0.5 | **1.0** (0 routed — every per-receipt noul outside the band) | **PASS** |

Emergence scores 3.81 / 3.48 / 3.15 of 4; 36/36 sessions, **zero parse
failures** (round 1 needed two recovery chunks); ~96K deepinfra tokens (≈ $0.01
with cache hits); wall 50s of API time.

## Reading

1. **Q1 closes the wave-74 loop.** The same protocol, judged reflectively,
   grounds at 1.0 in every replicate. Round-1's 0.39 was the System One layer
   distrusting what it could not locally re-verify — the fourth and cleanest
   sighting of the reflex/reflect signature, now with the intervention
   (routing the check) confirming the diagnosis. **The routing rule is no
   longer a calibration curiosity; it is the registered interface contract
   between Jev and the reflective panel.**
2. **Q3's failure is lane-convergent, not name-convergent.** MEM — the ledger
   lane — independently proposed ledger-semantics fields in all three
   replicates (`supersedes`, `due_round`, `no_change`); SENSE proposed
   uncertainty-quantification fields (`confidence`, `entropy_delta`). The
   *function* converged along lane lines even though the names did not. The
   registered name-matching rule was too literal; wave-76 should register
   two-level convergence (name OR functional class) and let MEM's
   `supersedes` proposal — which maps directly onto the P8 reconciliation
   events already implemented in quilt-neighbourhood v0.6.0 — become the
   first cell-proposed schema change to be actually adopted by the harness.
3. **The protocol is now boring in the right ways**: zero parse failures,
   propagation ~0.96 everywhere, auto-accept 1.0. Round 1's drama (429
   flaps, repair turns) was infrastructure, not concept. What remains
   interesting is exactly Q3: the cells are ready to co-design their own
   protocol, and the host should let them.

## Wave-76 seeds

1. **Adopt MEM's `supersedes` field** in the harness Ledger (emit + validate +
   replay semantics via P8-style supersede events), re-run one replicate, and
   measure whether MEM's grounding/commitment behavior changes when its own
   proposal is live.
2. Two-level convergence rule for schema amendments (name OR functional
   class), pre-registered, n=3 replicates.
3. Give FLOW the D* surface dial (75-d) and ask it to *choose* a P_SPLIT for
   a target crossing time — the first cell to operate a design dial rather
   than watch one.
