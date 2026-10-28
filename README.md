# 🛒 E-Commerce Data Analytics | SQL, Python & Power BI

## 📌 Project Overview

An end-to-end e-commerce data analytics project using the Brazilian E-Commerce Public Dataset by Olist. This project analyzes sales performance, customer reviews, payment methods, product categories, order statuses, and delivery performance using **MySQL, Python, and Power BI**.

**Author:** KBN Naveen Kumar

## 🎯 Business Objectives

- Analyze monthly order and sales trends.
- Identify top-performing product categories.
- Understand customer payment preferences.
- Evaluate customer review scores and satisfaction.
- Analyze order statuses and delivery performance.
- Identify data-quality issues and recommend business improvements.

## 🛠️ Tools and Technologies

- **Database:** MySQL 8.0
- **Programming:** Python
- **Python Libraries:** Pandas, Matplotlib
- **Visualization:** Microsoft Power BI
- **Version Control:** Git and GitHub

## 📊 Dashboard Preview

### 1. Sales Overview

![Sales Overview Dashboard](reports/customer_delivery_insights.png)

### 2. Customer & Delivery Insights

![Customer and Delivery Insights Dashboard](reports/sales_overview.png)

## 📂 Project Structure

```text
EcommerceDataAnalytics/
│
├── sql/
│   ├── 01_data_quality_checks.sql
│   └── 02_business_analysis.sql
│
├── python/
│   ├── 01_data_exploration.py
│   ├── 02_missing_values_analysis.py
│   ├── 03_product_quality_check.py
│   ├── 04_monthly_orders_analysis.py
│   ├── 05_top_product_categories.py
│   ├── 06_payment_analysis.py
│   └── 07_delivery_performance.py
│
├── reports/
│   ├── sales_overview.png
│   ├── customer_delivery_insights.png
│   ├── monthly_orders_trend.png
│   └── delivery_performance.png
│
├── powerbi/
├── data/
│   ├── raw/
│   └── processed/
│
├── .gitignore
└── README.md
```

## 🗄️ Dataset

This project uses the Brazilian E-Commerce Public Dataset by Olist.

The dataset contains information about orders, customers, order items, payments, products, sellers, reviews, geolocation, and product category translations.

**Note:** The original CSV files are not included in this repository. Obtain the dataset from its official source and place the files in the `data/raw/` folder before running the analysis.

## 🔍 Data Quality Checks

The project includes SQL and Python checks for:

- Missing values in product and order data.
- Duplicate geolocation records.
- Duplicate review identifiers.
- Missing order timestamps.
- Invalid or unexpected payment values.
- Negative product prices or freight charges.
- Relationships between orders, customers, products, and sellers.

Data-quality findings are documented without automatically deleting source records that may require further investigation.

## 📈 Business Questions Answered

1. How does order volume change month by month?
2. Which product categories generate the highest sales?
3. Which payment methods are most commonly used?
4. What proportion of orders are successfully delivered?
5. How are customer review scores distributed?
6. Which order statuses account for non-delivered orders?
7. What data-quality issues should be considered before making business decisions?

## 💡 Key Findings

### Sales Performance

- The dataset contains **99,441 orders**.
- November 2017 was the peak month, with **7,544 orders**.
- Total item sales were approximately **R$13.59 million**, excluding freight.
- Health and beauty was the highest-selling category by item sales, at approximately **R$1.26 million**.

### Payment Analysis

- Credit cards accounted for approximately **78.34%** of recorded payment value.
- Boleto accounted for approximately **17.92%** of recorded payment value.
- Credit cards were the dominant payment method in the dataset.

### Order and Delivery Performance

- Approximately **97.02%** of orders had a delivered status.
- Among eligible delivered orders, the average calendar delivery time was approximately **12.5 days**.
- Approximately **91.89%** of eligible delivered orders arrived on or before the estimated delivery date.

### Customer Reviews

- The average review score was approximately **4.1 out of 5**.
- Review titles and comments frequently contain missing values, which should be considered when interpreting customer feedback.

*These findings describe the available dataset and do not necessarily represent current e-commerce performance.*

## 🐍 Python Analysis

Python scripts are organized to perform:

- Initial data exploration.
- Missing-value analysis.
- Product data-quality checks.
- Monthly order trend analysis.
- Top product category analysis.
- Payment method analysis.
- Delivery performance analysis.

Generated CSV summaries and charts are stored in the relevant `data/processed/` and `reports/` folders when produced by the scripts.

## 📌 Important Data Considerations

- Item sales are calculated from product prices and exclude freight charges.
- Source records may contain missing values and duplicate identifiers.
- Delivery performance calculations use eligible delivered orders.
- Dataset dates and results reflect the original dataset period, not current market conditions.
- Findings should be interpreted in the context of the dataset's limitations.

## ✅ Project Status

- [x] Import raw CSV datasets into MySQL
- [x] Validate key table relationships
- [x] Create SQL business-analysis queries
- [x] Develop Python data-quality and analysis scripts
- [x] Build interactive Power BI dashboards
- [x] Add dashboard screenshots to GitHub
- [x] Publish project source files on GitHub
- [ ] Verify all final Python outputs
- [ ] Document final business recommendations
- [ ] Publish the Power BI `.pbix` file or a suitable sharing link

## 🚀 Business Value

This project demonstrates practical skills in SQL querying, data cleaning, exploratory data analysis, business intelligence, dashboard development, and communicating data-driven insights.

It provides a foundation for using e-commerce data to monitor sales performance, understand customer behavior, and identify operational improvement opportunities.

## 👨‍💻 Author

**KBN Naveen Kumar**

- **GitHub:** [kbn-naveen-kumar](https://github.com/kbn-naveen-kumar)
- **Project Repository:** [E-Commerce Data Analytics](https://github.com/kbn-naveen-kumar/ecommerce-data-analytics)

