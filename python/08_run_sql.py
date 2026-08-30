import sqlite3
import pandas as pd
from pathlib import Path


# ============================================================
# PATHS
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "data" / "database" / "ecommerce_analytics.db"
SQL_PATH = BASE_DIR / "sql" / "01_sales_performance.sql"
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
# SPLIT QUERIES
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

        output_file = OUTPUT_DIR / f"sql_result_{i}.csv"

        result.to_csv(output_file, index=False)

        print(
            f"Query {i} completed successfully "
            f"-> {output_file}"
        )

        print(result.head(5))
        print("-" * 60)

    except Exception as e:

        print(f"Query {i} failed:")
        print(e)


# ============================================================
# CLOSE DATABASE
# ============================================================

conn.close()

print("SQL analysis completed successfully.")