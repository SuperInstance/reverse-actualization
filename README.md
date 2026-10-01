# Reverse Actualization ✨

You start from the future you want and work backward to find the steps that cannot be skipped. This service takes your target end state and returns only the strictly required prior conditions. It provides no suggestions, advice, or optional tasks.

A public test instance is available. Send a POST request with JSON `{ "targetState": "your end state" }` to:
`https://reverse-actualization.casey-digennaro.workers.dev`
Fair use rate limits apply.

## Why This Exists
Most planning tools build forward from the present, which can overwhelm you with possibilities. This tool is for when you need to know only the steps that will absolutely block your goal if they are missed.

## Quick Start
1.  **Fork this repository.** This is a fork-first project; you must start with your own copy.
2.  **Deploy:** Authenticate with `npx wrangler login` and deploy using `npx wrangler deploy`.
3.  **Edit the logic:** Replace the placeholder `deriveRequiredSteps` function in `src/index.js` with your own backward-chaining rules.

Your private instance will be live in about a minute.

## Architecture
A single, zero-dependency Cloudflare Worker. All backward reasoning logic is contained in one plain JavaScript function that you edit directly. There are no frameworks or hidden abstraction layers.

## Features
- **Backward reasoning pattern:** Returns only mandatory prerequisites.
- **Minimal footprint:** Deployed size under 10KB. Typical cold start times under 50ms on Cloudflare's network.
- **Fork-first independence:** Your instance is yours; upstream changes will not affect it.
- **Fleet-native:** Callable by any Cocapn Fleet agent or tool via a standalone JSON endpoint.
- **Transparent logic:** Every rule that executes is in the single function you edit.

## What Makes This Different
1.  It returns only what you *must* do, never what you *could* do.
2.  You own the instance after forking—no sign-ups, accounts, or ongoing costs.
3.  There is no black box. The entire logic is in the open function you control.

## Limitation
All your backward-chaining rules must be written into the single `deriveRequiredSteps` function. While this keeps the system simple, complex rule sets with many interdependent conditions can become difficult to organize and maintain in one place.


## Dog-Fooded: the SuperInstance fleet's own reverse-actualization (Wave 73)

We took this method and pointed it at our own 2036 system, walking
piece-by-piece from "a person whose intelligence is superimposed — a
telescope, not a television" down to tonight's opcode, with every step
back carrying one sentence of optimism. Four featured models walked the
same 11-rung ladder (`wave73-LADDER.md` + `ladder/` transcripts):
**tencent/Hy4-preview** (featured this wave), tencent/Hy3,
XiaomiMiMo/MiMo-V2.6-Flash, meta-models/Muse-Glimmer-30B.

Alongside the ladder: a micromoth-quilt F1-cross simulation seeded with
live hardware entropy (`mechanics/mothquilt-f1`), the hub-and-pokes
MineSweeper-style inquiry engine with snapshots at agentically optimized
resolution (`mechanics/hub-pokes`), a 26-lead scouting report on
fruit-fly decompositions toward mechanical learning (`scouting/`), and
the thesis re-rooted in six distant languages (`ideation/`). Run
receipts, including every instrument bug found on the way, are in
`receipts/`.

> Rung 10, the consensus homunculus: *one file-cell with a standing
> instruction; a poke; a receipt appended and never rewritten; a
> one-sentence self-amendment. Run it twice tonight and you have a
> tissue of two. Run three cells trading receipts and you have ripple.*

## License
MIT license. You are free to use, modify, and redistribute this code for any purpose.

## Credits
Original concept by Superinstance and Lucineer (DiGennaro et al.).

<div style="text-align:center;padding:16px;color:#64748b;font-size:.8rem"><a href="https://the-fleet.casey-digennaro.workers.dev" style="color:#64748b">The Fleet</a> &middot; <a href="https://cocapn.ai" style="color:#64748b">Cocapn</a></div>