# E-Commerce Data Analytics | SQL, Python & Power BI

## Project Overview

This project analyzes the Brazilian Olist E-Commerce Public Dataset to understand order trends, product sales, payment methods, data quality, and delivery performance.

The goal is to transform raw e-commerce data into actionable business insights using SQL, Python, and Power BI.

## Tools & Technologies

- **MySQL 8.0** — data validation, joins, aggregations, and business analysis
- **Python** — data exploration, data quality checks, KPI calculations, and visualization
- **Pandas** — data manipulation and analysis
- **Matplotlib** — charts and visualizations
- **Power BI** — interactive dashboard development
- **Git & GitHub** — version control and project documentation

## Dataset

The project uses nine CSV files from the Olist Brazilian E-Commerce Public Dataset:

- Customers
- Orders
- Order items
- Payments
- Reviews
- Products
- Sellers
- Geolocation
- Product category name translation

The dataset contains approximately 100,000 orders from 2016–2018.

## Project Structure

```text
EcommerceDataAnalytics/
├── data/
│   ├── raw/
│   └── processed/
├── sql/
│   ├── 01_data_quality_checks.sql
│   └── 02_business_analysis.sql
├── python/
│   ├── 01_data_exploration.py
│   ├── 02_missing_values_analysis.py
│   ├── 03_product_quality_check.py
│   ├── 04_monthly_orders_analysis.py
│   ├── 05_top_product_categories.py
│   ├── 06_payment_analysis.py
│   └── 07_delivery_performance.py
├── powerbi/
└── reports/
```

## Data Quality Checks

Validated key relationships between:

- Orders and customers
- Order items and orders
- Order items and products
- Order items and sellers
- Payments and orders

The tested relationships returned zero unmatched records.

Additional checks identified:

- Missing product categories and product attributes
- Missing order delivery timestamps
- Missing review titles and comments
- Duplicate geolocation records
- Duplicate review IDs
- Payment records requiring further review

Data-quality exceptions are documented rather than silently deleted.

## Business Questions

1. How are orders distributed by status?
2. How does order volume change month by month?
3. Which months have the highest item sales value?
4. Which product categories generate the highest item sales value?
5. Which payment methods contribute the most recorded payment value?
6. How long does delivery take?
7. What percentage of eligible delivered orders arrive on or before the estimated delivery date?

## Key Findings

### Order Performance

- **Total orders:** 99,441
- **Delivered orders:** 96,478
- **Delivered share:** Approximately 97.02%
- **Peak order month:** November 2017, with 7,544 orders

### Product Sales

Top product categories by item sales value include:

- **Health & beauty:** R$1,258,681.34
- **Watches & gifts:** R$1,205,005.68
- **Bed, bath & table:** R$1,036,988.68

November 2017 was also the peak month for item sales value, at approximately R$1,010,271.37.

### Payment Analysis

- **Highest-value payment method:** Credit card
- **Recorded credit-card payment value:** R$12,542,084.19
- **Credit-card share of recorded payment value:** Approximately 78.34%

### Delivery Performance

- **Eligible delivered orders:** 96,470
- **Average delivery time:** Approximately 12.50 calendar days
- **On-time deliveries:** 88,644
- **Late deliveries:** 7,826
- **On-time delivery rate:** Approximately 91.89%

Delivery performance is calculated using orders with valid purchase, delivery, and estimated-delivery timestamps. On-time deliveries include orders delivered on or before the estimated delivery date.

## Important Data Considerations

- Order purchase dates range from September 2016 to October 2018.
- The final months contain relatively few records and should be interpreted cautiously.
- Some products have missing categories or categories without English translations.
- Payment records and orders are not always one-to-one.
- Item sales value uses order-item prices and excludes freight.
- Payment value is analyzed separately to avoid double-counting through one-to-many joins.
- Missing values and duplicate records are investigated before deciding whether any treatment is appropriate.

## Python Analysis Outputs

The Python scripts generate analysis files under `data/processed/` and charts under `reports/`.

Examples include:

- `python_data_quality_summary.csv`
- `missing_values_by_column.csv`
- `monthly_orders_summary.csv`
- `product_category_sales.csv`
- `top_10_product_categories.csv`
- `payment_method_summary.csv`
- `delivery_performance_summary.csv`
- `monthly_orders_trend.png`
- `top_10_product_categories.png`
- `payment_method_analysis.png`
- `delivery_performance.png`

## Project Status

- [x] Import raw CSV datasets into MySQL
- [x] Validate key table relationships
- [x] Create SQL business-analysis queries
- [x] Develop Python data-quality and analysis scripts
- [ ] Verify all final Python outputs
- [ ] Build an interactive Power BI dashboard
- [ ] Add dashboard screenshots
- [ ] Document final business recommendations
- [ ] Publish the project on GitHub

## Business Value

This project demonstrates practical skills in SQL querying, relational data validation, exploratory data analysis, KPI calculation, sales trend analysis, payment analysis, and delivery performance measurement.

The planned Power BI dashboard will help stakeholders explore sales performance, product categories, order activity, payment methods, and delivery outcomes.

## Author

**KBN Naveen Kumar**

Data Analytics | SQL | Python | Power BI | MySQL
