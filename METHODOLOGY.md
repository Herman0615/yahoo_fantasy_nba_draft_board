# Methodology

How the Draft Night Board was built: the background, how players are ranked, how the suggested pick works, and what it can't do.

Information is current as of **16 Oct 2026**.

---

## 1. Background

The goal was to win an 8-team Yahoo head-to-head points league among friends in the 2026-27 NBA season. The draft is a live 13-round snake draft on **Saturday 17 Oct 2026 at 12:00 pm EDT** (midnight going into Sunday 18 Oct in Singapore/Malaysia time), with a 2-minute pick clock.

The league's settings, taken from the Yahoo *League Settings* page:

| Setting | Value |
|---|---|
| Teams | 8 |
| Scoring | H2H points: PTS 1, REB 1.2, AST 1.5, STL 3, BLK 3, TO −1 |
| Roster | PG, SG, G, SF, PF, F, C, C, UTIL, UTIL, 3 bench, 3 IL |
| Acquisitions | 4 per week, no season limit |
| Waivers | 2 days, continual rolling list |
| Lineups | Daily |
| Trades | League vote, deadline 4 Mar 2027 |
| Playoffs | 6 teams, weeks 20–22, ends Sun 4 Apr 2027 |

### What these settings mean for strategy

- **Steals and blocks (stocks) are worth 3.** One block is worth the same as 3 points scored. Players with lots of steals and blocks are worth more here than their scoring suggests.
- **No shooting-percentage penalty.** A missed shot or free throw costs nothing, so minutes and volume matter more than efficiency.
- **Weekly totals.** Every game a player misses is zero points from that lineup slot, so durability is a real factor.
- **Two center slots.** Good centers run out faster than guards or wings, and they add rebounds and blocks.
- **8 teams × 13 rounds = 104 players drafted.** The free-agent pool stays deep, so it's better to take the best player available than to fill positions, and the 4 weekly adds are useful for streaming.
- **3 IL slots** don't count against the roster, so an injured player who returns before the playoffs costs only a late pick.

---

## 2. How the ranking was built

The board's **My #** column is built in four layers.

### Layer 1: Base expert ranking

The starting point is **Dan Titus's (Yahoo Sports) top 250 for points leagues**, published on NBA.com on 29 Sep 2026. It was chosen because it's built for Yahoo points leagues, which use the same scoring as this league. It's stored in `data/expert_rank_titus_2026-09-29.txt` and shown in the **Expert** column.

### Layer 2: Real fantasy points from last season (FP/G)

Each player's 2025-26 per-game stats (Basketball-Reference) were converted to fantasy points with this league's formula:

```
FP/G = PTS + 1.2 × REB + 1.5 × AST + 3 × STL + 3 × BLK − TOV
```

191 of the 250 players have data. The other 59 are rookies, players who missed the season (Haliburton, Kyrie Irving, Lillard), or players outside the data used (under about 9 points per game). Players with fewer than 25 games are marked with `*` because a small sample is unreliable (for example Tatum, 16 games; Kessler, 5).

Top 10 in this league's scoring last season:

| Player | FP/G | Games |
|---|---|---|
| Nikola Jokić | 62.1 | 65 |
| Luka Dončić | 57.5 | 64 |
| Victor Wembanyama | 53.4 | 64 |
| Shai Gilgeous-Alexander | 50.6 | 68 |
| Giannis Antetokounmpo | 49.1 | 36 |
| Tyrese Maxey | 48.8 | 70 |
| Cade Cunningham | 48.2 | 64 |
| Jalen Johnson | 48.1 | 72 |
| Kawhi Leonard | 45.9 | 65 |
| Jaylen Brown | 45.2 | 71 |

FP/G was used as a check on the expert order. For example, it showed Kawhi Leonard ranked well below his production, so he moved up. It also feeds the suggested-pick score (section 4). Note that NBA.com's own "High Score" fantasy format scores differently; its numbers (such as 68.7 for Jokić) aren't comparable to this league's.

