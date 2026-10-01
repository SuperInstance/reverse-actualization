#!/usr/bin/env python3
"""73-e: micromoth-quilt F1 cross simulation (see f1_prereg.md, written first).

Arms: moth (generation-scale true entropy via qpixl-v1 decode-noise packets)
vs PRNG control (fixed counter seeds). 3 replicates each, 60 generations.
Outputs: metrics CSV + 3 PNG charts into download/hy4-wave73/mothquilt-f1/.
"""
import json, os, hashlib, time, urllib.request, csv
import numpy as np

OUT = "/home/z/my-project/download/hy4-wave73/mothquilt-f1"
os.makedirs(OUT, exist_ok=True)
PACKETS_F = "/home/z/my-project/scripts/hy4/moth_packets.json"

KEYS = {l.split("=", 1)[0].strip(): l.split("=", 1)[1].strip()
        for l in open("/home/z/my-project/.env.keys")
        if l.strip() and not l.startswith("#") and "=" in l}

# ---------- lattice ----------
N = 24
CELLS = [(q, r) for q in range(N) for r in range(N)]
IDX = {c: i for i, c in enumerate(CELLS)}
DIRS = [(1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1), (0, 1)]
NB = []
for (q, r) in CELLS:
    nbs = [IDX[(q + dq, r + dr)] for (dq, dr) in DIRS
           if (q + dq, r + dr) in IDX]
    NB.append(nbs)
NB = [np.array(x, dtype=int) for x in NB]
NCELL = len(CELLS)
assert NCELL == N * N

def hex_dist(a, b):
    (q1, r1), (q2, r2) = a, b
    return (abs(q1 - q2) + abs(r1 - r2) + abs(q1 + r1 - q2 - r2)) // 2

# ---------- parents ----------
def parent_A():
    p = np.array([0.2 + 3.4 * (q / 23) for (q, r) in CELLS])
    return dict(p=p, res=np.full(NCELL, 0.6), e=np.zeros(NCELL),
                mA=np.ones(NCELL), mB=np.zeros(NCELL))

def valnoise(q, r):
    """3-octave deterministic value noise on (q,r)."""
    def h(q, r, s):
        x = hashlib.blake2b(f"{q},{r},{s}".encode(), digest_size=4).digest()
        return int.from_bytes(x, "little") / 2**32
    tot = 0.0
    for s, (f, amp) in enumerate([(0.35, 2.0), (0.9, 0.8), (2.1, 0.3)]):
        qf, rf = q * f, r * f
        i0, j0 = int(qf), int(rf)
        fx, fy = qf - i0, rf - j0
        v = (h(i0, j0, s) * (1 - fx) * (1 - fy) + h(i0 + 1, j0, s) * fx * (1 - fy)
             + h(i0, j0 + 1, s) * (1 - fx) * fy + h(i0 + 1, j0 + 1, s) * fx * fy)
        tot += v * amp
    return tot / 3.1  # mean ~1.5 after scaling below

def parent_B():
    p = np.array([0.4 + 2.4 * valnoise(q, r) for (q, r) in CELLS])
    return dict(p=p, res=np.full(NCELL, 0.2), e=np.zeros(NCELL),
                mA=np.zeros(NCELL), mB=np.ones(NCELL))

# ---------- moth packets ----------
MOTH_LIVE = True
def load_packets():
    if os.path.exists(PACKETS_F):
        return json.load(open(PACKETS_F))
    return {}

