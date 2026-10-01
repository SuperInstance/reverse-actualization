#!/usr/bin/env python3
"""negative_ladder.py — wave-73b: rungs -1..-10 (2046 -> 2037), the ladder walked PAST the telescope day.

REGISTRATION (frozen before the first call; this file is committed pre-run):
  - Four walkers, the same four as the registered 2036->tonight ladder:
    tencent/Hy4-preview, tencent/Hy3, XiaomiMiMo/MiMo-V2.6-Flash, meta-models/Muse-Glimmer-30B.
  - Mode: CUMULATIVE (each model sees its own prior rungs; the blind-walk instrument bug of
    the first 2036 pass was receipted and fixed there — not repeated).
  - Seed context: the registered distillation (wave73-LADDER.md rungs 0..10), one paragraph,
    so walkers continue THEIR OWN ladder rather than re-deriving it. No model sees another
    model's answers (parity with the original protocol).
  - Direction: rungs count NEGATIVE, years count UP (2037..2046). Hy4 already counted rungs
    negative descending; the hook is in the corpus.
  - Guiding question per rung is OPEN (year + one probe, no prescribed content). Probes:
    -1 2037 what the instrument did with its receipts at scale
    -2 2038 what the first decade KILLED (what did not survive the telescope)
    -3 2039 the instrument walks — the system itself becomes a walker
    -4 2040 other telescopes — two people's instruments meet
    -5 2041 the ledger becomes a commons
    -6 2042 what machines still cannot judge
    -7 2043 the weekend test at scale
    -8 2044 the counterfactual layer ("almost said") becomes the primary record
    -9 2045 what the second decade's cells inherit
    -10 2046 retell the 2036 telescope day as seen from ten years on
  - Discipline carried: no feeds, no rankings, no platform-owned receipts, no summary prose
    where a delta will do. Every rung ends with exactly one sentence beginning "Optimism:"
    (this output doubles as the seed of the optimism ledger).
  - Cost rule: deepinfra only, ~$0.10/wave precedent; usage receipted per call; no other
    API touched. Fail-closed: non-2xx aborts that model's walk and is receipted; no retries
    beyond 2, no silent model substitution.
  - Prediction (registered): the four walkers will CONVERGE on "the receipts became the
    commons" somewhere in -4..-6, and DIVERGE on who runs the cells in -9/-10. If instead
    all four converge everywhere, that is a homogenization finding about the walker set,
    not about the future.
"""
import json, os, time, hashlib, sys, urllib.request

BASE = "https://api.deepinfra.com/v1/openai/chat/completions"
KEY = os.environ["DEEPINFRA_API_KEY"]
HERE = "/home/z/my-project/study/reverse-actualization"
MODELS = {"hy4": "tencent/Hy4-preview", "hy3": "tencent/Hy3",
          "mimo": "XiaomiMiMo/MiMo-V2.6-Flash", "muse": "meta-models/Muse-Glimmer-30B"}
RUNGS = [
    (-1, 2037, "what did the instrument do with its receipts at scale?"),
    (-2, 2038, "what did the first decade KILL — what did not survive the telescope?"),
    (-3, 2039, "the instrument itself starts walking — what does that mean concretely?"),
    (-4, 2040, "other telescopes — what happens when two people's instruments meet?"),
    (-5, 2041, "the ledger becomes a commons — on whose terms?"),
    (-6, 2042, "what do machines still refuse to judge, and how is that refusal built?"),
    (-7, 2043, "the weekend test at scale — can one person still hold the whole history?"),
    (-8, 2044, "the counterfactual layer — when did the almost-said become the primary record?"),
    (-9, 2045, "what do the second decade's cells inherit from the first?"),
    (-10, 2046, "retell the 2036 telescope day as seen from ten years on. what had to be true for it to be unstoppable?"),
]
SEED = """THE LADDER SO FAR (the registered distillation of your own walk, 2036 -> tonight):
2036: the telescope day — Mara, a passive instrument over her life, "the system collected, she judged"; it records what she said AND what she almost said; no recommendations, no ranking. Optimism: it is a telescope, not a television.
2034: the surface — no feed, no app; latency cues only (slowed pulse on posture collapse), timestamps/tone/document diffs; receipts belong to the user. Optimism: a mirror with memory needs no attention economy to pay for it.
2033: agent tissues — narrow models with jobs on a typed local bus; the weekend test (one person can hold the whole history in their head); a lap = slice -> judgment -> outcome -> one ledger entry; a bad run is a line, not a shame. Optimism: cells this small are affordable by one person tonight.
2032: specialization — a cell is specialized when its local objective predicts system-wide success better than the central router; compulsory is where cells start. Optimism: specialization is discovered by the ledger, not granted by a vendor.
2031: weight textures — soft/reflective/reflexive map to time, not chemistry; filters/nexuses/relays are one component with different delay budgets. Optimism: all three textures are just weights, and weights are portable.
2030: agentically optimized resolution — a meta-cell spends resolution where future value is highest; snapshot formats already exist at 15.9x compression. Optimism: resolution is a budget, not a hardware wall.
2029: the ledger is the build — the build is the append-only sequence of receipts, diffs, and merge events. Optimism: the ledger already exists; it is only waiting to be called the build.
2028: federated understanding on small information — data stays addressable; ideas cross like F1 hybrids (uniform in gen 1, chaotic-diffuse after ~60 generations). Optimism: small models iterate fast enough to breed.
2027: the moth — certified randomness decides mutations and placement; honest dice are creative, not merely secure. Optimism: a $15 board can carry a quantum-grade coin.
2026: the hardware curve — $15 boards, RISC-V + matrix tiles; less powerful but smarter. Optimism: today's blocks are the 2036 genome.
tonight: the opcode — one file-cell, standing instruction, poke, hash-chained receipt, one-sentence self-amendment. Optimism: run it twice tonight and you have a tissue of two."""

