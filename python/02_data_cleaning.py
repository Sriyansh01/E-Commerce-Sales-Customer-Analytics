import pandas as pd

# --------------------------------------------------
# 1. Load raw dataset
# --------------------------------------------------

file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)

print("========== RAW DATA ==========")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")


# --------------------------------------------------
# 2. Standardize column names
# --------------------------------------------------

df.columns = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "Quantity",
    "InvoiceDate",
    "UnitPrice",
    "CustomerID",
    "Country"
]


# --------------------------------------------------
# 3. Remove exact duplicates
# --------------------------------------------------

duplicates = df.duplicated().sum()

df = df.drop_duplicates()

print(f"\nDuplicate rows removed: {duplicates:,}")


# --------------------------------------------------
# 4. Convert data types
# --------------------------------------------------

df["InvoiceNo"] = df["InvoiceNo"].astype(str)
df["StockCode"] = df["StockCode"].astype(str)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["CustomerID"] = df["CustomerID"].astype("Int64")


# --------------------------------------------------
# 5. Handle missing descriptions
# --------------------------------------------------

df["Description"] = df["Description"].fillna("Unknown Product")


# --------------------------------------------------
# 6. Remove cancelled invoices
# --------------------------------------------------

cancelled = df["InvoiceNo"].str.startswith("C")

print(f"Cancelled transactions removed: {cancelled.sum():,}")

df = df[~cancelled]


# --------------------------------------------------
# 7. Remove invalid quantities
# --------------------------------------------------

invalid_quantity = df["Quantity"] <= 0

print(f"Invalid quantity rows removed: {invalid_quantity.sum():,}")

df = df[df["Quantity"] > 0]


# --------------------------------------------------
# 8. Remove invalid prices
# --------------------------------------------------

invalid_price = df["UnitPrice"] <= 0

print(f"Invalid price rows removed: {invalid_price.sum():,}")

df = df[df["UnitPrice"] > 0]


# --------------------------------------------------
# 9. Create Revenue
# --------------------------------------------------

df["Revenue"] = df["Quantity"] * df["UnitPrice"]


# --------------------------------------------------
# 10. Sort data
# --------------------------------------------------

df = df.sort_values("InvoiceDate")

df = df.reset_index(drop=True)


# ==================================================
# DATASET 1 — SALES ANALYTICS
# ==================================================

sales_df = df.copy()

sales_output = "data/processed/sales_cleaned.csv"

sales_df.to_csv(
    sales_output,
    index=False
)


# ==================================================
# DATASET 2 — CUSTOMER ANALYTICS
# ==================================================

customer_df = df.dropna(
    subset=["CustomerID"]
).copy()

customer_df["CustomerID"] = customer_df["CustomerID"].astype(int)

customer_output = "data/processed/customer_transactions.csv"

customer_df.to_csv(
    customer_output,
    index=False
)


# --------------------------------------------------
# Final validation
# --------------------------------------------------

print("\n========== SALES DATASET ==========")

print(f"Rows: {len(sales_df):,}")
print(f"Customers identified: {sales_df['CustomerID'].nunique():,}")
print(f"Products: {sales_df['StockCode'].nunique():,}")
print(f"Orders: {sales_df['InvoiceNo'].nunique():,}")
print(f"Revenue: £{sales_df['Revenue'].sum():,.2f}")


print("\n========== CUSTOMER DATASET ==========")

print(f"Rows: {len(customer_df):,}")
print(f"Customers: {customer_df['CustomerID'].nunique():,}")
print(f"Products: {customer_df['StockCode'].nunique():,}")
print(f"Orders: {customer_df['InvoiceNo'].nunique():,}")
print(f"Revenue: £{customer_df['Revenue'].sum():,.2f}")


print("\n========== MISSING VALUES ==========")

print("Sales dataset:")
print(sales_df.isnull().sum())

print("\nCustomer dataset:")
print(customer_df.isnull().sum())


# --------------------------------------------------
# Save confirmation
# --------------------------------------------------

print("\n========== FILES CREATED ==========")

print(sales_output)
print(customer_output)

print("\nData cleaning completed successfully.")