# E-Commerce Sales & Customer Analytics

An end-to-end **Data Analytics and Business Intelligence project** focused on analyzing e-commerce sales performance, customer purchasing behavior, customer segmentation, product performance, and geographic sales trends using **Python, SQL, and Power BI**.

The project follows a complete analytics workflow from data cleaning and preprocessing to exploratory analysis, customer analytics, cohort analysis, SQL analysis, and interactive Power BI dashboards.

---

## 📌 Project Overview

This project analyzes e-commerce transactional data to generate meaningful business insights across sales, products, customers, and markets.

The project covers the complete analytics workflow:

- Data inspection
- Data cleaning and preprocessing
- Data quality validation
- Exploratory Data Analysis (EDA)
- Customer analytics
- Customer segmentation
- Cohort analysis
- SQL-based business analysis
- Power BI data modeling
- Interactive dashboard development
- Business insights and recommendations

The final deliverable is a **3-page interactive Power BI dashboard** designed for business performance monitoring and data-driven decision-making.

---

## 🎯 Business Objectives

The main objectives of this project are:

1. Analyze overall sales and revenue performance.
2. Identify monthly revenue trends.
3. Identify top-performing products.
4. Analyze revenue contribution by country.
5. Understand customer purchasing behavior.
6. Segment customers based on purchasing activity and value.
7. Identify high-value customers.
8. Identify at-risk and lost customers.
9. Compare customer segments based on revenue and purchasing behavior.
10. Generate actionable business recommendations.

---

## 🛠️ Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| **Python** | Data cleaning, preprocessing, EDA and customer analysis |
| **Pandas** | Data manipulation and transformation |
| **NumPy** | Numerical analysis |
| **Matplotlib** | Exploratory data visualization |
| **SQL** | Sales and customer analysis |
| **SQLite** | Analytical database |
| **Power BI** | Interactive dashboard development |
| **DAX** | KPI calculations and measures |
| **Git & GitHub** | Version control and project documentation |

---

## 🔄 Project Workflow

```text
Raw E-Commerce Data
        ↓
Data Inspection
        ↓
Data Cleaning & Preprocessing
        ↓
Data Quality Checks
        ↓
Exploratory Data Analysis
        ↓
Customer Analytics
        ↓
Cohort Analysis
        ↓
SQLite Database
        ↓
SQL Analysis
        ↓
Power BI Data Modeling
        ↓
Interactive Dashboard
        ↓
Business Insights & Recommendations
```

---

## 📁 Project Structure

```text
E-Commerce-Sales-Customer-Analytics/
│
├── E-Commerce-Sales-Customer-Analytics Dashboard/
│   └── Power BI Dashboard (.pbix)
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│
├── python/
│   ├── 01_data_inspection.py
│   ├── 02_data_cleaning.py
│   ├── 03_eda.py
│   ├── 04_data_quality.py
│   ├── 05_customer_analytics.py
│   ├── 06_cohort_analysis.py
│   ├── 07_create_database.py
│   ├── 08_run_sql.py
│   └── 09_run_customer_sql.py
│
├── sql/
│   ├── 01_sales_performance.sql
│   └── 02_customer_analysis.sql
│
├── .gitattributes
├── .gitignore
├── requirements.txt
└── README.md
```

---

# 🧹 Data Preparation

The raw e-commerce transaction data was cleaned and prepared before performing analysis.

The data preparation process included:

- Inspecting dataset structure
- Checking column names and data types
- Identifying missing values
- Checking duplicate records
- Identifying invalid transactions
- Filtering invalid quantity values
- Checking price-related values
- Converting date fields into appropriate formats
- Creating revenue-related calculations
- Preparing monthly date fields
- Creating customer-level metrics
- Preparing processed data for SQL and Power BI

Data quality checks were performed to improve the consistency and reliability of the analysis.

---

# 🐍 Python Analysis

Python was used for data inspection, cleaning, exploratory analysis, customer analytics, cohort analysis, and database preparation.

## 1. Data Inspection

**File:** `python/01_data_inspection.py`

The dataset was inspected to understand:

- Number of rows and columns
- Column names
- Data types
- Missing values
- Duplicate records
- Basic statistics
- Customer and transaction information

---

## 2. Data Cleaning

**File:** `python/02_data_cleaning.py`

The data cleaning process included:

- Handling invalid records
- Preparing data types
- Cleaning transaction data
- Creating analytical fields
- Preparing the processed dataset

---

## 3. Exploratory Data Analysis

**File:** `python/03_eda.py`

Exploratory analysis was performed to understand:

- Revenue trends
- Sales patterns
- Product performance
- Geographic performance
- Transaction behavior

---

## 4. Data Quality Checks

**File:** `python/04_data_quality.py`

