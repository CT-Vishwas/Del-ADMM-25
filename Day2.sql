USE Northwind;
-- See the tables
SHOW TABLES;
-- Describing a table
DESCRIBE Employees;
-- See all the records in the table
SELECT * FROM Employees;
-- Get all the customers who are from london
SELECT * FROM Customers
WHERE city= 'london';
-- Get the customers who are from brazil
SELECT * FROM Customers
WHERE Country = 'Brazil';
-- Get Customer Names who are from Brazil
SELECT CustomerName FROM Customers
WHERE Country = 'Brazil';
-- Get the CustomerIDs FROM Customers
SELECT CustomerID FROM Customers;
-- Get the customers from portland & seattle
SELECT * FROM Customers WHERE City = 'Portland' OR City = 'Seattle';
-- Get Products which belong to category 2 & whose price is greater than 15
SELECT * FROM Products
WHERE CategoryID = 2 AND Price > 15;
-- Get the products which belong to category 2 & price is not 21
SELECT * FROM Products
WHERE CategoryID = 2 AND Price != 21;

SELECT * FROM Products
WHERE CategoryID = 2 AND Price <> 21;
-- Get all the customers who are not from brazil, spain
SELECT * FROM Customers
WHERE Country != 'Brazil' AND Country != 'Spain';
-- Get all the customers who are not from Sweden or Germany
SELECT * FROM Customers
WHERE Country != 'Sweden' AND Country !='Germany';

SELECT * FROM Customers
WHERE Country NOT IN ('Sweden','Germany');
-- Get the customers from mexico, canada
SELECT * FROM Customers 
WHERE Country IN ('Mexico', 'Canada');
-- LIKE ( Pattern in the string )
-- '%': Any Character & any number of character
-- '_': Any Single Character
-- Get the Contact Names of Customers Starting with 'An'
SELECT ContactName FROM Customers
WHERE ContactName LIKE 'An%';
-- Get the contactname of customers 
-- whose contactname contains 'n' in the second place
SELECT ContactName FROM Customers
WHERE ContactName LIKE '_n%';
-- Get contact names which do not have 
-- a format Like 'first_name last_name'
SELECT ContactName 
FROM Customers 
WHERE ContactName NOT LIKE '% %';
-- Sort the Customers based on country
SELECT * FROM Customers
ORDER BY Country;

SELECT * FROM Customers
ORDER BY Country DESC;

-- Sort the customers based on country, city
SELECT * FROM Customers
ORDER BY Country ASC, City DESC;

-- Get the products & their category based, 
-- with expensive product first in each category
SELECT ProductName, CategoryID
FROM Products 
ORDER BY CategoryID, Price DESC;
-- Top 2 Most expensive Products for category 2
SELECT * FROM Products
WHERE CategoryID = 2
ORDER BY Price DESC
LIMIT 2;
-- Get 2 least expensive products supplied by the supplierID 3
SELECT * FROM Products
WHERE SupplierID = 3
ORDER BY Price ASC
LIMIT 2;
-- Get 3,4,5 most expensive products in inventory
SELECT * FROM Products
ORDER BY Price DESC
LIMIT 3 OFFSET 2;
-- Get the orders which are not assigned to an employee
SELECT * FROM Orders
WHERE EmployeeID IS NULL;
-- Get the Current Date & Time
SELECT NOW() FROM DUAL;
SELECT 2 * 5 FROM DUAL;
-- Get the orders & their order dates
SELECT OrderDate, OrderID, CustomerID
FROM Orders;
-- Get the order years, month, day of orders
SELECT OrderID, 
YEAR(OrderDate), MONTH(OrderDate), DAY(OrderDate), 
DAYNAME(OrderDate), CustomerID
FROM Orders;
-- Get the age of employees
-- Difference between two dates DATEDIFF()
SELECT FirstName, 
 ceil(DATEDIFF(NOW(), BirthDate) /365) AS Age 
FROM Employees;
-- What is the date 30 days from today
SELECT CURDATE() AS Today, DATE_ADD(CURDATE(), INTERVAL 30 DAY);
-- Formatting the date
SELECT date_format(CURDATE(), '%d/%m/%y') FROM DUAL;
SELECT date_format(CURDATE(),'%d %M %y') FROM DUAL;
-- Aggregate Functions
-- COUNT, SUM, MIN, MAX, AVG
-- Get the Number of products in the inventory
SELECT COUNT(ProductID) AS TotalProducts FROM Products;
SELECT COUNT(ProductID) 'Total Products' FROM Products;
-- Get Total Number of Customers from Germany
SELECT COUNT(CustomerID) AS total_customers_germany
FROM Customers
WHERE country= 'Germany';
-- Get the average price of product for categoryID 2
SELECT AVG(Price) 
FROM Products
WHERE CategoryID = 2;
-- Get the Minimum & Maximum price of products for category 2
-- Get Average, min, max price for each category
SELECT CategoryID, AVG(Price), MIN(Price), MAX(Price)
FROM Products
GROUP BY CategoryID
ORDER BY CategoryID;
-- Get the number of products by category, get the categoryID which has
-- highest number of products
SELECT CategoryID, COUNT(ProductID) AS 'Number of Products'
FROM Products
GROUP BY CategoryID
ORDER BY 'Number of Products'
LIMIT 1;
-- Get the products whose price is greater than average price 
SELECT ProductID, Price FROM Products WHERE Price > 
(SELECT AVG(Price) FROM Products);
-- Get the Average price in each category
SELECT CategoryID, AVG(Price) 
FROM Products
GROUP BY CategoryID;
-- Get the average of the Average price in each category
SELECT AVG(T1.avg_price) FROM (SELECT CategoryID, AVG(Price) AS avg_price 
FROM Products
GROUP BY CategoryID) T1;
-- Get the Count of orders served by each shipper
SELECT ShipperID, COUNT(OrderID) FROM Orders
GROUP BY ShipperID;
-- Get the Shippers who have shipped More than 70 Orders
SELECT ShipperID, COUNT(OrderID) FROM Orders
GROUP BY ShipperID
HAVING COUNT(OrderID) > 70; 