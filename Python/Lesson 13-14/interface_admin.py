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

    def add_product_category(self, data:list):

        rezults = self.insertData('product_category', data)
        



if __name__ == "__main__":

    admin = Admin('login', 'password')

    data = {
        'category_name':'Milk'
    }





