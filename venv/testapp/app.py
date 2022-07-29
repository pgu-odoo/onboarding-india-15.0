import uuid
from flask import Flask,make_response, render_template,request
import json

app=Flask(__name__)

products = [
            {'id':1, 'name':'Table', 'price':100 }, 
            {'id':2, 'name':'Chair', 'price':99},
            {'id':3, 'name':'Clock', 'price':129},
            {'id':4, 'name':'Desk', 'price':199},
            {'id':5, 'name':'Bed', 'price':999},
            {'id':6, 'name':'Laptop', 'price':19999},
            {'id':7, 'name':'Bottle', 'price':139},
            {'id':8, 'name':'Mobile', 'price':799}
            ]

orders = []
qty=1


"""order_lines = [{'id': 1, 'order_id': 1, 'product_id': 5, 'qty': 2},
				{'id': 2, 'order_id': 2, 'product_id': 3, 'qty': 2} 
			]"""
order_lines=[]

@app.route("/")
def index():
	resp = make_response()
	resp.set_cookie('name','cookie')
	return render_template("index.html")

@app.route("/search", methods=["GET","POST"])
def search():
	data = []
	product_name = json.loads(request.data).get('name')
	p = next(data.append(x) for x in products if x['name'] == product_name)
	return {'product': data }

def get_product(product_id):
	for q in order_lines:
		if q['product_id']==product_id:
			q['quantity']+=1
			return True
	return False

@app.route("/add", methods=["GET","POST"])
def add_to_cart():

	product_id = int(json.loads(request.data))
	line = {}
	order_id = False

	for p in products:
		if p['id'] == product_id:
			item = p

	line['id']=uuid.uuid4()
	line['quantity']=qty
	line['product_id']= item['id']
	line['order_id']= 2
	line['name']= item['name']
	line['price']=item['price']

	for i in orders:
		if i['state']=='draft':
			order_id=i['id']
	if order_id:
		if not get_product(product_id):
			order_lines.append(line)
	else:
		new_order={}
		new_order['id']=2
		new_order['date']='22/07/2020'
		new_order['state']='draft'
		orders.append(new_order)
		order_lines.append(line)

	return {'order':order_lines}

@app.route("/remove", methods=["GET","POST"])
def remove_from_cart():
	import pdb
	pdb.set_trace()
	product_id = json.loads(request.data)
	product_id=int(product_id.split('_')[1])
	
	for  i in order_lines:
		if i['product_id']==product_id:
			if i['quantity']>1:
				i['quantity']-=1
			else:
				return {'order':" "}
		
		return {'order':order_lines}

@app.route("/checkout", methods=["GET","POST"])
def checkout():
	total_price=0

	for i in order_lines:
		number=i.get('quantity')
		product_id=i.get('product_id')
		for i in products:
			if i['id']==product_id:
				checkout_price = i['price']
				price = number*checkout_price
				total_price=total_price+price

	#total_price=number*checkout_price

	return {'Total': total_price}

if __name__=='__main__':
	app.run()

