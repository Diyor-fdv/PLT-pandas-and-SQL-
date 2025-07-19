DROP TABLE IF EXISTS orders;

CREATE TABLE orders (
    OrderID SERIAL PRIMARY KEY,
    CustomerName VARCHAR(50),
    Country VARCHAR(50),
    Product VARCHAR(50),
    Category VARCHAR(50),
    Quantity INTEGER,
    Price NUMERIC(10, 2),
    OrderDate DATE
);

INSERT INTO orders (CustomerName, Country, Product, Category, Quantity, Price, OrderDate)
VALUES 
  ('Ali Valiyev', 'Uzbekistan', 'Smartphone', 'Electronics', 2, 350.00, '2025-07-18'),
  ('Jane Doe', 'USA', 'Laptop', 'Electronics', 1, 999.99, '2025-07-17'),
  ('Ahmad Karimov', 'Uzbekistan', 'Chair', 'Furniture', 4, 45.50, '2025-07-15'),
  ('Emily Smith', 'UK', 'Table', 'Furniture', 1, 80.00, '2025-07-16'),
  ('Tom Hardy', 'USA', 'Smartwatch', 'Electronics', 3, 120.00, '2025-07-18'),
  ('John Wick', 'Canada', 'Keyboard', 'Electronics', 2, 40.00, '2025-07-14'),
  ('Sara Lee', 'Germany', 'Desk', 'Furniture', 2, 150.00, '2025-07-12');

SELECT * FROM orders
WHERE Category = 'Electronics';

SELECT * FROM orders
ORDER BY Price DESC;

SELECT Country, SUM(Quantity) AS TotalQuantity
FROM orders
GROUP BY Country;

SELECT Category, AVG(Price) AS AvgPrice
FROM orders
GROUP BY Category;

SELECT Product, COUNT(*) AS OrderCount
FROM orders
GROUP BY Product
ORDER BY OrderCount DESC;

SELECT * FROM orders
WHERE OrderDate > '2025-07-17';

SELECT * FROM orders
ORDER BY Price DESC
LIMIT 3;

UPDATE orders
SET Quantity = 5
WHERE CustomerName = 'John Wick';

DELETE FROM orders
WHERE Product = 'Desk';

-- Diyorbek 



  



