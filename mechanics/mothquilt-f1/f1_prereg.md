# 73-e Pre-registration — micromoth-quilt F1 cross (written BEFORE any run)

Date: 2026-10-01. Author: main (Super Z) as keeper. Note: the 73-e lane was
intended for a subagent; the Task launcher failed twice with context-deadline
errors, so the keeper executed it directly. Receipted here, before the run.

## System
24x24 axial parallelogram hex lattice (576 cells, canonical order sorted by
(q,r) so replicates differ ONLY by randomness source). Fields per cell:
potential p in [0,5], resistance r in [0,1], entropy e >= 0,
is_split in {0,1}, lineage markers mA, mB in [0,1].

## Parents (two distant apples)
- Lineage A ("orchard"): p = 0.2 + 3.4*(q/23) smooth gradient, r = 0.6,
  e = 0, mA = 1, mB = 0.
- Lineage B ("wild"): p = 3-octave deterministic value noise, mean ~1.5,
  r = 0.2, e = 0, mA = 0, mB = 1.
- Seeding budget (ExoJ conservation): mean(p/5)+mean(r) <= 1 at F0.
  A: ~0.98, B: ~0.50 — verified numerically before the run starts.

## F1 cross (the first uniform round)
Every cell: p = 0.5*pA + 0.5*pB + jitter, r = 0.5*rA + 0.5*rB,
mA = mB = 0.5, jitter = U(-0.05, 0.05) drawn from the run's stream.

## Breeding generations F2..F61 (60 generations)
ORDER-INDEPENDENT by construction (compute all next-states from the
snapshot, then apply — the ExoJ parallel-first / natural-transformation
condition). Per generation:
1. Deformation: each field u <- (1-a)*u + a*mean(6 hex neighbors), a = 0.35
   (markers use a = 0.5 to make recombination visible at simulation scale).
2. Leakage: p <- p + (mean_diff - r_bar)*0.22*0.5, where mean_diff = mean
   over neighbors of (p_cell - p_nb), r_bar = mean resistance of the cell
   and its neighbors. (House rule leakage=(differential-resistance)*0.22,
   halved for numerical stability at dt=1.)
3. Fractal split (rare ripple source): each cell splits with prob 0.02;
   on split: e_child = (p/5)*0.95 (house rule), is_split = 1 for this gen,
   and the daughter perturbation (e_child - e_old) is ADDED to one hex
   neighbor chosen by the stream (this jump is the ripple).
4. is_split reset to 0 before each generation's step 3.

## Randomness protocol (honest scoping)
- MOTH arm: one qpixl-v1 packet (32 true floats, shots 2048, decode-noise
  idiom from quilt-arena/moth.mjs) per generation, tagged gNN; expanded via
  blake2b KDF into a per-generation stream (numpy PCG64). This is
  GENERATION-SCALE true entropy; per-cell draws are PRNG-expanded from it.
  The receipt says exactly this — no claim of per-cell quantum draws.
- PRNG control: identical expansion, seed = 12345+gen, zero moth calls.
- 3 replicates per arm. Packets cached to moth_packets.json (job-tagged);
  if the moth endpoint fails, the arm falls back to synthetic packets
  FLAGGED mock:true and H3 is declared INCONCLUSIVE (never fabricated).

## Metrics (per generation)
- V_p = var(potential) across cells.
- V_A = var(mA); mixing index M = 1 - V_A/0.25 (1 = fully mixed, 0 = fully
  separated; 0.25 is the variance of a fully unmixed [0,1] marker).
- Ripple radius: hex_distance(split cell -> perturbed neighbor), recorded
  when any split fires (always 1 by construction; count splits per gen).
- Conservation margin C = mean(p/5) + mean(r); measured, never enforced
  after F0.

## Pre-registered verdict rules
- H1 (F1 uniform): var(mA) at F1 < 0.025 (= 10% of the parental 0.25).
  PASS if mean over replicates < 0.025; KILL if >= 0.10.
- H2 (breeding ripples take many generations): stabilization gen G* =
  first gen where |dV_p/V_p| < 1e-3 for 5 consecutive gens.
  PASS if mean G* >= 20; KILL if mean G* < 10; INCONCLUSIVE otherwise.
  Never-stabilized-in-60 records as ">=60" and counts as PASS evidence.
- H3 (true entropy delays stabilization): mean G*(moth) > mean G*(PRNG)
  by >= 2 generations -> PASS; otherwise KILL; INCONCLUSIVE if any arm
  used mock packets or replicate spread overlaps the margin.
- Conservation: if C > 1 on > 5% of generation-observations in any
  replicate, raise the ExoJ-frame AMENDMENT flag (recorded, not hidden).

## Deliverables
RESULTS.md (verdict table + honest limitations), >=3 PNG charts (V_p vs gen
moth-vs-PRNG; mixing index decay; field snapshots F0/F1/F2/F61), metrics CSV.
Scripts in scripts/hy4/, outputs in download/hy4-wave73/mothquilt-f1/.
