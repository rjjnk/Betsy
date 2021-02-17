__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

from models import User, Product, Order
import peewee

def get_user_password(user_name):
    '''finds username and returns user passwords from database'''
    try:
        user = User.get(User.username == user_name)
        return user.password
    except peewee.DoesNotExist:
        return False

def create_user(user_name, user_full_name, user_address, user_bio, user_avatar, user_password):
    '''adds a user to database'''
    try:
        return User.create(
            username=user_name, full_name=user_full_name, address=user_address, bio=user_bio, avatar_url=user_avatar, password=user_password 
        )
    except peewee.PeeweeException:
        return False

def search(term):
    ...


def list_user_products(user_id):
    ...


def list_products_per_tag(tag_id):
    ...


def add_product_to_catalog(user_id, product):
    ...


def update_stock(product_id, new_quantity):
    ...


def purchase_product(product_id, buyer_id, quantity):
    ...


def remove_product(product_id):
    ...