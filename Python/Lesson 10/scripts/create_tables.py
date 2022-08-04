import psycopg2
from psycopg2 import Error
from scripts.config import *


try:
    connection = psycopg2.connect(user=USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                database = 'store_db')
    cursor = connection.cursor()

    create_table_query = '''CREATE TABLE IF NOT EXISTS clients 
                            (id INT PRIMARY KEY NOT NULL,
                            name VARCHAR NOT NULL,
                            email VARCHAR);'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table created!')


except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')