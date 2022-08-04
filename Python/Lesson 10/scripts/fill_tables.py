import psycopg2
from psycopg2 import Error
from config import *


try:
    connection = psycopg2.connect(user=USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                database = 'store_db')
    cursor = connection.cursor()

    # PRODUCT CATEGORY
    # insert_query = '''INSERT INTO product_category (id, category_name)
    #                     VALUES
    #                     (1,'Cheese'),
    #                     (2,'Fruits'),
    #                     (3,'Meat'),
    #                     (4,'Fish'),
    #                     (5,'Drink');'''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Table "product_category" was updated!')


except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')