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
        select_query = f'''SELECT {','.join(fields)} FROM {','.join(table)} {selector} ORDER BY ID;'''
        # print(select_query)
        cursor.execute(select_query)
        connection.commit()
        results = cursor.fetchall()
        # print('Data: ',results)

        self.closeDB(connection, cursor)
        return results

    def insertData(self, table, data:dict):
        connection, cursor = self.openDB()
        # POST
        id = self.getNextId(table)
        # print(data)
        fields = list(data.keys())
        fields.insert(0,"id")
        values = f"""({id},{','.join(map(lambda item: f"'{item}'",data.values()))})"""
        insert_query = f'''INSERT INTO {table} ({','.join(fields)}) VALUES {values};'''
        # print(insert_query)
        cursor.execute(insert_query)
        connection.commit()
        self.closeDB(connection, cursor)
        return f"Table '{table}' was updated!"

    def updateData(self, table, data:dict, selector=""):
        connection, cursor = self.openDB()
        # PUT
        set_items = ''
        for key in data:
            set_items+= f"""{key} = '{data[key]}',"""

        update_query = f'''UPDATE {table} SET {set_items[:-1]} WHERE {selector};'''
        cursor.execute(update_query)
        connection.commit()
        print('Data was updated')
        
        self.closeDB(connection, cursor)
        return f"Data in table '{table}' was updated!"


    def deleteData(self, table, selector=""):
        connection, cursor = self.openDB()
        # DELETE
        delete_query = f'''DELETE FROM {table} WHERE {selector};'''
        cursor.execute(delete_query)
        connection.commit()
        print('Category was deleted!')
        
        self.closeDB(connection, cursor)
        selector = selector.split("=")[1]
        return f"Category{selector} was deleted!"

    def getNextId(self,table):
        table = (table,)
        fields = ("max(id)",)
        id = self.getData(table,fields)
        if id == []:
            return 1
        else:
            return id[0][0] + 1

        
if __name__ == "__main__":

    conn = Connection()

    # conn.getData(("product_category",), ("*",), "WHERE category_name='Cheese'")
    # conn.getData(("product_category",), ("*",))
    # conn.getData(("product_category",), ("id", "category_name"))
    # conn.getData(("product",) , ("product_name", "category_name"), """left join product_category product_category on product_category.id = product.product_category_id group by product_name, category_name""")

    data = {
        'category_name':'Milk'
    }

    conn.insertData("product_category", data)
    # conn.updateData(("product_category",), ("category_name = 'Milk'",), "id=7")
    # conn.deleteData(("product_category",), "id=7")


    # print(conn.getNextId("product_category"))

