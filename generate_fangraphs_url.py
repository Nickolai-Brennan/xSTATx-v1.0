import urllib.parse

BASE_URL = "https://www.fangraphs.com/leaders.aspx"

# Default parameters for the leaderboard
DEFAULT_PARAMS = {
    "pos": "all",
    "team": "0",
    "stats": "bat",
    "type": "0",
    "season": "2025",
    "month": "0",
    "qual": "y",
    "ind": "0",
    "sortcol": "1",
    "sortdir": "desc",
}


def generate_url(overrides=None):
    """Generate a FanGraphs leaderboard URL with optional parameter overrides."""
    params = DEFAULT_PARAMS.copy()
    if overrides:
        params.update({k: str(v) for k, v in overrides.items() if v is not None})
    query = urllib.parse.urlencode(params)
    return f"{BASE_URL}?{query}"


if __name__ == "__main__":
    # Example usage
    example = {
        "pos": "cf",
        "team": "14",
        "stats": "bat",
        "type": "1",
        "sortcol": "3",
    }
    print(generate_url(example))
