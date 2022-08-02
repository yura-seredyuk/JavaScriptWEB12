import psycopg2
from psycopg2 import Error
from config import *


try:
    connection = psycopg2.connect(user=USER,
                                password = PASSWORD,
                                host = HOST,
                                port = PORT,
                                database = 'test_db')
    cursor = connection.cursor()

    # print('Server information:')
    # print(connection.get_dsn_parameters())
    # cursor.execute('SELECT version()')
    # # print(cursor.fetchall())
    # # print(cursor.fetchmany(size=2))
    # print(cursor.fetchone())

    # create_table_query = '''CREATE TABLE IF NOT EXISTS clients 
    #                         (id INT PRIMARY KEY NOT NULL,
    #                         name VARCHAR NOT NULL,
    #                         email VARCHAR);'''
    # cursor.execute(create_table_query)
    # connection.commit()
    # print('Table created!')

    # SQL CRUD commands
    # C - create/insert
    # R - read/select
    # U - update/update
    # D - delete/delete


    # CREATE
    insert_query = '''INSERT INTO clients (id, name, email) VALUES (1, 'Bob', 'bob@gmail.com');'''
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