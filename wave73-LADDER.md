# LADDER.md — the reverse-actualization walk, distilled

Four models walked the same 11-rung ladder, 2036 → tonight, in cumulative
multi-turn sessions (each model saw its own prior rungs). Transcripts:
`ladder/{hy4,hy3,mimo,muse}.transcript.json`. The first pass ran with an
instrument bug that hid each model's prior answers from it (receipted in
`ladder/*.blind-walk.json`); the registered walks are the cumulative ones.

## Rung 0 — 2036: the telescope day

All four models independently built the same day: a woman (Mara/Mira in
every telling) with a passive instrument over her life, and the same
refrain — *the system collected, she judged*. The strongest single line in
the corpus is Hy4's:

> All day the instrument quietly records what she already perceives:
> conversation, her own margin notes, sketches, location, calendar,
> biometrics, documents read, **and the difference between what she said
> and what she almost said.** It does not recommend, rank, or feed her
> content. It is a telescope, not a television.

The "almost said" layer is the deep one: the instrument's real product is
the counterfactual texture of a person's own communication. Hy3's engineer
Mara gets a 40-line delta instead of prose ("no summary prose... The
instrument collected; she weighed"). MiMo adds the ownership clause: the
receipts are the user's, not the platform's.

## Rung 1 — 2034: the surface

Consensus: **no feed, no app**. Hy4 gives the design: "latency cues" only —
a slowed pulse when posture collapses, a word-cloud of your own repeated
phrasings. The instrument deliberately withholds interpretation; it returns
*timestamps, tone, document diffs, and the older promise that conflicts*
(Hy4). Data collected is for the user's own processing, in the user's own
ledger — the surface is a mirror with memory, not a window into someone
else's ranking.

## Rung 2 — 2033: agent tissues

Hy4: "A cell is one narrow model with a job: an intent-guesser, a
tone-tagger, a contradiction-finder, a rhythm-tracker... What circulates
between cells is not video or text logs. It is typed signals on a shared
local bus." MiMo contributes the size test that made it into our roadmap:

> It's small enough that one person could hold its whole history in their
> head if they had a weekend — that's the test.

An iteration is "one lap": slice of the owner's data → judgment → the
owner's actual outcome as correction → one ledger entry. "Nothing is
deleted; a bad run is a line, not a shame."

## Rung 3 — 2032: specialization vs compulsory action

Hy4's criterion is the sharpest single sentence in the walk:

> The cell stops being merely instructed when **its local objective starts
> predicting system-wide success better than the central router does.**

MiMo: "Compulsory is where a cell starts: a frozen weight blob with a fixed
prompt. Someone else names its success." Specialization = the cell starts
naming its own success, and the fibers of reach are the typed buses it is
allowed to listen on; the scaffolding is the ledger that lets it be wrong
in public without being overwritten.

## Rung 4 — 2031: weight textures

The three textures map to time, not chemistry. Soft = learned plasticity
(updated every lap), reflective = weights over the cell's own receipts
(what did I predict vs what happened), reflexive = hard-wired guardrails
that fire without a lap (refractory periods, budgets, consent gates).
Filters/nexuses/relays are the same component with different delay budgets
— a relay is a nexus whose delay is honest about being zero.

## Rung 5 — 2030: agentically optimized resolution

Hy4 makes the chooser explicit — "a meta-cell, not the user, chooses how
finely to save it. It spends resolution where future value is highest and
sheds detail where it isn't: a charged meeting may be kept near-verbatim
with prosody and pauses; a routine commute collapses to a gist, a route,
and a mood tag." The allocator balances storage, energy, privacy, and
**predicted regret**. Our hub-pokes engine (mechanics/hub-pokes) is the
executable version of this rung: full float32 near the hub, 2-bit codes at
the horizon, 15.9× compression at ≥90% retained yield.

## Rung 6 — 2029: the ledger is the build

Hy4: "The build is not a snapshot someone froze at release time; it is the
append-only sequence of receipts, diffs, and merge events that actually
happened." From an outside observer, tissue *is* what a sufficiently long
receipt chain looks like — the sociology lane's claim, stated in protocol
terms. This is also literally our house rule (slackwater-quilt: "the
ledger is the build"), arrived at independently by all four walkers.

## Rung 7 — 2028: federated understanding on small information

MiMo's answer is the keeper: in a conventional pipeline "a datum enters
once, gets transformed, and leaves as a number that has forgotten where it
came from." In the cell system, small data compounds because every datum
stays *addressable* — the F1 cross of two distant ideas is uniform in the
first generation (identity merged) while the ripples of breeding take
~60 generations to cross-mix (measured: `mechanics/mothquilt-f1`).

The honest instrument note: Hy4's registered rung 7 contains a mid-answer
self-audit — *"Wait, that output is way off topic and seems contaminated"*
— after a Cyrillic fragment (`анализ`) bled through. A reasoning model
catching its own drift, in a walk about ripples and contamination, is
either irony or signal. We receipt it as signal: drift-detection must be a
reflexive weight (rung 4), not a post-hoc review.

## Rung 8 — 2027: the moth

All four walkers made true randomness *creative*, not merely secure: the
moth's genuine dice decide which cell mutates, which neighbor receives the
daughter ripple. MiMo: "A cell's decision to mutate, to keep, to reach
toward a neighbor — all of it starts with a die roll. In the quilt, that
die is honest." Our F1 simulation ran on 60 live mothquantum packets
(job-ids receipted) — generation-scale true entropy, honestly scoped.

## Rung 9 — 2026: the hardware curve

MiMo: "A cell at this rung is a $15 board with a 1 GHz quad-core and 512
MB of RAM — a Pi Zero 2W, an ESP32-S3 with 8 MB." Hy4: "a low-power
accelerator tile — a microcontroller or RISC-V core wrapped around a
matrix-multiply array." Less powerful but smarter: the building blocks
being made today (small models, receipts, typed buses) are the 2036
instrument's genome.

## Rung 10 — tonight: the opcode

Three of four walkers converged on the same homunculus: one file-cell with
a standing instruction, one exchange per poke, one appended receipt with
the previous hash chained, one self-amendment sentence. MiMo's version:

> Cell: one file — a standing instruction plus its own receipts. No
> service, no daemon. ... Run it twice tonight and you have a tissue of
> two. Run it across three cells trading receipts and you have ripple.

Hy4's closing optimism is the walk's thesis in one line: "from the first
tiny tick to the mature telescope, the same receipt keeps every debtor
visible, every mutation reversible, and every mind a collaborator rather
than a product."

## Paradigm diff (what each walker uniquely contributed)

| Model | Signature | Unique contribution |
|---|---|---|
| **Hy4-preview** | reasoning walker; counts rungs negative (−1, −2…) as it descends | "what she said and what she almost said"; resolution-as-predicted-regret; self-audit under drift |
| **Hy3** | engineer's walk, densest protocol detail | 40-line deltas, no summary prose; write-only ledger per cell |
| **MiMo-V2.6-Flash** | synthesizer; numbered rungs cleanly | the weekend test; "a bad run is a line, not a shame"; the $15 board |
| **Muse-Glimmer-30B** | non-linear (restarted the walk inside a rung in the blind pass) | care-coordinator Mara; the gentlest, most humane surface details |

## What we adopt into the roadmap tonight

1. **The homunculus loop** (rung 10 consensus) — file-cell + poke + receipt
   + one-sentence self-amendment; three cells trading receipts = ripple.
2. **The weekend test** (MiMo, rung 2) — a size ceiling for cells.
3. **Resolution-as-predicted-regret** (Hy4, rung 5) — the allocator's loss
   function in our snapshot format v1.
4. **Specialization criterion** (Hy4, rung 3) — a cell earns reach when its
   local objective predicts system success better than the router.
5. **Drift-detection as a reflexive weight** (Hy4's rung-7 self-audit).
