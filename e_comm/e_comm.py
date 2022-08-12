from flask import Flask, redirect, render_template, url_for, request
from product import get_product

e_comm = Flask(__name__)

@e_comm.route('/')
def login():
    return render_template('index.html')

@e_comm.route('/homepage')
def homePage():
    return render_template('/homepage.html')


@e_comm.route('/shop')
def shop():
    products = get_product()
    return render_template('/shop.html', products=products)

@e_comm.route('/cart')
def cart():
    return render_template('/cart.html')

count = 0
@e_comm.route("/plus", methods=["POST"])
def upvote():
    global count
    count = count + 1
    return str(count)

@e_comm.route("/minus", methods=["POST"])
def downvote():
    global count
    if count >= 1:
        count = count - 1
    return str(count)

if __name__ == "__main__":
    e_comm.run(debug=True)
