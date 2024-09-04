-- 1. Find the average balance of customers grouped by their job
SELECT job, AVG(balance) AS average_balance
FROM bank
GROUP BY job;

-- 2. Count the number of customers for each marital status
SELECT marital, COUNT(*) AS total_customers
FROM bank
GROUP BY marital;

-- 3. Find customers who have a balance above a certain threshold
SELECT *
FROM bank
WHERE balance > 10000;

-- 4. Find the total balance for each education level
SELECT education, SUM(balance) AS total_balance
FROM bank
GROUP BY education;


-- 5. Filter customers who subscribed to the product in the previous campaign
SELECT *
FROM bank
WHERE subscribed = 'yes';

-- 6. Get the number of customers by age group
SELECT 
    CASE 
        WHEN age < 25 THEN 'Under 25'
        WHEN age BETWEEN 25 AND 40 THEN '25-40'
        WHEN age BETWEEN 41 AND 60 THEN '41-60'
        ELSE 'Above 60'
    END AS age_group, 
    COUNT(*) AS total_customers
FROM bank
GROUP BY age_group;

-- 7. Get the maximum, minimum, and average balance across all customers
SELECT MAX(balance) AS max_balance, MIN(balance) AS min_balance, AVG(balance) AS avg_balance
FROM bank;













