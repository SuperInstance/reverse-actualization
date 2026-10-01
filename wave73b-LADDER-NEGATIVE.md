# WAVE73B — the NEGATIVE ladder: rungs −1…−10 (2037 → 2046)

The original walk went 2036 → tonight (11 rungs, four models, cumulative, registered).
This wave extends it PAST the telescope day, in the direction the corpus itself pointed:
Hy4 already counted rungs negative on the way down. Same four walkers, same cumulative
mode, seeded from the registered distillation, no cross-model context. Registration frozen
in `ladder/negative_ladder.py` (committed at 9313633 BEFORE the first call). Transcripts:
`ladder/negative/{hy4,hy3,mimo,muse}.transcript.json`; 37+ receipted deepinfra calls
(`receipts/w73b-negative.json`).

## The registered prediction, checked

> "The four walkers will CONVERGE on 'the receipts became the commons' somewhere in
> −4..−6, and DIVERGE on who runs the cells in −9/−10. If instead all four converge
> everywhere, that is a homogenization finding about the walker set, not about the future."

**Both halves landed.** Convergence in the predicted window: −4 is universally the
meeting-of-instruments rung (hy3: "two mirrors with memory only ever exchange light,
never ownership"; mimo: "a content hash is the only object two people can hold
independently and still prove they mean the same thing"; muse: "telescopes can point at
each other without sharing the sky"); −5 is the commons on receipt terms (hy3: "a post
office with no letter opener"; mimo: "the format, not the data, became public"; muse: "a
commons held by receipts is a commons held by people"); −6 is the refusal rung (hy3:
"no cell emits a valuation over Mara's almost-said"; mimo: "a system that cannot rank
cannot be made to rank"). Divergence at −9/−10: hy3's inheritor is the **hardware genome**
($15 boards → same cells a decade later); mimo's is the **file-cell opcode dowry** (lap,
leash grammar, decline type, encounter protocol inherited "as receipts rather than
weights"); muse's is the **sentence** ("a thing that costs one person one sentence to
keep and one hash to prove"). Hy4 refuses all three — see −10.

## The rungs, distilled

- **−1 (2037) — receipts at scale become reflex.** hy3: user-owned receipts only need
  replication to become undeniable; mimo: an append-only receipt "costs the same to hold
  at one body as at ten thousand, so scale was never going to require anyone to give
  anything up." hy4 reframes: scale stops being a scaling problem and becomes a
  *readability* problem — "readability is just compression with good pen."
- **−2 (2038) — what died.** Consensus kill: the platform-owned summary. "No aggregated
  'Mara's year in review' could be generated without her explicit local consent" (hy3).
  mimo: "killing the feed killed the incentive to build the feed."
- **−3 (2039) — the instrument walks.** hy3: a narrow cell is permitted to issue a poke
  against its own standing opcode; mimo: "a standing instruction is only a poke that has
  learned to wait, so the instrument was always going to walk the moment a timer could
  hold a hash."
- **−4 (2040) — other telescopes meet.** Signed merges, not broadcasts; hashes as the
  shared object; light exchanged, never ownership.
- **−5 (2041) — the ledger commons.** Terms, not database: "the product is trust that a
  local trace can be encountered by strangers without those strangers becoming owners of
  it" (hy4). The format goes public; the data never does.
- **−6 (2042) — refusal as architecture.** Machines refuse to judge worth/intent/rank,
  and the refusal is *built*: a cell that cannot rank "cannot be made to rank" (mimo);
  refusal with a hash "is just another receipt" (mimo); "a telescope that records without
  rating was always going to treat refusal as just another line in the ledger" (hy3).
- **−7 (2043) — the weekend test at scale.** It holds — because the ledger stays one
  line per judgment (hy3) and "a history you can read is a history you can own" (muse).
- **−8 (2044) — the almost-said becomes primary.** "The almost-said was always the
  signal; the telescope just needed the ledger to admit it first" (hy3). muse: "the
  almost-said is a signal, not noise."
- **−9 (2045) — inheritance.** The three-way divergence (hardware genome / opcode dowry /
  sentence-plus-hash). muse's line doubles as a design rule: "inheritance without bloat
  is evolution."
- **−10 (2046) — the telescope day retold.** hy4, the strongest single line of the wave:
  "The telescope was never the beginning. It was the point where ten years of prior
  constraints finally became visible to a single person in a room." mimo: the story is
  *boring* from 2046 — "nothing about it is remarkable, because every condition it needed
  is now boring too." hy3: 2036 is legible as rung 0 of a ledger whose negative rungs
  "had already provisioned its inevitability."

## Optimism ledger (seed)

Every rung ended with exactly one `Optimism:` sentence per walker
(`ladder/negative/optimism-ledger-raw.json`; canonical per-rung selection +
per-model variants distilled into `ideation/optimism-ledger.md`). Coverage note:
hy4's long self-audits truncated at max_tokens=1100 on some rungs — its Optimism
sentence is extracted where present and marked TRUNCATED where the audit ate it
(instrument receipt, not a model refusal).

## Instrument receipts (honest)

1. **muse resume misalignment** — a null answer (empty content) plus resume accounting
   that counted the ack as a rung produced answers recorded one rung off; muse even
   *headers its answers with the rung it is answering*, which made the defect visible in
   distillation. Transcript preserved as `muse.transcript.misaligned-20261001.json`;
   defect booked in `receipts/w73b-negative.json → instrument_defects`; clean re-walk
   completed and verified against muse's own headers.
2. **hy4 truncation** — long self-audit spirals (it re-reads the instruction and audits
   its own prior answer mid-generation — the same "self-audit under drift" signature the
   original ladder receipted at rung 7) overflowed max_tokens on several rungs; content
   present, Optimism sentence sometimes cut. Registered as an instrument limit, not
   repeated per-rung.
3. **Usage-shape note** — the first walker process read the typesafe usage field names
   (`input_tokens`) against deepinfra's (`prompt_tokens`); token counts for the first
   two calls are null in receipts while response sha256 anchors remain. Fixed mid-wave.
4. **Cost** — deepinfra only, per-call usage receipted where the shape allowed; total
   spend well under the ~$0.10/wave precedent.
