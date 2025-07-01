"""Pull data from FanGraphs leaderboards.

This script downloads CSV exports from FanGraphs and stores them in the raw_data directory.
"""

import pathlib

RAW_DATA_DIR = pathlib.Path(__file__).resolve().parents[2] / 'raw_data'

def pull_leaderboard(url: str, output_name: str) -> pathlib.Path:
    """Download leaderboard CSV and save to disk."""
    # Placeholder implementation
    output_path = RAW_DATA_DIR / output_name
    output_path.write_text('')
    return output_path

if __name__ == '__main__':
    print('FanGraphs pull script placeholder')
