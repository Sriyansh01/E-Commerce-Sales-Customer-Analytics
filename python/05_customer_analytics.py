import pandas as pd


# ==================================================
# 1. Load customer transaction data
# ==================================================

file_path = "data/processed/customer_transactions.csv"

df = pd.read_csv(
    file_path,
    parse_dates=["InvoiceDate"]
)

print("Customer transaction data loaded.")
print(f"Rows: {len(df):,}")


# ==================================================
# 2. Define analysis date
# ==================================================

# One day after the latest transaction
analysis_date = df["InvoiceDate"].max() + pd.Timedelta(days=1)

print(f"\nAnalysis date: {analysis_date.date()}")


# ==================================================
# 3. Create customer-level RFM metrics
# ==================================================

rfm = (
    df.groupby("CustomerID")
      .agg(
          Recency=(
              "InvoiceDate",
              lambda x: (analysis_date - x.max()).days
          ),
          Frequency=("InvoiceNo", "nunique"),
          Monetary=("Revenue", "sum")
      )
      .reset_index()
)


# ==================================================
# 4. Calculate additional customer metrics
# ==================================================

customer_quantity = (
    df.groupby("CustomerID")["Quantity"]
      .sum()
      .reset_index(name="TotalQuantity")
)

rfm = rfm.merge(
    customer_quantity,
    on="CustomerID",
    how="left"
)


# Average order value
rfm["AverageOrderValue"] = (
    rfm["Monetary"] / rfm["Frequency"]
)


# ==================================================
# 5. Create RFM scores
# ==================================================

# Rank first to avoid problems with duplicate values
# when using qcut.

rfm["R_Score"] = pd.qcut(
    rfm["Recency"].rank(method="first"),
    5,
    labels=[5, 4, 3, 2, 1]
).astype(int)


rfm["F_Score"] = pd.qcut(
    rfm["Frequency"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)


rfm["M_Score"] = pd.qcut(
    rfm["Monetary"].rank(method="first"),
    5,
    labels=[1, 2, 3, 4, 5]
).astype(int)


# Combined RFM score
rfm["RFM_Score"] = (
    rfm["R_Score"].astype(str)
    + rfm["F_Score"].astype(str)
    + rfm["M_Score"].astype(str)
)


# ==================================================
# 6. Create customer segments
# ==================================================

def segment_customer(row):

    r = row["R_Score"]
    f = row["F_Score"]
    m = row["M_Score"]

    # Champions
    if r >= 4 and f >= 4 and m >= 4:
        return "Champions"

    # Loyal Customers
    elif r >= 3 and f >= 4 and m >= 3:
        return "Loyal Customers"

    # Potential Loyalists
    elif r >= 4 and f >= 2 and m >= 2:
        return "Potential Loyalists"

    # New Customers
    elif r >= 4 and f <= 2:
        return "New Customers"

    # Big Spenders
    elif m >= 4 and f <= 3:
        return "Big Spenders"

    # At Risk
    elif r <= 2 and f >= 3:
        return "At Risk"

    # Lost Customers
    elif r <= 2 and f <= 2:
        return "Lost Customers"

    else:
        return "Regular Customers"


rfm["Segment"] = rfm.apply(
    segment_customer,
    axis=1
)


# ==================================================
# 7. Customer value classification
# ==================================================

rfm["CustomerValue"] = pd.cut(
    rfm["Monetary"],
    bins=[
        0,
        250,
        1000,
        5000,
        float("inf")
    ],
    labels=[
        "Low Value",
        "Medium Value",
        "High Value",
        "Very High Value"
    ]
)


# ==================================================
# 8. Display customer analytics
# ==================================================

print("\n========== CUSTOMER ANALYTICS ==========")

print(f"Total customers: {len(rfm):,}")

print(
    f"Average customer revenue: "
    f"£{rfm['Monetary'].mean():,.2f}"
)

print(
    f"Median customer revenue: "
    f"£{rfm['Monetary'].median():,.2f}"
)

print(
    f"Average orders per customer: "
    f"{rfm['Frequency'].mean():.2f}"
)


# ==================================================
# 9. Customer segments
# ==================================================

print("\n========== CUSTOMER SEGMENTS ==========")

segment_summary = (
    rfm.groupby("Segment", observed=True)
       .agg(
           Customers=("CustomerID", "count"),
           Revenue=("Monetary", "sum"),
           AvgRevenue=("Monetary", "mean"),
           AvgOrders=("Frequency", "mean")
       )
       .sort_values("Revenue", ascending=False)
)

print(segment_summary)


# ==================================================
# 10. Top customers
# ==================================================

print("\n========== TOP 20 CUSTOMERS ==========")

top_customers = (
    rfm.sort_values(
        "Monetary",
        ascending=False
    )
    .head(20)
)

print(
    top_customers[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "AverageOrderValue",
            "Segment"
        ]
    ].to_string(index=False)
)


# ==================================================
# 11. At-risk customers
# ==================================================

print("\n========== AT-RISK CUSTOMERS ==========")

at_risk = rfm[
    rfm["Segment"] == "At Risk"
].sort_values(
    "Monetary",
    ascending=False
)

print(f"At-risk customers: {len(at_risk):,}")

print(
    at_risk[
        [
            "CustomerID",
            "Recency",
            "Frequency",
            "Monetary",
            "Segment"
        ]
    ]
    .head(20)
    .to_string(index=False)
)


# ==================================================
# 12. Save customer-level dataset
# ==================================================

output_file = (
    "data/processed/customer_rfm_analysis.csv"
)

rfm.to_csv(
    output_file,
    index=False
)


# ==================================================
# 13. Save segment summary
# ==================================================

segment_summary.to_csv(
    "data/processed/customer_segment_summary.csv"
)


# ==================================================
# 14. Final confirmation
# ==================================================

print("\n========== FILES CREATED ==========")

print("data/processed/customer_rfm_analysis.csv")
print("data/processed/customer_segment_summary.csv")

print("\nRFM analysis completed successfully.")
