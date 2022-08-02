import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
from config import *

try:
    connection = psycopg2.connect(user=USER,
                            password = PASSWORD,
                            host = HOST,
                            port = PORT)
    connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = connection.cursor()
    sql_create_db = "CREATE DATABASE clients_db;"
    cursor.execute(sql_create_db)
    print(cursor)

except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')