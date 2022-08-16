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

    # POST
    insert_query = '''INSERT INTO product_category (id, category_name)
                        VALUES
                        (7,'Cheese');'''
    cursor.execute(insert_query)
    connection.commit()
    print('Table "product_category" was updated!')

    # GET
    select_query = '''SELECT * FROM product_category WHERE category_name='Cheese';'''
    cursor.execute(select_query)
    connection.commit()
    results = cursor.fetchall()
    print('Data: ',results)

    # PUT
    update_query = '''UPDATE product_category SET category_name='Cheesee' WHERE id=7;'''
    cursor.execute(update_query)
    connection.commit()
    print('Data update.')

    # DELETE
    delete_query = '''DELETE FROM product_category WHERE id=7;'''
    cursor.execute(delete_query)
    connection.commit()
    print('Category deleted.')


except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')