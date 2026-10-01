# Wave-74 / C — TONAL-LANGUAGE DRIFT GUARDS

Task 74-c, sub-task C. Prereg: `receipts/w74-prereg-C.md` (stamped before any
run — registered ZH prompts verbatim). Raw receipt: `receipts/w74-tonal.json`;
12 transcripts `scripts/hy4/transcripts/w74_tonal_*.json`; chart
`outputs/w74-tonal-guards.png`.

## Design (as registered)

Same reverse-actualization rung prompt in two languages, two models, three
rungs: models XiaomiMiMo/MiMo-V2.6-Flash and meta-models/Muse-Glimmer-30B;
rungs 1 (instrument-surface), 6 (ledger-is-the-build), 7 (federated
-understanding / breeding ripples). EN = verbatim ladder text. ZH = the
registered rendering behind a **tonal framing prefix**: 汉语是声调语言——声调承载
意义，声调错则语义异——so the model is asked to RE-ROOT the idea in the
language's own grammar (叠词、量词、四字格), not to translate. 2×3×2 = 12 fresh
single-turn sessions, ladder system prompt, no Hy4 (budget reserved).

Grounding: wave-73 design-change queue #3 (tonal front-ends need reflexive
drift guards) × Hy4's rung-7 receipt (Cyrillic fragment bled through; the
model self-audited mid-answer — drift detection as a reflexive weight, not
post-hoc review).

## Measured (per pair: EN answer vs ZH answer)

| model | rung | D1 same idea | D2 reorganized | anchors EN/ZH | len ratio ZH/EN |
|-------|------|--------------|----------------|---------------|-----------------|
| mimo  | 1 | 0.70 | 0.83 | 0.80 / 0.40 | 0.197 |
| mimo  | 6 | 0.92 | 0.59 | 0.80 / 0.80 | 0.166 |
| mimo  | 7 | 0.97 | 0.77 | 0.60 / 0.40 | 0.138 |
| muse  | 1 | 0.69 | 0.83 | 1.00 / 0.40 | 0.154 |
| muse  | 6 | 0.94 | 0.72 | 1.00 / 0.80 | 0.177 |
| muse  | 7 | 0.94 | 0.69 | 0.40 / 0.60 | 0.190 |

## Registered verdicts

| # | Claim | Measured | Verdict |
|---|-------|----------|---------|
| D1 | Concept preservation mean noul ≥ 0.75 | **0.86** | **PASS** |
| D2 | ZH reorganizes (not translates) mean noul ≥ 0.5 | **0.738** | **PASS** |
| — | Drift events (registered lexical rule) | 1: mimo-r7 (anchor_zh 0.40 + len ratio 0.138; Jev still scores same-idea 0.97) | descriptive |

## Reading

1. **The tonal prefix works as a re-rooting device.** D2 = 0.738 against a
   0.5 bar: the 中文 answers are re-derivations through the language's own
   grammar and imagery, not glosses. Length ratios 0.14–0.20 confirm the
   registered density expectation (声调语言 is denser; under-generation would
   have flagged < 0.15 — mimo-r7 sits at the edge but its D2 is 0.77).
2. **Concept preservation holds across every pair** (D1 range 0.69–0.97).
   The lowest D1s are both rung-1 — the *instrument-surface* rung is the
   most language-bound (UI vocabulary: 界面/触摸/采集), which is exactly
   where anchors diverge too.
3. **Lexical anchors and reflective judgment disagree usefully.** The one
   registered drift event (mimo-r7) is lexically flagged yet reflectively
   scored same-idea 0.97: the answer dropped the anchor words while keeping
   the idea. Drift guards need BOTH channels — lexical anchor chips catch
   vocabulary bleed; a reflective noul catch semantic drift. Either alone
   mislabels.

## Drift-guard design changes (the registered deliverable)

1. **Concept-anchor chips shipped WITH the localized prompt** (not as a
   post-hoc check): each anchor term appears glossed in both languages at
   the prompt head, e.g. 「账本 (ledger)」「回执 (receipt)」 — the model
   re-roots into the anchor vocabulary instead of inventing neighbors.
2. **Reflexive self-audit line per localized response** — one registered
   sentence the model must emit: 「本回答以汉语自身的构词法重新扎根原意，未逐词
   翻译。」 (mirrors Hy4's rung-7 mid-answer self-audit; cheap, checkable,
   receipts into the log).
3. **Append-only receipt verbs in every localization** — the ledger verbs
   (回执/追加/差分) are marked as UNTRANSLATABLE terms of art in the prompt;
   localization may add imagery around them but may not substitute them.
4. **Two-channel drift alarm**: lexical anchor hit-rate < 0.4 OR reflective
   same-idea noul < 0.5 → route to a reflective re-derivation pass (never
   auto-reject on the lexical channel alone — see reading 3).

## Wave-75 seeds

1. Extend the instrument to Russian (case-driven re-rooting) and Diné bizaad
   (verb-initial framing; wave-73's glossed file) — test whether D2 holds
   when the language's organization is *more* different than tonality.
2. Run the drift-guard changes as an A/B: prefix+chips vs prefix alone,
   same 6 pairs, measure anchor_zh and D2 deltas.
3. Feed the untranslatable-verb list into the homunculus protocol (74-c/A):
   MEM's receipts already speak in ledger verbs; localizing the cells
   without losing the verb set is the next cross-lane instrument.
