# 🚀 Cracking the Google SQL Interview: Top 5 Seller-Buyer Transactions in MySQL

In this blog post, we tackle an **SQL interview question** reportedly asked at **Google**. The challenge involves analyzing **transaction data** and identifying the **top 5 seller-buyer combinations** with the highest transaction count, while following certain business rules. Additionally, we implement an extension where we disqualify customers who act as both sellers and buyers.

---

## 📌 **Problem Statement**

We have a `transactions` table with the following characteristics:

- Every **successful transaction** generates **two row entries** in the table.
- The first entry represents the **seller**, and the second represents the **buyer**.
- The **amount** and **transaction_time** remain identical for both rows of a single transaction.

### **🎯 Goal:**
- Identify the **top 5 seller-buyer pairs** with the **highest transaction count**.
- **Extension:** Disqualify customers who act as both sellers and buyers.

---

## 📌 **Table Schema**
```sql
CREATE TABLE transactions (
    transaction_id BIGINT,
    customer_id BIGINT,
    amount DECIMAL(10, 2),
    transaction_time DATETIME
);
```

## 📌 **Sample data - Insert Query**
```sql
INSERT INTO transactions VALUES
(1, 101, 100.00, '2024-01-01 10:00:00'), -- Seller
(2, 102, 100.00, '2024-01-01 10:00:00'), -- Buyer
(3, 103, 200.00, '2024-01-02 11:00:00'), -- Seller
(4, 104, 200.00, '2024-01-02 11:00:00'), -- Buyer
(5, 101, 300.00, '2024-01-03 12:00:00'), -- Seller
(6, 104, 300.00, '2024-01-03 12:00:00'), -- Buyer
(7, 105, 400.00, '2024-01-04 13:00:00'), -- Seller
(8, 106, 400.00, '2024-01-04 13:00:00'), -- Buyer
(9, 107, 500.00, '2024-01-05 14:00:00'), -- Seller
(10, 108, 500.00, '2024-01-05 14:00:00'), -- Buyer
(11, 101, 600.00, '2024-01-06 15:00:00'), -- Seller
(12, 106, 600.00, '2024-01-06 15:00:00'), -- Buyer
(13, 109, 700.00, '2024-01-07 16:00:00'), -- Seller
(14, 110, 700.00, '2024-01-07 16:00:00'), -- Buyer
(15, 101, 800.00, '2024-01-08 17:00:00'), -- Seller
(16, 106, 800.00, '2024-01-08 17:00:00'), -- Buyer
(21, 107, 10.00, '2024-01-01 10:00:00'), -- Seller
(22, 108, 10.00, '2024-01-01 10:00:00'), -- Buyer
(23, 107, 20.00, '2024-01-02 11:00:00'), -- Seller
(24, 108, 20.00, '2024-01-02 11:00:00'), -- Buyer

-- Transactions where the same person is both seller & buyer (Disqualified)
(17, 102, 900.00, '2024-01-09 18:00:00'), 
(18, 101, 900.00, '2024-01-09 18:00:00'),
(19, 106, 1000.00, '2024-01-10 19:00:00'), 
(20, 101, 1000.00, '2024-01-10 19:00:00');

```

## 📌 **Solution - Finding the Top 5 Seller-Buyer Pairs**

We use window functions (LEAD()) to pair sellers with buyers and aggregate the transaction count.

```sql
WITH base AS (
    SELECT 
        transaction_id, 
        customer_id AS seller_id, 
        amount, 
        transaction_time,
        LEAD(customer_id, 1) OVER(ORDER BY transaction_id) AS buyer_id
    FROM transactions
),

agg_base AS (
    SELECT seller_id, buyer_id, COUNT(*) AS no_of_transactions
    FROM base
    WHERE transaction_id % 2 = 1 -- Ensures only the first transaction_id (seller) is selected
    GROUP BY seller_id, buyer_id
)

SELECT * FROM agg_base
ORDER BY no_of_transactions DESC
LIMIT 5;
```

## **📌 Solution - Disqualifying Mutual Sellers/Buyers**

To remove cases where the same user acts as both seller and buyer, we use INTERSECT:

```sql
WITH base AS (
    SELECT 
        transaction_id, 
        customer_id AS seller_id, 
        amount, 
        transaction_time,
        LEAD(customer_id, 1) OVER(ORDER BY transaction_id) AS buyer_id
    FROM transactions
),

agg_base AS (
    SELECT seller_id, buyer_id, COUNT(*) AS no_of_transactions
    FROM base
    WHERE seller_id % 2 = 1 
    GROUP BY seller_id, buyer_id
),

final1 AS (
    SELECT seller_id AS user_id FROM agg_base
    INTERSECT
    SELECT buyer_id AS user_id FROM agg_base
)

SELECT * FROM agg_base 
WHERE seller_id NOT IN (SELECT user_id FROM final1)
AND buyer_id NOT IN (SELECT user_id FROM final1)
ORDER BY no_of_transactions DESC
LIMIT 5;
```

## **📌 Performance Optimization**
    1) Using LEAD() instead of self-joins for efficient seller-buyer pairing.
    2) INTERSECT for disqualification instead of nested subqueries.
