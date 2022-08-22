from crypt import methods
import datetime
from readline import get_current_history_length
import uuid
import flask
from flask import Flask, render_template, request


odoo_shop = Flask(__name__)
odoo_shop.config['order_id'] = 1

# JSON data
sessions = [
    {'id': '1'}
]

products = [
    {'id': 1, 'name':"Chair", 'price': 100},
    {'id': 2, 'name':"Table", 'price': 500},
    {'id': 3, 'name':"Bed", 'price': 1000},
    {'id': 4, 'name':"Side Table", 'price': 700},
    {'id': 5, 'name':"Reck", 'price': 450},
]

orders = [
    {
        'id': 1,
        'session_id': 'session_1',
        'state': "draft",
        'date': "2022-05-06 13:59:42.706483",
    }
]

order_lines = [
    {'order_id': 1, 'product_id': 1, 'qty': 1, 'price': 100},
    {'order_id': 1, 'product_id': 2, 'qty': 1, 'price': 500},
]

def is_valid_session():
    if (session['id'] == request.cookies.get('id') for session in sessions):
        return True


@odoo_shop.route('/')
def index():
    if not request.cookies.get('id'):
        res = ""
        vals = {
            'id': str(uuid.uuid4())
        }
        res = flask.make_response()
        res.set_cookie("id", str(uuid.uuid4()))
        sessions.append(vals)
        return render_template('index.html')

@odoo_shop.route('/search', methods=['GET', 'POST'])
def search_product():
    res = "Invalid Session"
    name = request.get_json().get('product_name')  # request: <Request 'http://127.0.0.1:5001/search' [POST]>
    print("name ==> ", name)
    product_list = []
    if is_valid_session():  # this will return True
        for product in products:
            if name.lower() in (product['name'].lower()):
                product_list.append(product)
        return {'products': product_list}
    return res

def get_product(product_id):
    for product in products:
        if int(product_id) == product.get('id'):
            return product

def get_current_order():
    for order in orders:
        if order.get('session_id') == request.cookies.get('id') and order.get('state') == 'draft':
            return order

def get_order_line(order, product_id):
    for line in order_lines:
        if line.get('order_id') == order.get('id') and line.get('product_id') == product_id:
            return line

def get_order_lines(order):
    product_list = []
    print("order_lines: ", order_lines)
    for line in order_lines:
        # print("order.get('id') ----- ", order.get('id'))
        if line['order_id'] == order.get('id'):
            p_name = get_product(line['product_id'])
            vals = {
                'name': p_name['name'],
                'qty': line['qty'],
                'price': line['price'],
                'id': line['product_id']
            }
            product_list.append(vals)
    return product_list

def add_order_line(order, product, qty):
    vals = {
        'order_id': order.get('id'),
        'product_id': product['id'],
        'price': (int(qty) * product['price']),
        'qty': int(qty),
    }
    order_lines.append(vals)

def get_new_order_id():
    odoo_shop.config['order_id'] += 1
    return odoo_shop.config['order_id']

def add_order():
    order_id = get_new_order_id()
    vals = {
        'id': order_id,
        'session_id': request.cookies.get('id'),
        'state': 'draft',
        'date': str(datetime.datetime.now())
    }
    orders.append(vals)
    return vals

@odoo_shop.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
    if is_valid_session():
        qty = 1
        product_id = int(request.get_json().get('product_id'))
        product = get_product(product_id)
        print("product_id: ", product_id)
        order = get_current_order()
        print("add_to_cart, order: ", order)
        if order:
            line = get_order_line(order, product['id'])
            print("line :", line)
            if line:
                line['qty'] += qty
                line['price'] += (qty * product['price'])
            else:
                add_order_line(order, product, qty)
        else:
            order = add_order()
            add_order_line(order, product, qty)
    return {'order_lines': get_order_lines(order or order_id)}


@odoo_shop.route('/remove_from_cart', methods=['GET', 'POST'])
def remove_from_cart():
    if is_valid_session():
        product_id = int(request.get_json().get('product_id').split('_')[1])
        order = get_current_order()
        if order:
            line = get_order_line(order, product_id)
            if line:
                order_lines.remove(line)
                if not order_lines:
                    orders.remove(order)
        return {'order_lines': get_order_lines(order)}
    return 'order not found'


def get_lines_total(lines):
    return sum(line.get('price') for line in lines)

def set_order_done(order):
    if order.get('state') == 'draft':
        order['state'] = 'done'
    return True

@odoo_shop.route('/checkout', methods=['GET', 'POST'])
def checkout():
    res = "Not valid session X"
    if is_valid_session():
        print("inside route checkout")
        order = get_current_order()
        if order:
            order_lines = get_order_lines(order)
            vals = {
                'products': order_lines,
                'total': get_lines_total(order_lines)
            }
            set_order_done(order)
            res = {'order_detail': vals}
    return res


if __name__ == '__main__':
    odoo_shop.run(debug=True)



"""
    request: <Request 'http://127.0.0.1:5001/search' [POST]>
    request.get_json() : will grab JSON, {'product_name': '<input>'}, refer onSearch() method in `app.js`
"""