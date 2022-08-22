registry = {};

class Base {
	template = ``
	constructor(parent) {
		this.parent = parent;
	}
	// render method, convert template from string to html format (using DOMparser)  and append it to its parent.
	render() {
		console.log("super render gets called");
		var parser = new DOMParser();  // interface provides the ability to parse XML or HTML source code from a string into a DOM Document 
		var tmpl = parser.parseFromString(this.template, "text/html").body.childNodes;  //`body` -> whole html body, `childNodes` -> separate node NodeList [div]
		this.parent.appendChild(tmpl[0]);
	}
	// on method: update the global dictionary “registry” with key and method as its value
	on(key, method) {
		registry[key] = method;
	}
	// trigger method: call the method whose key is given and pass data as argument
	trigger(key, data) {
		let fn = registry[key];
		console.log("reg", registry);
		console.log("fn: ", fn);
		fn(data);
	}
}

class App extends Base {
	template = `
	<div>
		<div id='top_bar'></div>
		<div id='left_panel' style='float: left;'></div>
		<div id='right_panel' style='float: right;'></div>
	</div>
	`
	async render() {
		console.log("App render gets called");
		await super.render();

		// top_bar
		let top = document.getElementById('top_bar');
		let search = new Search(top);
		search.render();

		// left_panel
		let left = document.getElementById("left_panel");
		let product_list = new ProductList(left);
		product_list.render();

		// right_panel
		let right = document.getElementById("right_panel");
		let cart = new Cart(right);
		cart.render();
	}
}

class Search extends Base {
	template = `
	<div>
		<h2>Search Product</h2>
		<input id='product_name' style='margin-right: 10px'/>
		<button id='search'>Search</button>
	</div>
	`
	// Add a method which will be called when you click on the Search button
	onSearch(){
		console.log("I am searching");
		var name = document.getElementById('product_name').value;
		fetch('/search', {
			method: "POST",
			body: JSON.stringify({'product_name': name}),
			headers: {'Content-Type': 'application/json'},
		})  // fetch only Promise, can't find JSON here
		.then(response => {
			console.log(response);
			return response.json();
		})
		// Trigger update_list, so that product list can render its data
		.then(response => {
			this.trigger('update_list', response)
		})
	}
	render() {
		console.log("search render called");
		super.render();
		document.getElementById('search').addEventListener('click', (e) => {this.onSearch()});
	}
}

class Item extends Base {
	data = []

	addToCart(e){
		fetch('/add_to_cart',{
			method: 'POST',
			headers: {'Content-Type': 'application/json'},
			body: JSON.stringify({'product_id': e.target.id})
		})
		.then(response => {
			console.log("addToCart response: ", response);
			return response.json();
		})
		.then(data => {
			this.trigger('update_cart', data)
		})
	}
	render() {
		let btn = '';
		if (this.data.length > 0){
			this.parent.innerHTML = '';
		}
		for (var i = 0; i < this.data.length; i++) {
			btn = this.data[i].id;
			this.template = `
			<div>
				<div>${this.data[i]['name']}, ${this.data[i]['price']}</div>
				<button id=${btn} style='margin-top: 5px;'>Add to Cart</button>
			</div>
			`
			super.render();

			document.getElementById(btn).addEventListener('click', (e) => {this.addToCart(e)})
		}
	}
}

class ProductList extends Base {
	template = `
	<div>
		<div id='product_list'></div>
	</div>
	`
	products = [];
	constructor (parent) {
		super(parent);
		this.on('update_list', (data) => {this.onUpdate(data)})
	}
	onUpdate(data) {
		this.products = data['products'];
		this.render();
	}
	render() {
		super.render()
		let root_element = document.getElementById("product_list");
		let item = new Item(root_element);
		item.data = this.products;
		item.render()
	}
}

class Cart extends Base {
	order = []
	template = `
	<div>
		<h2>Cart Info</h2>
		<div id='cart_list></div>
	</div>
	`
	constructor(parent) {
		super(parent);
		this.on('update_cart', (data) => {this.onUpdate(data)});
	}

	onUpdate(data) {
		if(data['order_lines']){
			this.order = data['order_lines'];
			this.render();
		}
		if(data['order_detail']) {
			this.order = data['order_detail'];
			this.renderCheckout();
		}
	}
	
	removeFromCart(e) {
		fetch('remove_from_cart', {
			method : 'POST',
			headers: {'Content-Type' : 'application/json'},
			body : JSON.stringify({'product_id': e.target.id})
		})
		.then(response => {
			return response.json();
		})
		.then(data => {
			if (data) {
				this.trigger('update_cart', data)
			}
		});
	}

	checkout() {
		fetch('/checkout', {
			method: 'POST',
			headers : {'Content-Type':'application/json'},
		})
		.then(response => {
			return response.json();
		})
		.then(data => {
			if(data) {
				this.trigger('update_cart', data);
			}
		});
	}
	
	renderCheckout() {
		this.parent.innerHTML = '';
		this.template = `<div></div>`
		super.render();

		for(var i = 0; i < this.order.products.length; i++){
			this.template = `
			<div>
				${this.order['products'][i].name},
				${this.order['products'][i].qty},
				${this.order['products'][i].price}
			</div>`
			super.render();
		}
		this.template = `
		<div>
			<hr>Total : ${this.order['total']}</hr>
		</div>
		`
		super.render();
	}
	

	render() {
		var btn = "";
		if (this.order.length > 0) {
			this.parent.innerHTML = `
			<div>
				<button id='btn_checkout'/>Checkout
			</div>
			`
		}
		for (var i = 0; i < this.order.length; i++) {
			btn = `r_${this.order[i].id}`;
			this.template = `
			<div>
				<div>
					${this.order[i].name},
					${this.order[i].qty},
					${this.order[i].price}
				</div>
				<div>
					<button id=${btn} style='margin-top: 5px;'>Remove</button>
				</div>
			</div>
			`
			super.render();
			document.getElementById(btn).addEventListener('click', (e) => {this.removeFromCart(e)});
			document.getElementById('btn_checkout').addEventListener('click', (e) => {this.checkout(e)});
		}
		if (this.order.length == 0) {
			this.parent.innerHTML = '';
			this.template = `<div></div>`
			super.render()
		}
	}
}


window.onload = function() {
	let root_element = document.getElementById('container');
	let app = new App(root_element)
	app.render();
}