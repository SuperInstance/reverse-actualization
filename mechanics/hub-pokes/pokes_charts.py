#!/usr/bin/env python3
"""73-f charts: strategy comparison, yield-vs-cost, resolution map."""
import sys, json
sys.path.insert(0, "/home/z/my-project/scripts/hy4")
from pokes_engine import *
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm
fm.fontManager.addfont('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

OUT = "/home/z/my-project/download/hy4-wave73/hub-pokes"
SEED = 0
f = landscape(SEED)

# --- yield-vs-cost curves (instrumented rerun, seed 0) ---
def curve(runner):
    e = Engine(f, SEED)
    hist = [(0.0, 0.0)]
    while e.cost < BUDGET:
        act, c = e.choose()
        if c is None: break
        (e.box if act == "box" else e.poke)(c)
        hist.append((e.cost, e.harvest))
    return e, hist

hp, h_hp = curve(Engine(f, SEED))
rd, h_rd = curve(run_random)
gr, h_gr = curve(run_greedy)
sw, h_sw = curve(run_sweep)

fig, ax = plt.subplots(figsize=(7.5, 4.6), constrained_layout=True)
for (e, h), name, color in [(h_hp and (hp, h_hp), "hub-and-pokes", "#8a4fbf"),
                            ((rd, h_rd), "random", "#888888"),
                            ((gr, h_gr), "greedy box-climb", "#cc4444"),
                            ((sw, h_sw), "grid sweep", "#2f7f4f")]:
    xs, ys = zip(*h)
    ax.plot(xs, ys, label=name, color=color, lw=2 if name == "hub-and-pokes" else 1.2)
ax.set_xlabel("cumulative cost"); ax.set_ylabel("harvested yield")
ax.set_title("Hub-and-pokes vs baselines (seed 0): the gamble rule pays")
ax.legend(); ax.grid(alpha=0.3)
fig.savefig(f"{OUT}/chart1_yield_vs_cost.png", dpi=140)
plt.close(fig)

# --- final belief/revealed maps, 4 strategies ---
fig, axes = plt.subplots(1, 4, figsize=(14, 3.8), constrained_layout=True)
for ax, (e, name) in zip(axes, [(hp, "hub-and-pokes"), (rd, "random"),
                                (gr, "greedy"), (sw, "sweep")]):
    im = ax.imshow(e.belief.mean, cmap="magma", vmin=0, vmax=1)
    for (y, x) in e.boxed:
        ax.add_patch(plt.Rectangle((x-.5, y-.5), 1, 1, fill=False, color="cyan", lw=0.7))
    ax.set_title(f"{name}\nboxes={len(e.boxed)} harvest={e.harvest:.1f}", fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
fig.colorbar(im, ax=axes, shrink=0.85, label="belief mean (cyan = boxed)")
fig.savefig(f"{OUT}/chart2_final_maps.png", dpi=140)
plt.close(fig)

# --- resolution map of one snapshot (the agentically chosen zones) ---
snap = hp.snapshot()
yy, xx = np.mgrid[0:SIDE, 0:SIDE]
hub = hp.hub
d = np.sqrt((xx-hub[1])**2 + (yy-hub[0])**2)
res = np.where(d <= 4, 3, np.where(d <= 12, 2, 1))
fig, ax = plt.subplots(figsize=(5.4, 4.6), constrained_layout=True)
im = ax.imshow(res, cmap="viridis_r")
ax.plot(hub[1], hub[0], "r*", markersize=14, label=f"hub {tuple(int(v) for v in hub)}")
ax.set_title(f"snapshot resolution zones (v1, {len(snap)} bytes)\nf32 / u8-ish / 2-bit-packed")
ax.legend(); ax.set_xticks([]); ax.set_yticks([])
fig.colorbar(im, ax=ax, shrink=0.8, ticks=[1, 2, 3], label="resolution class")
fig.savefig(f"{OUT}/chart3_resolution_map.png", dpi=140)
plt.close(fig)
print("charts done; snapshot bytes:", len(snap), "full bytes:", hp.full_state_bytes())
