# Write your MySQL query statement below
SELECT 
    P.product_name, 
    SUM(O.unit) AS unit
FROM 
    Orders O
JOIN 
    Products P ON O.product_id = P.product_id
WHERE 
    O.order_date >= '2020-02-01' AND O.order_date < '2020-03-01'
GROUP BY 
    O.product_id, P.product_name
HAVING 
    SUM(O.unit) >= 100;
