import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "sql" / "supply_chain.db"

conn = sqlite3.connect(DB_PATH)

query = """
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;
"""

tables = conn.execute(query).fetchall()

print("Tables available in Supply Chain database:\n")

for table in tables:
    print(table[0])

conn.close()