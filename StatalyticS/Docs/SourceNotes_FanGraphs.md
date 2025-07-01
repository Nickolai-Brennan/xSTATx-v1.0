# FanGraphs Source Notes

Got it! Here's your updated table with all parameter values **formatted in uppercase** for consistency and clarity:

---

### 🗺️ **FanGraphs Leaderboard URL Parameter Map (Uppercase Format)**

| Parameter   | Code Value(s)                                                                                                                                                | Description / Meaning                                          |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- |
| `&POS=`     | `C`, `1B`, `2B`, `3B`, `SS`, `LF`, `CF`, `RF`, `OF`, `DH`, `SP`, `RP`, `ALL`                                                                                 | Filters by position                                            |
| `&TEAM=`    | `0` to `31`                                                                                                                                                  | `0 = ALL TEAMS`; others = specific MLB teams (verify manually) |
| `&STATS=`   | `BAT`, `PIT`, `FLD`                                                                                                                                          | Batting, Pitching, or Fielding stats                           |
| `&TYPE=`    | `0` = STANDARD<br>`1` = ADVANCED<br>`2` = BATTED BALL<br>`3` = WIN PROBABILITY<br>`6` = VALUE<br>`8` = DASHBOARD<br>`23` = +STATS<br>`24` = STATCAST         | Controls stat preset layout                                    |
| `&MONTH=`   | `0` = FULL SEASON<br>`1` = LAST 7 DAYS<br>`2` = LAST 14 DAYS<br>`3` = LAST 30 DAYS<br>`13` = VS. LHP<br>`14` = VS. RHP<br>`30` = 1ST HALF<br>`31` = 2ND HALF | Split or time-based filters                                    |
| `&SORTCOL=` | `1` to `N`                                                                                                                                                   | Sorts by column index in the stat table                        |
| `&SORTDIR=` | `ASC`, `DESC`                                                                                                                                                | Sort direction (ascending or descending)                       |
| `&SEASON=`  | `2025`, `2024`, etc.                                                                                                                                         | Target season year                                             |
| `&QUAL=`    | `Y`, `N`                                                                                                                                                     | Include only qualified players (`Y` = Yes)                     |
| `&IND=`     | `0`, `1`                                                                                                                                                     | Individual season vs combined view                             |
| `&HAND=`    | `R` = RIGHT-HANDED<br>`L` = LEFT-HANDED                                                                                                                      | Filters by player handedness                                   |

---

### 🧠 FanGraphs `&type=` Parameter: Stat Presets

| `type=` | Stat View       | Description                          |
| ------- | --------------- | ------------------------------------ |
| 0       | Standard        | Basic stats like AVG, HR, RBI        |
| 1       | Advanced        | OBP, SLG, wOBA, wRC+                 |
| 2       | Batted Ball     | GB%, FB%, LD%, BABIP                 |
| 3       | Win Probability | WPA, RE24, Clutch                    |
| 6       | Value           | WAR, \$ Values                       |
| 8       | Dashboard       | Mixed summary with key stat metrics  |
| 23      | +Stats          | Plate discipline, contact %, chase % |
| 24      | Statcast        | xwOBA, Barrel%, Exit Velo            |

---
Logged and added ✅

Here's your latest parameter mapping update:

| Parameter | Code Value(s)                                                         | Description                                |
| --------- | --------------------------------------------------------------------- | ------------------------------------------ |
| `&ROST=`  | `0` = Active Rosters<br>`1` = Qualified Rookies<br>`2` = Hall of Fame | Filters leaderboard by player roster group |

You can now fine-tune queries like:

```
&stats=bat&pos=all&season=2025&rost=1
```

⬆️ Pulls **2025 rookie batting leaderboard**.

Would you like me to finish this out into a full FanGraphs Query Builder template in Sheets, HTML, or Python?

You now have all the ingredients to construct dynamic, filter-specific URLs for StatalyticS.

Want me to generate a CSV or URL-building script based on these parameters?
