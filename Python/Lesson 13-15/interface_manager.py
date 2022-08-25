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

    
    # ORDERS
    @authenticated
    def get_orders(self, status=""):
        if self.authenticated:
            if status:
                selector = f"WHERE status = '{status}'"
                return self.getData(('orders',),("*",), selector)
            else:
                return self.getData(('orders',),("*",))
        else: return "Wrong username or password."
    

    # EMPLOYEE!!!!!!!
    @authenticated
    def add_manager(self, data:dict):
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
        # profile_id = self.create_profile(profile_data)[1]
        # employee_data = {
        #     "first_name": data["first_name"],
        #     "last_name": data["last_name"],
        #     "date_of_birth": data["date_of_birth"],
        #     "city_id": city_id,
        #     "profile_id": profile_id
        # }
        # employee = self.insertData('employee',employee_data)
        # return employee
        


if __name__ == "__main__":

    manager = Manager('manager1', 'P@$$w0Rd')
    manager.login_self()
    # admin.logout_self()

    # print(manager.get_orders())
    print(manager.get_orders('closed'))





    





