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
# 2. Create transaction month
# ==================================================

df["InvoiceMonth"] = (
    df["InvoiceDate"]
    .dt.to_period("M")
)


# ==================================================
# 3. Find each customer's first purchase month
# ==================================================

customer_first_purchase = (
    df.groupby("CustomerID")["InvoiceMonth"]
      .min()
      .reset_index()
)

customer_first_purchase.columns = [
    "CustomerID",
    "CohortMonth"
]


# ==================================================
# 4. Add cohort month to transactions
# ==================================================

df = df.merge(
    customer_first_purchase,
    on="CustomerID",
    how="left"
)


# ==================================================
# 5. Calculate months since first purchase
# ==================================================

df["CohortIndex"] = (
    (df["InvoiceMonth"].dt.year - df["CohortMonth"].dt.year) * 12
    +
    (df["InvoiceMonth"].dt.month - df["CohortMonth"].dt.month)
    + 1
)


# ==================================================
# 6. Calculate unique customers by cohort
# ==================================================

cohort_data = (
    df.groupby(
        ["CohortMonth", "CohortIndex"]
    )["CustomerID"]
    .nunique()
    .reset_index()
)


# ==================================================
# 7. Create retention matrix
# ==================================================

cohort_table = cohort_data.pivot(
    index="CohortMonth",
    columns="CohortIndex",
    values="CustomerID"
)


# ==================================================
# 8. Calculate retention percentages
# ==================================================

cohort_sizes = (
    cohort_table.iloc[:, 0]
)

retention_table = (
    cohort_table
    .divide(cohort_sizes, axis=0)
    * 100
)


# ==================================================
# 9. Round values
# ==================================================

retention_table = retention_table.round(2)


# ==================================================
# 10. Display results
# ==================================================

print("\n========== COHORT RETENTION ==========")

print("\nCustomer counts:")
print(cohort_table)

print("\nRetention percentages:")
print(retention_table)


# ==================================================
# 11. Overall retention metrics
# ==================================================

# Month 1 retention
if 2 in retention_table.columns:

    month_1_retention = retention_table[2].dropna().mean()

    print(
        f"\nAverage Month 1 Retention: "
        f"{month_1_retention:.2f}%"
    )


# Month 3 retention
if 4 in retention_table.columns:

    month_3_retention = retention_table[4].dropna().mean()

    print(
        f"Average Month 3 Retention: "
        f"{month_3_retention:.2f}%"
    )


# Month 6 retention
if 7 in retention_table.columns:

    month_6_retention = retention_table[7].dropna().mean()

    print(
        f"Average Month 6 Retention: "
        f"{month_6_retention:.2f}%"
    )


# ==================================================
# 12. Cohort sizes
# ==================================================

print("\n========== COHORT SIZES ==========")

cohort_sizes_df = (
    cohort_sizes
    .reset_index()
)

cohort_sizes_df.columns = [
    "CohortMonth",
    "Customers"
]

print(cohort_sizes_df)


# ==================================================
# 13. Save retention table
# ==================================================

retention_output = (
    "data/processed/cohort_retention.csv"
)

retention_table.to_csv(
    retention_output
)


# ==================================================
# 14. Save cohort customer counts
# ==================================================

cohort_output = (
    "data/processed/cohort_customer_counts.csv"
)

cohort_table.to_csv(
    cohort_output
)


# ==================================================
# 15. Save customer cohort mapping
# ==================================================

customer_cohort_output = (
    "data/processed/customer_cohort.csv"
)

customer_first_purchase.to_csv(
    customer_cohort_output,
    index=False
)


# ==================================================
# 16. Final confirmation
# ==================================================

print("\n========== FILES CREATED ==========")

print(retention_output)
print(cohort_output)
print(customer_cohort_output)

print("\nCohort analysis completed successfully.")