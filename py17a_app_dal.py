import pymssql
from pymssql import Connection, Cursor # для type hint
import py17b_app_init as params


def getAllProducts():

    connection: Connection
    with (pymssql.connect(
        server=params.DB_SERVER,
        database=params.DATABASE,
        user=params.DB_USER,
        password=params.DB_PASSWORD
    )) as connection:

        sql = f"""
            SELECT ProductID, Name, ProductNumber, ListPrice 
            FROM Production.Product
        """
        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql)
            products = cursor.fetchall()

        # В одну строку кода сгененерируйте список словарей из списка кортежей (10:05)
        results = [ {"id": p[0], "name": p[1], "code": p[2], "price": float(p[3])} for p in products]

    return results

def getProductsByFirstLetters(letters):

    connection: Connection
    with (pymssql.connect(
        server=params.DB_SERVER,
        database=params.DATABASE,
        user=params.DB_USER,
        password=params.DB_PASSWORD
    )) as connection:

        sql = f"""
            SELECT ProductID, Name, ProductNumber, ListPrice 
            FROM Production.Product
            WHERE Name LIKE %s
        """
        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql, letters + "%")
            products = cursor.fetchall()

        # В одну строку кода сгененерируйте список словарей из списка кортежей (10:05)
        results = [ {"id": p[0], "name": p[1], "code": p[2], "price": float(p[3])} for p in products]

    return results

if __name__ == "__main__":
    print(getAllProducts())
    print(getProductsByFirstLetters("a"))