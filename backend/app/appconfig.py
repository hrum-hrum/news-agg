from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

DATABASE_NAME = "db.sqlite3"
DATABASE_PATH = DATA_DIR / DATABASE_NAME
