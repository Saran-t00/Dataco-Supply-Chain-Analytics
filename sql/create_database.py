import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "supply_chain.db"

conn = sqlite3.connect(DB_PATH)

print("Supply Chain database created successfully.")
print(f"Database: {DB_PATH}")

conn.close()