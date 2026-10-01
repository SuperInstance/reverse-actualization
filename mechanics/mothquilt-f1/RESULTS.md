# 73-e RESULTS — Micromoth-quilt F1 cross (registered run 3)

Prereg: `scripts/hy4/f1_prereg.md` (written before run 1). All three runs'
artifacts are preserved — the failed runs are receipts, not hidden.

## Verdict table

| Hypothesis | Verdict | Numbers |
|---|---|---|
| H1 — F1 is uniform ("uniform the first round") | **PASS** (amended metric) | var(gA) at F1 = 1.22–1.36e-4 < 1.5e-4 jitter bound in 6/6 replicates. Prereg metric var(mA)=0 was vacuous (uniform by construction) — receipted. |
| H2 — breeding ripples take many generations | **PASS** | No replicate stabilizes (relative-delta rule) in 60 generations; V_p < 1e-3 absolute only at ~gen 58–59, exactly 0 at gen 60. The founder's "many many" is ~60 gens at these parameters. |
| H3 — moth true entropy delays stabilization | **INCONCLUSIVE** | G* undefined in BOTH arms (never stabilize) → comparison undefined. Also honest scoping: this is generation-scale true entropy (KDF-expanded), not per-cell quantum draws. |
| Conservation (ExoJ frame) | **HOLDS** | C = mean(p/5)+mean(r) ≤ 0.752 in every generation of every replicate; 0 violations. |

## The phenomenon, as measured

Two distant parental lineages (orchard: smooth gradient, high resistance;
wild: fractal noise, low resistance) are crossed per-site at F1. The F1
generation is genomically uniform (every cell the same hybrid within the
meiosis-jitter bound) while its phenotype is only partially homogenized —
F1 potential variance is 27% of the parental MEAN variance, but not below
the smoother parent's own variance. Genotype-uniform, phenotype partially
uniform: the first round looks uniform because identity merged, not because
space did.

Breeding then takes ~60 generations of ripples to cross-mix fully — during
which recurrent fractal splits (~11 per generation, each seeding a daughter
entropy ripple with a small phenotypic footprint into a random neighbor)
keep injecting variance. The system does not settle into equilibrium; it
crosses into uniformity and stops. "Ripples of breeding that stable take
many many to stabilize and cross mix to have a true chaotic-diffuse" is
quantitatively confirmed in shape, though the end state is uniform rather
than chaotic-diffuse at these parameters — the chaotic-diffuse regime likely
requires either sustained splits (larger P_SPLIT) or the leaky hex transport
of slackwater-lattice rather than mean-blend deformation. Queued as 73-e2.

## Instrument-failure receipts (both fixed BEFORE the registered run)

1. **Run 1 — arms identical.** The moth endpoint initially returned
   Cloudflare 1010 (python-urllib user-agent banned; browser UA passes) and
   the synthetic fallback seeded WITHOUT the arm name, collapsing moth/prng
   to identical streams. Artifact: `f1_metrics_FAILED_RUN1_arms_identical.csv`.
2. **Run 2 — observables blind.** Live moth packets obtained (60/60 LIVE,
   job-ids in `moth_packets.json`), streams verified distinct (split counts
   differ, 680 vs 678), but the stochastic channel (splits → entropy) never
   touched potential/markers, so every preregistered observable was
   byte-identical across arms. Artifact:
   `f1_metrics_FAILED_RUN2_observables_blind.csv`.
3. **Amendments before run 3:** (1) meiosis jitter — each F1 hybrid's genome
   fraction carries U(-0.02,0.02); (2) the daughter ripple is phenotypic —
   perturbs the neighbor's potential by 0.1 × daughter delta.

## Randomness provenance

60/60 qpixl-v1 packets LIVE from api.mothquantum.com (decode-noise idiom of
`quilt-arena/arena/moth.mjs`: probe waveform → qubit angles → one 2048-shot
measurement → the sampling noise of the decode IS the harvest). Each
packet expands via blake2b KDF into a per-generation PCG64 stream. Arm and
replicate are always in the seed text. Zero mock packets in the registered
run. Job-ids receipted in `scripts/hy4/moth_packets.json`.

## Files

- `f1_metrics.csv` — registered run 3, all metrics, all replicates
- `f1_verdict.json` — machine-readable verdicts
- `chart1_variance.png` — V_p vs generation, moth vs PRNG (log scale)
- `chart2_mixing_entropy.png` — genome-fraction decay + entropy-field variance
- `chart3_snapshots.png` — F0 / F1 / F2 / F60 field snapshots
- Sim: `scripts/hy4/f1_sim.py`; charts: `scripts/hy4/f1_charts.py`;
  prereg: `scripts/hy4/f1_prereg.md`

## Limitations (honest)

- n=3 replicates per arm; generation-scale entropy only; H3 untested per-cell.
- The stabilization rule (relative delta < 1e-3 × 5 gens) is pathological
  near V_p → 0; both the rule-literal reading and the absolute-threshold
  reading are reported above.
- Hex boundary cells have fewer neighbors (no wrap); means are over
  available neighbors.
- The chaotic-diffuse end state was NOT reached — uniformity was. See 73-e2
  queued follow-up (sustained splits / lattice transport).
