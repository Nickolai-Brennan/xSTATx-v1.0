# StatalyticS

StatalyticS is a modular baseball analytics engine designed to pull and unify statistics from multiple sources. The goal is to provide a clean database and set of models for building tools such as the Reliever Reliability Index (RRI), draft utilities, and positional rankings.

## Repository Layout

```
StatalyticS/
├── DataPipeline/       # Data ingestion and database scripts
│   ├── raw_data/
│   ├── processed_data/
│   ├── player_map/
│   ├── sql_queries/
│   └── database/
├── Docs/               # Documentation and formulas
├── Models/             # Scoring and machine learning models
├── Config/             # API keys and runtime settings
├── Outputs/            # Generated exports and logs
```

Each subfolder contains starter scripts or placeholders for future development. See `Docs/ProjectOverview.md` for a detailed breakdown of planned phases.

The FanGraphs pull script demonstrates how to use the `month` parameter (`0` for full season, `1` for last 7 days, etc.) when requesting leaderboard data.
