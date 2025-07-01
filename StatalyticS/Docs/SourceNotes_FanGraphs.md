# FanGraphs Source Notes

The FanGraphs leaderboard endpoints support a ``month`` parameter that controls
the date range for returned statistics.  Common values include:

- ``month=0`` – full season statistics
- ``month=1`` – last 7 days
- ``month=2`` – last 14 days
- ``month=3`` – last 30 days

For custom date ranges outside of these presets, use FanGraphs' Splits Tool and
set specific start and end dates.  The ``month`` parameter can be appended to
any leaderboard URL to automate retrieval of these time-frame splits.

