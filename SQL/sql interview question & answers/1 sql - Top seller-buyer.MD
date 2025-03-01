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
    WHERE seller_id % 2 = 1 -- Ensures only the first transaction_id (seller) is selected
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
