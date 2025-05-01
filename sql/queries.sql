-- Query 1: Top 10 Customers by Total Billing

SELECT c.customer_id, c.name, SUM(b.amount) AS total_billed
FROM 
    OPENROWSET(
        BULK 'https://telecomdatalake123.dfs.core.windows.net/synapse-data/customers.csv',
        FORMAT = 'CSV',
        FIRSTROW = 2
    ) WITH (
        customer_id INT,
        name NVARCHAR(100),
        email NVARCHAR(100),
        phone NVARCHAR(50),
        signup_date DATE,
        plan_type NVARCHAR(50)
    ) AS c
JOIN 
    OPENROWSET(
        BULK 'https://telecomdatalake123.dfs.core.windows.net/synapse-data/billing.csv',
        FORMAT = 'CSV',
        FIRSTROW = 2
    ) WITH (
        bill_id INT,
        customer_id INT,
        bill_date DATE,
        amount FLOAT,
        payment_status NVARCHAR(50),
        due_date DATE
    ) AS b
ON c.customer_id = b.customer_id
GROUP BY c.customer_id, c.name
ORDER BY total_billed DESC
OFFSET 0 ROWS FETCH NEXT 10 ROWS ONLY

-- Query 2: Average Data Usage by Plan Type
SELECT c.plan_type, AVG(u.data_used_gb) AS avg_data_usage
FROM 
    OPENROWSET(
        BULK 'https://telecomdatalake123.dfs.core.windows.net/synapse-data/customers.csv',
        FORMAT = 'CSV',
        FIRSTROW = 2
    ) WITH (
        customer_id INT,
        name NVARCHAR(100),
        email NVARCHAR(100),
        phone NVARCHAR(50),
        signup_date DATE,
        plan_type NVARCHAR(50)
    ) AS c
JOIN 
    OPENROWSET(
        BULK 'https://telecomdatalake123.dfs.core.windows.net/synapse-data/usage.csv',
        FORMAT = 'CSV',
        FIRSTROW = 2
    ) WITH (
        usage_id INT,
        customer_id INT,
        call_minutes FLOAT,
        data_used_gb FLOAT,
        sms_count INT,
        usage_date DATE
    ) AS u
ON c.customer_id = u.customer_id
GROUP BY c.plan_type
