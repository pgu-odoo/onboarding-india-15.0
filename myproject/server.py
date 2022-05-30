
from calendar import c
from datetime import date
import datetime
import json
from signal import valid_signals
from tokenize import String
import uuid
from flask import send_from_directory
from logging import raiseExceptions
import os, random, string
from flask import Flask, Request, make_response
from flask import render_template , session, request, redirect, url_for
import requests



products = [{'id': '1001', 'name': 'shirt black', 'price': 699},
{'id': '1008', 'name': 'jeans', 'price': 1899},
{'id': '1002', 'name': 'jacket', 'price': 4300},
{'id': '1003', 'name': 'shoes', 'price': 799},
{'id': '1004', 'name': 'hat', 'price': 399},
{'id': '1005', 'name': 'pajamas', 'price': 499},
{'id': '1006', 'name': 'shirt red', 'price': 699},
{'id': '1007', 'name': 'shirt white', 'price': 699},
]

sessions = [{'id':'ba'},{'id':'bb'},{'id':'bc'},{'id':'bd'}]

orders =[{'id':'1','date':'05-05-2022','session_id':'ba','product_id':'1001','state':'draft'},
{'id':'2' ,'session_id': 'ba', 'date':'09/09/22' ,'product_id':'1002','state':'draft'},
{'id':'3' ,'session_id': 'bc', 'date':'09/09/22' ,'product_id':'1003', 'state':'draft'},
{'id':'4' ,'session_id': 'bd', 'date':'09/09/22' ,'product_id':'1004', 'state':'draft'},
{'id':'5' ,'session_id': 'be', 'date':'09/09/22' ,'product_id':'1005', 'state':'draft'}]

order_details = [
{'order_id':'1', 'product_id': '1001','qty': 5,'price':1000,'session_id':'ba'},
{'order_id':'2', 'product_id':'1004', 'qty': 5,'price':170,'session_id':'bb'},
{'order_id':'3', 'product_id':'1004', 'qty': 5,'price':140,'session_id':'bf'},
{'order_id':'3', 'product_id':'1004', 'qty': 5,'price':10,'session_id':'bf'},
{'order_id':'4', 'product_id':'1004', 'qty': 5,'price':104,'session_id':'bd'},
{'order_id':'4', 'product_id':'1002','qty': 5,'price':1440,'session_id':'bd'},
{'order_id':'4', 'product_id':'1003','qty': 5,'price':410,'session_id':'bc'}]

test = [{}]
def get_current_order():
    for order in orders:
        if order.get('session_id') == request.cookies.get('id') and order.get('state') == 'draft':
            return order

app = Flask(__name__)
session_valid = False

def check_authentictaion(session_id):
    for session in sessions:
        if session_id == session['id'] :
            return (True)
        else:
            return(False)
            exit()

def authenticate(session_id):
    if session_id not in sessions:
        # here we can make user to login to our site and then will add their session id to cookie
        vals ={
        'id':session_id }
        sessions.append(vals)
        return(True)
    else:
        return(True)

def is_valid_session():
    if (session[id] == request.cookies.get('id') for session in sessions): 
        return True

def get_current_order():
    for order in orders:
        if orders.get('session_id') == request.cookies.get('id') and order.get('state') == 'draft':
            return order

def get_order_details(order, product_id):
    for line in order_details:
        if line.get('order_id') == order.get('id') or line.get('product_id') == product_id:
            return line

def get_product(pid):
    for product in products:
        if int(pid) == product.get('id'):
            return product

def add_order_detail(order, product, qty):
    vals = {
        'order_id': order.get('id'),
        'product_id': product['id'],
        'price': (int(qty) * product['price']),
        'qty': int(qty),
    }

    order_details.append(vals)
def get_new_order_id():
    app.config['order_id'] += 1
    return app.config['order_id']

def add_order():
    order_id = get_new_order_id()
    vals = {
        'id': order_id,
        'session_id': request.cookies.get('id'),
        'state': "draft",
        'date': str(datetime.datetime.now())
    }
    orders.append(vals)
    return vals
# @app.route('/static/<path:path>')
# def send_report(path):
#     return send_from_directory('static', path)

@app.route("/")
def home():
    session_id = request.cookies.get('session_id')
    resp = make_response(render_template("index.html"))
    if not session_id:
        random_key = str(uuid.uuid4())
        vals = {
            'id': random_key,
        }
        session_id = vals
        resp.set_cookie('session_id', random_key)
        sessions.append(vals)
    return resp



