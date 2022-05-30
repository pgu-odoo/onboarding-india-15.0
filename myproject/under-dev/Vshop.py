from multiprocessing.dummy import Array
from attr import fields
from requests import session


class Core:
    __name__= 'core class for all'
    state = list(("New","Draft","In-Progress","Confirmed"))
    def printHello():
        print('hello')


class AddToCartInfo(Core):
    product_id = int()
    session_id = str()
    quantity = int()
    price = float()

class RemoveFromCart(Core):
    product_id = int()
    quantity = int()


class Checkout(Core):
    session_id = str()
    current_order = int()
    

