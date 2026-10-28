-- Olist E-Commerce Data Analytics
-- File: 02_business_analysis.sql
-- Purpose: Analyze orders, sales, products, payments, and delivery

USE ecommerce_analytics;

-- 1. Orders by status
SELECT
    order_status,
    COUNT(*) AS total_orders
FROM olist_orders_dataset
GROUP BY order_status
ORDER BY total_orders DESC;


-- 2. Monthly order trends
SELECT
    DATE_FORMAT(order_purchase_timestamp, '%Y-%m') AS order_month,
    COUNT(*) AS total_orders
FROM olist_orders_dataset
WHERE order_purchase_timestamp IS NOT NULL
GROUP BY DATE_FORMAT(order_purchase_timestamp, '%Y-%m')
ORDER BY order_month;


-- 3. Monthly item sales and freight value
SELECT
    DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m') AS order_month,
    COUNT(DISTINCT o.order_id) AS total_orders,
    COUNT(*) AS total_items_sold,
    ROUND(SUM(oi.price), 2) AS item_sales_value,
    ROUND(SUM(oi.freight_value), 2) AS freight_value
FROM olist_orders_dataset o
JOIN olist_order_items_dataset oi
    ON o.order_id = oi.order_id
WHERE o.order_purchase_timestamp IS NOT NULL
GROUP BY DATE_FORMAT(o.order_purchase_timestamp, '%Y-%m')
ORDER BY order_month;


-- 4. Top 10 product categories by item sales value
SELECT
    COALESCE(
        t.product_category_name_english,
        p.product_category_name,
        'unknown_category'
    ) AS product_category,
    COUNT(*) AS total_items_sold,
    COUNT(DISTINCT oi.order_id) AS total_orders,
    ROUND(SUM(oi.price), 2) AS item_sales_value
FROM olist_order_items_dataset oi
JOIN olist_products_dataset p
    ON oi.product_id = p.product_id
LEFT JOIN product_category_name_translation t
    ON p.product_category_name = t.product_category_name
GROUP BY
    COALESCE(
        t.product_category_name_english,
        p.product_category_name,
        'unknown_category'
    )
ORDER BY item_sales_value DESC
LIMIT 10;


-- 5. Payment method analysis
SELECT
    payment_type,
    COUNT(*) AS payment_records,
    COUNT(DISTINCT order_id) AS total_orders,
    ROUND(SUM(payment_value), 2) AS total_payment_value,
    ROUND(AVG(payment_value), 2) AS average_payment_value
FROM olist_order_payments_dataset
GROUP BY payment_type
ORDER BY total_payment_value DESC;


-- 6. Delivery performance
SELECT
    COUNT(*) AS delivered_orders,
    ROUND(
        AVG(DATEDIFF(
            order_delivered_customer_date,
            order_purchase_timestamp
        )),
        2
    ) AS avg_delivery_days,
    SUM(
        order_delivered_customer_date <= order_estimated_delivery_date
    ) AS on_time_orders,
    SUM(
        order_delivered_customer_date > order_estimated_delivery_date
    ) AS late_orders,
    ROUND(
        100.0 * SUM(
            order_delivered_customer_date <= order_estimated_delivery_date
        ) / COUNT(*),
        2
    ) AS on_time_delivery_percentage
FROM olist_orders_dataset
WHERE order_status = 'delivered'
  AND order_delivered_customer_date IS NOT NULL
  AND order_estimated_delivery_date IS NOT NULL
  AND order_purchase_timestamp IS NOT NULL;