@app.route("/search", methods = ['POST'])
def product_search():
    session_id = request.cookies.get('session_id')
    auth = authenticate(session_id)
    if auth == False:
        exit()

    res = []
    for product in products:
        if request.json.get('product_name').lower() in product['name'].lower():
            res.append(product)
    if not res:
        res = "Sorry this product is unavailaible!!"    
    return {'result': res}

@app.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
   
    qty = 1
    p_id = int(request.get_json().get('product_id'))
    product_price = request.json.get("price")
    product = get_product(p_id)
    order = get_current_order()
    if order:
        details = get_order_details(order, product['id'])
        if details:
            details['qty'] += qty
            details['price'] += (qty * product['price'])
        else:
            add_order_detail(order, product, qty)
    else:
        order = add_order()
        add_order_detail(order, product, qty)
    return {'order': get_order_details(order)}



# @app.route("/add_to_cart", methods = ['POST'])
# def add_to_cart():
#     session_id = request.cookies.get('session_id')
#     auth = check_authentictaion(session_id)

    
#     user_id= "bd"
#     product_id =request.json.get('product_id')
#     quantity = 1
#     product_price = request.json.get("price")


#     match = False
#     valid_session = False
#     for session in sessions:
#         if (user_id != session['id']):
#             random_key = ''.join(random.choices(string.ascii_letters+string.digits,k=16))  
#             vals = random_key
#             break
#         else:
#             vals= user_id
        
#     new_key = vals
#     # import pdb 
#     # pdb.set_trace()
#     res=[]
#     count = (len(orders)+1)
#     for session in sessions:
#         if user_id == session['id']:
#             match = True
#             break
#         else:
#             vals={"id":count,
#             "session_id":user_id,
#             "product_id":product_id,
#             "date":(datetime.datetime.now()),
#             "state":'draft'
#             }
#             break
#     orders.append(vals)

#     if match:
#         valid_session = True
#     else:
#         vals = new_key
#         sessions.append(vals)
#         valid_session = True

#     if valid_session:
#         order = {
#             'id': count,
#             'date':(datetime.datetime.now()),
#             'session_id':new_key,
#             'product_id': product_id,
#             'state':'draft'
#         }
#         value =[]
#         for product in products:
#             if (product['id'] == product_id):
#                     product_price = product['price']  #check this line
#                     order_detail = {
#                     'order_id':len(orders),
#                     'product_id':product_id,
#                     'qty': quantity,
#                     'price':product_price,
#                     'session_id':user_id
#                     }
#                     orders.append(order)
#                     value.append(order_detail)
#                     order_details.append(order_detail)
#         # vals ={ "product_id":order_details[len(order_details)-1]['product_id'],"quantity":order_details[len(order_details)-1]['qty'],"price":order_details[len(order_details)-1]['price']}

#         return {'order':value}

@app.route("/remove_from_cart", methods = ['POST'])
def remove_item():
    # import pdb
    # pdb.set_trace()
    session_id = request.cookies.get('session_id')
    auth = check_authentictaion(session_id)
    product_name= request.json.get('product_name')
    user_id = 'bd'
    # user_id = session_id

    for p in products:
        if p['name'] == product_name:
            product_id = p['id']
            break

    for p in products:
        if (p['name'] == product_name ):
            product_id = p['id']
    for order in orders:
        if(user_id == order['session_id']):    
            for detail in order_details:
                if detail['order_id'] == order['id'] and detail['product_id'] == product_id:
                    order = orders.remove(order)
    return {'orders': order_details}

@app.route("/checkout", methods = ['POST'])
def checkout():
    session_id = request.cookies.get('session_id')
    if (check_authentictaion(session_id) == False):
        print("you are not the correct user")


    for order in orders:
        if order['session_id'] == request.json.get('user_id'):
            current_order = order
    product_list = []
    total_amount = 0.0
    for detail in order_details:
        if detail['order_id'] == current_order['id']:
            total_amount += detail['price']
            for p in products:
                if p['id'] == detail['product_id']:
                    detail['name'] = p['name']
            product_list.append(detail)
                
    order_detail = {
        'products': product_list,
        'total_amount': total_amount,
    }   
    return order_detail
     
if __name__ == '__main__':
        app.run(debug=True,port=9013)