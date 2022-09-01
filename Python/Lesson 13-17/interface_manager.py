import psycopg2
from psycopg2 import Error
from scripts.config import *

from connection import Connection, authenticated


class Manager(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.group = 'manager'
        self.authenticated = False

    def login_self(self):
        
        if self.login_check(self.login, self.password):
            self.authenticated = True
        # print(self.login_check(self.login, self.password))

    def logout_self(self):
        self.authenticated = False

    def _manager_data(self):
        selector = f"""where username = '{self.login}' and "password"='{self.password}'"""
        profile_id, address_id = self.getData(("profile",),("id", "address_id"), selector)[0]
        selector = f"""where profile_id = '{profile_id}'"""
        mahager_id = self.getData(("employee",),("id",), selector)[0][0]
        return profile_id, address_id, mahager_id

    # ORDERS
    @authenticated
    def get_orders(self, status=""):
        """select o.id, concat(e.first_name, ' ',e.last_name) as "employee",
        concat(c.first_name, ' ',c.last_name) as "customer", ci.city_name,
        o.date_of_order, p.product_name, o.price, o.status 
        from  orders o 
        left join employee e on e.id = o.employee_id
        left join customer c  on c.id = o.customer_id
        left join city ci  on ci.id = o.city_id 
        left join product p on p.id = o.product_id
        where o.status = 'opened'
        order by id;"""
        customer_id = ""
        fields = """o.id, concat(e.first_name, ' ',e.last_name) as "employee",
        concat(c.first_name, ' ',c.last_name) as "customer", ci.city_name,
        o.date_of_order, p.product_name, o.price, o.status"""
        tables = ("orders o",)
        selector = """left join employee e on e.id = o.employee_id
        left join customer c  on c.id = o.customer_id
        left join city ci  on ci.id = o.city_id 
        left join product p on p.id = o.product_id"""
        if status:
            selector += f" WHERE o.status = '{status}' order by id"
            return self.getData(tables,(fields,), selector)
        else:
            return self.getData(tables,(fields,), selector + " order by id")
    

    @authenticated
    def add_employee(self, data:dict):
        country_id = self.get_country_id(data["country_id"])
        city_id = self.get_city_id(data["city_id"], country_id=country_id)
        address_data = {
            "street": data["street"],
            "appartaments": data["appartaments"],
            "zip": data["zip"],
            "city_id": city_id,
            "country_id": country_id
        }
        address_id = self.create_address(address_data)[1]
        profile_data = {
            "username": data["username"],
            "password": data["password"],
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "date_of_birth": data["date_of_birth"],
            "user_group": "manager",
            "phone": data["phone"],
            "email": data["email"],
            "city_id": city_id,
            "address_id": address_id
        }
        profile_id = self.create_profile(profile_data)[1]
        _, _, manager_id = self._manager_data()
        employee_data = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "date_of_birth": data["date_of_birth"],
            "city_id": city_id,
            "chief_id": manager_id,
            "profile_id": profile_id
        }
        employee = self.insertData('employee',employee_data)
        return employee
        


if __name__ == "__main__":

    manager = Manager('manager1', 'P@$$w0Rd')
    manager.login_self()
    # admin.logout_self()

    # print(manager.get_orders())
    # print(manager.get_orders('closed'))
    data = {
        "username": "emp1",
        "password": "P@$$w0Rd",
        "first_name": "Ricardo",
        "last_name": "Bobik",
        "date_of_birth": "1996-08-31",
        "phone": "+380981234567",
        "email": "rik.bob@gmail.com",
        "street": "Beautiful st. 11",
        "appartaments": "20",
        "zip": "33027",
        "city_id": "Rivne",
        "country_id": "Ukraine"
    }
    manager.add_employee(data)





    





