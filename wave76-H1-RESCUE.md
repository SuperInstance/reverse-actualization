# Wave-76 / 76-c — THE H1 RESCUE: instrument the cap, swap the drop rule, invert the dial

Task 76-c. Prereg: `scripts/w76_h1rescue_prereg.md` (registered **2026-10-01T10:39:00Z**,
BEFORE any run; stamped expectations `receipts/w76-h1rescue.expectation.json`, prereg
sha256 `a102ade2dfcf4ccf…`). Receipts: `receipts/w76-h1rescue.json` + `receipts/w76-h1rescue.csv`
(per-gen rows, all arms). Sim: `scripts/w76_h1rescue.py` (imports the 75-surface machinery
UNCHANGED — `w75_surface.FragLayerT`/`run_cell`, `w74_chaotic.w74_stream`, `f1_sim`;
no line of the 73-e/74-c/75-d code edited). Charts: `outputs/w76-h1rescue-drops.png`,
`outputs/w76-h1rescue-hpool.png`.

## What was run

The 75-d verdict left H1 upgraded to FAIL (margin −0.058 nats at 600 gens, plateau
H_pool = 0.975, pool peaking ~gen 100–150 then eroding) with two named suspects: cap-4
overflow dropping the OLDEST fragments (rare types die first) and gA homogenization.
This task executed the pre-registered diagnosis → rescue → verification chain at the
baseline operating point (P_SPLIT = 0.02, transport T = 1.0):

- **Arm R `base600`** — the registered cap-4-oldest-drops rule, instrumented: every
  overflow drop logs (type, age, holder-count class). Pure bookkeeping; the registered
  **blocking integrity check** passed with max |ΔH_pool| = **0** (bit-identical
  reproduction of the 75-d per-gen receipt, D\* 84/None/102 exact) — instrumentation
  touched no physics and no draw order.
- **Arm X `rarity600`** — `FragLayerR`: overflow drops the **most-common-held type's
  newest copy** (key `(-hc, -birth, type, iid)`; hc = pool-wide holder count = distinct
  cells holding ≥1 copy; ties by birth then type then iid; deterministic, zero RNG).
- **Arm V `p0.030419_t1.0`** — inverted-dial verification, run by
  `w75_surface.run_cell` UNCHANGED (2 seeds × 240 gens).
- Entropy: the BOOKED 74-c/75-d seeded-local protocol reused UNCHANGED (`w74_stream`;
  arm encodes the config); no live moth fetch (74-c receipted 81/2048-byte infeasibility).
  Provenance downgraded, verdict rules unchanged. Wall: **1.21 min** (6 × 600-gen
  instrumented + 2 × 240-gen runs).

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| T1 | Under the registered cap, singleton-holder (rare) types are dropped at a higher per-tick rate than common types (ratio ≥ 1.5) | drops rare = **37**, common = **31,387** (pooled, 3 seeds × 599 ticks); ratio = **0.0012** — 1250x BELOW the bar; per-seed 0.0014/0.0012/0.0009 | **FAIL** |
| T2 | Rarity-biased cap raises H_pool(300–600) vs registered cap, same seeds | wins **3/3**; H_late 2.107/2.131/1.947 vs 0.800/1.017/1.108; mean delta **+1.087 nats** | **PASS** |
| T3 | Rarity cap at 600 gens: margin H(300–600) − H(20–70) ≥ 0.05 nats on ≥ 2/3 seeds | margins **+1.050 / +1.010 / +1.089** — 3/3 cross, ~20x the bar; **plateau = 2.061 nats** (vs 0.975 registered) | **PASS** |
| T4 | D\* log-linear in P_SPLIT at T = 1.0 (R² ≥ 0.9) AND inverted dial (target D\*=30) verified within factor 1.5 | R² = **0.988**; p\* = **0.030419**; verification D\* = 30/29 → mean **29.5** (window [20, 45]; 1.7% error) | **PASS** |

## The diagnosis inverted — and the rescue worked anyway (booked honestly)

