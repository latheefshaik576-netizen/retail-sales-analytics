-- All results use simulated practice data, not real company transactions.
-- Assumes CSV is loaded into a SQLite table named retail_sales.
SELECT ROUND(SUM(sales),2) AS revenue, ROUND(SUM(profit),2) AS profit,
       SUM(units_sold) AS units, COUNT(*) AS orders,
       ROUND(100.0*SUM(profit)/NULLIF(SUM(sales),0),2) AS margin_pct
FROM retail_sales;

SELECT month, ROUND(SUM(sales),2) AS revenue, ROUND(SUM(profit),2) AS profit
FROM retail_sales GROUP BY month ORDER BY month;

SELECT category, ROUND(SUM(sales),2) AS revenue, ROUND(SUM(profit),2) AS profit,
       SUM(units_sold) AS units
FROM retail_sales GROUP BY category ORDER BY revenue DESC;

SELECT region, ROUND(SUM(sales),2) AS revenue, ROUND(SUM(profit),2) AS profit
FROM retail_sales GROUP BY region ORDER BY revenue DESC;

SELECT product, ROUND(SUM(sales),2) AS revenue, ROUND(SUM(profit),2) AS profit,
       SUM(units_sold) AS units
FROM retail_sales GROUP BY product ORDER BY revenue DESC LIMIT 10;

SELECT CASE WHEN discount_pct=0 THEN '0%'
            WHEN discount_pct<=0.05 THEN '1-5%'
            WHEN discount_pct<=0.10 THEN '6-10%'
            WHEN discount_pct<=0.15 THEN '11-15%' ELSE '16-20%' END AS discount_band,
       ROUND(AVG(sales),2) AS avg_sales, ROUND(AVG(profit),2) AS avg_profit, COUNT(*) AS orders
FROM retail_sales GROUP BY discount_band ORDER BY MIN(discount_pct);
