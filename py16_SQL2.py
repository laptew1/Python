# Параметрические запросы (гарантируют защиту от SQL Injection)

import pymssql
from pymssql import Connection, Cursor # для type hint

connection: Connection
with (pymssql.connect(
    server="yand.dyndns.org",
    database="AdventureWorks",
    user="northwind",
    password="northwind"
)) as connection:

    filter = "b"

    # Так можно. %s - указание, что в это место нужно подставить параметр типа строка
    sql = f"""
        SELECT ProductID, Name, ProductNumber, ListPrice 
        FROM Production.Product
        WHERE Name LIKE %s
    """
    cursor: Cursor
    with connection.cursor() as cursor:
        cursor.execute(sql, filter + "%") #значение параметра передается вторым аргументом
        products = cursor.fetchall()
        # print(products)

for p in products:
    id = p[0]
    name = p[1]
    code = p[2]
    price = p[3]
    print(f"{name}\t{code}\t{price}")


