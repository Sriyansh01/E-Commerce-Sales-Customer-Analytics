E-Commerce Sales & Customer Analytics

An end-to-end Data Analytics and Business Intelligence project that analyzes e-commerce sales performance, customer purchasing behavior, customer segmentation, product performance, and geographic sales trends using Python, SQL, and Power BI.

The project follows a complete analytics workflow, from data inspection and cleaning to exploratory analysis, customer analytics, cohort analysis, SQL analysis, and interactive Power BI dashboards.

📌 Project Overview

E-commerce transaction data contains valuable information about sales, customers, products, and markets. This project transforms transactional data into actionable business insights through data preparation, exploratory analysis, SQL-based analysis, customer segmentation, and interactive visualization.

The project focuses on answering important business questions related to:

Sales and revenue performance
Monthly sales trends
Customer purchasing behavior
Customer segmentation
Customer retention
Product performance
Geographic sales contribution
High-value customers
At-risk and lost customers

The final output is a 3-page interactive Power BI dashboard designed for business performance monitoring and decision-making.

🎯 Business Objectives

The main objectives of this project are:

Analyze overall sales and revenue performance.
Identify monthly revenue trends.
Identify top-performing products.
Analyze revenue contribution by country.
Understand customer purchasing behavior.
Segment customers based on purchasing activity and value.
Identify high-value customers.
Identify customers who are at risk of being lost.
Compare customer segments based on revenue and purchasing behavior.
Generate actionable business recommendations from the analysis.
🛠️ Tools & Technologies
Tool / Technology	Purpose
Python	Data inspection, cleaning, preprocessing and analysis
Pandas	Data manipulation and transformation
NumPy	Numerical analysis
Matplotlib	Exploratory data visualization
SQL	Business and customer analysis
SQLite	Analytical database
Power BI	Interactive dashboard and visualization
DAX	KPI calculations and analytical measures
Git & GitHub	Version control and project documentation
🔄 Project Workflow
text
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
SQL Analysis
        ↓
Power BI Data Modeling
        ↓
Interactive Dashboard
        ↓
Business Insights & Recommendations
📁 Project Structure
E-Commerce-Sales-Customer-Analytics/
│
├── E-Commerce-Sales-Customer-Analytics Dashboard/
│   ├── E-Commerce_Sales_Customer_Analytics.pbix
│   └── Screenshots/
│       ├── page 1 - E-Commerce Sales & Customer Analytics.png
│       ├── page 2 - Customer Analysis & Segmentation.png
│       └── page 3 - Product & Sales Insights.png
│
├── data/
│   ├── raw/
│   └── processed/
│
├── images/
│   └── monthly_revenue.png
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
🧹 Data Preparation

The raw e-commerce transaction data was cleaned and prepared before performing analysis.

The data preparation process included:

Inspecting the dataset structure
Checking column names and data types
Identifying missing values
Identifying duplicate records
Identifying invalid transactions
Filtering invalid quantities
Checking price-related values
Converting date columns into appropriate formats
Creating revenue-related calculations
Preparing monthly and date-based fields
Creating customer-level metrics
Preparing cleaned data for SQL and Power BI analysis

Data quality checks were performed throughout to improve the reliability and consistency of the analysis.

🐍 Python Analysis

Python was used for data inspection, cleaning, exploratory data analysis, customer analytics, cohort analysis, and database preparation.

Python Analysis Workflow

1. Data Inspection — 01_data_inspection.py Used to understand:

Dataset structure
Number of rows and columns
Data types
Missing values
Duplicate records
Basic statistics
Unique customers and transactions

2. Data Cleaning — 02_data_cleaning.py Used to prepare the dataset for analysis by:

Cleaning invalid records
Handling missing values
Preparing data types
Creating analytical fields
Preparing the processed dataset

3. Exploratory Data Analysis — 03_eda.py Used to explore:

Revenue trends
Sales patterns
Product performance
Geographic performance
Transaction behavior

4. Data Quality — 04_data_quality.py Used to perform additional data validation and identify potential data-quality issues.

5. Customer Analytics — 05_customer_analytics.py Used to analyze customer-level purchasing behavior and calculate customer metrics.

6. Cohort Analysis — 06_cohort_analysis.py Used to analyze customer behavior and retention patterns across customer cohorts.

7. Database Creation — 07_create_database.py Used to create the analytical SQLite database for SQL-based analysis.

8. Sales SQL Execution — 08_run_sql.py Used to execute sales performance SQL analysis.

9. Customer SQL Execution — 09_run_customer_sql.py Used to execute customer-focused SQL analysis.

🗄️ SQL Analysis

SQL was used to perform structured business analysis on the cleaned e-commerce transaction data. The analysis is divided into two main areas.

