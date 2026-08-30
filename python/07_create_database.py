import pandas as pd
import sqlite3
from pathlib import Path


# ==================================================
# 1. File paths
# ==================================================

sales_file = "data/processed/sales_cleaned.csv"
customer_file = "data/processed/customer_transactions.csv"
rfm_file = "data/processed/customer_rfm_analysis.csv"
cohort_file = "data/processed/customer_cohort.csv"

database_folder = Path("data/database")
database_folder.mkdir(parents=True, exist_ok=True)

database_file = database_folder / "ecommerce_analytics.db"


# ==================================================
# 2. Load datasets
# ==================================================

print("Loading datasets...")

sales_df = pd.read_csv(
    sales_file,
    parse_dates=["InvoiceDate"]
)

customer_df = pd.read_csv(
    customer_file,
    parse_dates=["InvoiceDate"]
)

rfm_df = pd.read_csv(
    rfm_file
)

cohort_df = pd.read_csv(
    cohort_file
)

print(f"Sales transactions: {len(sales_df):,}")
print(f"Customer transactions: {len(customer_df):,}")
print(f"RFM customers: {len(rfm_df):,}")
print(f"Cohort customers: {len(cohort_df):,}")


# ==================================================
# 3. Connect to SQLite
# ==================================================

conn = sqlite3.connect(database_file)


# ==================================================
# 4. Load tables
# ==================================================

sales_df.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

customer_df.to_sql(
    "customer_transactions",
    conn,
    if_exists="replace",
    index=False
)

rfm_df.to_sql(
    "customer_rfm",
    conn,
    if_exists="replace",
    index=False
)

cohort_df.to_sql(
    "customer_cohort",
    conn,
    if_exists="replace",
    index=False
)


# ==================================================
# 5. Create useful indexes
# ==================================================

cursor = conn.cursor()

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_sales_invoice
ON sales(InvoiceNo)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_sales_customer
ON sales(CustomerID)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_sales_product
ON sales(StockCode)
""")

cursor.execute("""
CREATE INDEX IF NOT EXISTS idx_customer_transactions_customer
ON customer_transactions(CustomerID)
""")

conn.commit()


# ==================================================
# 6. Verify database
# ==================================================

print("\n========== DATABASE TABLES ==========")

tables = pd.read_sql_query(
    """
    SELECT name
    FROM sqlite_master
    WHERE type = 'table'
    ORDER BY name
    """,
    conn
)

print(tables)


# ==================================================
# 7. Verify row counts
# ==================================================

print("\n========== ROW COUNTS ==========")

for table in [
    "sales",
    "customer_transactions",
    "customer_rfm",
    "customer_cohort"
]:

    result = pd.read_sql_query(
        f"SELECT COUNT(*) AS rows FROM {table}",
        conn
    )

    print(
        f"{table}: "
        f"{result['rows'].iloc[0]:,}"
    )


# ==================================================
# 8. Close database
# ==================================================

conn.close()


# ==================================================
# 9. Final confirmation
# ==================================================

print("\n========== DATABASE CREATED ==========")

print(f"Database: {database_file}")

print("\nSQL database created successfully.")