Additional validation checks were performed to identify potential data-quality issues before analysis.

---

## 5. Customer Analytics

**File:** `python/05_customer_analytics.py`

Customer-level analysis was performed to understand:

- Customer purchasing behavior
- Customer revenue
- Purchase frequency
- Customer activity
- Customer value

---

## 6. Cohort Analysis

**File:** `python/06_cohort_analysis.py`

Cohort analysis was used to study customer behavior and retention patterns across different customer cohorts.

---

## 7. Database Creation

**File:** `python/07_create_database.py`

The cleaned dataset was loaded into a SQLite database to enable structured SQL analysis.

---

## 8. Sales SQL Execution

**File:** `python/08_run_sql.py`

This script was used to execute sales performance queries against the analytical database.

---

## 9. Customer SQL Execution

**File:** `python/09_run_customer_sql.py`

This script was used to execute customer-focused SQL analysis.

---

# 🗄️ SQL Analysis

SQL was used to perform structured business analysis on the cleaned e-commerce data.

The SQL analysis is divided into two main areas:

1. Sales Performance Analysis
2. Customer Analysis

---

## 1. Sales Performance Analysis

**File:** `sql/01_sales_performance.sql`

The sales analysis focuses on:

- Total revenue
- Total orders
- Total quantity sold
- Average order value
- Monthly revenue
- Revenue by country
- Revenue by product
- Product performance
- Overall sales performance

### Business Questions

The analysis helps answer:

- What is the total revenue?
- How many orders were placed?
- How many units were sold?
- Which countries generate the most revenue?
- Which products generate the most revenue?
- How does revenue change over time?
- What is the average order value?

---

## 2. Customer Analysis

**File:** `sql/02_customer_analysis.sql`

The customer analysis focuses on:

- Customer count
- Customer revenue
- Purchase frequency
- Customer purchasing behavior
- Customer-level metrics
- Customer value
- Customer segmentation

### Business Questions

The analysis helps answer:

- Who are the highest-value customers?
- How frequently do customers purchase?
- Which customers contribute the most revenue?
- How does customer value differ across customers?
- Which customers may require retention efforts?

SQL analysis was also used to validate important metrics used in the Power BI dashboard.

---

# 👥 Customer Segmentation

Customer segmentation was performed to understand differences in customer purchasing behavior and value.

The analysis considers three key behavioral metrics:

### Recency

Measures how recently a customer made a purchase.

### Frequency

Measures how frequently a customer made purchases.

### Monetary Value

Measures how much revenue a customer generated.

These metrics were used to categorize customers into meaningful business segments.

## Customer Segments

| Segment | Description |
|---|---|
| **Champions** | Highly active and valuable customers |
| **Big Spenders** | Customers generating high revenue |
| **Loyal Customers** | Customers with strong purchasing engagement |
| **Potential Loyalists** | Customers showing potential for increased engagement |
| **Regular Customers** | Customers with relatively normal purchasing behavior |
| **New Customers** | Recently acquired customers |
| **At Risk** | Customers showing reduced purchasing activity |
| **Lost Customers** | Customers with a significant period of inactivity |

This segmentation helps identify customers who require different marketing and retention strategies.

---

# 📊 Power BI Dashboard

The final Power BI report contains **3 interactive dashboard pages**.

---

## 1️⃣ E-Commerce Sales & Customer Analytics

The first page provides an executive overview of overall business performance.

### Key KPIs

- **Total Orders:** 20K
- **Total Customers:** 4K
- **Total Revenue:** 10.64M
- **Total Quantity Sold:** 6M

### Visualizations

- Monthly Revenue Trend
- Revenue by Country
- Top 10 Products by Revenue
- KPI Cards

### Purpose

This page provides a quick overview of:

- Overall business performance
- Revenue trends
- Geographic revenue contribution
- Top-performing products
- Sales volume

---

## 2️⃣ Customer Analysis & Segmentation

The second page focuses on customer behavior, customer value, and segmentation.

### Key KPIs

- **Customers:** 4,338
- **Champions:** 942
- **At Risk Customers:** 570
- **Lost Customers:** 994

### Visualizations

- Customer Distribution by Segment
- Average Revenue by Customer Segment
- Customer Value vs Purchase Frequency
- Customer Segment Performance Table

### Purpose

This page helps identify:

- High-value customers
- Loyal customers
- Potential loyalists
- New customers
- At-risk customers
- Lost customers
- Differences in customer value and purchase frequency

---

## 3️⃣ Product & Sales Insights

The third page focuses on product and geographic sales performance.

### Key KPIs

- **Total Revenue:** 10.64M
- **Total Orders:** 20K
- **Total Quantity Sold:** 6M
- **Average Order Value:** 533.17

### Visualizations

- Top 10 Products by Revenue
- Revenue by Country

