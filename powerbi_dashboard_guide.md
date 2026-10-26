# Power BI Dashboard Guide

Import `data/retail_sales_simulated.csv` via **Get data → Text/CSV**.

## Suggested layout
- KPI cards: Total Revenue, Total Profit, Profit Margin %, Units Sold, Order Count
- Line chart: Revenue and Profit by Month
- Bar charts: Revenue by Category and Region
- Product table: Product, Revenue, Profit, Units Sold
- Slicers: Order Date, Region, Category

## Example DAX measures
```DAX
Total Revenue = SUM(retail_sales[sales])
Total Profit = SUM(retail_sales[profit])
Units Sold = SUM(retail_sales[units_sold])
Order Count = DISTINCTCOUNT(retail_sales[order_id])
Profit Margin % = DIVIDE([Total Profit], [Total Revenue], 0)
Average Order Value = DIVIDE([Total Revenue], [Order Count], 0)
```
The dataset has no real-world currency specified. Use generic amount labels unless you intentionally choose a currency for display. Label the dashboard as simulated practice data.
