import psycopg2
from psycopg2 import Error
from scripts.config import *

from connection import Connection


class User(Connection):

    def __init__(self, login, password):
        self.login = login
        self.password = password
        self.group = 'customer'


    def sign_in(self, data:dict):
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
        customer_data = {
            "first_name": data["first_name"],
            "last_name": data["last_name"],
            "city_id": city_id,
            "profile_id": profile_id
        }
        customer = self.insertData('customer',customer_data)
        return customer

    def get_products(self, price = 0, category = 'all'):
        """select p.id, p.product_name, p.unit_price, c.country_name, pc.category_name  from product p
            left join country c on c.id  = p.country_id
            left join product_category pc on pc.id = p.product_category_id;"""
            
        fields = ('p.id', 'p.product_name', 'p.unit_price', 'c.country_name', 'pc.category_name')
        selector = """left join country c on c.id  = p.country_id 
        left join product_category pc on pc.id = p.product_category_id"""
        if price > 0 and category == 'all':
            selector += f" WHERE p.unit_price <= {price}"
        elif price == 0 and category != 'all':
            product_category = self.getData(('product_category',),("id",), f"WHERE category_name = '{category}'")[0][0]
            selector += f" WHERE p.product_category_id = {product_category}"
        elif price > 0 and category != 'all':
            product_category = self.getData(('product_category',),("id",), f"WHERE category_name = '{category}'")[0][0]
            selector += f" WHERE p.unit_price <= {price} AND p.product_category_id = {product_category}"

        
        products = self.getData(('product p',),fields, selector)
        print(products)
        


if __name__ == "__main__":

    user = User('manager1', 'P@$$w0Rd')

    data = {
        "username": "cust1",
        "password": "P@$$w0Rd",
        "first_name": "Petro",
        "last_name": "Cukor",
        "date_of_birth": "1996-08-31",
        "phone": "+380981234567",
        "email": "petro.sweet@gmail.com",
        "street": "Beautiful st. 12",
        "appartaments": "20",
        "zip": "33027",
        "city_id": "Rivne",
        "country_id": "Ukraine"
    }
    # user.sign_in(data)
    # user.get_products(price=100)
    # user.get_products(category='Drink')
    user.get_products(price=120, category='Drink')






    





