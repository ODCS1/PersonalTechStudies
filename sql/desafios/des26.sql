SELECT SalesOrderDetailID, LineTotal
FROM Sales.SalesOrderDetail
WHERE LineTotal > 5000
UNION
SELECT SalesOrderDetailID, LineTotal
FROM Sales.SalesOrderDetail
WHERE OrderQty = 1