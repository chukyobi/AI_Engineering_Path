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
HAVING AVG(score) < 900
ORDER BY [average_score] DESC;