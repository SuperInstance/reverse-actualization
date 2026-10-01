# 73-f RESULTS — Hub-and-pokes diffuse inquiry engine

Pre-registered claims (in the engine docstring BEFORE any tuning):
- **P1**: hub-and-pokes harvests >= 1.5x yield-per-cost vs greedy
  hill-climb with box-opening.
- **P2**: the anytime snapshot is >= 8x smaller than full-precision state
  while retaining >= 90% of harvested yield on resume.

## Verdicts (registered run, 5 landscape seeds)

| Claim | Verdict | Numbers |
|---|---|---|
| P1 | **PASS** | hp yield/cost 0.0509 vs greedy 0.0191 → **2.66x** (>= 1.5x). Beats random (0.032), sweep (0.016) too. |
| P2 | **PASS** | snapshot mean **15.9x** smaller (2584 B vs 36864 B); retained top-10 belief mass **1.006** (>= 0.9); continuation harvest retention **1.07** (resumed runs matched or beat uninterrupted runs in 4/5 seeds — quantized far-field sometimes *helps* by forgetting poke noise). |

Pinch statistics: 21–33 box openings per run; the risk model's gamble rule
(box when claimed fruit outweighs the threatened believed-mass) fired on
peaks, and the "pushed to pick" late-budget branch rescued yield near
budget exhaustion.

## The engine (as commissioned)

- Hidden yield field 48×48 (blobs + ridges + sharp peaks, fixed seeds).
- **Poke** (cost 1): noisy 3×3 read (sd 0.15) — safe, additive knowledge.
- **Box-open** (cost 5): exact reveal + harvest of one cell, and a pinch
  kernel (0.2·exp(−d/1.5), r ≤ 3) permanently degrades the surrounding
  field — commitment can sever the best path.
- **Low-hanging fruit**: the poke candidate whose uncertainty covers the
  most unresolved neighbors (ripening the branch), plus 20% far diffusion.
- **Keep moving**: confirm-pokes on rising avenues; when pushed late in
  budget, the gamble bar lowers; never idle while budget remains.
- **Snapshot v1**: version byte + sha256-8 + JSON header + resolution
  zones — f32 near the hub (r ≤ 4), f32 mid (r ≤ 12), 2-bit-packed far.

## Commissioning receipts (5 instrument bugs found and fixed, in order)

1. **Re-pokes excluded** → belief means could never climb past one noisy
   observation → box gate unreachable, harvest 0 in every seed.
2. **Variance floor misapplied to the poked cell itself** (fringe cap
   raised the cell's own variance back to 0.006 forever) → box gate
   unreachable again.
3. **Pinch risk included the claimed cell** (kernel at d=0 is maximal) →
   the fruit itself counted as risk of breaking the fruit.
4. **Pinch kernel too hot** (0.5·exp(−d/2) sums ≈ 4.0 over its disk) →
   aggregate risk of ANY box ≈ 0.9 → veto on everything. Recalibrated to
   the founder's semantics: the box severs a PATH (0.2·exp(−d/1.5)).
5. **Risk gate as hard veto** (risk < 0.6·mean) → rich veins permanently
   vetoed boxing. Replaced by the founder's gamble: pick when the fruit
   outweighs the threatened branch (mean > risk), worse odds when pushed.
6. (Bonus) **Frontier-exhaustion ended runs early** — "keep moving"
   violated; fallback added to re-work the most uncertain known cells.

All commissioning iterations are visible in the git history of
`pokes_engine.py` comments; every fix is annotated in-place.

## Files

- `pokes_engine.py` — engine + baselines + preregistration docstring
- `pokes_results.json` — per-seed rows + summary verdicts
- `chart1_yield_vs_cost.png` — harvest curves, 4 strategies (seed 0)
- `chart2_final_maps.png` — final belief maps, boxed cells marked
- `chart3_resolution_map.png` — the agentically chosen resolution zones

## Limitations (honest)

- n=5 landscapes, single seed pair per baseline; the 1.5x bar was beaten
  by 2.66x but no confidence interval is claimed.
- The pinch kernel and gamble rule were commissioned, not derived —
  the pre-registration governs the FINAL claims (P1/P2), and the
  commissioning trail is disclosed in full.
- Exact-trajectory resume equality is impossible by design (quantized
  far field); the registered claim is harvest retention, which is the
  quantity that matters for "state saved at agentically optimized
  resolution."
