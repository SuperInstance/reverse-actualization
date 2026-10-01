# Wave-76 / D — MULTILINGUAL EXTENSION: re-rooting survives case grammar and honest verb-first learner register

Task 76-d. Prereg: `scripts/w76_multiling_prereg.md` + stamped expectations
(`outputs/w76-multiling.expectation.json`, sha f1085836219de51c, before any
call). Raw: `receipts/w76-multiling.json`; 16 new sessions
`scripts/hy4/transcripts/w76_multi_*.json`; chart `receipts/w76-multiling.png`;
harness `scripts/hy4/w76_multiling.py` (reuses w74_tonal's anchors/judging).

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| V1 | RU concept-preservation ≥ 0.75 | **0.833** | **PASS** |
| V2 | RU reorganization ≥ 0.5 | **0.785** — the highest D2 of any language so far (ZH was 0.738) | **PASS** |
| V3 | DINE concept-preservation ≥ 0.6 (learner-register protocol) | **0.715**; D2 0.527 | **PASS** |
| V4 | anchor-chips raise ZH anchor hit-rate ≥ 0.15 on rungs 1/7 without D2 < 0.5 | **4/4 cells**: 0.4 → 1.0 (+0.4…+0.6), chips-D2 0.67–0.80 | **PASS** |

## Per-pair texture

- **RU (case-driven)**: D1 0.82–0.94 everywhere except one outlier,
  mimo-r1 at **D1 = 0.46 with D2 = 0.86** — the model reorganized so hard at
  the instrument-surface rung that Jev judged the idea itself drifted. This
  replicates 74-c's observation that rung 1 is the most language-bound rung
  (UI vocabulary) and adds a new failure mode: **over-reorganization** —
  re-rooting so aggressive that concept preservation fails *from the
  reorganization side*, not the translation side. Drift guards monitor
  translation-bleed; they now also need an over-reorganization tripwire
  (low D1 with high D2).
- **DINE (honest learner-register)**: the verb-first protocol preserved
  concepts (0.715 ≥ 0.6 bar registered a priori) with a clear model split —
  MiMo D2 0.59–0.64 (genuine re-rooting) vs Muse 0.34–0.60 (closer to
  restatement). No lexical anchors were registered (booked honestly: none can
  be asserted at learner register) and none were needed for the verdict.
- **A/B (anchor-chips)**: the guard works exactly as designed — anchors
  converge to 1.0 and D2 is *unharmed* (0.67–0.80 vs 0.69–0.83 baseline).
  Chips shape vocabulary without suppressing re-derivation.

## Design-change update (the registered deliverable)

1. **Anchor-chips are promoted** from candidate to shipped guard (74-c
   design-change #1 now has its A/B evidence).
2. **New guard: the over-reorganization tripwire** — when D1 < 0.5 while
   D2 > 0.7, the localization drifted by *creative excess*; route to a
   reflective re-anchoring pass (mirror of the lexical channel's
   translation-drift route).
3. **Learner-register honesty is a viable protocol**: for low-resource or
   weakly-modeled languages, the verb-first re-rooting exercise measures
   structural adaptation without demanding or fabricating fluency. This is
   the honest shape of wave-73's multilingual ideation program: the
   *organization* of a language is what re-roots ideas, and organization can
   be engaged at learner register.

## Wave-77 seeds

1. Over-reorganization tripwire A/B: register D1<0.5 ∧ D2>0.7 as a route
   trigger, re-run mimo-r1-ru with a re-anchoring pass, measure D1 recovery.
2. RU + chips combined (chips were only tested on ZH): does the vocabulary
   guard survive morphological richness (stem-matching anchors)?
3. The homunculus goes multilingual: give MEM's ledger lane the RU ledger
   vocabulary (реестр/квитанция/дифф) and test cross-language receipt
   understanding between cells (the untranslatable-verb list from 74-c).
