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

    # CREATE
    insert_query = '''INSERT INTO clients (id, name, email) 
                    VALUES
                    (3, 'Did', 'did@gmail.com'),
                    (4, 'Dod', 'dod@gmail.com'),
                    (5, 'Dad', 'dad@gmail.com');'''
    cursor.execute(insert_query)
    connection.commit()
    print('Table was updated!')


except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')