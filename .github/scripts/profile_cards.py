"""Draw the profile README stat cards (desk / scrapbook theme) from the GitHub GraphQL API.

Usage: GITHUB_TOKEN=... python profile_cards.py <out_dir> <main_user> <work_user>
Writes stats.svg, langs.svg and work.svg. Standard library only.
"""
import base64
import datetime as dt
import json
import os
import sys
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
INK, CREAM, RED, BLUE, OLIVE, PURPLE, ORANGE, YELLOW, GREEN = (
    "#1b1b1b", "#f3f1ea", "#d33a36", "#2a2fd0", "#6f7f2b", "#7b3a7d", "#df7a2c", "#f0c43a", "#1d6a44")
MUTED = "#4a4636"
LANG_COLORS = [RED, BLUE, OLIVE, PURPLE, ORANGE, GREEN, "#c99a1e", "#5b5440"]


def gql(query, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": query, "variables": variables}).encode(),
        headers={"Authorization": f"bearer {os.environ['GITHUB_TOKEN']}", "Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=30) as r:
        body = json.load(r)
    if body.get("errors"):
        raise RuntimeError(body["errors"])
    return body["data"]


MAIN_Q = """
query($login: String!) {
  user(login: $login) {
    followers { totalCount }
    pullRequests { totalCount }
    issues { totalCount }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
      contributionCalendar { totalContributions }
    }
    repositories(ownerAffiliations: OWNER, isFork: false, first: 100) {
      totalCount
      nodes {
        stargazerCount
        languages(first: 10, orderBy: {field: SIZE, direction: DESC}) { edges { size node { name } } }
      }
    }
  }
}"""

WORK_Q = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      restrictedContributionsCount
      contributionCalendar { totalContributions weeks { contributionDays { contributionCount date } } }
    }
  }
}"""


def esc(s):
    return str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def fonts_css():
    out = []
    for fam, wt, f in [("Bagel", 400, "bagel.woff2"), ("SMono", 400, "spacemono.woff2"), ("SMono", 700, "spacemono-bold.woff2")]:
        with open(os.path.join(HERE, "fonts", f), "rb") as fh:
            b64 = base64.b64encode(fh.read()).decode()
        out.append(f"@font-face{{font-family:'{fam}';font-weight:{wt};src:url(data:font/woff2;base64,{b64}) format('woff2')}}")
    return "".join(out) + ".b{font-family:Bagel,sans-serif}.m{font-family:SMono,monospace}.mb{font-family:SMono,monospace;font-weight:700}"


def card(w, h, title, label, body):
    """Cream paper card with a hard shadow and a tape strip."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{esc(label)}">'
            f'<title>{esc(label)}</title><style>{fonts_css()}</style>'
            f'<rect x="10" y="12" width="{w-12}" height="{h-14}" fill="rgba(0,0,0,.25)"/>'
            f'<rect x="2" y="2" width="{w-12}" height="{h-14}" fill="{CREAM}" stroke="{INK}" stroke-width="4"/>'
            f'<rect x="{w/2-50}" y="-6" width="100" height="22" fill="rgba(240,196,58,.85)" transform="rotate(-3 {w/2} 4)"/>'
            f'<text x="24" y="44" class="b" font-size="24" fill="{RED}">{esc(title)}</text>'
            f'{body}</svg>')


def fmt(n):
    return f"{n/1000:.1f}k" if n >= 10000 else f"{n:,}"


def stats_card(u, login):
    repos = u["repositories"]
    cc = u["contributionsCollection"]
    rows = [
        ("Contributions (last year)", cc["contributionCalendar"]["totalContributions"], BLUE),
        ("Commits (last year)", cc["totalCommitContributions"] + cc["restrictedContributionsCount"], RED),
        ("Pull requests", u["pullRequests"]["totalCount"], PURPLE),
        ("Public repos", repos["totalCount"], OLIVE),
        ("Stars earned", sum(n["stargazerCount"] for n in repos["nodes"]), ORANGE),
    ]
    body = ""
    for i, (lab, val, col) in enumerate(rows):
        y = 84 + i * 30
        body += (f'<text x="26" y="{y}" class="m" font-size="15" fill="{MUTED}">{esc(lab)}</text>'
                 f'<line x1="26" y1="{y+9}" x2="440" y2="{y+9}" stroke="{INK}" stroke-opacity=".12" stroke-width="1.5" stroke-dasharray="4 4"/>'
                 f'<text x="440" y="{y+2}" class="b" font-size="22" fill="{col}" text-anchor="end">{fmt(val)}</text>')
    return card(470, 250, f"@{login} · stats", f"GitHub stats for {login}", body)