### Purpose

This page helps identify:

- Best-performing products
- Major revenue-generating markets
- Product revenue contribution
- Geographic sales concentration

---

# 📸 Dashboard Preview

## Page 1 – E-Commerce Sales & Customer Analytics

![E-Commerce Sales & Customer Analytics](E-Commerce-Sales-Customer-Analytics%20Dashboard/Screenshots/page%201%20-%20E-Commerce%20Sales%20%26%20Customer%20Analytics.png)

This page provides an overall view of the e-commerce business, including:

- Total Orders
- Total Customers
- Total Revenue
- Total Quantity Sold
- Monthly Revenue Trend
- Revenue by Country
- Top 10 Products by Revenue

---

## Page 2 – Customer Analysis & Segmentation

![Customer Analysis & Segmentation](E-Commerce-Sales-Customer-Analytics%20Dashboard/Screenshots/page%202%20-%20Customer%20Analysis%20%26%20Segmentation.png)

This page focuses on customer behavior and segmentation using RFM-based customer analysis.

Key insights include:

- Total Customers
- Champions
- At Risk Customers
- Lost Customers
- Customer Distribution by Segment
- Average Revenue by Customer Segment
- Customer Value vs Purchase Frequency
- Customer Segment Performance
- Segment, Recency, Frequency and Revenue analysis

---

## Page 3 – Product & Sales Insights

![Product & Sales Insights](E-Commerce-Sales-Customer-Analytics%20Dashboard/Screenshots/page%203%20-%20Product%20%26%20Sales%20Insights.png)

This page focuses on product performance and geographic sales contribution.

Key insights include:

- Total Revenue
- Total Orders
- Total Quantity Sold
- Average Order Value
- Top 10 Products by Revenue
- Revenue by Country

---

## 📊 Dashboard Highlights

The Power BI dashboard combines sales, customer and product analytics into an interactive three-page reporting solution.

### Page 1 – Sales Overview

Provides a high-level summary of business performance and identifies monthly revenue trends, major markets and top-performing products.

### Page 2 – Customer Analytics

Analyzes customer value and purchasing behavior through customer segmentation, helping identify Champions, Loyal Customers, Potential Loyalists, At Risk Customers and Lost Customers.

### Page 3 – Product & Sales Insights

Highlights the products contributing most to revenue and shows the geographic distribution of sales across countries.

---

> **Note:** The dashboard screenshots are stored in the `E-Commerce-Sales-Customer-Analytics Dashboard/Screenshots/` directory..

---

# 📈 Key Business Insights

## Overall Sales Performance

- Total revenue is approximately **10.64M**.
- The dataset contains approximately **20K orders**.
- Approximately **6M units** were sold.
- Average order value is approximately **533.17**.

## Revenue Trend

Revenue varies throughout the analyzed period, with stronger sales performance toward the later months.

The analysis shows a significant increase in revenue around **November 2011**.

## Product Performance

The analysis identifies several high-performing products contributing significantly to overall revenue.

Examples include:

- DOTCOM POSTAGE
- REGENCY CAKESTAND 3 TIER
- PAPER CRAFT, LITTLE BIRDIE
- WHITE HANGING HEART T-LIGHT HOLDER
- PARTY BUNTING

## Geographic Performance

The **United Kingdom** is the dominant revenue-generating country in the dataset.

This makes the UK the most important market within the analyzed transactions.

## Customer Segmentation

The customer analysis highlights significant differences in purchasing behavior and customer value.

**Champions** represent highly valuable customers with strong purchasing activity and revenue contribution.

## Customer Retention

The presence of **At Risk** and **Lost Customers** highlights opportunities for customer retention and re-engagement.

---

# 💡 Business Recommendations

## 1. Retain Champions

Champions represent highly valuable customers.

Recommended strategies:

- Loyalty programs
- Exclusive offers
- Personalized recommendations
- Early access to products
- VIP benefits

## 2. Re-Engage At-Risk Customers

At-risk customers can be targeted through:

- Personalized email campaigns
- Special discounts
- Product recommendations
- Limited-time offers
- Re-engagement campaigns

## 3. Win Back Lost Customers

Lost customers can be targeted through:

- Win-back campaigns
- Personalized offers
- New product announcements
- Discounts based on previous purchases

## 4. Increase Potential Loyalists

Potential loyalists can be encouraged to increase purchase frequency through:

- Cross-selling
- Product bundles
- Loyalty rewards
- Personalized recommendations

## 5. Optimize High-Performing Products

Top-performing products can be prioritized for:

- Inventory planning
- Marketing campaigns
- Promotional activities
- Product bundling
- Cross-selling

## 6. Strengthen High-Performing Markets

The strong contribution from the UK suggests opportunities to:

