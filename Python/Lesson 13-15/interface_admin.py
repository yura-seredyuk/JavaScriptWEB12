import psycopg2
from psycopg2 import Error
from scripts.config import *

from connection import Connection

def authenticated(func):
    def wrapper():
        if True:
            print("Welcome.")
            func()
        else:
            print("Wrong username or password.")
    return wrapper

def check_authorization(attribute):
    def _check_authorization(f):
        def wrapper(self, *args):
            print(getattr(self, attribute))
            return f(self, *args)
        return wrapper
    return _check_authorization

class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.group = 'admin'
        self.authenticated = False

    def login_self(self):
        
        if self.login_check(self.login, self.password):
            self.authenticated = True
        print(self.login_check(self.login, self.password))

    def logout_self(self):
        self.authenticated = False

    

    @authenticated
    def say_whee(self):
        print("Whee!")  

    # @check_authorization(self.authenticated)
    # def get(self):
    #     print('get')

    # PRODUCT_CATEGORY
    def add_product_category(self, data:dict):
        if self.authenticated:
            return self.insertData('product_category', data)
        else: return "Wrong username or password."

    def get_product_category(self, selector):
        if self.authenticated:
            selector = f"WHERE category_name = '{selector}'"
            return self.getData(('product_category',), ("*",), selector)
        else: return "Wrong username or password."

    def get_product_category_list(self):
        return self.getData(('product_category',),("*",))

    def edit_product_category(self, data:dict, selector):
        selector = f"category_name = '{selector}'"
        return self.updateData('product_category', data, selector)

    def delete_product_category(self, selector):
        selector = f"category_name = '{selector}'"
        return self.deleteData('product_category', selector)

    # COUNTRY
    def add_country(self, data:dict):
        return self.insertData('country', data)

    # PRODUCT
    def add_product(self, data:dict):
        data["country_id"] = self.get_country_id(data["country_id"])
        
        product_category_id = self.getData(("product_category",),("id",),
                    f"""WHERE category_name = '{data["product_category_id"]}'""")
        if len(product_category_id) > 0:
            data["product_category_id"] = product_category_id[0][0]
        else:
           _, id = self.add_product_category({'category_name':data["product_category_id"]})
           data["product_category_id"] = id
        print(data)
        return self.insertData('product', data)

    # MANAGER
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

    admin = Admin('admin', 'admin')
    admin.login_self()
    # admin.logout_self()

    # PRODUCT_CATEGORY
    # data = {
    #     'category_name':'Phones'
    # }
    # print(admin.add_product_category(data))

    print(admin.get_product_category("Phones"))

    # print(admin.get_product_category_list())

    # data = {
    #     'category_name':'Phones'
    # }
    # print(admin.edit_product_category(data, "Books"))

    # print(admin.delete_product_category("Milk"))

    # PRODUCT
    # data = {
    #     "product_name":"Green tea",
    #     "unit_price":"120",
    #     "country_id": "England",
    #     "product_category_id": "Drink"
    # }
    # admin.add_product(data)
    # data = {
    #     "product_name":"Rice",
    #     "unit_price":"120",
    #     "country_id": "China",
    #     "product_category_id": "Porridge"
    # }
    # admin.add_product(data)

    data = {
        "username": "manager1",
        "password": "P@$$w0Rd",
        "first_name": "Bob",
        "last_name": "Robinson",
        "date_of_birth": "1996-08-31",
        "phone": "+380981234567",
        "email": "bob.robinson@gmail.com",
        "street": "Beautiful st. 10",
        "appartaments": "20",
        "zip": "33027",
        "city_id": "Rivne",
        "country_id": "Ukraine"
    }
    # admin.add_manager(data)

    





