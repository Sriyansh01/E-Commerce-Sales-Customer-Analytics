-- ============================================================
-- CUSTOMER & BUSINESS ANALYSIS
-- ============================================================


-- ============================================================
-- 1. TOP 20 CUSTOMERS BY REVENUE
-- ============================================================

SELECT
    CustomerID,
    Frequency AS Orders,
    Monetary AS Revenue,
    AverageOrderValue,
    Segment
FROM customer_rfm
ORDER BY Monetary DESC
LIMIT 20;


-- ============================================================
-- 2. CUSTOMER SEGMENT PERFORMANCE
-- ============================================================

SELECT
    Segment,
    COUNT(*) AS Customers,
    ROUND(SUM(Monetary), 2) AS Total_Revenue,
    ROUND(AVG(Monetary), 2) AS Avg_Customer_Revenue,
    ROUND(AVG(Frequency), 2) AS Avg_Orders_Per_Customer,
    ROUND(AVG(AverageOrderValue), 2) AS Avg_Order_Value
FROM customer_rfm
GROUP BY Segment
ORDER BY Total_Revenue DESC;


-- ============================================================
-- 3. AT-RISK CUSTOMER ANALYSIS
-- ============================================================

SELECT
    CustomerID,
    Recency,
    Frequency,
    ROUND(Monetary, 2) AS Revenue,
    ROUND(AverageOrderValue, 2) AS AverageOrderValue,
    Segment
FROM customer_rfm
WHERE Segment = 'At Risk'
ORDER BY Monetary DESC
LIMIT 20;


-- ============================================================
-- 4. REVENUE CONTRIBUTION OF TOP 10% CUSTOMERS
-- ============================================================

WITH customer_rank AS (
    SELECT
        CustomerID,
        Monetary,
        NTILE(10) OVER (ORDER BY Monetary DESC) AS Revenue_Decile
    FROM customer_rfm
)

SELECT
    ROUND(
        SUM(
            CASE
                WHEN Revenue_Decile = 1 THEN Monetary
                ELSE 0
            END
        ),
        2
    ) AS Top_10_Percent_Revenue,

    ROUND(SUM(Monetary), 2) AS Total_Revenue,

    ROUND(
        100.0 *
        SUM(
            CASE
                WHEN Revenue_Decile = 1 THEN Monetary
                ELSE 0
            END
        ) / SUM(Monetary),
        2
    ) AS Revenue_Contribution_Percent
FROM customer_rank;


-- ============================================================
-- 5. COUNTRY PERFORMANCE BY AVERAGE ORDER VALUE
-- ============================================================

SELECT
    Country,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    COUNT(DISTINCT CustomerID) AS Customers,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(
        SUM(Revenue) / COUNT(DISTINCT InvoiceNo),
        2
    ) AS Average_Order_Value
FROM customer_transactions
GROUP BY Country
HAVING COUNT(DISTINCT InvoiceNo) >= 10
ORDER BY Average_Order_Value DESC
LIMIT 15;


-- ============================================================
-- 6. PRODUCT PERFORMANCE
-- ============================================================

SELECT
    Description AS Product,
    COUNT(DISTINCT InvoiceNo) AS Orders,
    SUM(Quantity) AS Quantity_Sold,
    ROUND(SUM(Revenue), 2) AS Revenue,
    ROUND(AVG(UnitPrice), 2) AS Average_Unit_Price
FROM customer_transactions
GROUP BY Description
HAVING SUM(Quantity) > 0
ORDER BY Revenue DESC
LIMIT 20;


-- ============================================================
-- 7. CUSTOMER RETENTION OPPORTUNITY
-- ============================================================

SELECT
    Segment,
    COUNT(*) AS Customers,
    ROUND(AVG(Recency), 2) AS Avg_Recency,
    ROUND(AVG(Frequency), 2) AS Avg_Frequency,
    ROUND(AVG(Monetary), 2) AS Avg_Revenue
FROM customer_rfm
GROUP BY Segment
ORDER BY Avg_Revenue DESC;