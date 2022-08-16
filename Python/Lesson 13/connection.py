import psycopg2
from psycopg2 import Error
from scripts.config import *


class Connection():

    @classmethod
    def openDB(cls):
        connection = psycopg2.connect(user=USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                database = 'store_db')
        cursor = connection.cursor()
        return connection, cursor

    @classmethod
    def closeDB(cls, connection, cursor):
        cursor.close()
        connection.close()

    def getData(self, table, fields:tuple, selector=""):
        connection, cursor = self.openDB()
        # GET
        select_query = f'''SELECT {','.join(fields)} FROM {','.join(table)} {selector};'''
        print(select_query)
        cursor.execute(select_query)
        connection.commit()
        results = cursor.fetchall()
        print('Data: ',results)

        self.closeDB(connection, cursor)
        return results


if __name__ == "__main__":

    conn = Connection()

    conn.getData(("product_category",), ("*",), "WHERE category_name='Cheese'")
    conn.getData(("product_category",), ("*",))
    conn.getData(("product_category",), ("id", "category_name"))
    conn.getData(("product",) , ("product_name", "category_name"), """left join product_category product_category on product_category.id = product.product_category_id group by product_name, category_name""")
