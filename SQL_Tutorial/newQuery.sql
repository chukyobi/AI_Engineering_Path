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
        [country],
        SUM(score) [total_score]
FROM [dbo].[customers]
GROUP BY [country]
ORDER BY [country] ASC,  SUM(score) DESC;