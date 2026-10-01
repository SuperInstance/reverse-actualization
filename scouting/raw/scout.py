#!/usr/bin/env python3
"""73-g fruit-fly scouting: web fallback scraper.

z-ai web_search upstream returned 429/400 errors and then degraded results
(1 truncated-URL hit per query), so this script implements the task's
fallback: curl-based DuckDuckGo HTML search + arXiv API queries.
No LLM APIs are called. No API keys used.
"""
import json, re, time, random, urllib.parse, urllib.request, sys

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0 Safari/537.36"

def http_get(url, timeout=30):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", errors="replace")

def ddg(query):
    """DuckDuckGo HTML search -> list of {title,url,snippet}."""
    q = urllib.parse.quote_plus(query)
    html = http_get(f"https://html.duckduckgo.com/html/?q={q}")
    out = []
    # results are in <a rel="nofollow" class="result__a" href="//duckduckgo.com/l/?uddg=ENCODED&...">TITLE</a>
    # snippets: <a class="result__snippet" ...>SNIPPET</a>
    for m in re.finditer(r'class="result__a"[^>]*href="([^"]+)"[^>]*>(.*?)</a>(.*?)(?=class="result__a"|class="result__footer"|$)', html, re.S):
        href, title, rest = m.group(1), m.group(2), m.group(3)
        u = urllib.parse.unquote(href)
        mm = re.search(r"uddg=([^&]+)", u)
        if mm:
            u = urllib.parse.unquote(mm.group(1))
        title = re.sub(r"<[^>]+>", "", title).strip()
        sn = re.search(r'class="result__snippet"[^>]*>(.*?)</a>', rest, re.S)
        snippet = re.sub(r"<[^>]+>", "", sn.group(1)).strip() if sn else ""
        out.append({"title": title, "url": u, "snippet": snippet[:400]})
    return out

def arxiv(query, maxr=4):
    q = urllib.parse.quote(query)
    xml = http_get(f"https://export.arxiv.org/api/query?search_query={q}&max_results={maxr}&sortBy=relevance")
    out = []
    for m in re.finditer(r"<entry>(.*?)</entry>", xml, re.S):
        e = m.group(1)
        t = re.search(r"<title>(.*?)</title>", e, re.S)
        i = re.search(r"<id>(.*?)</id>", e)
        s = re.search(r"<summary>(.*?)</summary>", e, re.S)
        d = re.search(r"<published>(.*?)</published>", e)
        out.append({"title": re.sub(r"\s+", " ", t.group(1)).strip() if t else "",
                    "url": i.group(1).strip() if i else "",
                    "snippet": re.sub(r"\s+", " ", s.group(1)).strip()[:500] if s else "",
                    "date": d.group(1)[:10] if d else ""})
    return out

DDG_QUERIES = {
    # Thread 1: drosophila
    "t1_fly_connectome": "drosophila connectome mushroom body Kenyon cells sparse code",
    "t1_flywire": "FlyWire complete connectome adult fruit fly brain 2024",
    "t1_lateral_horn": "lateral horn innate odor circuits fruit fly hardwired",
    "t1_mb_dopamine": "mushroom body dopamine reward prediction error MBON valuation",
    # Thread 2: minimal organisms
    "t2_ceil": "C. elegans learning 302 neurons simple organism associative learning",
    "t2_physarum": "Physarum polycephalum slime mold network routing computation",
    "t2_aplysia": "Aplysia single neuron habituation synaptic plasticity Kandel",
    "t2_homeostat": "homeostatic plasticity synaptic scaling stability",
    # Thread 3: tiny iterative systems
    "t3_moe": "mixture of experts modular small expert models",
    "t3_ttt": "test-time training learning at inference time",
    "t3_reservoir": "reservoir computing echo state network few nodes small data",
    "t3_hyper": "hypernetworks generate weights of smaller networks",
    # Thread 4: mechanical learning
    "t4_forwardforward": "forward-forward algorithm Hinton learning without backpropagation",
    "t4_predcoding": "predictive coding local learning rule neuroscience-inspired",
    "t4_oja": "Oja rule Hebbian local learning principal component",
    "t4_rstdp": "reward-modulated STDP spiking local learning",
    "t4_ca": "learning in cellular automata differentiable cellular automata self-organizing",
    # Thread 5: data for the user
    "t5_flywheel": "personal data flywheel on-device memory local-first AI",
    "t5_telescope": "personal computing instrument telescope not television augment thinking",
    "t5_tinyml": "tinyML on-device learning microcontroller",
}

ARXIV_QUERIES = {
    "a1_ff": 'ti:"forward-forward" OR abs:"forward-forward algorithm"',
    "a1_predcoding": 'abs:"predictive coding" AND abs:"local learning"',
    "a1_oja": 'abs:"Oja" AND abs:"Hebbian"',
    "a1_rstdp": 'abs:"reward-modulated"',
    "a1_reservoir": 'abs:"reservoir computing" AND abs:"echo state"',
    "a1_ttt": 'abs:"test-time training"',
    "a1_hypernet": 'abs:"hypernetwork"',
    "a1_ca": 'abs:"cellular automata" AND abs:"differentiable"',
    "a1_connectome": 'abs:"connectome" AND abs:"learning"',
    "a1_kenyon": 'abs:"Kenyon cells"',
    "a1_homeostat": 'abs:"homeostatic plasticity"',
    "a1_moe": 'abs:"mixture of experts" AND abs:"modular"',
    "a1_tinyml": 'abs:"tiny machine learning" OR abs:"tinyML"',
    "a1_physarum": 'abs:"Physarum"',
    "a1_flywire": 'abs:"Drosophila" AND abs:"connectome"',
}

if __name__ == "__main__":
    all_out = {"ddg": {}, "arxiv": {}, "failures": []}
    only = sys.argv[1] if len(sys.argv) > 1 else "all"
    if only in ("all", "ddg"):
        for key, q in DDG_QUERIES.items():
            for attempt in range(3):
                try:
                    res = ddg(q)
                    all_out["ddg"][key] = {"query": q, "results": res[:8]}
                    print(f"ddg {key}: {len(res)} results")
                    break
                except Exception as e:
                    all_out["failures"].append(f"ddg:{key}:attempt{attempt}:{e}")
                    print(f"ddg {key} attempt {attempt} FAILED: {e}")
                    time.sleep(6 + attempt * 6)
            time.sleep(2.5 + random.random() * 2)
    if only in ("all", "arxiv"):
        for key, q in ARXIV_QUERIES.items():
            try:
                res = arxiv(q)
                all_out["arxiv"][key] = {"query": q, "results": res}
                print(f"arxiv {key}: {len(res)} results")
            except Exception as e:
                all_out["failures"].append(f"arxiv:{key}:{e}")
                print(f"arxiv {key} FAILED: {e}")
            time.sleep(1.5)
    with open("fallback_scrape.json", "w") as f:
        json.dump(all_out, f, indent=1)
    print("WROTE fallback_scrape.json; failures:", len(all_out["failures"]))
