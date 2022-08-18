import psycopg2
from psycopg2 import Error
from scripts.config import *

from connection import Connection


class Admin(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password

    def login_self(self):
        pass

    def add_product_category(self, data:dict):
        return self.insertData('product_category', data)

    def edit_product_category(self, data:dict, selector):
        selector = f"category_name = '{selector}'"
        return self.updateData('product_category', data, selector)

    def delete_product_category(self, selector):
        selector = f"category_name = '{selector}'"
        return self.deleteData('product_category', selector)
        



if __name__ == "__main__":

    admin = Admin('login', 'password')

    # data = {
    #     'category_name':'Phones'
    # }

    # print(admin.add_product_category(data))

    data = {
        'category_name':'Phones'
    }
    print(admin.edit_product_category(data, "Books"))

    # print(admin.delete_product_category("Milk"))





