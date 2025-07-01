"""Load processed data into the analytics database."""

import pathlib

DATABASE_DIR = pathlib.Path(__file__).resolve().parents[2] / 'database'

def update() -> None:
    """Placeholder database update routine."""
    print('Updating database at', DATABASE_DIR)

if __name__ == '__main__':
    update()
