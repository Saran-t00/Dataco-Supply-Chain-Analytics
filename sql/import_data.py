import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DB_PATH = BASE_DIR / "sql" / "supply_chain.db"

files = {
    "supply_chain": "DataCoSupplyChainDataset.csv",
    "dataset_description": "DescriptionDataCoSupplyChain.csv",
    "access_logs": "tokenized_access_logs.csv"
}

conn = sqlite3.connect(DB_PATH)

for table_name, file_name in files.items():
    file_path = DATA_DIR / file_name

    try:
        df = pd.read_csv(file_path, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding="latin1")

    df.to_sql(table_name, conn, if_exists="replace", index=False)

    print(f"{table_name}: {len(df):,} rows loaded")

conn.close()

print("\nAll datasets loaded successfully.")