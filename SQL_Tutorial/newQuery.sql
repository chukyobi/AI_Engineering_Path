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
   -- WHERE [country] = 'Germany'
    ORDER BY [country], [score] DESC;