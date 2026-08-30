import pandas as pd
import matplotlib.pyplot as plt


# --------------------------------------------------
# 1. Load cleaned dataset
# --------------------------------------------------

file_path = "data/processed/online_retail_cleaned.csv"

df = pd.read_csv(file_path, parse_dates=["InvoiceDate"])

print("Dataset loaded successfully.")
print(f"Rows: {len(df):,}")
print(f"Columns: {len(df.columns)}")


# --------------------------------------------------
# 2. Create date features
# --------------------------------------------------

df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["MonthName"] = df["InvoiceDate"].dt.strftime("%b")
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M").astype(str)


# --------------------------------------------------
# 3. Overall sales metrics
# --------------------------------------------------

total_revenue = df["Revenue"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()

average_order_value = total_revenue / total_orders

print("\n========== OVERALL SALES ==========")
print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Total Quantity: {total_quantity:,}")
print(f"Total Orders: {total_orders:,}")
print(f"Total Customers: {total_customers:,}")
print(f"Average Order Value: £{average_order_value:,.2f}")


# --------------------------------------------------
# 4. Monthly revenue
# --------------------------------------------------

monthly_sales = (
    df.groupby("YearMonth")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("InvoiceNo", "nunique"),
          Customers=("CustomerID", "nunique")
      )
      .reset_index()
)

print("\n========== MONTHLY SALES ==========")
print(monthly_sales.to_string(index=False))


# --------------------------------------------------
# 5. Top 10 products by revenue
# --------------------------------------------------

top_products = (
    df.groupby("Description")
      .agg(
          Revenue=("Revenue", "sum"),
          Quantity=("Quantity", "sum"),
          Orders=("InvoiceNo", "nunique")
      )
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\n========== TOP 10 PRODUCTS BY REVENUE ==========")
print(top_products)


# --------------------------------------------------
# 6. Top 10 countries by revenue
# --------------------------------------------------

top_countries = (
    df.groupby("Country")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("InvoiceNo", "nunique"),
          Customers=("CustomerID", "nunique")
      )
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\n========== TOP 10 COUNTRIES BY REVENUE ==========")
print(top_countries)


# --------------------------------------------------
# 7. Top 10 customers by revenue
# --------------------------------------------------

top_customers = (
    df.groupby("CustomerID")
      .agg(
          Revenue=("Revenue", "sum"),
          Orders=("InvoiceNo", "nunique"),
          Quantity=("Quantity", "sum")
      )
      .sort_values("Revenue", ascending=False)
      .head(10)
)

print("\n========== TOP 10 CUSTOMERS ==========")
print(top_customers)


# --------------------------------------------------
# 8. Customer purchase frequency
# --------------------------------------------------

customer_orders = (
    df.groupby("CustomerID")["InvoiceNo"]
      .nunique()
)

print("\n========== CUSTOMER PURCHASE FREQUENCY ==========")
print(customer_orders.describe())


# --------------------------------------------------
# 9. Repeat customers
# --------------------------------------------------

repeat_customers = (customer_orders > 1).sum()
one_time_customers = (customer_orders == 1).sum()

repeat_rate = repeat_customers / total_customers * 100

print("\n========== CUSTOMER RETENTION ==========")
print(f"One-time customers: {one_time_customers:,}")
print(f"Repeat customers: {repeat_customers:,}")
print(f"Repeat purchase rate: {repeat_rate:.2f}%")


# --------------------------------------------------
# 10. Revenue by country
# --------------------------------------------------

country_revenue = (
    df.groupby("Country")["Revenue"]
      .sum()
      .sort_values(ascending=False)
)

print("\n========== REVENUE BY COUNTRY ==========")
print(country_revenue)


# --------------------------------------------------
# 11. Save monthly analysis
# --------------------------------------------------

monthly_sales.to_csv(
    "data/processed/monthly_sales_analysis.csv",
    index=False
)


# --------------------------------------------------
# 12. Save product analysis
# --------------------------------------------------

top_products.to_csv(
    "data/processed/top_products_analysis.csv"
)


# --------------------------------------------------
# 13. Save country analysis
# --------------------------------------------------

top_countries.to_csv(
    "data/processed/top_countries_analysis.csv"
)


# --------------------------------------------------
# 14. Monthly revenue chart
# --------------------------------------------------

plt.figure(figsize=(12, 6))

plt.plot(
    monthly_sales["YearMonth"],
    monthly_sales["Revenue"],
    marker="o"
)

plt.title("Monthly Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (£)")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig(
    "images/monthly_revenue.png",
    dpi=150
)

plt.close()


print("\nEDA completed successfully.")
print("Analysis files saved to data/processed/")
print("Chart saved to images/monthly_revenue.png")