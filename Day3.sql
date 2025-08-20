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
SELECT c.CustomerName, COUNT(o.OrderID) AS 'Number of Orders'
FROM Customers c
INNER JOIN Orders o
ON c.CustomerID = o.CustomerID;