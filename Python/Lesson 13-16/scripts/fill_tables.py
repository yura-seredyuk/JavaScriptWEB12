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

    # # COUNTRY
    # insert_query = '''INSERT INTO country (id, country_name)
    #                 VALUES
    #                 (1,'England'),
    #                 (2,'France'),
    #                 (3,'Spain');'''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Table "country" was updated!')

    # # CITY
    # insert_query = '''INSERT INTO city(id, city_name, country_id)
    #                 VALUES
    #                 (1,'London',1),
    #                 (2,'Paris',3),
    #                 (3,'Madrid',2);'''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Table "city" was updated!')

    # # CUSTOMER
    # insert_query = '''INSERT INTO customer (id, city_id, first_name, last_name)
    #                 VALUES
    #                 (1,2,'Eduard','Alcock'),
    #                 (2,1,'Yousef','Espinoza'),
    #                 (3,1,'Luther','Mackie'),
    #                 (4,3,'Igor','Gunn'),
    #                 (5,2,'Stacy','Major'),
    #                 (6,2,'Muhamed','Mustafa'),
    #                 (7,3,'Harvie' ,'Berry'),
    #                 (8,1,'Chester','Larson'),
    #                 (9,2,'Veronika','Regan'),
    #                 (10,3,'Maddison','Holding');'''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Table "customer" was updated!')

    # # EMPLOYEE
    # insert_query = '''INSERT INTO employee (id, first_name, last_name, date_of_birth, city_id, chief_id)
    #                 VALUES
    #                 (1,'Rahul','Lott','1964-03-23',1,9),
    #                 (2,'Ishaan','Dunn','1972-03-31',1,3),
    #                 (3,'Nina','Palacios','1972-07-26',2,1),
    #                 (4,'Zac','Copeland','1986-08-04',2,1),
    #                 (5,'Stuart','Willis','1993-08-16',3,2),
    #                 (6,'Cristina','Salt','1965-08-31',3,2),
    #                 (7,'Dean' ,'Taylor','1987-02-11',3,3),
    #                 (8,'Joseff','Witt','1995-02-28',2,4),
    #                 (9,'Nathanael','Bartlett','1978-08-29',1,1),
    #                 (10,'Zak','Spooner','1997-12-11',2,2);'''
    # cursor.execute(insert_query)
    # connection.commit()
    # print('Table "employee" was updated!')

    # PRODUCT
    insert_query = '''INSERT INTO product (id ,product_name,unit_price,country_id,product_category_id)
                    VALUES
                    (1,'Tofu',100,2,1),
                    (2,'Apple',50,1,2),
                    (3,'Meat',150,3,3),
                    (4,'Fish',80, 1,4),
                    (5,'Coffe',200,3,5),
                    (6,'Tea',120,2,5);'''
    cursor.execute(insert_query)
    connection.commit()
    print('Table "product" was updated!')

    # ORDER
    insert_query = '''INSERT INTO orders (id,employee_id,customer_id,city_id,date_of_order,product_id,price)
                    VALUES
                    (1,3,1,2,'2020-01-25',2,700),
                    (2,2,2,1,'2020-03-30',2,750),
                    (3,4,4,1,'2020-09-03',1,170),
                    (4,2,3,3,'2020-11-18',5,100),
                    (5,4,5,3,'2020-12-28',4,80),
                    (6,5,2,2,'2020-09-07',3,200),
                    (7,6,3,1,'2020-11-12',2,800),
                    (8,1,5,3,'2020-11-19',1,150),
                    (9,2,6,1,'2020-06-12',4,85),
                    (10,8,1,3,'2020-07-28',5,100);'''
    cursor.execute(insert_query)
    connection.commit()
    print('Table "orders" was updated!')

except (Exception, Error) as error:
    print("Error connection: ", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print('Connection was closed!')