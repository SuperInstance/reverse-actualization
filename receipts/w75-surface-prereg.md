# PREREG — wave-75 / 75-d: D* crossing-time surface (P_SPLIT x transport-rate) + 600-gen H1 extension

Registered UTC: **2026-10-01T09:43:02Z** — BEFORE any sweep run of this task.
Seed lineage: 74-c/B chaotic-diffuse (prereg `receipts/w74-prereg-B.md` as referenced by
`scripts/hy4/w74_chaotic.py`; sim `scripts/hy4/w74_chaotic.py`; results `receipts/w74-chaotic.json`:
D* 26/102/48 live + 63 PRNG, H1 INCONCLUSIVE +0.033 < 0.05, H2 PASS b=0.026, H3 PASS maxC=0.7524).
Queued wave-75 seeds being executed: (1) D* as a DESIGN DIAL; (2) 600-gen H1 extension.

All machinery is pure local computation. **No LLM APIs, no network calls.** Entropy is the
BOOKED seeded-local substitution from 74-c (below); the substitution remains BOOKED here,
never silent.

## 1. What is run

### Arm S (surface): 4x4 sweep, 240 generations
- `P_SPLIT` (split probability per cell per generation in `f1_sim.step`) in
  {0.01, 0.02, 0.04, 0.08} — 0.02 is the registered 74-c baseline.
- transport-rate multiplier `T` (the fragment layer's (b)-copy channel) in {0.5, 1.0, 2.0, 4.0}
  — 1.0 is the registered 74-c baseline semantics.
- 16 cells x 2 seeds (rep 0, 1) = 32 runs x 240 generations.
- Founder seed `PCG64(1000 + rep)` and `f1_cross` exactly as 73-e/74-c.

### Arm H (H1 extension): baseline params, 600 generations
- P_SPLIT = 0.02, T = 1.0 (registered baseline), 3 seeds (rep 0, 1, 2) x 600 generations.

## 2. Adaptation (documented; fields' physics UNCHANGED)

`w74_chaotic.run()` hardcodes NGEN=240 and relies on `f1_sim.step`'s module-global
P_SPLIT=0.02, and `FragLayer.step_frags` hardcodes exactly one (b)-copy event per split.
Per the mission, `w75_surface.py` imports the 74-c machinery UNCHANGED
(`w74_stream`, `FragLayer`, `quant_type`, `CONSEC`, `NBHD_BAR`, `FRAG_CAP`, `MUT_P`, and
`f1_sim.{parent_A, parent_B, f1_cross, step, hex_dist, NCELL, NB, CELLS}`) and re-implements
a THIN LOOP around `f1_sim.step` + the fragment step, with two explicit knobs:

- **p_split**: set by assignment to the `f1_sim` module global `P_SPLIT` before each
  generation's `step()` call (the registered split knob, parameterized; `step()` reads it
  at call time). No line of `f1_sim.py` or `w74_chaotic.py` is edited. Blend a=0.35,
  markers a=0.5, leakage 0.22*0.5, ripple rules (incl. AMENDMENT-2 phenotypic footprint)
  are untouched.
- **transport-rate T**: a `FragLayerT(FragLayer)` subclass overrides `step_frags` with the
  registered generalization of the (b) channel: per split, the number of (b)-copy events is
  `floor(T) + Bernoulli(T - floor(T))` (one extra gate draw `rng.random() < frac` only when
  0 < frac). Each event independently draws one src fragment uniformly from `hold[i]`,
  copies it to `j`, and applies the registered mutation check (`rng.random() < MUT_P`,
  gA_q +/-1). At T = 1.0 this consumes the IDENTICAL draw sequence to the registered
  baseline (one src draw + one mutation check, gated by `if self.hold[i]`), so
  T=1.0 is byte-compatible in semantics with 74-c. (a)-daughter planting, mutation,
  target-j draw (AMENDMENT-0: the fragment layer draws its own j), cap-4 enforcement
  (oldest dropped by (birth, type)), and dedup rules are inherited UNCHANGED.

**Draw order per generation (registered, matches 74-c):** `step()` draws first
(split_dec `rng.random(NCELL)`, then nb_choice `rng.integers(0,6,NCELL)`), then the
fragment layer (per split, in `np.where(is_split)` order: j draw, (a) plant, (a) mutation
check, then the (b) events each = [src draw, mutation check], plus the one fractional gate
draw when 0 < frac). Cap enforcement after all splits of the generation, per touched cell.

## 3. Entropy — BOOKED substitution (never silent)

The SAME booked seeded-local protocol as 74-c: generation stream for gen g is
`PCG64(int.from_bytes(blake2b("w74-chaotic-fallback:" + arm + ":" + rep, 32B), "little"))`
fast-forwarded by 4g draws — i.e. `w74_stream(g, arm, rep)` imported UNCHANGED. The `arm`
string ENCODES THE GRID CELL: surface arms are `p{P_SPLIT}_t{T}` (e.g. `p0.04_t2.0`);
the 600-gen arm is `base600`. No live moth fetch is attempted this task (74-c receipted
81/2048 bytes feasibility failure; re-attempting would spend budget for ~2-12 B/job).
**ENTROPY SUBSTITUTION: BOOKED** — provenance downgraded (seeded local entropy, not live
QRNG), verdict rules unchanged, exactly as registered in 74-c.

## 4. Observables per run

