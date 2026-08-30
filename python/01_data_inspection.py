import pandas as pd

# --------------------------------------------------
# 1. Load the raw dataset
# --------------------------------------------------

file_path = "data/raw/Online Retail.xlsx"

df = pd.read_excel(file_path)

# --------------------------------------------------
# 2. Basic dataset information
# --------------------------------------------------

print("\n========== DATASET SHAPE ==========")
print(f"Rows: {df.shape[0]:,}")
print(f"Columns: {df.shape[1]}")

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# --------------------------------------------------
# 3. Missing values
# --------------------------------------------------

print("\n========== MISSING VALUES ==========")
missing_values = df.isnull().sum()

print(missing_values[missing_values > 0].sort_values(ascending=False))

# --------------------------------------------------
# 4. Duplicate records
# --------------------------------------------------

print("\n========== DUPLICATES ==========")
print(f"Duplicate rows: {df.duplicated().sum():,}")

# --------------------------------------------------
# 5. Unique values
# --------------------------------------------------

print("\n========== UNIQUE VALUES ==========")

print(f"Unique invoices: {df['InvoiceNo'].nunique():,}")
print(f"Unique products: {df['StockCode'].nunique():,}")
print(f"Unique customers: {df['CustomerID'].nunique():,}")
print(f"Unique countries: {df['Country'].nunique():,}")

# --------------------------------------------------
# 6. Date information
# --------------------------------------------------

print("\n========== DATE RANGE ==========")

print(f"Minimum date: {df['InvoiceDate'].min()}")
print(f"Maximum date: {df['InvoiceDate'].max()}")

# --------------------------------------------------
# 7. Numerical summary
# --------------------------------------------------

print("\n========== NUMERICAL SUMMARY ==========")
print(df[['Quantity', 'UnitPrice']].describe())

# --------------------------------------------------
# 8. Countries
# --------------------------------------------------

print("\n========== TOP 10 COUNTRIES ==========")
print(df['Country'].value_counts().head(10))