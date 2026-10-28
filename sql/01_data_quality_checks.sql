-- Olist E-Commerce Data Analytics
-- File: 01_data_quality_checks.sql
-- Purpose: Validate source tables and key relationships

USE ecommerce_analytics;

-- 1. Check total records in core tables
SELECT 'customers' AS table_name, COUNT(*) AS total_rows
FROM olist_customers_dataset
UNION ALL
SELECT 'orders', COUNT(*) FROM olist_orders_dataset
UNION ALL
SELECT 'order_items', COUNT(*) FROM olist_order_items_dataset
UNION ALL
SELECT 'payments', COUNT(*) FROM olist_order_payments_dataset
UNION ALL
SELECT 'reviews', COUNT(*) FROM olist_order_reviews_dataset
UNION ALL
SELECT 'products', COUNT(*) FROM olist_products_dataset
UNION ALL
SELECT 'sellers', COUNT(*) FROM olist_sellers_dataset;

-- 2. Check for order items without a matching order
SELECT COUNT(*) AS order_items_without_matching_order
FROM olist_order_items_dataset oi
LEFT JOIN olist_orders_dataset o
    ON oi.order_id = o.order_id
WHERE o.order_id IS NULL;

-- 3. Check for payments without a matching order
SELECT COUNT(*) AS payments_without_matching_order
FROM olist_order_payments_dataset p
LEFT JOIN olist_orders_dataset o
    ON p.order_id = o.order_id
WHERE o.order_id IS NULL;

-- 4. Check for orders without a matching customer
SELECT COUNT(*) AS orders_without_matching_customer
FROM olist_orders_dataset o
LEFT JOIN olist_customers_dataset c
    ON o.customer_id = c.customer_id
WHERE c.customer_id IS NULL;

-- 5. Check for order items without matching products
SELECT COUNT(*) AS items_without_matching_product
FROM olist_order_items_dataset oi
LEFT JOIN olist_products_dataset p
    ON oi.product_id = p.product_id
WHERE p.product_id IS NULL;

-- 6. Check for order items without matching sellers
SELECT COUNT(*) AS items_without_matching_seller
FROM olist_order_items_dataset oi
LEFT JOIN olist_sellers_dataset s
    ON oi.seller_id = s.seller_id
WHERE s.seller_id IS NULL;