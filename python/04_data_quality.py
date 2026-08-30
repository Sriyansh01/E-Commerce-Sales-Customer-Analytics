import pandas as pd

# --------------------------------------------------
# Load cleaned dataset
# --------------------------------------------------

file_path = "data/processed/online_retail_cleaned.csv"

df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])


# --------------------------------------------------
# 1. Highest quantity transactions
# --------------------------------------------------

print("\n========== TOP 20 TRANSACTIONS BY QUANTITY ==========")

top_quantity = (
    df[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "InvoiceDate",
            "UnitPrice",
            "CustomerID",
            "Country",
            "Revenue"
        ]
    ]
    .sort_values("Quantity", ascending=False)
    .head(20)
)

print(top_quantity.to_string(index=False))


# --------------------------------------------------
# 2. Highest revenue transactions
# --------------------------------------------------

print("\n========== TOP 20 TRANSACTIONS BY REVENUE ==========")

top_revenue = (
    df[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "Revenue",
            "CustomerID",
            "Country"
        ]
    ]
    .sort_values("Revenue", ascending=False)
    .head(20)
)

print(top_revenue.to_string(index=False))


# --------------------------------------------------
# 3. Quantity distribution
# --------------------------------------------------

print("\n========== QUANTITY DISTRIBUTION ==========")

print(df["Quantity"].describe(percentiles=[
    0.90,
    0.95,
    0.99,
    0.995,
    0.999
]))


# --------------------------------------------------
# 4. Transactions with quantity above 1,000
# --------------------------------------------------

high_quantity = df[df["Quantity"] > 1000]

print("\n========== TRANSACTIONS WITH QUANTITY > 1,000 ==========")

print(f"Number of transactions: {len(high_quantity):,}")

print(
    high_quantity[
        [
            "InvoiceNo",
            "StockCode",
            "Description",
            "Quantity",
            "UnitPrice",
            "Revenue",
            "CustomerID",
            "Country"
        ]
    ].sort_values("Quantity", ascending=False).to_string(index=False)
)


# --------------------------------------------------
# 5. Zero / negative revenue check
# --------------------------------------------------

print("\n========== REVENUE QUALITY CHECK ==========")

print(f"Zero revenue rows: {(df['Revenue'] == 0).sum():,}")
print(f"Negative revenue rows: {(df['Revenue'] < 0).sum():,}")

print("\nData quality investigation completed.")