**T1 refuted the pre-registered mechanism.** Under the registered cap the overflow
channel is ~99.9% *common-type* drops: a singleton-holder type almost never sits in the
drop slot. Reading of the drop log (non-registered interpretation, clearly post-hoc):
rarity and drop-risk anti-correlate because hc = 1 types are mostly *young* — freshly
minted (a)-planting/mutation events that have not spread — while the cap evicts the
*oldest* fragments, whose types have usually already spread (hc ≥ 2) or already died.
The 37 rare drops that did occur were the oldest events in the log (mean dropped age
247.5 vs 149.9 for common) and **every one was an extinction** (37/37; rare drops are the
only observed type-death channel — the killing blow always lands when a type is down to
one holder). So the cap does terminate rare lineages, just rarely; it is not the mass
erosion channel 75-d suspected. The erosion of the registered arm is *concentration*,
not eviction: n_types falls 9–10 → 4–6 while n_frags stays pinned at the 2304 saturation
cap and no common type ever goes extinct (0/31,387 drops) — the homogenized field keeps
minting the same few types and they fill every slot.

**T2/T3: the rarity cap rescued H1 anyway, by a different mechanism.** `FragLayerR`
dropped 35,748 fragments, **zero of them rare** (by construction it never targets
hc = 1 first) — but note the registered cap also avoided rare drops; the operative
difference is *which common copies die*: oldest-birth lineages (registered, mean dropped
age ≈ 150) vs the **dominant type's newest spread wave** (rarity). Pruning the newest
copies of the most-common-held type keeps cells from saturating with the homogenized
dominant types and preserves slot space (and old-birth lineage carriers) for everything
else: late H_pool jumps to **2.06 nats plateau** (2.1x the registered 0.975), final type
count 12–14 (vs 4–6), and the margin swings from −0.058 (75-d FAIL) to **+1.05 nats**
(3/3 seeds) — the 74-c bar, uncrossed at 240 and 600 gens under the registered cap, is
crossed by ~20x under the rescue cap. Side observation: D\* under the rescue cap was
49/53/148 (vs 84/None/102) — crossing not harmed on 2/3 seeds, delayed on one.
C_max stayed at the surface invariant ≈ 0.752 on every arm (ExoJ band intact, H3-style
guard never threatened).

Mechanistic honesty: T2/T3's PASS therefore does **not** confirm the registered T1
mechanism; it establishes the *intervention* (dominance-pruning cap) as effective and
re-attributes the mechanism post-hoc. The gA-homogenization suspect (ii) remains the
birth-side driver — the rarity cap neutralizes its retention-side consequence.

## The operator's calibration curve (T4)

Over the four baseline rows (T = 1.0, P_SPLIT ∈ {0.01, 0.02, 0.04, 0.08}; mean D\* =
93 / 39 / 23.5 / 12.5, none censored):

    ln D* = 0.1122 − 0.9417 · ln P_SPLIT          (R² = 0.988, n = 4)

**Inverted dial — to cross by generation D\*, set**

    P_SPLIT = exp((ln D* − 0.1122) / (−0.9417)) = 1.1265 · D*^(−1.062)

Registered verification: target D\* = 30 → p\* = 0.030419 → measured D\* = 30/29
(mean 29.5; factor-1.5 window [20, 45]). Worked examples: D\* = 10 → p ≈ 0.098;
D\* = 50 → p ≈ 0.018. Validated range: D\* ∈ [8, 188] gens at T = 1.0, 240-gen
observation window; extrapolation beyond it is unbooked.

## Wave-77 seeds

1. **Birth-side rescue**: the retention side is fixed (+1.05 nats); attack suspect (ii)
   directly — reduce the gA/marker blend (a = 0.5 → lower) or re-quantize types on
   slower channels, and measure whether type BIRTH rate recovers under the registered
   cap (no cap surgery).
2. **Rescue × dial interaction**: re-run the T4 verification cell at p\* with the
   rarity cap — does dominance pruning shift the calibration curve (refit a, b)?
3. **Occupancy instrumentation**: log per-type (type, holder)-pair counts over time in
   the registered arm to quantify the concentration process directly (effective number
   of types exp(H_pool) vs n_types), closing the mechanism question T1 opened.

## Honest limitations

3 seeds per arm at one operating point (registered budget); T1's ratio is a
class-aggregate (rare = hc 1, common = hc ≥ 2) — per-type hazards not registered;
the T1-classification snapshot is taken pre-removal with the overflow included
(simultaneous-drop semantics for the registered cap, sequential for the rescue cap —
inherent to the two rules, documented in the prereg); the mechanism re-attribution is
post-hoc and non-registered; entropy provenance remains seeded-local (BOOKED, never
silent); the T4 fit has n = 4 points and inherits 75-d's 2-seeds-per-cell noise.
