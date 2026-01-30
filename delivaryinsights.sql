-- Query to show the 'Cost of Being Late'

SELECT

Status,

AVG(Customer_Rating) AS Avg_Rating,

COUNT(*) AS Total_Orders

FROM delivery_data

GROUP BY Status;


SELECT
Region,

AVG(Delivery_Time_Days) AS Avg_Delivery_Days,

COUNT(OrderID) AS Total_Orders

FROM delivery_data

GROUP BY Region

ORDER BY Avg_Delivery_Days DESC;

SELECT

Status,

AVG(Customer_Rating) AS Average_Rating, MIN(Customer_Rating) AS Lowest_Rating, MAX(Customer_Rating) AS Highest_Rating FROM delivery_data

GROUP BY Status;