- Strengthen customer retention
- Optimize marketing campaigns
- Improve product availability
- Identify expansion opportunities in other markets

---

# 📌 Key Metrics

| Metric | Value |
|---|---:|
| Total Revenue | 10.64M |
| Total Orders | 20K |
| Total Quantity Sold | 6M |
| Average Order Value | 533.17 |
| Total Customers | 4,338 |
| Champions | 942 |
| At Risk Customers | 570 |
| Lost Customers | 994 |

---

# 🎛️ Power BI Dashboard Features

The dashboard includes:

- Interactive KPI cards
- Revenue trend analysis
- Country-level analysis
- Product-level analysis
- Customer segmentation
- Customer value analysis
- Purchase frequency analysis
- Date filtering
- Country filtering
- Customer segment filtering
- Cross-filtering between visuals
- Interactive business analysis

---

# 🧮 DAX & KPI Analysis

Power BI measures were used to calculate important business metrics including:

- Total Revenue
- Total Orders
- Total Customers
- Total Quantity Sold
- Average Order Value
- Customer Counts
- Average Revenue by Customer Segment
- Customer Purchase Frequency
- Customer Recency

These measures allow dashboard metrics and visualizations to respond dynamically to user selections and filters.

---

# 🚀 How to Run the Project

## Prerequisites

Make sure you have the following installed:

- Python 3.x
- Power BI Desktop
- Git

---

## Step 1 — Clone the Repository

```bash
git clone https://github.com/Sriyansh01/E-Commerce-Sales-Customer-Analytics.git
```

---

## Step 2 — Navigate to the Project

```bash
cd E-Commerce-Sales-Customer-Analytics
```

---

## Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Step 4 — Run Data Inspection

```bash
python python/01_data_inspection.py
```

---

## Step 5 — Run Data Cleaning

```bash
python python/02_data_cleaning.py
```

---

## Step 6 — Run Exploratory Data Analysis

```bash
python python/03_eda.py
```

---

## Step 7 — Run Data Quality Checks

```bash
python python/04_data_quality.py
```

---

## Step 8 — Run Customer Analytics

```bash
python python/05_customer_analytics.py
```

---

## Step 9 — Run Cohort Analysis

```bash
python python/06_cohort_analysis.py
```

---

## Step 10 — Create SQLite Database

```bash
python python/07_create_database.py
```

---

## Step 11 — Run Sales SQL Analysis

```bash
python python/08_run_sql.py
```

---

## Step 12 — Run Customer SQL Analysis

```bash
python python/09_run_customer_sql.py
```

---

## Step 13 — Open Power BI Dashboard

Open the `.pbix` file located inside:

```text
E-Commerce-Sales-Customer-Analytics Dashboard/
```

using Power BI Desktop.

---

# 📚 Skills Demonstrated

## Data Analytics

- Data Cleaning
- Data Preprocessing
- Exploratory Data Analysis
- Data Quality Checks
- Customer Analytics
- Cohort Analysis
- Business Analysis

## Python

- Pandas
- NumPy
- Matplotlib
- Data Transformation
- Data Analysis
- SQLite Integration

## SQL

- Data Aggregation
- Filtering
- Grouping
- Sorting
- Revenue Analysis
- Customer Analysis
- Product Analysis
- Country-Level Analysis
- Business-Oriented Analytical Queries

## Power BI

- Data Modeling
- DAX
- KPI Development
- Interactive Dashboards
- Data Visualization
- Customer Segmentation
- Cross-Filtering
- Business Intelligence

## Business Intelligence

- KPI Monitoring
- Customer Value Analysis
- Customer Retention Analysis
- Product Performance Analysis
- Geographic Analysis
- Business Recommendations
- Data Storytelling

---

# 🎓 Project Learning Outcomes

This project provided practical experience in building an end-to-end analytics solution.

Key learning outcomes include:

- Working with transactional e-commerce data
- Cleaning and preparing data for analysis
- Performing exploratory data analysis
- Writing analytical SQL queries
- Creating customer-level metrics
- Performing customer segmentation
- Analyzing customer retention behavior
- Building interactive Power BI dashboards
- Developing DAX measures
- Identifying business trends
- Translating analytical findings into business recommendations
- Presenting insights through data visualization

---

# 🔮 Future Improvements

Potential future enhancements include:

- Customer Lifetime Value (CLV) analysis
- Profit and margin analysis
- Sales forecasting
- Customer churn prediction
- Product recommendation analysis
- Advanced customer segmentation
- Year-over-Year growth analysis
- Automated Power BI refresh
- Power BI Service deployment
- Advanced cohort retention analysis

---

# 👤 Author

## Sriyansh Mishra

**Data Analytics | Python | SQL | Power BI**

GitHub: https://github.com/Sriyansh01

---

# ⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.

---