def langs_card(u, login):
    totals = {}
    for repo in u["repositories"]["nodes"]:
        for e in repo["languages"]["edges"]:
            totals[e["node"]["name"]] = totals.get(e["node"]["name"], 0) + e["size"]
    top = sorted(totals.items(), key=lambda kv: -kv[1])[:6]
    whole = sum(v for _, v in top) or 1
    x, bar = 26.0, ""
    for i, (_, v) in enumerate(top):
        w = 390 * v / whole
        bar += f'<rect x="{x:.1f}" y="66" width="{w:.1f}" height="20" fill="{LANG_COLORS[i]}"/>'
        x += w
    bar += f'<rect x="26" y="66" width="390" height="20" fill="none" stroke="{INK}" stroke-width="3"/>'
    legend = ""
    for i, (name, v) in enumerate(top):
        name = {"Jupyter Notebook": "Jupyter"}.get(name, name)
        name = name if len(name) <= 13 else name[:12] + "."
        cx, cy = 26 + (i % 2) * 200, 120 + (i // 2) * 34
        legend += (f'<rect x="{cx}" y="{cy-12}" width="14" height="14" fill="{LANG_COLORS[i]}" stroke="{INK}" stroke-width="2"/>'
                   f'<text x="{cx+22}" y="{cy}" class="mb" font-size="14" fill="{INK}">{esc(name)}</text>'
                   f'<text x="{cx+180}" y="{cy}" class="m" font-size="13" fill="{MUTED}" text-anchor="end">{100*v/whole:.1f}%</text>')
    if not top:
        legend = f'<text x="26" y="130" class="m" font-size="14" fill="{MUTED}">No language data yet</text>'
    return card(442, 250, "top languages", f"Top languages for {login}", bar + legend)


def work_card(u, login):
    cc = u["contributionsCollection"]
    cal = cc["contributionCalendar"]
    weeks = [sum(d["contributionCount"] for d in w["contributionDays"]) for w in cal["weeks"]][-52:]
    peak = max(weeks) if weeks else 0
    W, H = 920, 250
    x0, y0, cw, ch = 300, 70, 590, 140
    bars = ""
    step = cw / max(len(weeks), 1)
    for i, n in enumerate(weeks):
        h = 0 if not peak else max(3, ch * n / peak) if n else 2
        col = BLUE if n else "#d9d4c4"
        bars += f'<rect x="{x0 + i*step:.1f}" y="{y0 + ch - h:.1f}" width="{step-3:.1f}" height="{h:.1f}" fill="{col}"/>'
    bars += f'<line x1="{x0}" y1="{y0+ch+1}" x2="{x0+cw}" y2="{y0+ch+1}" stroke="{INK}" stroke-width="3"/>'
    first_day = cal["weeks"][-len(weeks)]["contributionDays"][0]["date"] if weeks else ""
    month = dt.date.fromisoformat(first_day).strftime("%b %Y") if first_day else ""
    bars += (f'<text x="{x0}" y="{y0+ch+24}" class="m" font-size="12" fill="{MUTED}">{esc(month)}</text>'
             f'<text x="{x0+cw}" y="{y0+ch+24}" class="m" font-size="12" fill="{MUTED}" text-anchor="end">this week</text>')
    active = sum(1 for n in weeks if n)
    left = (f'<text x="26" y="132" class="b" font-size="68" fill="{BLUE}">{fmt(cal["totalContributions"])}</text>'
            f'<text x="28" y="160" class="m" font-size="14" fill="{MUTED}">contributions, last 12 months</text>'
            f'<text x="28" y="186" class="mb" font-size="14" fill="{INK}">{active} active weeks · peak {peak}/wk</text>'
            f'<text x="28" y="210" class="m" font-size="12" fill="{MUTED}">mostly private startup repos</text>')
    return card(W, H, f"work account · @{login}", f"Work account activity for {login}: {cal['totalContributions']} contributions in the last year", left + bars)


def main():
    out, main_user, work_user = sys.argv[1], sys.argv[2], sys.argv[3]
    os.makedirs(out, exist_ok=True)
    if os.environ.get("CARDS_FIXTURE"):
        with open(os.environ["CARDS_FIXTURE"]) as fh:
            fx = json.load(fh)
        mu, wu = fx["main"], fx["work"]
    else:
        mu = gql(MAIN_Q, {"login": main_user})["user"]
        wu = gql(WORK_Q, {"login": work_user})["user"]
    for name, svg in [("stats.svg", stats_card(mu, main_user)), ("langs.svg", langs_card(mu, main_user)),
                      ("work.svg", work_card(wu, work_user))]:
        with open(os.path.join(out, name), "w") as fh:
            fh.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
