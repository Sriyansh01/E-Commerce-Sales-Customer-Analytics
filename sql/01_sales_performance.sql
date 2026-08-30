-- ============================================================
-- E-COMMERCE SALES & CUSTOMER ANALYTICS
-- SQL ANALYSIS 01: SALES PERFORMANCE
-- ============================================================


-- ============================================================
-- 1. MONTHLY SALES PERFORMANCE
-- ============================================================
-- Business Question:
-- How does revenue, orders and customers change month by month?

SELECT
    strftime('%Y-%m', InvoiceDate) AS Month,
    ROUND(SUM(Revenue), 2) AS Revenue,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    COUNT(DISTINCT CustomerID) AS Customers
FROM sales
GROUP BY Month
ORDER BY Month;


-- ============================================================
-- 2. MONTHLY REVENUE GROWTH
-- ============================================================
-- Business Question:
-- Which months experienced the strongest revenue growth?

WITH monthly_sales AS (
    SELECT
        strftime('%Y-%m', InvoiceDate) AS Month,
        SUM(Revenue) AS Revenue
    FROM sales
    GROUP BY Month
)

SELECT
    Month,
    ROUND(Revenue, 2) AS Revenue,
    ROUND(
        (Revenue - LAG(Revenue) OVER (ORDER BY Month))
        / LAG(Revenue) OVER (ORDER BY Month) * 100,
        2
    ) AS Revenue_Growth_Percent
FROM monthly_sales
ORDER BY Month;


-- ============================================================
-- 3. AVERAGE ORDER VALUE
-- ============================================================
-- Business Question:
-- What is the average revenue generated per order?

SELECT
    ROUND(SUM(Revenue), 2) AS Total_Revenue,
    COUNT(DISTINCT InvoiceNo) AS Total_Orders,
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS Average_Order_Value
FROM sales;


-- ============================================================
-- 4. TOP 10 PRODUCTS BY REVENUE
-- ============================================================
-- Business Question:
-- Which products contribute the most revenue?

SELECT
    Description AS Product,
    ROUND(SUM(Revenue), 2) AS Revenue,
    SUM(Quantity) AS Quantity_Sold,
    COUNT(DISTINCT InvoiceNo) AS Orders
FROM sales
GROUP BY Description
ORDER BY Revenue DESC
LIMIT 10;


-- ============================================================
-- 5. TOP 10 COUNTRIES BY REVENUE
-- ============================================================
-- Business Question:
-- Which markets generate the most revenue?

SELECT
    Country,
    ROUND(SUM(Revenue), 2) AS Revenue,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    COUNT(DISTINCT CustomerID) AS Customers
FROM sales
GROUP BY Country
ORDER BY Revenue DESC
LIMIT 10;


-- ============================================================
-- 6. YEARLY SALES PERFORMANCE
-- ============================================================
-- Business Question:
-- How did yearly revenue and order volume change?

SELECT
    strftime('%Y', InvoiceDate) AS Year,
    ROUND(SUM(Revenue), 2) AS Revenue,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    COUNT(DISTINCT CustomerID) AS Customers
FROM sales
GROUP BY Year
ORDER BY Year;


-- ============================================================
-- 7. PRODUCT REVENUE CONTRIBUTION
-- ============================================================
-- Business Question:
-- What percentage of total revenue comes from each product?

WITH product_sales AS (
    SELECT
        Description AS Product,
        SUM(Revenue) AS Revenue
    FROM sales
    GROUP BY Description
)

SELECT
    Product,
    ROUND(Revenue, 2) AS Revenue,
    ROUND(
        Revenue * 100.0 /
        SUM(Revenue) OVER (),
        2
    ) AS Revenue_Percentage
FROM product_sales
ORDER BY Revenue DESC
LIMIT 20;