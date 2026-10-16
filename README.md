[README.md](https://github.com/user-attachments/files/33556813/README.md)
# yahoo_fantasy_nba_draft_board
live draft assistant for yahoo fantasy NBA draft pick
# Draft Night Board

A live draft board for a **Yahoo Fantasy Basketball** head-to-head points league in the **2026-27 NBA season**. It ranks 250 players for this league's scoring, flags injuries, breakouts and bust risks, tracks the snake draft pick by pick, and suggests the next pick from the players still available.

It's one HTML file with no build step and no server. Open it in a browser or host it on GitHub Pages.

**Live version:** `https://<your-username>.github.io/fantasy-draft-board/` (after you enable GitHub Pages; see below)

---

## The league

| Setting | Value |
|---|---|
| Format | Head-to-head points, 8 teams |
| Draft | Live snake draft, 13 rounds, 2-minute pick clock, **Sat 17 Oct 2026, 12:00 pm EDT** (midnight SGT) |
| Roster | PG, SG, G, SF, PF, F, C, C, UTIL, UTIL + 3 bench + 3 IL |
| Scoring | PTS **1** · REB **1.2** · AST **1.5** · STL **3** · BLK **3** · TO **−1** |
| Moves | 4 adds per week, daily lineups, rolling waivers |
| Playoffs | 6 teams, weeks 20–22 (ends Sun 4 Apr 2027) |

Three things drive the strategy:

1. **Steals and blocks are worth 3 points each**, so defensive players are worth more here than in most leagues.
2. **Missed shots cost nothing.** There's no FG% or FT% penalty, so volume and minutes matter most.
3. **Only 8 teams**, so the waiver wire stays deep all season. Draft the best player available and fill gaps from free agency.

---

## Features

- **Forecast ranking ("My #")** next to the original expert rank, with arrows showing how far each player moved and why.
- **FP/G column:** each player's real 2025-26 fantasy points per game in this league's scoring.
- **Playoff G column:** how many games his team plays in fantasy playoff weeks 20–22.
- **Tags:** STOCKS, SLEEPER, BREAKOUT, BOOST, VALUE, INJ, DURABILITY, BUST RISK, FADE, STASH, OUT, WATCH, each with a short reason.
- **Pick tracker:** choose your draft slot, mark picks as *Mine* or *Gone*, and see your next pick and how many picks away it is.
- **Suggested pick:** the top 3 choices for your next pick, each with reasons, adjusted for your roster needs.
- **Roster panel** that fills your lineup slots as you draft.
- Search, position filter, "hide gone," light and dark mode, and a phone layout.

Your draft progress is saved in your own browser (localStorage), so a page refresh doesn't lose it.

---

## How to use it on draft night

1. Open the board and choose your **draft slot** once Yahoo shows the order.
2. After every pick, tap **Gone** (another team's pick) or **Mine** (your pick).
3. When **Your next pick** says *you're up*, check **Suggested pick**. If #1 is taken, take #2.
4. If the clock is nearly out, take the highest **My #** player left. If players are close, pick a center, then the one with more stocks, then the healthier one.

Full details of how the ranking and suggestions work are in **[docs/METHODOLOGY.md](docs/METHODOLOGY.md)**.

---

## Project structure

```
fantasy-draft-board/
├── index.html                                   # The board (open this)
├── README.md
├── docs/
│   ├── METHODOLOGY.md                           # How players are ranked and picks suggested
│   └── screenshot.png
├── data/
│   ├── expert_rank_titus_2026-09-29.txt         # Base ranking: name|positions|team
│   ├── stats_2025-26.csv                        # Last season's per-game stats
│   └── schedule_fantasy_playoffs_2027.csv       # Every game 15 Mar – 4 Apr 2027
└── scripts/
    └── build_data.py                            # Recomputes FP/G and playoff games into index.html
```

### Updating the data

Edit the CSV files, then run:

```bash
python scripts/build_data.py
```

This recalculates fantasy points per game and playoff games, and writes them into `index.html`. It needs Python 3.8 or later and no extra packages. To change the scoring or the playoff week dates, edit `SCORING` or `WEEKS` at the top of the script.

The forecast adjustments (`ADJ`) and tags (`NOTES`) are edited by hand inside `index.html`.

---

## Sources

- Expert ranking: Dan Titus (Yahoo Sports), [Top 250 points league rankings](https://www.nba.com/news/nba-fantasy-top-250-points-league-rankings), NBA.com, 29 Sep 2026
- Player stats: [Basketball-Reference 2025-26 per-game stats](https://www.basketball-reference.com/leagues/NBA_2026_per_game.html)
- Schedule: Basketball-Reference ([March](https://www.basketball-reference.com/leagues/NBA_2027_games-march.html), [April](https://www.basketball-reference.com/leagues/NBA_2027_games-april.html)) and CBS Sports daily schedules
- Forecasts and news: CBS Sports, Athlon Sports (via Yardbarker), NBA.com, AOL, FantasySP, Fantasy Alarm, Covers, ABC News/AP, RotoBaller. The full list is in [METHODOLOGY.md](docs/METHODOLOGY.md#sources).

Rankings, stats and schedules belong to their original publishers. This is a personal, non-commercial project.

## Disclaimer

This is a planning tool, not a prediction you can count on. Injuries, trades and luck decide much of a fantasy season. Information is current as of **16 Oct 2026**; check the latest news before you draft.

