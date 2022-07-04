from flask import Flask, render_template, request
import uuid
import flask
import datetime

app = Flask(__name__)
app.config['order_id']=1


products = [
    {'id': 1, 'name':"Mobile Cover", 'price': 200},
    {'id': 2, 'name':"Table", 'price': 500},
    {'id': 3, 'name':"Desk", 'price': 3000},
    {'id': 4, 'name':"Battle Sword", 'price': 13700},
    {'id': 5, 'name':"Bat", 'price': 2800},
]

orders = [
    {'id': 1, 'state': "draft", 'date': "27-06-2022"},
]

order_details = [{'order_id': 1, 'product_id': 1, 'qty': 5, 'price':1000}]

session = [{'id': 'session_1'},]


def is_valid_session():
	if (sess[id] == request.cookies.get('id') for sess in session):
		return True
    
def get_product(pid):
    for product in products:
        if int(pid) == product.get('id'):
            return product


def get_current_order():
    for order in orders:
        if order.get('state') == 'draft':
            return order


def get_order_detail(order, product_id):
    for detail in order_details:
        if detail.get('order_id') == order.get('id') and detail.get('product_id') == product_id:
            return detail

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
        'state': "draft",
        'date': str(datetime.datetime.now())
    }
    orders.append(vals)
    return vals

def get_order_details(order):
    product_list = []
    for detail in order_details:
        if detail['order_id'] == order.get('id'):
            p_name = get_product(detail['product_id'])
            vals = {
                'name': p_name['name'],
                'qty': detail['qty'],
                'price': detail['price'],
                'id': detail['product_id']
            }
            product_list.append(vals)
    return product_list

def get_order_total(order_detail):
    return sum(x.get('price') for x in order_detail)

def set_order_done(order):
    if order.get('state') == 'draft':
        order['state'] = 'done'
    return True

@app.route('/')
def index():
	result=""
	if not request.cookies.get('id'):
		vals={
			'id':str(uuid.uuid4())
		}
		result=flask.make_response()
		result.set_cookie("id",str(uuid.uuid4()))
		session.append(vals)

	return render_template('index.html')


@app.route('/search',methods=['GET','POST'])
def search_product():
	p_name = request.get_json().get('p_name')
	product=[]
	res="Invalid Session"
	result="Not Found"
	if is_valid_session():
		for x  in products:
			if p_name.lower() in (x['name'].lower()):
				product.append(x)
				result = {'Found':product}
		return result
	return  res


@app.route('/add_to_cart',methods=['GET','POST'])
def add_to_cart():
	qty=1
	product_id=int(request.get_json().get('product_id'))
	product=get_product(product_id)
	order=get_current_order()
	if order:
		detail=get_order_detail(order,product['id'])
		if detail:
			detail['qty'] += qty
			detail['price'] += (qty*product['price'])
		else:
			add_order_detail(order,product,qty)
	else:
		order=add_order()
		add_order_detail(order,product,qty)
	return {'order_details':get_order_details(order)}
	


@app.route('/remove_from_cart', methods=['GET','POST'])
def remove_from_cart()	:
	if is_valid_session():
		pid=int(request.get_json().get('product_id').split('_')[1])
		order=get_current_order()
		if order:
			order_detail=get_order_detail(order,pid)
			if order_detail:
				order_details.remove(order_detail)
				if not order_details:
					orders.remove(order)
		return {'order_details':get_order_details(order)}
	return 'Order not Found'



@app.route('/checkout', methods=['GET','POST'])
def checkout():
	res="Invalid Session"
	if is_valid_session():
		order=get_current_order()
		if order:
			order_details=get_order_details(order)
			vals={
				'products':order_details,
				'total':get_order_total(order_details)
			}
			set_order_done(order)
			res={'order_detail':vals}
	return res


