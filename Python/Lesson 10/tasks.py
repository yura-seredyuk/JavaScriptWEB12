# import psycopg2
# from psycopg2 import Error
# from scripts.config import *


# try:
#     connection = psycopg2.connect(user=USER,
#                                 password = PASSWORD,
#                                 host = HOST,
#                                 port = PORT,
#                                 database = 'store_db')
#     cursor = connection.cursor()

#     # TASKS
#     # 1. Show all info about the employee with ID 8.
    
#     # select_query = '''select * from employee e where id=8;'''
#     # cursor.execute(select_query)
#     # rez = cursor.fetchall()
#     # for row in rez:
#     #     print(*row, sep="\t")

#     # TASKS
#     # 2. Calculate the count of employees from London.
    
#     select_query = '''select count(*) as "Employee from London" from employee where city_id in 
# (select id from city c where city_name = 'London');'''
#     cursor.execute(select_query)
#     rez = cursor.fetchall()
#     for row in rez:
#         print(*row, sep="\t")




# except (Exception, Error) as error:
#     print("Error connection: ", error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()
#         print('Connection was closed!')


# import datetime
# t = datetime.datetime(2009, 10, 21, 0, 0)

# print((t-datetime.datetime(1970,1,1)).total_seconds())

# t = datetime.datetime(1970, 1, 1, 0, 0)

# print((t-datetime.datetime(1970,1,1)).total_seconds())


--select count(*) as "Employee from London" from employee where city_id in 
--(select id from city c where city_name = 'London');

--select first_name, last_name from employee where  date_of_birth in 
--(select min(date_of_birth) from employee);

--select first_name, last_name from employee where  date_of_birth in 
--(select min(date_of_birth) from employee group by city_id);

--select first_name, last_name, date_of_birth from employee where  extract(month from date_of_birth) = extract(month from now());

--select first_name, last_name from employee
--where id in
--	(select employee_id from orders o 
--	where city_id in 
--		(select id from city c  
--		where city_name = 'Madrid'
--		));

select first_name, last_name, count(date_of_order)  from employee
left join orders on employee.id = orders.employee_id 
where extract(year from date_of_order) = 2020 and date_of_order > '2020-09-01'
group by first_name, last_name;