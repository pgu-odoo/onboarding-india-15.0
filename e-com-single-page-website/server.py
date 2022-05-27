import flask
import datetime
import uuid
from flask import Flask, render_template
from flask import request

app = Flask(__name__)
app.config['order_id'] = 1

products = [
    {'id': 1, 'name':"Shirt Black", 'price': 600},
    {'id': 2, 'name':"Jeans", 'price': 500},
    {'id': 3, 'name':"Jacket", 'price': 1000},
    {'id': 4, 'name':"Shoes", 'price': 700},
    {'id': 5, 'name':"Shirt White", 'price': 450},
]

orders = [
    {'id': 1, 'session_id': 'session_1', 'state': "draft", 'date': "2022-05-06 13:59:42.706483"},
]

order_lines = [
    {'order_id': 1, 'product_id': 1, 'qty': 1, 'price': 600},
    {'order_id': 1, 'product_id': 2, 'qty': 1, 'price': 500},
]

sessions = [
    {'id': 'session_1'},
]

def is_valid_session():
    if (session[id] == request.cookies.get('id') for session in sessions): 
        return True

def get_current_order():
    for order in orders:
        if order.get('session_id') == request.cookies.get('id') and order.get('state') == 'draft':
            return order

def get_order_line(order, product_id):
    for line in order_lines:
        if line.get('order_id') == order.get('id') and line.get('product_id') == product_id:
            return line

def get_product_by_name(name):
    for product in products:
        if name.lower() == product['name'].lower():
            return product

def get_product(pid):
    for product in products:
        if int(pid) == product.get('id'):
            return product

def add_order_line(order, product, qty):
    vals = {
        'order_id': order.get('id'),
        'product_id': product['id'],
        'price': (int(qty) * product['price']),
        'qty': int(qty),
    }
    order_lines.append(vals)

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

def get_order_lines(order):
    product_list = []
    for line in order_lines:
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

def get_lines_total(lines):
    return sum(l.get('price') for l in lines)

def set_order_done(order):
    if order.get('state') == 'draft':
        order['state'] = 'done'
    return True

@app.route('/')
def index():
    res = ""
    if not request.cookies.get('id'):
        vals = {
            'id': str(uuid.uuid4())
        }
        res = flask.make_response()
        res.set_cookie("id", str(uuid.uuid4()))
        sessions.append(vals)
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search_product():
    res = 'Invalid Session'
    name = request.get_json().get('p_name')
    product_list = []
    if is_valid_session():
        for product in products:
            if name.lower() in (product['name'].lower()):
                product_list.append(product)
        return {'products': product_list}
    return res

@app.route('/add_to_cart', methods=['GET', 'POST'])
def add_to_cart():
    if is_valid_session():
        qty = 1
        p_id = int(request.get_json().get('product_id'))
        product = get_product(p_id)
        order = get_current_order()
        if order:
            line = get_order_line(order, product['id'])
            if line:
                line['qty'] += qty
                line['price'] += (qty * product['price'])
            else:
                add_order_line(order, product, qty)
        else:
            order = add_order()
            add_order_line(order, product, qty)
    return {'order_lines': get_order_lines(order)}

@app.route('/remove_from_cart', methods=['GET', 'POST'])
def remove_from_cart():
    if is_valid_session():
        pid = int(request.get_json().get('product_id'))
        order = get_current_order()
        if order:
            line = get_order_line(order, pid)
            if line:
                order_lines.remove(line)
                if not order_lines:
                    orders.remove(order)
        return {'order_lines': get_order_lines(order)}
    return 'Order not found'


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    res = "Not valid session"
    if is_valid_session():
        order = get_current_order()
        if order:
            order_lines = get_order_lines(order)
            vals = {
                'products': order_lines,
                'total': get_lines_total(order_lines)
            }
            set_order_done(order)
        return{'products': order_lines}
    # return {'order_detail': order_lines,
    #         'total':get_lines_total(order_lines)}

if __name__ == '__main__':
        app.run(debug=True,port=9015)