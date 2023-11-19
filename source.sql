SELECT customer_id, first_name, last_name, email, registration_date
FROM customers;


-- Total number of transactions per customer
SELECT customer_id, COUNT(*) AS total_transactions
FROM transactions
GROUP BY customer_id;

-- Total amount spent by each customer
SELECT customer_id, SUM(amount) AS total_spent
FROM transactions
GROUP BY customer_id;

-- Monthly new customer acquisition
SELECT EXTRACT(MONTH FROM registration_date) AS month, COUNT(*) AS new_customers
FROM customers
GROUP BY month;

-- Monthly total sales
SELECT EXTRACT(MONTH FROM order_date) AS month, SUM(amount) AS total_sales
FROM transactions
GROUP BY month;

-- Monthly cohort analysis
SELECT EXTRACT(MONTH FROM registration_date) AS cohort_month,
       EXTRACT(MONTH FROM order_date) AS purchase_month,
       COUNT(DISTINCT customer_id) AS customers
FROM customers
JOIN transactions ON customers.customer_id = transactions.customer_id
GROUP BY cohort_month, purchase_month;

-- RFM (Recency, Frequency, Monetary) analysis
SELECT customer_id,
       MAX(order_date) AS last_purchase_date,
       COUNT(DISTINCT order_id) AS total_orders,
       SUM(amount) AS total_spent
FROM transactions
GROUP BY customer_id;

-- Products frequently bought together
SELECT product_id_1, product_id_2, COUNT(*) AS frequency
FROM (
    SELECT t1.product_id AS product_id_1, t2.product_id AS product_id_2
    FROM transactions t1
    JOIN transactions t2 ON t1.order_id = t2.order_id AND t1.product_id < t2.product_id
) AS product_pairs
GROUP BY product_id_1, product_id_2
ORDER BY frequency DESC;

-- Monthly customer retention
SELECT EXTRACT(MONTH FROM registration_date) AS cohort_month,
       EXTRACT(MONTH FROM last_purchase_date) AS last_purchase_month,
       COUNT(DISTINCT customer_id) AS retained_customers
FROM (
    SELECT customer_id, MIN(order_date) AS registration_date, MAX(order_date) AS last_purchase_date
    FROM transactions
    GROUP BY customer_id
) AS customer_lifecycle
GROUP BY cohort_month, last_purchase_month;
