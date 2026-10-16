"""Rebuild the board's data from the CSV files in /data.

Computes:
  FP  - 2025-26 fantasy points per game in this league's scoring
  GM  - each team's games in fantasy playoff weeks 20-22
and writes them into index.html (the `const FP=` and `const GM=` lines).

Usage:  python scripts/build_data.py
"""
import csv, json, re, unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
INDEX = ROOT / "index.html"

# League scoring (Yahoo H2H points, this league's settings)
SCORING = {"pts": 1.0, "reb": 1.2, "ast": 1.5, "stl": 3.0, "blk": 3.0, "tov": -1.0}

# Fantasy playoff weeks (Mon-Sun). Check these against Yahoo > League > Schedule.
WEEKS = [("2027-03-15", "2027-03-21"),  # week 20
         ("2027-03-22", "2027-03-28"),  # week 21
         ("2027-03-29", "2027-04-04")]  # week 22

TEAM = {"Atlanta Hawks": "ATL", "Boston Celtics": "BOS", "Brooklyn Nets": "BKN", "Charlotte Hornets": "CHA",
        "Chicago Bulls": "CHI", "Cleveland Cavaliers": "CLE", "Dallas Mavericks": "DAL", "Denver Nuggets": "DEN",
        "Detroit Pistons": "DET", "Golden State Warriors": "GSW", "Houston Rockets": "HOU", "Indiana Pacers": "IND",
        "Los Angeles Clippers": "LAC", "Los Angeles Lakers": "LAL", "Memphis Grizzlies": "MEM", "Miami Heat": "MIA",
        "Milwaukee Bucks": "MIL", "Minnesota Timberwolves": "MIN", "New Orleans Pelicans": "NOP",
        "New York Knicks": "NYK", "Oklahoma City Thunder": "OKC", "Orlando Magic": "ORL",
        "Philadelphia 76ers": "PHI", "Phoenix Suns": "PHX", "Portland Trail Blazers": "POR",
        "Sacramento Kings": "SAC", "San Antonio Spurs": "SAS", "Toronto Raptors": "TOR", "Utah Jazz": "UTA",
        "Washington Wizards": "WAS"}


def norm(name):
    """Match names across sources: drop accents, suffixes (Jr., III) and punctuation."""
    n = unicodedata.normalize("NFD", name)
    n = "".join(c for c in n if unicodedata.category(c) != "Mn").lower()
    n = re.sub(r"\b(jr|sr|ii|iii|iv)\b\.?", "", n)
    return re.sub(r"[^a-z]", "", n)


def fantasy_points():
    stats = {}
    with open(DATA / "stats_2025-26.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            fp = sum(float(r[k]) * w for k, w in SCORING.items())
            stats[norm(r["player"])] = [round(fp, 1), int(r["games"])]
    board = (DATA / "expert_rank_titus_2026-09-29.txt").read_text(encoding="utf-8").splitlines()
    out, missing = {}, []
    for line in board:
        name = line.split("|")[0]
        if norm(name) in stats:
            out[name] = stats[norm(name)]
        else:
            missing.append(name)
    print(f"FP/G matched {len(out)} of {len(board)} players; no data for {len(missing)} (rookies, missed season, <9 ppg)")
    return out


def playoff_games():
    games = {t: [0, 0, 0] for t in TEAM.values()}
    with open(DATA / "schedule_fantasy_playoffs_2027.csv", newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f):
            for i, (a, b) in enumerate(WEEKS):
                if a <= r["date"] <= b:
                    games[TEAM[r["away"]]][i] += 1
                    games[TEAM[r["home"]]][i] += 1
    for t, g in sorted(games.items(), key=lambda kv: -sum(kv[1])):
        print(f"  {t}: {'-'.join(map(str, g))} = {sum(g)}")
    return games


def main():
    fp, gm = fantasy_points(), playoff_games()
    html = INDEX.read_text(encoding="utf-8")
    html, n1 = re.subn(r"^const FP=.*;$", "const FP=" + json.dumps(fp, ensure_ascii=False) + ";", html, flags=re.M)
    html, n2 = re.subn(r"^const GM=.*;$", "const GM=" + json.dumps(gm) + ";", html, flags=re.M)
    assert n1 == 1 and n2 == 1, "Could not find the FP/GM lines in index.html"
    INDEX.write_text(html, encoding="utf-8")
    print("Updated index.html")


if __name__ == "__main__":
    main()