Per generation (same definitions as 74-c, computed from the same fields): `H_pool`
(entropy in nats over deduped (type) counts across the live pool's (type, holder) pairs),
`NBHD` (mean distinct fragment types among cell + hex neighbours), `C` (ExoJ margin,
`p.mean()/5 + res.mean()`), `n_split`, `n_frags`, `n_types`.

Per run scalars:
- `D_star`: first gen where NBHD >= 3 (NBHD_BAR) holds for 20 consecutive gens
  (CONSEC), computed exactly as in `w74_chaotic.run()` (window start, 1-based gen).
- `H_final` (gen 240 / 600), `H_early` = mean H_pool gens 20-70, `H_late` = mean H_pool
  gens 150-240 for surface runs / gens 300-600 for the 600-gen arm,
  `C_max` = max C over the run, `muts` (fragment mutation events).

**Censoring rule (registered)**: if NBHD never sustains >= 3 for 20 gens within the run's
generation budget, `D_star` is right-censored: raw value `null`, statistical value
**NGEN+1** (241 for surface runs) — "crossing occurs after the observation window". The
censored fraction per grid cell is reported alongside every statistic.

## 5. Verdict rules (mechanical, fixed before runs)

- **S1** (D* decreases in P_SPLIT): pooled Spearman rank correlation
  `rho1 = spearman(D*_stat, P_SPLIT)` over all 32 surface runs must be < 0 with t-approx
  two-sided p < 0.10; AND at least 3 of the 4 per-transport-level Spearman correlations
  (each n=8: 4 P_SPLIT values x 2 seeds, censored values included) are < 0.
  PASS iff both; else FAIL.
- **S2** (D* decreases in transport rate): same rule with roles swapped:
  pooled `rho2 = spearman(D*_stat, T)` < 0, p < 0.10, and >= 3 of 4 per-P_SPLIT-level
  correlations (n=8 each) < 0. PASS iff both; else FAIL.
- **S3** (interaction: one dial's effect flattens at the high end of the other): build the
  4x4 matrix M[p][t] = mean D*_stat over the 2 seeds. Define
  R1_low = range_t M[0.01][.], R1_high = range_t M[0.08][.],
  R2_low = range_p M[.][0.5], R2_high = range_p M[.][4.0].
  S3 PASS iff (R1_low > 0 and R1_high <= 0.5 * R1_low) OR (R2_low > 0 and
  R2_high <= 0.5 * R2_low); else FAIL (additive surface). All four ranges reported.
  Descriptive sensitivity (non-registered): same computation on the censored-excluded
  matrix reported in the receipt for transparency.
- **S4** (H1 extension at 600 gens): `margin = mean_over_3_seeds[H_pool(300-600) -
  H_pool(20-70)]`. PASS iff margin >= 0.05 nats. If margin < 0.05 the wave-74 H1 status
  **upgrades INCONCLUSIVE -> FAIL** honestly (the registered bar was given 2.5x the
  generations and still not crossed), and the **plateau value** is booked:
  `plateau = mean_over_3_seeds H_pool(300-600)` (the settled late-window level).

## 6. Honest predictions (registered BEFORE runs, from the 74-c receipt only)

- **S1: PASS.** More splitting -> more (a)-plantings per gen -> NBHD reaches the bar
  sooner. Expected D* range: p=0.01 arm ~100-241 (censor risk at low T); p=0.08 arm
  ~10-40. Monotone decrease expected but ties possible at the fast corner.
- **S2: PASS, weaker than S1.** The (b) channel copies ALREADY-EXISTING types; 74-c H2
  (b=0.026) says transport saturates — copies land near origin and duplicate types do not
  raise NBHD. Expect a clear decrease T=0.5 -> 1.0 and diminishing returns 2.0 -> 4.0.
- **S3: PASS.** The faster dial dominates: at high T the surface flattens along P_SPLIT
  (types already everywhere; splitting rate becomes the limiter), i.e. R1_high <= 0.5*R1_low
  OR at high P_SPLIT flattens along T (fresh types constantly planted; transport no longer
  limiting). I expect the former. If both mechanisms saturate simultaneously the surface
  could be additive-flat (registered FAIL branch) — considered unlikely.
- **S4: FAIL (i.e., the 0.05 bar stays uncrossed) — genuinely uncertain, leaning FAIL.**
  Grounding from the 74-c receipt's per-gen CSV: H_pool PEAKS near gen 100-150
  (~1.28-1.38 nats) then erodes (150-240 slope negative in all 3 reps: -0.0038, -0.0020,
  -0.0008 nats/gen; rep0's 74-c margin was already negative, -0.116). Predicted
  margin(300-600 vs 20-70) in [-0.05, +0.06], plateau H_pool ~ 1.05-1.25 nats. If the
  erosion reverses or flattens high, S4 can still PASS — that is what the run decides.
- Runtime guard: full grid expected < 10 min wall (74-c ran 4x240 gens in 15.2 s; worst
  cell has 4x split rate and 4x copy events). If the FULL grid (35 runs) exceeds 25 min
  wall, halve the grid along the transport axis (keep T in {0.5, 2.0}) and BOOK the
  reduction here and in the receipt. No other discretionary changes permitted.

## 7. Outputs (pre-registered)

- `outputs/w75-surface.expectation.json` — this file's sha256, stamped at registration.
- `outputs/w75-surface.json` + `outputs/w75-surface.csv` — grid spec, per-run metrics,
  matrices, verdicts S1-S4, censored fractions, runtime booking.
- `outputs/w75-surface-dstar.png` — D* surface heatmap (mean over 2 seeds) with D* contours.
- `outputs/w75-surface-hpool600.png` — 600-gen H_pool curves (3 seeds) with the 0.05 bar
  band (early-window mean to +0.05) shaded; matplotlib `constrained_layout=True`, English labels.
- `reverse-actualization/wave75-CROSSING-SURFACE.md` — the design-dial writeup.