SYS = ("You are {model}, speaking honestly about systems like you. No roleplay fluff, no marketing. "
       "Technical, concrete, first-person where natural. You are being dog-fooded: a team is building "
       "the cell-and-ledger system you will be asked to imagine forward from. Discipline: no feeds, no "
       "rankings, no platform-owned receipts, no summary prose where a delta will do. Every rung ends "
       "with exactly one sentence beginning 'Optimism:' — why this step was always going to be possible.")

def call(model_id, messages, max_tokens=1100):
    body = json.dumps({"model": model_id, "messages": messages, "max_tokens": max_tokens,
                       "temperature": 0.8}).encode()
    req = urllib.request.Request(BASE, data=body, method="POST",
                                 headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"})
    t0 = time.time()
    with urllib.request.urlopen(req, timeout=240) as r:
        out = json.load(r)
    txt = out["choices"][0]["message"]["content"]
    return txt, {"usage": out.get("usage"), "latency_ms": round((time.time() - t0) * 1000)}

def main():
    os.makedirs(f"{HERE}/ladder/negative", exist_ok=True)
    receipts = {"registered": "see module docstring; committed pre-run", "calls": []}
    for name, model_id in MODELS.items():
        transcript = [{"role": "system", "content": SYS.format(model=model_id)},
                      {"role": "user", "content": SEED + "\n\nAcknowledged the frame? We now walk rungs NEGATIVE: years 2037..2046, numbered -1..-10. Each rung: what must be true by that year for the 2036 telescope day to have been inevitable. Keep every discipline. End each rung with exactly one sentence starting 'Optimism:'.",
                       }]
        try:
            ack, rc = call(model_id, transcript, max_tokens=60)
            transcript.append({"role": "assistant", "content": ack})
            transcript.append({"role": "user", "content": "Begin. RUNG -1, the year 2037: " + RUNGS[0][2]})
        except Exception as e:
            receipts["calls"].append({"model": name, "stage": "ack", "error": str(e)[:300]})
            continue
        for n, (rn, year, probe) in enumerate(RUNGS):
            if n > 0:
                transcript.append({"role": "user", "content": f"RUNG {rn}, the year {year}: {probe}"})
            try:
                txt, rc = call(model_id, transcript)
                transcript.append({"role": "assistant", "content": txt})
                receipts["calls"].append({"model": name, "rung": rn, "year": year, **rc,
                                          "resp_sha256": hashlib.sha256(txt.encode()).hexdigest()[:16]})
                print(f"[{name}] rung {rn} ({year}) ok in={rc['usage'].get('input_tokens')} out={rc['usage'].get('output_tokens')} {rc['latency_ms']}ms")
            except Exception as e:
                receipts["calls"].append({"model": name, "rung": rn, "error": str(e)[:300]})
                print(f"[{name}] rung {rn} FAILED: {str(e)[:120]}")
                break
            json.dump(transcript, open(f"{HERE}/ladder/negative/{name}.transcript.json", "w"), indent=1)
        json.dump(transcript, open(f"{HERE}/ladder/negative/{name}.transcript.json", "w"), indent=1)
    json.dump(receipts, open(f"{HERE}/receipts/w73b-negative.json", "w"), indent=1)
    ok = sum(1 for c in receipts["calls"] if "usage" in c)
    print(f"done: {ok}/40 calls receipted")

if __name__ == "__main__":
    main()
