# Wave-74 / A — HOMUNCULUS RECEIPT-TRADING (the rung-10 finding, executable tonight)

Task 74-c, sub-task A. Prereg: `receipts/w74-prereg-A.md` (sha256 ef8adaefc61793ac,
stamped before any run). Raw receipt: `outputs/w74-homunculus.json` (also
`receipts/w74-homunculus.json` this repo). Transcript set:
`scripts/hy4/transcripts/w74_hunc_*.json` (13 sessions).

## What was built

Three persistent cells traded JSON receipts for 4 rounds — the wave-73 ladder's
rung-10 ("tonight: the homunculus") finding made executable:

| Cell | Model | Lane |
|------|-------|------|
| FLOW | tencent/Hy4-preview (featured) | lattice dynamics: potentials, leakage, splits, ripples |
| MEM  | XiaomiMiMo/MiMo-V2.6-Flash | folds history: ledger, receipts, append-only proofs |
| SENSE | inclusionAI/Ling-3.0-flash | watches the entropy source (the moth) |

Protocol per round: each cell receives its cumulative inbox and emits 1–2
receipts (`type` ∈ observation/question/commitment) addressed to named
recipients, in one fresh session per cell per round (cumulative context).
A live mothquantum entropy feed seeded SENSE's observations (provenance:
`live`). 25 receipts total (7 commitments), 21 propagation edges extracted,
1 parse failure (booked per registered rule, not retried into compliance).

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| P1 | Cross-cell propagation observable by round 3 | 5 shaped edges by r3 from 3 distinct source cells | **PASS** |
| P2 | Grounding noul ≥ 0.8 | Jev grounding = **0.39** | **FAIL** |
| P3 | Jev-vs-Seed agreement ≥ 0.7 on both nouls | 0.685 | **FAIL** (marginal) |
| — | Propagation noul (Jev) | 0.98; emergence score 3.6/4 ("multiple propagations with re-use") | descriptive |

## The finding that matters

The P2/P3 failure is **not noise — it is the reflex/reflect signature again**,
third independent sighting this wave (see `studies/JEV-CALIBRATION-74.md` and
74-b's judge tables):

- Jev (System One) reads the receipt log as *salience*: propagation 0.98
  (clear cross-cell causation) but grounding 0.39 (it distrusts what it cannot
  re-verify locally).
- Seed-2.0-mini (System Two, full log in context) scores propagation 1.0 AND
  grounding 1.0 — it traces every receipt to its cited ancestors.

Design consequence queued for wave-75: **grounding checks are reflective work;
do not assign them to the reflex layer.** Jev's job is the cheap 0.98-class
propagation flag; when its noul lands in the boundary band, escalate to a
reflective auditor with receipt-citation tooling. This is the same routing
rule 74-a derived from the 10-edge calibration, now replicated on a live
multi-agent protocol.

## Cost + provenance

- deepinfra: 34,031 tokens total (≈ $0.004; Seed audit $0.0022 with cache hits).
- TypeSafe: 1 judging call (2 noul + 1 score over the full receipt log).
- Instrument notes: Hy4 flapped 429 on the first incarnation's FLOW r1
  (booked honestly, recovered in chunk 2); patient_deadline harness fix
  receipted in `di_client.py`.

## Wave-75 seeds

1. Run the same protocol 3 replicates × 4 rounds with the grounding rule
   routed reflectively; P2 restated as "reflective-auditor grounding ≥ 0.8".
2. Let cells negotiate the receipt schema (the rung-10 "protocol modifies
   itself" criterion) — Jev watches for protocol-level emergence.
3. Feed SENSE the chaotic-diffuse H-pool curve (74-B) as its observation
   payload — the three lanes then share one measured substrate.
