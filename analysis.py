from pathlib import Path
import json
import pandas as pd
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parent
df=pd.read_csv(ROOT/"data/retail_sales_simulated.csv",parse_dates=["order_date"])
out=ROOT/"reports"; out.mkdir(exist_ok=True)
required=["order_id","order_date","region","category","product","units_sold","unit_price","discount_pct","sales","cost","profit"]
quality={"rows":int(len(df)),"duplicate_order_ids":int(df.order_id.duplicated().sum()),
         "missing_values":int(df[required].isna().sum().sum()),"negative_units":int((df.units_sold<0).sum())}
kpis={"dataset_type":"SIMULATED — not real company data","orders":int(df.order_id.nunique()),
      "units_sold":int(df.units_sold.sum()),"revenue":round(float(df.sales.sum()),2),
      "profit":round(float(df.profit.sum()),2),"profit_margin_pct":round(float(df.profit.sum()/df.sales.sum()*100),2),
      "average_order_value":round(float(df.sales.mean()),2),"data_quality":quality}
(out/"kpi_summary.json").write_text(json.dumps(kpis,indent=2),encoding="utf-8")
df["month"]=df.order_date.dt.to_period("M").astype(str)
monthly=df.groupby("month",as_index=False).agg(revenue=("sales","sum"),profit=("profit","sum"))
monthly.to_csv(out/"monthly_summary.csv",index=False)
category=df.groupby("category",as_index=False).agg(revenue=("sales","sum"),profit=("profit","sum"),units=("units_sold","sum")).sort_values("revenue",ascending=False)
category.to_csv(out/"category_summary.csv",index=False)
region=df.groupby("region",as_index=False).agg(revenue=("sales","sum"),profit=("profit","sum")).sort_values("revenue",ascending=False)
region.to_csv(out/"region_summary.csv",index=False)
plt.figure(figsize=(10,5)); plt.plot(monthly.month,monthly.revenue,marker="o",label="Revenue"); plt.plot(monthly.month,monthly.profit,marker="o",label="Profit")
plt.xticks(rotation=45,ha="right"); plt.title("Monthly Revenue and Profit (Simulated Data)"); plt.xlabel("Month"); plt.ylabel("Amount"); plt.legend(); plt.tight_layout()
plt.savefig(out/"monthly_revenue_profit.png",dpi=150); plt.close()
plt.figure(figsize=(9,5)); plt.bar(category.category,category.revenue); plt.xticks(rotation=20,ha="right")
plt.title("Revenue by Category (Simulated Data)"); plt.xlabel("Category"); plt.ylabel("Revenue"); plt.tight_layout()
plt.savefig(out/"category_revenue.png",dpi=150); plt.close()
print(json.dumps(kpis,indent=2))