### Layer 3: Forecast adjustments for 2026-27

Last season's numbers don't capture what has changed since. Each adjustment below moves a player up (negative) or down (positive) from his expert rank. They're based on:

- **Role changes** from trades and departures. LeBron James moved to Philadelphia, which opens up the Lakers' offense; Jaylen Brown moved to Philadelphia; Ja Morant and Jaren Jackson Jr. left Memphis; Russell Westbrook retired and DeMar DeRozan left Sacramento.
- **Breakout, sleeper and bust calls** from several outlets: CBS Sports' projection model, Athlon Sports, NBA.com's "draft values" list, and AOL's bust list. A player picked by several sources got a bigger move.
- **Preseason production** through 14 Oct (NBA.com preseason standouts).
- **Games-missed history**: players who regularly miss large parts of seasons.
- **Current injuries** from reports dated 8–16 Oct.

| Player | Expert | Move | Reason |
|---|---|---|---|
| Aday Mara | 249 | −80 | Preseason: 2.8 blocks/game as backup C; waiver watch |
| Yaxel Lendeborg | 133 | −26 | Strong preseason, may start for GSW |
| Darius Acuff Jr. | 91 | −16 | CBS model breakout; Kings' main option |
| Walker Kessler | 58 | −11 | Sleeper (3 sources); 2.4 blocks in his last full season |
| Kyshawn George | 120 | −10 | Preseason production, likely starter |
| Austin Reaves | 38 | −9 | Bigger role with LeBron gone |
| Derrick White | 71 | −9 | Boston's No. 2 option after Brown left |
| Cedric Coward | 90 | −9 | Usage opens up in Memphis |
| Ryan Rollins | 65 | −6 | Runs Milwaukee's offense |
| Brandon Miller | 44 | −5 | Inherits usage in Charlotte |
| Kel'el Ware | 73 | −5 | More minutes in Milwaukee |
| Day'Ron Sharpe | 87 | −5 | Likely Brooklyn's starting C |
| Dylan Harper | 93 | −5 | Minutes rising |
| Kawhi Leonard | 33 | −5 | 45.9 FP/G over 65 games last season |
| Tyrese Haliburton | 11 | −2 | Fully cleared; may slide in drafts |
| Jamal Murray | 19 | −1 | Steady first-round-level value |
| Giannis Antetokounmpo | 4 | +3 | 36 games last season |
| Dejounte Murray | 50 | +3 | Toe injury |
| Kon Knueppel | 79 | +3 | Hamstring |
| Cooper Flagg | 12 | +4 | CBS model bust: Kyrie back, new coach |
| Coby White | 82 | +4 | Calf, missed preseason |
| Kyrie Irving | 45 | +5 | Long layoff; may be managed |
| Nic Claxton | 94 | +5 | Hamstring, questionable for opener |
| LaMelo Ball | 21 | +6 | Averages about 48 games a season |
| Zion Williamson | 43 | +7 | Injury history; scoring at career low |
| De'Aaron Fox | 59 | +7 | Bust call; shooting, role |
| Anthony Davis | 15 | +8 | 40 games or fewer in 3 of last 6 seasons |
| Ja Morant | 46 | +8 | Injuries, bust call |
| Jaylen Brown | 34 | +9 | Shares the ball with three stars in PHI |
| Brandon Ingram | 69 | +10 | Partially torn Achilles, no return date |
| LeBron James | 20 | +12 | Age 41, foot arthritis, managed minutes |
| Joel Embiid | 47 | +15 | Knee; may not reach 40 games |
| Nikola Vučević | 179 | +15 | Declining, may lose role |
| Kristaps Porziņģis | 142 | +60 | Out indefinitely |

The sizes of these moves are **judgment calls**, not output from a statistical model. They're deliberately modest: the top of the board barely changes, and most moves are under 10 spots.

### Layer 4: Tiers and tags

