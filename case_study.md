# Retail Sales Performance Analysis

## Objective
Demonstrate a repeatable analytics workflow for sales, profit, volume, categories, regions, and discount patterns.

## Data transparency
The included dataset is synthetic and generated for practice. It does not represent real company transactions or verified commercial outcomes.

## Questions explored
1. How do revenue and profit vary by month?
2. Which categories and regions contribute most to sales?
3. Which products rank highest by revenue?
4. How do discount bands relate to average order sales and profit?
5. What data-quality checks should be performed before reporting?

## Workflow
- Validate required fields, missing values, duplicate order IDs, and units.
- Use Python/Pandas to aggregate KPIs and summaries.
- Use SQLite-compatible SQL queries for business questions.
- Build a Power BI dashboard with KPIs, trends, category/region breakdowns, and filters.

## Reporting guidance
Run `analysis.py` to create checked summaries and charts. Use the resulting outputs to write exact observations. Do not present simulated results as real business findings or make causal claims from simple comparisons.

## Next steps
Add screenshots of your completed dashboard, explain the key observations and limitations, and include a short project walkthrough.
## Dashboard overview

The Power BI dashboard, titled **Sales Performance Analytics**, provides an interactive overview of retail sales performance.

The dashboard includes:
- **Total Sales:** Displays overall revenue.
- **Total Profit:** Displays the overall profit generated.
- **Units Sold:** Shows the total quantity of products sold.
- **Monthly Sales Trend:** Tracks sales performance over time.
- **Category Analysis:** Compares sales across product categories.
- **Regional Analysis:** Compares sales across geographical regions.
- **Region Slicer:** Allows users to filter the dashboard interactively.

## Tools and Technologies

| Tool | Purpose |
|---|---|
| Python | Data analysis and processing |
| Pandas | Data manipulation and aggregation |
| SQL | Business queries and data analysis |
| Power BI | Interactive dashboard development |
| GitHub | Project version control and documentation |

## Project Limitations

- The dataset is synthetic and does not represent actual company transactions.
- The analysis is limited to the fields and records available in the dataset.
- The dashboard presents historical data rather than live business transactions.
- Findings should be interpreted as practice-based analytical observations.

## Conclusion

This project demonstrates an end-to-end retail sales analytics workflow using Python, SQL, and Power BI. It combines data preparation, analytical queries, KPI calculations, and interactive visualization to demonstrate how data can be transformed into meaningful business information.

The project also demonstrates practical skills in data analysis, business intelligence, visualization, and analytical reporting.
