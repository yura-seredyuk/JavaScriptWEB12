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
    insert_query = '''INSERT INTO clients (id, name, email) 
                    VALUES
                    (3, 'Did', 'did@gmail.com'),
                    (4, 'Dod', 'dod@gmail.com'),
                    (5, 'Dad', 'dad@gmail.com');'''
    cursor.execute(insert_query)
    connection.commit()
    print('Table was updated!')

    # # UPDATE
    # update_query = '''update clients SET email='robin@gmail.com' WHERE name = 'Rob';'''
    # cursor.execute(update_query)
    # connection.commit()
    # print('Information was changed!')

    # # DELETE
    # delete_query = '''DELETE FROM clients WHERE name = 'Did';'''
    # cursor.execute(delete_query)
    # connection.commit()
    # print('Row was deleted!')


    # READ
    columns = '''SELECT column_name FROM information_schema.columns WHERE TABLE_NAME = 'clients';'''
    cursor.execute(columns)
    rez = [item[0] for item in cursor.fetchall()]
    # print('Results: ',rez)
    print('\t'.join(rez))

    select_query = '''SELECT * from clients;'''
    cursor.execute(select_query)
    rez = cursor.fetchall()
    # print('Results: ',rez)
    for row in rez:
        print(*row, sep="\t")

except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')