1. Sales Performance Analysis — sql/01_sales_performance.sql

The analysis focuses on:

Total revenue
Total orders
Total quantity sold
Average order value
Monthly revenue
Revenue by country
Revenue by product
Product performance
Sales performance

Business questions answered:

How much revenue was generated?
How many orders were placed?
How many units were sold?
Which countries generate the most revenue?
Which products generate the most revenue?
How does revenue change over time?
What is the average order value?
2. Customer Analysis — sql/02_customer_analysis.sql

The analysis focuses on:

Customer count
Customer revenue
Customer purchasing behavior
Purchase frequency
Customer-level metrics
Customer value
Customer segmentation analysis

Business questions answered:

Who are the highest-value customers?
How frequently do customers purchase?
Which customers contribute the most revenue?
How does customer value differ across customers?
Which customers may require retention efforts?

SQL analysis was also used to support and validate important business metrics used in the dashboard.

👥 Customer Segmentation

Customer segmentation was performed to understand customer value and purchasing behavior, based on three key metrics:

Recency — How recently a customer made a purchase.
Frequency — How frequently a customer made purchases.
Monetary Value — How much revenue a customer generated.

These customer-level metrics were used to categorize customers into meaningful business segments.

Segment	Description
Champions	Highly active and valuable customers
Big Spenders	Customers generating high revenue
Loyal Customers	Customers with strong purchasing engagement
Potential Loyalists	Customers showing potential for increased engagement
Regular Customers	Customers with relatively normal purchasing behavior
New Customers	Recently acquired customers
At Risk	Customers showing reduced purchasing activity
Lost Customers	Customers with a significant period of inactivity

This segmentation helps businesses develop targeted marketing and customer-retention strategies.

📊 Power BI Dashboard

The final Power BI report contains three interactive dashboard pages.

1️⃣ E-Commerce Sales & Customer Analytics

Executive-level overview of overall business performance.

Key KPIs: Total Orders: 20K · Total Customers: 4K · Total Revenue: 10.64M · Total Quantity Sold: 6M

Visualizations: Monthly Revenue Trend · Revenue by Country · Top 10 Products by Revenue · KPI Cards

Purpose: Quick overview of overall business performance, revenue trends, geographic revenue contribution, top-performing products, and overall sales volume.

2️⃣ Customer Analysis & Segmentation

Focuses on customer behavior, customer value, and segmentation.

Key KPIs: Customers: 4,338 · Champions: 942 · At Risk Customers: 570 · Lost Customers: 994

Visualizations: Customer Distribution by Segment · Average Revenue by Customer Segment · Customer Value vs Purchase Frequency · Customer Segment Performance Table

Purpose: Identify high-value, loyal, potential-loyalist, new, at-risk, and lost customers, and differences in customer value and purchasing frequency.

3️⃣ Product & Sales Insights

Focuses on product and geographic sales performance.

Key KPIs: Total Revenue: 10.64M · Total Orders: 20K · Total Quantity Sold: 6M · Average Order Value: 533.17

Visualizations: Top 10 Products by Revenue · Revenue by Country

Purpose: Identify best-performing products, major revenue-generating markets, product revenue contribution, and geographic sales concentration.

📷 Dashboard Screenshots
Page 1 — Sales & Customer Analytics	Page 2 — Customer Segmentation	Page 3 — Product & Sales Insights
E-Commerce-Sales-Customer-Analytics Dashboard/Screenshots/page 1 - E-Commerce Sales & Customer Analytics.png	.../page 2 - Customer Analysis & Segmentation.png	.../page 3 - Product & Sales Insights.png
📈 Key Business Insights

Sales Performance

The business generated approximately 10.64M in total revenue.
More than 20K orders were recorded.
Approximately 6M units were sold.
The average order value is approximately 533.17.

Revenue Trends

Revenue varies across the analyzed period, with stronger sales performance toward the later months.
The monthly analysis shows a significant increase in revenue around November 2011.

Product Performance

A small group of products contributes significantly to overall revenue. High-performing products include:

DOTCOM POSTAGE
REGENCY CAKESTAND 3 TIER
PAPER CRAFT, LITTLE BIRDIE
WHITE HANGING HEART T-LIGHT HOLDER
PARTY BUNTING

Geographic Performance

The United Kingdom is the dominant revenue-generating country in the dataset, making it the most important market within the analyzed transactions.

Customer Performance

The customer segmentation analysis shows significant differences in customer purchasing behavior.
Champions represent highly valuable customers with strong purchasing activity and revenue contribution.

Customer Retention