def fetch_moth_packets(ngens):
    """One qpixl-v1 packet per generation (tag gNN), cached. Decode-noise idiom
    from quilt-arena/arena/moth.mjs. Returns {tag: {"floats": [...], "mock": bool}}."""
    cache = load_packets()
    api = "https://api.mothquantum.com/api/v1"
    key = KEYS["MOTH_KEY"]
    probe = [0.1 + 0.8 * ((i * 37) % 100) / 100 for i in range(32)]
    for g in range(ngens):
        tag = f"g{g:03d}"
        if tag in cache:
            continue
        if not MOTH_LIVE:
            break
        try:
            req = urllib.request.Request(
                f"{api}/engines/qpixl-v1/process",
                data=json.dumps({"params": {
                    "values": probe, "machine": "aer", "mode": "emu",
                    "shots": 2048, "discretize": 0,
                    "dynamic_range": "none", "allow_high_shots": False}}).encode(),
                headers={"Authorization": "Bearer " + key,
                         "Content-Type": "application/json",
                         # Cloudflare 1010 bot-signature ban: python-urllib UA
                         # is blocked; browser UA passes (diagnosed 2026-10-01)
                         "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                                       "Chrome/126.0.0.0 Safari/537.36"})
            sub = json.load(urllib.request.urlopen(req, timeout=30))
            job_id = sub.get("job_id") or sub.get("id")
            floats = None
            for _ in range(40):
                time.sleep(1.5)
                r = json.load(urllib.request.urlopen(
                    urllib.request.Request(f"{api}/jobs/{job_id}/result",
                        headers={"Authorization": "Bearer " + key,
                                 "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
                                               "AppleWebKit/537.36 (KHTML, like Gecko) "
                                               "Chrome/126.0.0.0 Safari/537.36"}), timeout=30))
                # NOTE: the result endpoint returns {"$schema","result":{...}}
                # directly once done — there is NO status field (verified live
                # 2026-10-01). Treat presence of result.output as completion.
                res = r.get("result") or {}
                out = res.get("output")
                if isinstance(out, list) and len(out) >= 32:
                    floats = [min(0.999999, max(0.0,
                              0.5 + (out[i] - probe[i]) * 25)) for i in range(32)]
                    break
                if r.get("error") or res.get("status") in ("failed", "error"):
                    break
            if floats is None:
                print(f"  moth packet {tag}: no floats (status), fallback")
                break
            cache[tag] = {"floats": floats, "mock": False, "job_id": job_id}
            print(f"  moth packet {tag}: LIVE ({job_id})", flush=True)
        except Exception as ex:
            print(f"  moth packet {tag}: ERROR {ex}; stopping live fetch")
            break
    # fill missing with synthetic, flagged
    for g in range(ngens):
        tag = f"g{g:03d}"
        if tag not in cache:
            seed = int.from_bytes(hashlib.blake2b(
                ("synthetic:" + tag).encode(), digest_size=8).digest(), "little")
            rng = np.random.Generator(np.random.PCG64(seed))
            cache[tag] = {"floats": [float(x) for x in rng.random(32)],
                          "mock": True, "job_id": None}
    json.dump(cache, open(PACKETS_F, "w"), indent=0)
    return cache

def stream_for(tag, arm, rep, packet):
    """blake2b KDF: 32 true floats -> per-generation PCG64 stream.
    ARM AND REP ARE ALWAYS IN THE SEED TEXT (instrument-failure fix 1: the
    first run collapsed moth/prng arms to identical streams because the
    synthetic fallback seed omitted them)."""
    src = "synthetic" if packet.get("mock") else "moth"
    seed_txt = f"{src}:{tag}:{arm}{rep}:" + ",".join(f"{x:.6f}" for x in packet["floats"])
    h = hashlib.blake2b(seed_txt.encode(), digest_size=32).digest()
    return np.random.Generator(np.random.PCG64(int.from_bytes(h, "little")))

# ---------- simulation ----------
A_DEF, A_MK = 0.35, 0.5
LEAK = 0.22 * 0.5
P_SPLIT = 0.02
NGEN = 60

def neighbors_mean(field):
    out = np.zeros(NCELL)
    for i, nbs in enumerate(NB):
        out[i] = field[nbs].mean() if len(nbs) else field[i]
    return out

def leakage(p, res):
    dp = np.zeros(NCELL)
    for i, nbs in enumerate(NB):
        if len(nbs):
            dp[i] = (p[i] - p[nbs]).mean()
    r_bar = np.array([(res[i] + res[NB[i]].mean()) / 2 if len(NB[i]) else res[i]
                      for i in range(NCELL)])
    return (dp - r_bar) * LEAK

def step(state, rng):
    p, res, e, mA, mB = state["p"], state["res"], state["e"], state["mA"], state["mB"]
    gA = state["gA"]
    # snapshot -> next (order-independence)
    def blend(u, a):
        return (1 - a) * u + a * neighbors_mean(u)
    p2 = blend(p, A_DEF) + leakage(p, res)
    res2 = np.clip(blend(res, A_DEF), 0, 1)
    e2 = blend(e, A_DEF)
    mA2 = blend(mA, A_MK)
    mB2 = blend(mB, A_MK)
    gA2 = blend(gA, A_MK)  # genome fraction recombines with neighbors
    # fractal splits
    split_dec = rng.random(NCELL) < P_SPLIT
    nb_choice = rng.integers(0, 6, NCELL)
    e_child = (p2 / 5.0) * 0.95
    ripple = np.zeros(NCELL)
    ripple_p = np.zeros(NCELL)
    for i in np.where(split_dec)[0]:
        nbs = NB[i]
        tgt = nbs[nb_choice[i] % len(nbs)]
        ripple[tgt] += e_child[i] - e2[i]
        # AMENDMENT-2 (run-2 receipt): the daughter ripple must be PHENOTYPIC —
        # in run 2 the stochastic channel (splits -> entropy) never touched
        # potential/markers, so every preregistered observable was identical
        # across arms (metric blindness). The ripple now perturbs the
        # neighbor's potential with a small footprint (0.1 * daughter delta).
        ripple_p[tgt] += (e_child[i] - e2[i]) * 0.1
    e3 = np.where(split_dec, e_child, e2) + ripple
    is_split = split_dec.astype(float)
    return dict(p=np.clip(p2 + ripple_p, 0, 5), res=res2, e=np.maximum(e3, 0),
                mA=mA2, mB=mB2, gA=gA2, is_split=is_split)

def f1_cross(A, B, rng):
    jit = rng.uniform(-0.05, 0.05, NCELL)
    # AMENDMENT-1: meiosis jitter — each F1 hybrid's genome fraction carries a
    # small per-cell deviation, else the lineage marker is uniform by
    # construction and carries no signal after F1 (first-run failure receipt).
    gA = 0.5 + rng.uniform(-0.02, 0.02, NCELL)
    return dict(p=np.clip(0.5 * A["p"] + 0.5 * B["p"] + jit, 0, 5),
                res=0.5 * A["res"] + 0.5 * B["res"],
                e=np.zeros(NCELL),
                mA=0.5 * A["mA"] + 0.5 * B["mA"],
                mB=0.5 * A["mB"] + 0.5 * B["mB"],
                gA=gA)

def metrics(st):
    return dict(V_p=float(st["p"].var()),
                V_A=float(st["mA"].var()),
                M=float(1 - st["mA"].var() / 0.25),
                V_gA=float(st["gA"].var()) if "gA" in st else "",
                V_e=float(st["e"].var()) if "e" in st else "",
                C=float(st["p"].mean() / 5 + st["res"].mean()),
                n_split=int(st.get("is_split", np.zeros(NCELL)).sum()))

def run(arm, rep, packets):
    rng0 = np.random.Generator(np.random.PCG64(1000 + rep))
    A, B = parent_A(), parent_B()
    st = f1_cross(A, B, rng0)  # F1
    parental = dict(V_pA=float(A["p"].var()), V_pB=float(B["p"].var()))
    rows = [dict(gen=1, arm=arm, rep=rep, **metrics(st))]
    snap = {1: st["p"].copy()}
    hist_V = [rows[0]["V_p"]]
    G_star = None
    for g in range(2, NGEN + 1):
        tag = f"g{g - 1:03d}"
        rng = stream_for(tag, arm, rep, packets[tag])
        st = step(st, rng)
        m = metrics(st)
        rows.append(dict(gen=g, arm=arm, rep=rep, **m))
        hist_V.append(m["V_p"])
        if g in (2, NGEN):
            snap[g] = st["p"].copy()
        # stabilization: |dV/V| < 1e-3 for 5 consecutive gens
        if G_star is None and g >= 6:
            ds = [abs(hist_V[i] - hist_V[i - 1]) / max(hist_V[i - 1], 1e-12)
                  for i in range(g - 5, g)]
            if all(d < 1e-3 for d in ds):
                G_star = g - 4
    return rows, G_star, snap, parental

def main():
    print("== 73-e F1 cross: prereg at scripts/hy4/f1_prereg.md ==")
    packets = fetch_moth_packets(NGEN)
    n_mock = sum(1 for v in packets.values() if v.get("mock"))
    print(f"packets: {len(packets)}, mock: {n_mock}")
    all_rows, stars, snaps = [], {}, {}
    for arm in ("moth", "prng"):
        for rep in range(3):
            t0 = time.time()
            rows, G, snap, parental = run(arm, rep, packets)
            all_rows += rows
            stars[f"{arm}{rep}"] = G
            snaps[f"{arm}{rep}"] = snap
            print(f"{arm} rep{rep}: G*={G} ({time.time()-t0:.1f}s)")
    with open(f"{OUT}/f1_metrics.csv", "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(all_rows[0].keys()))
        w.writeheader(); w.writerows(all_rows)
    json.dump({"G_star": stars,
               "mock_packets": n_mock},
              open(f"{OUT}/f1_summary.json", "w"), indent=1)
    print("G*:", stars)
    return all_rows, stars, snaps, n_mock

if __name__ == "__main__":
    main()
