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

    def getData(self, table:tuple, fields:tuple, selector=""):
        connection, cursor = self.openDB()
        # GET
        select_query = f'''SELECT {','.join(fields)} FROM {','.join(table)} {selector};'''
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
        return f"Table '{table}' was updated!", id

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

    def login_check(self, login:str, password:str):
        find_user = self.getData(('profile',),('*',),f"WHERE username = '{login}' AND password = '{password}'")
        if find_user:
            return find_user[0]
        else:
            return False



    def getNextId(self,table):
        table = (table,)
        fields = ("max(id)",)
        id = self.getData(table,fields)
        if id == [] or id[0][0] is None:
            return 1
        else:
            return id[0][0] + 1

    def get_city_id(self, city:str, country_id):
        city_id = self.getData(("city",),("id",),
                    f"""WHERE city_name = '{city}'""")
        if len(city_id) > 0:
            return city_id[0][0]
        else:
            _, id = self.insertData("city",{'city_name':city,
                                            'country_id':country_id})
            return id

    def get_country_id(self, country:str):
        country_id = self.getData(("country",),("id",),
                    f"""WHERE country_name = '{country}'""")
        if len(country_id) > 0:
            return country_id[0][0]
        else:
            _, id = self.insertData("country",{'country_name':country})
            return id

    def create_address(self, data:dict):
        return self.insertData("address",data)

    def create_profile(self, data:dict):
        return self.insertData("profile",data)

        
if __name__ == "__main__":

    conn = Connection()

    # conn.getData(("product_category",), ("*",), "WHERE category_name='Cheese'")
    # conn.getData(("product_category",), ("*",))
    # conn.getData(("product_category",), ("id", "category_name"))
    # conn.getData(("product",) , ("product_name", "category_name"), """left join product_category product_category on product_category.id = product.product_category_id group by product_name, category_name""")

    # data = {
    #     'category_name':'Milk'
    # }

    # conn.insertData("product_category", data)
    # conn.updateData(("product_category",), ("category_name = 'Milk'",), "id=7")
    # conn.deleteData(("product_category",), "id=7")


    # print(conn.getNextId("product_category"))

    # print(conn.get_country_id('Ukraine'))
    # print(conn.get_city_id('Lviv', country_id=5))
    # print(conn.login_check("manager1", "P@$$w0Rd"))
    print(conn.login_check("admin", "admin"))
