create Database classicmodels;
use classicmodels;

#1. display only their fullname and no.
select customerName, phone from customers;

#2.find the product names for each of the order in orderdetails table
SELECT orderNumber, productName
FROM orderdetails o
JOIN products p ON orderNumber = productName;

#3.find out the total amt spent by each customerid
select customerNumber, sum(amount) as total_amt_spent 
from payments
group by customerNumber;

#4.find out no. of customer from each country
select* from customers;
select country , count(*) as customer_count
from customers
group by country;

#5.find out the amt of sale driven by each sales representative
select salesRepEmployeeNumber, sum(creditLimit) as total_sales_amount
from customers
group by salesRepEmployeeNumber;

#6.find out the total no. of quantity ordered per each order
select* from orderdetails;
select orderNumber, sum(quantityOrdered) as total_quantity_ordered
from orderdetails
group by  orderNumber;

#7.find out the total no. of quantity ordered per each product ID
select productCode, sum(quantityOrdered ) as "total"
from orderdetails
group by  productCode;

#8.find out the total no. orders made where the order value is over 7000 INR
select count(*) as total_orders_over_7000 from payments
where amount >( 7000);

#9.list the customer names for those who their names are starting with A 
select customerName from customers
where customerName like 'A%';

#10.find the diffrence between the order date and the shipped date
select orderDate , shippedDate ,DATEDIFF(orderDate,shippedDate) as date_diff 
from orders;

#11.find out the profit for each product on the basic on buy price and sell price and find the overall profit for all the inventory in stock
select productCode,
(MSRP - buyPrice) AS profit_per_product,
(MSRP - buyPrice)*quantityInStock AS total_profit from products;

#12.find the profit for each product line and also see the inventory in stock
SELECT
  p.productLine,
  SUM((p.MSRP - p.buyPrice) * quantityInStock) AS total_profit,
  SUM(quantityInStock) AS total_inventory_in_stock
FROM products p
JOIN orderdetails i ON p.productCode = i.productCode
GROUP BY p.productLine;

#13. create a view that maps the customers and their payments, ignore fields that has greater than 30% null values in it
CREATE VIEW customer_payments_view AS
SELECT
  c.customerNumber,
  p.paymentDate,
  p.amount,
  p.checkNumber
FROM
  payments p
JOIN
  customers c ON p.customerNumber = c.customerNumber
WHERE
  (CASE WHEN p.paymentDate IS NULL THEN 1 ELSE 0 END +
   CASE WHEN p.amount IS NULL THEN 1 ELSE 0 END +
   CASE WHEN p.checkNumber IS NULL THEN 1 ELSE 0 END) / 3 <= 0.3;

#14. check if the overall purchase value has exceeded the credit limit set for them
SELECT c.customerNumber, c.creditLimit, SUM(p.purchase_value) AS total_purchase_value,
       CASE WHEN SUM(p.purchase_value) > c.creditLimit THEN 'Exceeded' ELSE 'Not Exceeded' END AS credit_Limit_status
FROM customers c
JOIN orderdetails p ON c.customerNumber= p.customerNumber
GROUP BY c.customerNumber, c.creditLimit;



#15. find the top performing sales agent, revenue generated and total number of customers for each of them induvidually
SELECT 
    salesRepEmployeeNumber AS top_sales_agent,
    COUNT(DISTINCT customerNumber) AS total_customers
FROM 
    customers
GROUP BY 
salesRepEmployeeNumber limit 1;
