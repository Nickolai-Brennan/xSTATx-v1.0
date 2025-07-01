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
    """
    Constructs a FanGraphs leaderboard URL using default parameters, with optional overrides.
    
    Parameters:
        overrides (dict, optional): Dictionary of query parameter overrides. Keys with `None` values are ignored, and all values are converted to strings.
    
    Returns:
        str: The complete FanGraphs leaderboard URL with encoded query parameters.
    """
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