Players are grouped into **tiers** by My # (tier 1 = ranks 1–5, ..., tier 8 = ranks 105+, the waiver wire). The tiers follow the 8-team round structure.

| Tag | Meaning |
|---|---|
| STOCKS | Strong steals/blocks producer; extra valuable in this scoring |
| SLEEPER | Likely to outperform where he's drafted |
| BREAKOUT | Expected to make a big jump this season |
| BOOST / VALUE | Bigger role this year, or ranked lower than his production |
| PRESEASON / WATCH | Strong preseason; watch on waivers |
| INJ | Currently injured; check news |
| DURABILITY | Healthy now but historically misses many games |
| BUST RISK | Downside bigger than people expect (role, injury, age) |
| FADE | Overpriced at his current draft position |
| STASH | Out now, expected back before the fantasy playoffs; IL candidate |
| OUT | Out indefinitely |

---

## 3. Playoff schedule (Playoff G)

Each team's games in fantasy playoff weeks were counted from the official 2026-27 schedule:

- Week 20: Mon 15 – Sun 21 Mar 2027
- Week 21: Mon 22 – Sun 28 Mar 2027
- Week 22: Mon 29 Mar – Sun 4 Apr 2027

| Games | Teams |
|---|---|
| 12 | DAL, PHX (4-4-4) |
| 11 | ATL, BOS, BKN, CHA, CHI, DEN, DET, GSW, HOU, IND, LAC, MEM, MIL, NYK, ORL, PHI, POR, SAC, SAS, TOR |
| 10 | LAL, MIA, MIN, OKC, UTA, WAS |
| 9 | CLE (3-2-4), NOP (4-3-2) |

The spread is small, so this is used only as a tiebreaker. A player's games follow his **current** team, and trades during the season will change them.

---

## 4. How the suggested pick works

Every time a pick is marked, the board scores the **14 best available players by My #**. **Lower score = better**, and the 3 lowest are shown.

```
score = My #
      − center bonus   (if you have < 2 C: −2 in your picks 1–2, −4 in picks 3–5, −8 from pick 6)
      − 2              STOCKS or WATCH tag
      − 2              last player left in his tier
      − 3              covers a position you have none of (from your 8th pick)
      − 1.5 × (playoff games − 11)
      − FP bonus       0.3 × (his FP/G − median FP/G of the 14), capped at ±3, only for 40+ games
      + 2              BUST RISK
      + 4              INJ or DURABILITY
      + 12             FADE
      + 40             OUT or STASH (effectively never suggested)
```

In your **last two picks (12–13)**, the third suggestion is replaced by the best available STASH player for an IL slot.

