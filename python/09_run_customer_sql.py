import sqlite3
import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "database" / "ecommerce_analytics.db"
SQL_PATH = BASE_DIR / "sql" / "02_customer_analysis.sql"
OUTPUT_DIR = BASE_DIR / "data" / "processed"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)


# ============================================================
# CONNECT TO DATABASE
# ============================================================

conn = sqlite3.connect(DB_PATH)

print("Connected to SQLite database successfully.")


# ============================================================
# READ SQL FILE
# ============================================================

with open(SQL_PATH, "r", encoding="utf-8") as file:
    sql_script = file.read()


# ============================================================
# SPLIT SQL QUERIES
# ============================================================

queries = [
    query.strip()
    for query in sql_script.split(";")
    if query.strip()
]

print(f"SQL queries found: {len(queries)}")


# ============================================================
# EXECUTE QUERIES
# ============================================================

for i, query in enumerate(queries, start=1):

    try:
        result = pd.read_sql_query(query, conn)

        output_file = OUTPUT_DIR / f"customer_sql_result_{i}.csv"

        result.to_csv(output_file, index=False)

        print(f"\n{'=' * 60}")
        print(f"QUERY {i} COMPLETED SUCCESSFULLY")
        print(f"Saved to: {output_file}")
        print("=" * 60)

        print(result.head(10).to_string(index=False))

    except Exception as e:

        print(f"\n{'=' * 60}")
        print(f"QUERY {i} FAILED")
        print("=" * 60)
        print(e)


# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()

print("\n" + "=" * 60)
print("CUSTOMER SQL ANALYSIS COMPLETED SUCCESSFULLY.")
print("=" * 60)