The presence of At Risk and Lost Customers highlights opportunities for customer retention and re-engagement.
💡 Business Recommendations
Retain Champions — loyalty programs, exclusive offers, personalized recommendations, early access to products, VIP benefits.
Re-Engage At-Risk Customers — personalized email campaigns, special discounts, product recommendations, limited-time offers, re-engagement campaigns.
Win Back Lost Customers — win-back campaigns, personalized offers, new product announcements, discounts based on previous purchases.
Increase Potential Loyalists — cross-selling, product bundles, loyalty rewards, personalized recommendations.
Optimize High-Performing Products — prioritize for inventory planning, marketing campaigns, promotional activities, product bundling, cross-selling.
Strengthen High-Performing Markets — strengthen customer retention, optimize marketing campaigns, improve product availability, and identify expansion opportunities in other markets given the UK's strong contribution.
📌 Key Metrics
Metric	Value
Total Revenue	10.64M
Total Orders	20K
Total Quantity Sold	6M
Average Order Value	533.17
Total Customers	4,338
Champions	942
At Risk Customers	570
Lost Customers	994
🎛️ Power BI Dashboard Features
Interactive KPI cards
Revenue trend analysis
Country-level analysis
Product-level analysis
Customer segmentation
Customer value analysis
Purchase frequency analysis
Date filtering
Country filtering
Customer segment filtering
Cross-filtering between visuals
Interactive business analysis
🧮 DAX & KPI Analysis

Power BI measures were used to calculate and analyze important business metrics, including:

Total Revenue
Total Orders
Total Customers
Total Quantity Sold
Average Order Value
Customer Counts
Average Revenue by Customer Segment
Customer Purchase Frequency
Customer Recency

These measures allow the dashboard to dynamically update based on selected filters and customer segments.

🚀 How to Run the Project

Step 1 — Clone the repository

bash
git clone https://github.com/Sriyansh01/E-Commerce-Sales-Customer-Analytics.git

Step 2 — Navigate to the project

bash
cd E-Commerce-Sales-Customer-Analytics

Step 3 — Install Python dependencies

bash
pip install -r requirements.txt

Step 4 — Run data inspection

bash
python python/01_data_inspection.py

Step 5 — Run data cleaning

bash
python python/02_data_cleaning.py

Step 6 — Run exploratory data analysis

bash
python python/03_eda.py

Step 7 — Run data quality checks

bash
python python/04_data_quality.py

Step 8 — Run customer analytics

bash
python python/05_customer_analytics.py

Step 9 — Run cohort analysis

bash
python python/06_cohort_analysis.py

Step 10 — Create the analytical database

bash
python python/07_create_database.py

Step 11 — Run sales SQL analysis

bash
python python/08_run_sql.py

Step 12 — Run customer SQL analysis

bash
python python/09_run_customer_sql.py

Step 13 — Open the Power BI dashboard

Open the following file using Power BI Desktop:

E-Commerce-Sales-Customer-Analytics Dashboard/
└── E-Commerce_Sales_Customer_Analytics.pbix
📚 Skills Demonstrated

Data Analytics — Data Cleaning · Data Preprocessing · Exploratory Data Analysis · Data Quality Checks · Customer Analytics · Cohort Analysis · Business Analysis

Python — Pandas · NumPy · Matplotlib · Data Transformation · Data Analysis · SQLite Integration

SQL — Data Aggregation · Filtering · Grouping · Sorting · Revenue Analysis · Customer Analysis · Product Analysis · Country-Level Analysis · Business-Oriented Analytical Queries

Power BI — Data Modeling · DAX · KPI Development · Interactive Dashboards · Data Visualization · Customer Segmentation · Cross-Filtering

Business Intelligence — KPI Monitoring · Customer Value Analysis · Customer Retention Analysis · Product Performance Analysis · Geographic Analysis · Business Recommendations · Data Storytelling

🎓 Project Learning Outcomes

This project provided practical experience in building an end-to-end analytics solution, including:

Working with real-world transactional data
Cleaning and preparing data for analysis
Performing exploratory data analysis
Writing analytical SQL queries
Creating customer-level metrics
Performing customer segmentation
Analyzing customer retention behavior
Building interactive Power BI dashboards
Developing DAX measures
Identifying business trends
Translating analytical findings into business recommendations
Presenting insights through data visualization
🔮 Future Improvements
Customer Lifetime Value (CLV) analysis
Profit and margin analysis
Sales forecasting
Customer churn prediction
Product recommendation analysis
Advanced customer segmentation
Year-over-Year growth analysis
Automated Power BI refresh
Power BI Service deployment
Advanced cohort retention analysis
👤 Author

Sriyansh Mishra Data Analytics | Python | SQL | Power BI

GitHub: https://github.com/Sriyansh01

⭐ Project

If you found this project useful, consider giving the repository a ⭐ on GitHub.