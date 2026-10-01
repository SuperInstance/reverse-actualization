# Wave-75 / 75-d — THE CROSSING-TIME SURFACE: D* as a design dial + the 600-gen H1 extension

Task 75-d. Prereg: `scripts/w75_surface_prereg.md` (registered **2026-10-01T09:43:02Z**,
BEFORE any sweep run; stamped expectations `receipts/w75-surface.expectation.json`, prereg
sha256 `878799f04ebfdce4…`). Receipts: `receipts/w75-surface.json` + `receipts/w75-surface.csv`
(per-run) + `receipts/w75-surface-hpool600.csv` (per-gen H1 curves). Sim:
`scripts/w75_surface.py` (imports the 74-c chaotic machinery UNCHANGED — thin loop around
`f1_sim.step` + `FragLayerT` transport knob; fields' physics untouched). Charts:
`outputs/w75-surface-dstar.png`, `outputs/w75-surface-hpool600.png`.

## What was run

The founder's phrase — *“many many generations”* — became a number in 74-c (D\* = 26/102/48
at the single registered operating point). This task turned the two obvious knobs and
measured the whole dial:

- **Arm S (surface)**: P_SPLIT ∈ {0.01, 0.02, 0.04, 0.08} × transport-rate T ∈ {0.5, 1.0,
  2.0, 4.0} × 2 seeds × 240 gens = 32 runs, 2.35 min wall (guard was 25 min; no reduction,
  `grid_reduction_booked: false`). T generalizes the 74-c (b)-copy event: expected copies
  per split = T (floor + Bernoulli); T = 1.0 consumes the identical draw sequence to the
  registered baseline.
- **Arm H (H1 extension)**: baseline params (P_SPLIT = 0.02, T = 1.0), 3 seeds × 600 gens.
- Entropy: the BOOKED 74-c seeded-local protocol reused unchanged (`w74_stream`;
  `blake2b("w74-chaotic-fallback:"+arm+":"+rep)` → PCG64, arm encodes the grid cell);
  substitution stays BOOKED (no live moth fetch attempted — 74-c receipted 81/2048-byte
  infeasibility). Provenance downgraded, verdict rules unchanged.

## The surface (mean D* over 2 seeds; censored runs scored 241, count in parens)

| P_SPLIT \ T | 0.5 | 1.0 | 2.0 | 4.0 |
|---|---|---|---|---|
| 0.01 | 155 (1) | 93 | 138 | 64.5 |
| 0.02 | 142 (1) | **39** | 138.5 (1) | 72 |
| 0.04 | 19 | 23.5 | 21 | 13 |
| 0.08 | 14 | 12.5 | 9.5 | **8** |

**Uncensored D* range across the surface: 8 → 188 generations** — a >20x design span from
one octaved dial pair. 3/32 runs censored (all at low P_SPLIT). Baseline reference: the
measured cell (p=0.02, T=1.0 → D* 38/40) sits in the 74-c receipt's range (26/102/48 live
arms). Invariant worth an operator's attention: **max C = 0.7524 on every run of the
surface** — the ExoJ conservation band (≤0.80, flag at 0.75) holds at every point of the
dial; crossing time is tunable WITHOUT breaking the margin H3 guards.

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| S1 | D* decreases monotonically in P_SPLIT | pooled Spearman ρ = **−0.890** (n=32, p ≈ 9.7e-12); per-T-level ρ = −0.86/−0.98/−0.88/−0.88 (4/4 negative) | **PASS** |
| S2 | D* decreases in transport rate | pooled ρ = **−0.127** (n=32, p = 0.49); per-P_SPLIT-level ρ = −0.44/+0.05/−0.47/−0.65 (3/4 negative, pooled ns) | **FAIL** |
| S3 | Interaction: one dial's span halves at the high end of the other | R1: 90.5 → **6.0** (P_SPLIT span at T=0.5 vs T=4.0, 15x flattening); R2: 141 → **64** (T span at p=0.01 vs p=0.08, 2.2x) — both registered conditions hold | **PASS** |
| S4 | H_pool(300-600) − H_pool(20-70) ≥ 0.05 nats at 600 gens | margin = **−0.058** nats (per-seed −0.174 / −0.116 / +0.117); **plateau = 0.975 nats** | **FAIL** |

### Reading the dial

- **P_SPLIT is the dial that works.** Doubling split rate roughly halves crossing time
  (0.02→39, 0.04→~21, 0.08→~12 gens); halving it (0.01) pushes crossing to 65–188+ gens
  with censoring risk. An operator who wants “crossed by gen N” sets P_SPLIT ≈ 0.02–0.04
  for N ≈ 20–40, and must accept N > 200 below p = 0.02.
- **Transport rate is NOT a usable dial (S2 FAIL — honest falsification).** The (b)-copy
  channel copies already-present types; consistent with 74-c's H2 saturation (b = 0.026),
  more hopping does not robustly advance the NBHD crossing. Its only visible effect is at
  the LOW end (T = 0.5 censoring at low p). Note the T axis is noisy at p ≤ 0.02
  (138.5 at T=2.0 vs 39 at T=1.0 — one censored seed) — with n=2 seeds/cell the low-p
  rows are the least trustworthy part of the surface.
- **S3 PASS — splitting dominates the interaction.** At high T the P_SPLIT span collapses
  90.5 → 6.0 gens (transport already spreads types; split rate becomes the sole limiter),
  and at high P_SPLIT the T span halves (fresh types planted constantly; transport no
  longer matters). The fast corner (p=0.08, T=4.0 → D* ≈ 8) is the surface's floor.

### H1 verdict history, honestly closed

- 74-c (240 gens): margin +0.033 → INCONCLUSIVE.
- 75-d (600 gens, 3 seeds): margin **−0.058** → **INCONCLUSIVE → FAIL**, booked per the
  registered rule. The pool **peaks near gen 100–150 then erodes** (visible in all three
  600-gen curves; rep 0 ends below its early window). **Plateau value: H_pool ≈ 0.975
  nats** (mean over seeds of the 300–600 window; per-seed 0.80 / 1.02 / 1.11). Mechanism
  hypothesis for wave-76: gA homogenization (blend a=0.5) concentrates quantized types
  while the cap-4 overflow drops old lineages — diversity is born faster than it is
  retained. Registered prediction was FAIL with margin [−0.05, +0.06] and plateau
  1.05–1.25: direction right, erosion slightly deeper than predicted.

## Honest limitations

2 seeds per surface cell (registered budget; per-level noise visible at low p); entropy
provenance seeded-local (BOOKED, never silent); censoring rule (D* = 241) inflates low-p
spans mechanistically rather than adversarially — raw + censored values both in the
receipt; S2's FAIL is partly a power statement (n=8/level) — but the pooled n=32 ρ = −0.13
gives no support to a usable transport dial at any power.

## Wave-76 seeds

1. **Retention vs birth**: instrument WHICH fragments the cap-4 overflow drops (age vs
   rarity) at p=0.08 — if overflow is the erosion channel, a rarity-biased cap is a
   one-line H1 rescue candidate.
2. **D* floor**: push P_SPLIT to {0.16, 0.32} to find where D* saturates and whether
   NBHD ever fails to stabilize (chaos without crossing).
3. **Surface with real entropy**: re-run the 6 corner cells with live moth bytes if a
   top-up path exists — the 74-c provenance downgrade is still an open replication.
4. **Operator contract**: fit log D* ≈ a − b·log P_SPLIT on the uncensored cells (the
   0.04/0.08 rows look log-linear) and register it as the dial's calibration curve.
