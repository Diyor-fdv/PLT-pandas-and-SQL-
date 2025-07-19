# 🛒 E-Commerce Sales Analysis Dashboard

**Author:** Diyorbek Abdusattorov  
**Tools Used:** Power BI, Python (pandas, matplotlib), SQL (PostgreSQL)  
**Dataset:** `ecommerce_sales_sample.csv`

---

## 📊 Project Overview

This project presents a full-stack analysis pipeline for e-commerce sales data using:
- 🔍 SQL for querying structured data
- 🐍 Python for data exploration and visualization
- 📈 Power BI for building interactive dashboards

The goal is to extract business insights such as:
- Top-selling products and countries
- Monthly revenue trends
- Category-wise price and profit metrics

---

## 🧰 Files Included

| File | Description |
|------|-------------|
| `ecommerce_sales_sample.csv` | Raw dataset of e-commerce transactions |
| `mainpy.py` | Python script for EDA and visualizations using pandas + matplotlib |
| `sqlproject.sql` | SQL queries: filtering, aggregation, sorting, and updates |
| `SalesDashboard.pbix` *(not uploaded yet)* | Power BI dashboard for final visualization (upload if exists) |

---

## 🔢 Key Analyses

### 🐍 Python Insights (`mainpy.py`)
- Checked for NaN values
- Calculated total revenue
- Top 5 countries by order volume
- Most sold products
- Average price by category
- Monthly revenue trends
- Revenue distribution by country (pie chart)

### 🧮 SQL Insights (`sqlproject.sql`)
- Created `orders` table and inserted sample data
- Selected top expensive products
- Aggregated quantity by country
- Average price by category
- Top ordered products
- Updated and deleted rows for data manipulation

### 📊 Power BI (planned/future)
- Dynamic slicers by Region
- Drill-down from Category → Sub-Category
- Tooltip insights for Profit and Revenue
- Monthly sales trend charts
- Region-wise performance filtering

---

## 🧠 What I Learned

- How to analyze and clean data using `pandas`
- Visualizing real-world data with `matplotlib`
- Writing SQL queries for business logic
- Combining Python/SQL results inside Power BI dashboard
- Structuring a data analytics project for GitHub portfolio

---

## 📦 How to Run

1. Clone this repo
2. Open `mainpy.py` and run in any Python IDE (requires `pandas` and `matplotlib`)
3. Execute `sqlproject.sql` in PostgreSQL or another SQL environment
4. Open `SalesDashboard.pbix` in Power BI Desktop (if available)

---

## 🔗 Author

👨‍💻 [Diyorbek Abdusattorov](https://github.com/Diyor-fdv)  
📧 Email: abdusattorovdiyor01@email.com

---

> ⭐ Star the repo if you liked it or fork it to contribute!
