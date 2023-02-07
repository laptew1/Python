import pymssql
from pymssql import Connection, Cursor # для type hint


def add_student(firstname: str, lastname: str) -> None:

    connection: Connection
    with (pymssql.connect(
        server="yand.dyndns.org",
        database="MyDB",
        user="northwind",
        password="northwind"
    )) as connection:

        sql = """
        INSERT INTO Students(FirstName, LastName, Code) 
        VALUES(%s, %s,'YA')
        """

        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql, (firstname, lastname))
            connection.commit()


def edit_student(id: int, firstname: str, lastname: str) -> None:

    connection: Connection
    with (pymssql.connect(
        server="yand.dyndns.org",
        database="MyDB",
        user="northwind",
        password="northwind"
    )) as connection:

        sql = """
        UPDATE Students
        SET FirstName = %s,
        LastName = %s
        WHERE PersonID = %s
        """

        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql, (firstname, lastname, id))
            connection.commit()


def delete_student(id: int) -> None:

    connection: Connection
    with (pymssql.connect(
        server="yand.dyndns.org",
        database="MyDB",
        user="northwind",
        password="northwind"
    )) as connection:

        sql = """
        DELETE Students
        WHERE PersonID = %s
        """

        cursor: Cursor
        with connection.cursor() as cursor:
            cursor.execute(sql,  id)
            connection.commit()


if __name__ == "__main__":
    # add_student('Vasya', 'Pupkin')
    #edit_student(17,'Yuri', 'Andrienko!')
    delete_student(17)


