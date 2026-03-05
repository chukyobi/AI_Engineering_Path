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

CREATE TABLE persons(
        id INT NOT NULL,
        person_name VARCHAR(50) NOT NULL,
        birth_date DATE NOT NULL,
)