**Example:** you're on pick 16 and have one center.
- Josh Giddey (My # 17, no tags, 11 playoff games): about **17**
- Anthony Davis (My # 20): −2 center, +4 DURABILITY, +1.5 for 10 playoff games = about **23.5**

Giddey is suggested first. The center boost doesn't outweigh Davis's injury risk.

The board also works out your pick numbers from your slot with 8-team snake order: in odd rounds you pick at position *slot*, and in even rounds at *9 − slot*. Pick 1 gets picks 1, 16, 17, 32, 33, ...

---

## 5. How Claude helped

This board was planned and built in a conversation with Claude (Anthropic's AI assistant) over two days before the draft:

1. **Gathered the league settings** from screenshots of the Yahoo settings page and worked out what they mean for strategy.
2. **Researched** current rankings, injury reports, preseason results, and breakout and bust forecasts with web search.
3. **Built the board** as one HTML file: ranking table, tags, pick tracker, roster panel.
4. **Changed it for 8 teams** after the league size was corrected from 12.
5. **Added the suggested-pick engine** with the scoring rules above.
6. **Added the forecast layer** after asking whether predictions would beat past performance alone.
7. **Calculated real fantasy points and playoff games** from stats and schedule data, and fixed an earlier mistake where NBA.com's differently scored numbers had been quoted as if they used this league's scoring.
8. **Live draft plan:** during the draft, the user sends picks in batches and asks for a ranked shortlist of 3 when 2–3 picks away, with the board as backup if a reply is too slow for the 2-minute clock.

---

## 6. Limitations

- **No full stat projections.** Complete 2026-27 projections are behind paywalls, so the forecast relies on last season plus expert judgment. Rookies have no FP/G.
- **Adjustment sizes are subjective** and haven't been backtested.
- **News goes stale.** Injury tags are from 8–16 Oct; check again on draft day.
- **The board doesn't connect to Yahoo.** Picks have to be marked by hand.
- **Playoff week dates are assumed** to be 15 Mar – 4 Apr; confirm them in Yahoo under *League → Schedule*.
- The board can't account for your league-mates' tendencies.

---

## Sources

- Dan Titus, [NBA Fantasy: Top 250 points league rankings](https://www.nba.com/news/nba-fantasy-top-250-points-league-rankings), NBA.com, 29 Sep 2026
- [2025-26 NBA player per-game stats](https://www.basketball-reference.com/leagues/NBA_2026_per_game.html), Basketball-Reference
- 2026-27 schedule: Basketball-Reference [March](https://www.basketball-reference.com/leagues/NBA_2027_games-march.html) and [April](https://www.basketball-reference.com/leagues/NBA_2027_games-april.html); CBS Sports [Mar 28](https://www.cbssports.com/nba/schedule/20270328/), [Mar 29](https://www.cbssports.com/nba/schedule/20270329/), [Mar 30](https://www.cbssports.com/nba/schedule/20270330/), [Mar 31](https://www.cbssports.com/nba/schedule/20270331/)
- [NBA Fantasy: Top High Score players from last season](https://www.nba.com/news/nba-fantasy-2026-27-top-high-score-players-from-last-season), NBA.com
- [NBA Fantasy: 25 draft values with first-round upside](https://www.nba.com/news/nba-fantasy-25-draft-values-with-first-round-upside), NBA.com
- [NBA Fantasy: Preseason standouts with High Score upside](https://www.nba.com/news/nba-fantasy-preseason-standouts-with-high-score-upside), NBA.com, 14 Oct 2026
- [Fantasy basketball rankings 2026-27: sleepers, breakouts and busts from proven NBA model](https://www.cbssports.com/fantasy/basketball/news/fantasy-basketball-rankings-2026-27-top-sleepers-breakouts-and-busts-from-proven-nba-model/), CBS Sports
- [2026-27 Fantasy Basketball Sleepers, Breakouts and Busts](https://www.yardbarker.com/nba/articles/2026_27_fantasy_basketball_sleepers_breakouts_and_busts/s1_17615_44347416), Athlon Sports via Yardbarker
- [Fantasy Basketball Busts 2026-27](https://www.aol.com/articles/fantasy-basketball-busts-2026-27-210904991.html), AOL
- [Notable Fantasy Basketball Injuries to Monitor](https://www.fantasysp.com/news/nba/3057505/notable-fantasy-basketball-injuries-to-monitor), FantasySP, 8 Oct 2026
- [NBA Injury Report: Key Injuries Heading Into the 2026-27 Season](https://www.fantasyalarm.com/articles/nba/fantasy-basketball-injury-report/nba-injury-report-heading-into-2026-27-season/197178), Fantasy Alarm, 15 Oct 2026
- [NBA Injuries](https://www.covers.com/sport/basketball/nba/injuries), Covers, 16 Oct 2026
- [Welcome back, Kyrie: Irving scores 17 in return](https://abcnews.com/Sports/wireStory/back-kyrie-irving-scores-17-mavs-china-return-137178212), ABC News/AP, 11 Oct 2026
- [Kyrie Irving enters Mavericks camp without restrictions](https://www.rotoballer.com/player-news/kyrie-irving-enters-mavericks-camp-without-restrictions/1951192), RotoBaller
