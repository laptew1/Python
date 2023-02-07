import pymssql
from pymssql import Connection, Cursor # для type hint


class Product:

    def __init__(self, id: int, name: str, code: str, price: float):
        self.id = id
        self.name = name
        self.code = code
        self.price = price


class ProductRepository:

    def __init__(self, server: str, database: str, user: str, password: str):
        self.server = server
        self.database = database
        self.user = user
        self.password = password

    def getAllProducts(self) -> list[Product]:
        connection: Connection
        with (pymssql.connect(
                server=self.server,
                database=self.database,
                user=self.user,
                password=self.password
        )) as connection:
            sql = f"""
                   SELECT ProductID, Name, ProductNumber, ListPrice 
                   FROM Production.Product
               """
            cursor: Cursor
            with connection.cursor() as cursor:
                cursor.execute(sql)
                products = cursor.fetchall()

            # В одну строку кода сгененерируйте список товаров (12:20)
            results = [Product(p[0],  p[1],  p[2],  float(p[3])) for p in products]

        return results

    def getProductsByFirstLetters(letters) -> list[Product]:
        pass

if __name__ == "__main__":
    repository = ProductRepository("yand.dyndns.org","AdventureWorks", "northwind", "northwind")

    products = repository.getAllProducts()
    for p in products:
        print(f"{p.name}\t{p.price}")