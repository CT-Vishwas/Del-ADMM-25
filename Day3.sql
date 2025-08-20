USE Northwind;
-- GET the orders and its customer names (INNER JOIN)
SELECT o.OrderID, c.CustomerID, c.CustomerName 
FROM Orders o
INNER JOIN Customers c
ON c.CustomerID = o.CustomerID;
-- Get the Orders and its products
-- Get the orders and its shippers
-- Get the orders with its employees
SELECT o.OrderID, c.CustomerID, c.CustomerName, s.ShipperName, e.FirstName
FROM Orders o
INNER JOIN Customers c ON c.CustomerID = o.CustomerID
INNER JOIN Shippers s ON s.ShipperID = o.ShipperID
INNER JOIN Employees e ON e.EmployeeID = o.EmployeeID;

-- Get the customer names & number of orders they have placed
SELECT c.CustomerName, COUNT(o.OrderID) AS Number_of_Orders
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID
GROUP BY c.CustomerName
ORDER BY Number_of_Orders DESC;

-- Get All the customers with their orders
SELECT c.CustomerName, o.OrderID
FROM Customers c 
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
ORDER BY o.OrderID;
-- Getting Customers who do not have an order
SELECT c.CustomerName, o.OrderID
FROM Customers c 
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
WHERE o.OrderID IS NULL
ORDER BY o.OrderID;

SELECT COUNT(DISTINCT CustomerID) FROM Customers;
SELECT COUNT(DISTINCT CustomerID) FROM Orders;

SELECT COUNT(CustomerID) FROM Customers
WHERE CustomerID NOT IN (SELECT CustomerID FROM Orders);

-- Are there any products which are never ordered
-- Using Join
SELECT p.ProductID, p.ProductName, od.OrderID
FROM Products p
LEFT JOIN OrderDetails od
ON p.ProductID = od.ProductID
WHERE od.OrderID IS NULL;

-- lower upper concat
-- Get the Full Name of a Employee Name in Uppercase
SELECT UPPER(concat(FirstName, ' ', LastName)) AS FullName FROM
Employees;

-- Get the Product Names
SELECT UPPER(ProductName) FROM Products;

-- Generate a Password Which is a combination of
-- first 3 characters of FirstName, 2 digits of the year for employees
SELECT CONCAT(UPPER(FirstName),' ',UPPER(LastName)) AS FullName, CONCAT(UPPER(SUBSTRING(FirstName,1,3)), DATE_FORMAT(BirthDate,'%y')) AS Password FROM Employees;

-- Get 3rd most expensive product in each category
SELECT * FROM Products
ORDER BY CategoryID, Price DESC;

SELECT productName, CategoryID, Price,
ROW_NUMBER() OVER (PARTITION BY CategoryID ORDER BY Price) AS NumberInRow
FROM Products;

SELECT productName, CategoryID, Price,
DENSE_RANK() OVER (PARTITION BY CategoryID ORDER BY Price DESC) AS RankedProduct
FROM Products;

SELECT productName, CategoryID, Price FROM
(SELECT productName, CategoryID, Price,
DENSE_RANK() OVER (PARTITION BY CategoryID ORDER BY Price DESC) AS RankedProduct
FROM Products) t1
WHERE t1.RankedProduct = 5;
--

SELECT c.CustomerName, 
 COALESCE(o.OrderID, 'NA')
FROM Customers c 
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
ORDER BY o.OrderID;

-- Get the List of Products & Total Number of Products for each Category
SELECT CategoryID, COUNT(ProductID) AS TotalProducts FROM Products
GROUP BY CategoryID;

SELECT
	productName,
    categoryID,
    COUNT(*) OVER (PARTITION BY CategoryID) AS TotalProducts
FROM 
	Products;

SELECT
	productName,
    categoryID,
    COUNT(*)  AS TotalProducts
FROM 
	Products
GROUP BY
	CategoryID, ProductName
WITH ROLLUP;

-- Generate a report of Customer Sale per order and
-- Total Revenue from each customer
SELECT 
	COALESCE(t1.ContactName, 'Grand Total') AS 'Customer',
    COALESCE(t2.OrderID, 'Customer Subtotal') AS 'Order ID',
    SUM(t4.Price * t3.Quantity) AS 'OrderTotal'
FROM
	Customers AS t1
JOIN
	Orders AS t2 ON t1.CustomerID = t2.CustomerID
JOIN
	OrderDetails AS t3 ON t2.OrderID = t3.OrderID
JOIN
	Products AS t4 ON t3.ProductID = t4.ProductID
GROUP BY
	t1.ContactName, t2.OrderID
WITH ROLLUP;

SHOW STATUS LIKE 'Thread%';
SHOW STATUS LIKE '%Handler%';

EXPLAIN SELECT c.CustomerName, 
 COALESCE(o.OrderID, 'NA')
FROM Customers c 
LEFT JOIN Orders o
ON c.CustomerID = o.CustomerID
ORDER BY o.OrderID;

SELECT o.orderID, c.CustomerName
FROM Orders o
JOIN Customers c ON o.CustomerID = c.CustomerID
WHERE c.CustomerID = 10308;

-- BEST Practices
-- Use Indexes where necessary
-- Use partitions when data is large
-- Avoid Functions in Where Clause
-- Use Limit 
-- Try to avoid SELECT *
