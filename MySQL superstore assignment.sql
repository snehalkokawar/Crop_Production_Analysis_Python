create database Superstores;
use Superstores;
#task1
#describe the data in hand in your own words
DESCRIBE mobile_sales;
SHOW COLUMNS FROM mobile_sales;
SHOW TABLES;
SELECT COUNT(*) FROM mobile_sales;

DESCRIBE pincodes_mapping;
SHOW COLUMNS FROM pincodes_mapping;
SHOW TABLES;
SELECT COUNT(*) FROM pincodes_mapping;

#Task 2 basic and Advance analysis
#1. Find the total and the average sale price (Revenue/Units) for each brand
SELECT 
    Brand,
    SUM(revenue) AS total_sale_price,
    AVG(revenue/units) AS average_sale_price
FROM
    mobile_sales
GROUP By Brand;

#2.find the total revenue and units sold for each product
select sum(Revenue) as total_revenue, sum(Units) as total_units,Product from mobile_sales
group by Product;

#3.find the state wise revenue and its overall share (revenue of that state/totalrevenue) including all mobile brands
SELECT
    S.state,
    SUM(M.revenue) AS state_revenue,
    SUM(M.revenue) / T.total_revenue AS revenue_share
FROM
    pincode_mapping.m
JOIN
    States S ON M.state = S.state
JOIN
    (SELECT
        SUM(revenue) AS total_revenue
    FROM
        mobile_sales)
GROUP BY
    S.state;
    
#In this query, the SELECT statement retrieves the state name, the sum of revenue as the state revenue, and the revenue share (state revenue divided by the total revenue across all states). The FROM clause includes the Sales table aliased as M and joins it with the States table aliased as S based on the common state_id. The JOIN clause also includes a subquery (aliased as T) that calculates the total revenue across all states. Finally, the GROUP BY clause groups the results by the state column.

#By executing this query, you will obtain the state-wise revenue and its overall share for all mobile brands. Ensure to adjust the column and table names according to your specific dataset structure.

#4.find the top product with most sales in metro region
SELECT
    SUM(s.Units) AS total_units_sold
FROM
    mobile_sales p
JOIN
    pincodes_mapping s ON p.Pincode = s.Pincode
JOIN
    city_tier r ON s.city_tier = r.city_tier
WHERE
    r.city_tier = 'Metro'
GROUP BY
    p.Product
ORDER BY
    units DESC
LIMIT 1;


#5.find the state where vicky smart phone are selling more than KSP
SELECT
    s.state
FROM
    pincodes_mapping s
JOIN
    mobile_sales p ON s.Pincode = p.Pincode
WHERE
    p.Product = 'Vicky' AND Brand = 'Vicky' AND Units > (
        SELECT
            SUM(s2.Units)
        FROM
            mobile_sales s2
        JOIN
            pincodes_mapping p2 ON s2.Pincode = p2.Pincode
        WHERE
            Product = 'KSP' AND Brand = 'KSP'
    );

#6. disply the top contributing cities in north region in descending order units sold for vicky smart phone
SELECT
    c.city_name,
    SUM(s.units_sold) AS total_units_sold
FROM
    Sales s
JOIN
    Cities c ON s.city_id = c.city_id
JOIN
    Regions r ON c.region_id = r.region_id
WHERE
    r.region_name = 'North' AND s.brand = 'Vicky'
GROUP BY
    c.city_name
ORDER BY
    total_units_sold DESC;

#7.What is the pincode coverage of the offline retailer in each state?
#Hint: Pincode coverage of the state equals Distinct No of pincodes from
#where sales are coming divided by total pincodes in that state




/*8.Write a query to get the average selling price (Revenue/Units) across city tier
individually for both the brands. After getting the output, check if Metro's average
selling price for each brand is higher than Tier 3 and other? This will verify
whether metro customer buys a high end mobile phone compared to a tier 1 or
tier 3 customer
Output example ( 2 tables; one for each brand ) */



/*9.Write a query to find sales details of all pincodes ordered by revenue in
descending order*/



/*Using SQL date functions categorize August month into 4 week periods ( 1-7:
week 1, 8-14: week 2 and so forth). After doing this check if after 15th August,
the sales increased due to good discounts on Independence day sale*/

