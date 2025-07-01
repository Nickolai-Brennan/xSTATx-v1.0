"""Utility for downloading FanGraphs leaderboards.

This module fetches CSV exports from FanGraphs and stores them in the
``raw_data`` directory.  Use :func:`pull_leaderboard` to retrieve a
leaderboard with the ``month`` parameter controlling the date range.

``month`` values:
    * ``0`` – full season
    * ``1`` – last 7 days
    * ``2`` – last 14 days
    * ``3`` – last 30 days

For custom date ranges beyond these presets, FanGraphs provides a Splits Tool
where you can specify start and end dates using a calendar interface.
"""

from __future__ import annotations

import pathlib
import requests

RAW_DATA_DIR = pathlib.Path(__file__).resolve().parents[2] / "raw_data"
RAW_DATA_DIR.mkdir(exist_ok=True)


def pull_leaderboard(base_url: str, output_name: str, month: int = 0) -> pathlib.Path:
    """Download a leaderboard CSV from FanGraphs.

    Parameters
    ----------
    base_url:
        The leaderboard URL **without** a ``month`` parameter.
    output_name:
        Name of the file to save the CSV as.
    month:
        Date range selector documented above.
    """

    url = f"{base_url}&month={month}"
    response = requests.get(url, timeout=30)
    response.raise_for_status()

    output_path = RAW_DATA_DIR / output_name
    output_path.write_bytes(response.content)
    return output_path


if __name__ == "__main__":
    print("FanGraphs pull script placeholder")
