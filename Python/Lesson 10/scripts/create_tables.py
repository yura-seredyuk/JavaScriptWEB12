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
    create_table_query = '''CREATE TABLE IF NOT EXISTS product_category 
                            (id SERIAL PRIMARY KEY,
                            category_name VARCHAR(30) NOT NULL);'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "product_category" created!')

    # COUNTRY
    create_table_query = '''CREATE TABLE IF NOT EXISTS country 
                            (id SERIAL PRIMARY KEY,
                            country_name VARCHAR(50) NOT NULL);'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "country" created!')

    # CITY
    create_table_query = '''CREATE TABLE IF NOT EXISTS city 
                            (id SERIAL PRIMARY KEY,
                            city_name VARCHAR(50) NOT NULL,
                            country_id INT NOT NULL REFERENCES country(id));'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "city" created!')

    # CUSTOMER
    create_table_query = '''CREATE TABLE IF NOT EXISTS customer 
                            (id SERIAL PRIMARY KEY,
                            city_id INT NOT NULL REFERENCES city(id),
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL);'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "customer" created!')

    # EMPLOYEE
    create_table_query = '''CREATE TABLE IF NOT EXISTS employee 
                            (id SERIAL PRIMARY KEY,
                            first_name VARCHAR(50) NOT NULL,
                            last_name VARCHAR(50) NOT NULL,
                            date_of_birth DATE,
                            city_id INT NOT NULL REFERENCES city(id),
                            chief_id INT NOT NULL REFERENCES employee(id));'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "employee" created!')

    # PRODUCT
    create_table_query = '''CREATE TABLE IF NOT EXISTS product 
                            (id SERIAL PRIMARY KEY,
                            product_name VARCHAR(30) NOT NULL,
                            unit_price DEC NOT NULL,
                            country_id INT NOT NULL REFERENCES country(id),
                            product_category_id INT NOT NULL REFERENCES product_category(id));'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "product" created!')

    # ORDER
    create_table_query = '''CREATE TABLE IF NOT EXISTS orders
                            (id SERIAL PRIMARY KEY,
                            employee_id INT NOT NULL REFERENCES employee(id),
                            city_id INT NOT NULL REFERENCES city(id),
                            date_of_order DATE,
                            customer_id INT NOT NULL REFERENCES customer(id),
                            product_id INT NOT NULL REFERENCES product(id),
                            price DEC);'''
    cursor.execute(create_table_query)
    connection.commit()
    print('Table "order" created!')

except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')