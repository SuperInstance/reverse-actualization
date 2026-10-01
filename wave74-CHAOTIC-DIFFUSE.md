# Wave-74 / B — CHAOTIC-DIFFUSE REGIME (73-e2): breeding ripples past the F1

Task 74-c, sub-task B. Prereg: `receipts/w74-prereg-B.md` (stamped before the
run). Raw receipt: `receipts/w74-chaotic.json`; per-gen metrics CSV + R(a)
table alongside; sim `scripts/hy4/w74_chaotic.py` (imports 73-e machinery
UNCHANGED — import, not fork); charts `outputs/w74-chaotic-{hpool,transport,
conservation}.png`.

## What was run

The wave-73 F1-cross stopped at the F1 uniform generation. The founder's
rung-7 claim was: *"the ripples of breeding that stability takes many many
generations to cross-mix into a true chaotic-diffuse."* This sub-task ran
that regime: **240 generations, sustained fractal splits** (P_SPLIT = 0.02
every generation, never switched off), on the same 24×24 hex lattice,
576 cells, blend a=0.35 (markers 0.5), leakage 0.22·0.5 — plus a NEW
genome-fragment layer riding alongside (bookkeeping only, fields untouched):

- Fragment = (type, origin_cell, birth_gen, holder_cell); type quantizes the
  parent's traits at birth: (round(gA·31), p-bin 0..3, res-bin 0..3) — ≤512 types.
- On each split at cell i: (a) a daughter fragment (type from i's CURRENT
  traits) is planted in a neighbor j the fragment layer draws itself
  (AMENDMENT-0 honored); (b) TRANSPORT: one of i's fragments is copied to j
  (the lattice transport channel); (c) mutation: gA_q ±1 with p=0.08 per
  planted/copied fragment.
- Per-cell capacity 4; overflow drops the oldest (birth_gen, tie by type).
- Fixed draw order per generation: 73-e step() first, then the fragment layer.

## Entropy substitution — BOOKED, never silent

The prereg targeted 2048 live comet-qrng-v1 bytes (gen g seeds from bytes
[8·(g mod 256) : +8]). Live fetch attempts (07:39Z and this session, 40+ job
submissions) yielded **81 bytes total** (~2–12 bytes/job — the emu engine's
tiny segment size makes 2048 bytes infeasible in budget; receipt:
`scripts/hy4/w74_moth_cache.json`). The registered fallback branch ran:
seeded local entropy `blake2b("w74-chaotic-fallback:"+arm+rep) → PCG64`, with
the substitution booked in the receipt. As registered, H1/H2/H3 are regime
dynamics claims — verdicts stand; provenance is downgraded and the wave-73
live-entropy comparison remains an open replication.

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| H1 | Pool diversity non-decreasing late vs early (margin ≥ 0.05 nats, mean over 3 live reps) | margin **+0.033** nats (late 150–240 vs early 20–70) | **INCONCLUSIVE** |
| H2 | Transport range sublinear (log-log slope b < 0.75, R² ≥ 0.6) | b = **0.026**, R² = 0.94 | **PASS** — hard saturation, far below the √t diffusion reference |
| H3 | ExoJ conservation margin max C ≤ 0.80 (flag if C > 0.75 on > 5% of obs) | max C = **0.7524**; C > 0.75 on 0.42% of observations; flag not raised | **PASS** |
| — | D* crossing (NBHD ≥ 3 sustained 20 gens) | gens **26 / 102 / 48** (live reps), 63 (PRNG control) | descriptive |

## Reading

1. **The founder's intuition survives, with a measured timescale.** The
   uniform F1 does NOT stay uniform: local neighborhood cross-mixing (NBHD)
   crosses the chaotic-diffuse bar in tens of generations (D* 26–102), while
   global pool diversity keeps rising slowly (H1 margin positive but under
   the registered 0.05 bar — hence INCONCLUSIVE, honestly booked).
2. **Transport saturates, it does not diffuse.** R(a) is flat past age ~2
   (slope 0.026): fragments plant near their origin and stay. Diversity
   spreads by *birth* (daughters born elsewhere), not by wandering —
   breeding ripples, not diffusion. This is a mechanistic distinction
   worth keeping in the architecture vocabulary: **a ripple system seeds
   copies; it does not commute.**
3. **ExoJ conservation holds under sustained splitting** — the ripple
   economics stay in the wave-73 band (max 0.7524 vs edge 0.75, band 0.80)
   across 960 generation-observations, 4× longer than wave-73's run.

## Wave-75 seeds

1. H1 replication with live moth entropy (the substitution path is booked;
   the claim deserves its registered source) — or a longer run (600+ gens)
   where the slow H_pool climb can cross the 0.05 bar.
2. The 73-g mechanical-learning hook: treat fragment transport as
   resistance-credit migration in the M1 lattice (74-b) — does seeding
   plasticity by fragment arrival beat k-winner-on-surprise?
3. D* as a *design dial*: P_SPLIT and transport rate sweep → the
   "many many generations" becomes a tunable crossing-time surface.
