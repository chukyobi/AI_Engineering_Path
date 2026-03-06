USE MyDatabase;

SELECT * FROM [dbo].[customers];

SELECT * FROM 
[dbo].[orders];

SELECT 
       [country],
       [score]
FROM   [dbo].[customers];

SELECT 
        [first_name],
        [score],
        [country]
FROM [dbo].[customers]
WHERE [country] = 'Germany' AND [score] > 400;

SELECT *
FROM [dbo].[customers]
ORDER BY [country] ASC, [score] DESC;

SELECT 
        [country] AS [customer_country],
        SUM(score) AS [total_score],
        COUNT(id) AS [number_of_customers]
FROM    [dbo].[customers]
WHERE   [score] > 500
GROUP BY [country]
HAVING   SUM(score) > 600
ORDER BY [country] DESC;  --SUM(score) DESC;


SELECT 
        [country] AS [customer_country],
        AVG(score) AS [average_score],
        COUNT(id) AS [number_of_customers]
FROM [dbo].[customers]
WHERE [score] != 0
GROUP BY [country]
HAVING AVG(score) > 430
ORDER BY [average_score] DESC;

SELECT DISTINCT
        [country]
FROM [dbo].[customers]
ORDER BY [country] ASC;

SELECT TOP (3) 
[first_name] AS [customer_name],
MAX(score) AS [Highest_score]
FROM [dbo].[customers]
GROUP BY [first_name]
HAVING MAX(score) > 500
ORDER BY [Highest_score] DESC;

SELECT * 
FROM [dbo].[orders]

SELECT
        [id],
        [first_name],
        'new customer' AS [customer_status]
FROM [dbo].[customers]



CREATE TABLE humans(
        id INT NOT NULL,
        person_name VARCHAR(50) NOT NULL,
        birth_date DATE,
        phone_number VARCHAR(20) NOT NULL,
        CONSTRAINT pk_humans PRIMARY KEY (id)
)

-- INSERT INTO [dbo].[persons] (id, person_name, birth_date, email)
-- VALUES (1, 'John Doe', '1990-01-01', 'john.doe@example.com');
-- ALTER TABLE persons
-- ADD email VARCHAR(50) NOT NULL;

SELECT * FROM customers;
SELECT * FROM humans;


-- ALTER TABLE persons
-- DROP COLUMN phone_number;


-- DROP TABLE persons;


INSERT INTO [dbo].[customers] (id, first_name, country, score)
VALUES (7, 'Jay Clinton', 'USA', 450);


INSERT INTO dbo.humans (id, person_name, birth_date, phone_number)
SELECT 
[id],
[first_name],
NULL,
'no phone number'
FROM dbo.customers;


UPDATE dbo.humans
SET birth_date = '1990-01-01',
phone_number = '123-456-7890'
WHERE id = 7;

UPDATE dbo.humans
SET birth_date = '1990-01-01';


SELECT * 
FROM customers
WHERE first_name LIKE '___T%';


SELECT 
     dbo.customers.id,
     dbo.customers.first_name,
     dbo.orders.order_date,
     dbo.orders.sales
FROM dbo.customers
INNER JOIN dbo.orders
ON dbo.customers.id = dbo.orders.customer_id