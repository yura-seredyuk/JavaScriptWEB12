from dataclasses import fields
import psycopg2
from psycopg2 import Error
from scripts.config import *

from connection import Connection, authenticated


class Customer(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.group = 'customer'
        self.authenticated = False

    def login_self(self):
        
        if self.login_check(self.login, self.password):
            self.authenticated = True

    def logout_self(self):
        self.authenticated = False

    def _customer_data(self):
        selector = f"""where username = '{self.login}' and "password"='{self.password}'"""
        profile_id, address_id = self.getData(("profile",),("id", "address_id"), selector)[0]
        selector = f"""where profile_id = '{profile_id}'"""
        customer_id = self.getData(("customer",),("id",), selector)[0][0]
        return profile_id, address_id, customer_id

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

        fields = """o.id, concat(e.first_name, ' ',e.last_name) as "employee",
        concat(c.first_name, ' ',c.last_name) as "customer", ci.city_name,
        o.date_of_order, p.product_name, o.price, o.status"""
        tables = ("orders o",)
        selector = """left join employee e on e.id = o.employee_id
        left join customer c  on c.id = o.customer_id
        left join city ci  on ci.id = o.city_id 
        left join product p on p.id = o.product_id"""
        if status:
            selector += f" WHERE status = '{status}' order by id"
            return self.getData(tables,(fields,), selector)
        else:
            return self.getData(tables,(fields,), selector + " order by id")
    
    # PROFILE
    @authenticated
    def get_customer(self):
        """select p.username, p."password", c.first_name, c.last_name, p.date_of_birth,
        p.phone, p.email, a.street, a.appartaments, a.zip, ci.city_name, co.country_name 
        from customer c
        left join profile p on c.profile_id = p.id
        left join address a on p.address_id = a.id
        left join city ci on a.city_id = ci.id
        left join country co on a.country_id = co.id
        where p.id = 2;"""
        _, _, customer_id = self._customer_data()
        fields = """p.username, p."password", c.first_name, c.last_name, p.date_of_birth,
        p.phone, p.email, a.street, a.appartaments, a.zip, ci.city_name, co.country_name"""
        selector = f"""left join profile p on c.profile_id = p.id
        left join address a on p.address_id = a.id
        left join city ci on a.city_id = ci.id
        left join country co on a.country_id = co.id
        where p.id = {customer_id}"""
        customer = self.getData(("customer c",), (fields,), selector)
        return customer



    @authenticated
    def edit_customer(self, data:dict):
        profile_id, address_id, customer_id = self._customer_data()
        country_id = self.get_country_id(data["country_id"])
        city_id = self.get_city_id(data["city_id"], country_id=country_id)
        address_data = {
            "street": data["street"],
            "appartaments": data["appartaments"],
            "zip": data["zip"],
            "city_id": city_id,
            "country_id": country_id
        }
        self.edit_address(address_data, address_id)
        profile_data = {
            "username": data["username"],
            "password": data["password"],
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "date_of_birth": data["date_of_birth"],
            "user_group": "customer",
            "phone": data["phone"],
            "email": data["email"],
            "city_id": city_id,
            "address_id": address_id
        }
        self.edit_profile(profile_data, profile_id)
        customer_data = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "city_id": city_id,
            "profile_id": profile_id
        }
        selector = f"WHERE id = {customer_id}"
        customer = self.updateData('customer',customer_data, selector)
        return customer
        


if __name__ == "__main__":

    customer = Customer('yousef', '12345')
    customer.login_self()
    # admin.logout_self()

    # print(customer.get_orders())
    # print(manager.get_orders('closed'))

    customer._customer_data()
    print(customer.get_customer())





    





