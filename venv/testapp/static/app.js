
registry = {}

class Base
{
	template = "";
	constructor(parent) {
		this.parent = parent;
	}
	render() {
		var doc = new DOMParser().parseFromString(this.template, 'text/html').body.childNodes;
		this.parent.appendChild(doc[0]);
	}

	on(key, method) {
		registry[key] = method;
	}

	trigger(key, data){
		var func = registry[key];
		func(data);
	}
}

class App extends Base {

	template = "<div><div id='top' align='center'></div><div id='left' align='left'></div><div id='right' align='right'></div></div>"

	render(){
		super.render();

		var p1 = document.getElementById("top");
 		let a1 = new Search(p1);
 		a1.render();

        var p2 = document.getElementById("left");
 		let a2=new ProductList(p2);
		a2.render();

        var p3 = document.getElementById("right");
		let a3 = new Cart(p3);
		a3.render();
	}
} 

class Search extends Base {
	template ="<div><lable>Search</lable><input type='text' id='input'/><br><button id='but'>Submit</button></div>"

	onSearch() {
		var val=document.getElementById('input').value;
		var data={'name': val}
		fetch("/search",
		 {
			 method: 'POST',
			 header: {'Content-Type':'application/json'},
			 datatype: "json",
			 body: JSON.stringify(data)
		})

		.then(response=> {
			return response.json();
		})

		.then(response=> {
			this.trigger('update_list', response);
		})
	}

	render(){
		super.render();
		document.getElementById("but").addEventListener("click",(e)=>{this.onSearch()});
	}
}

class Item extends Base {
	products = [];
	template = "<span id='left'></span>"

	add_to_cart(e){

		fetch("/add", 
		{
			method: 'POST',
			header: {'Content-Type':'application/json'},
			datatype: "json",
			body: JSON.stringify(e.target.id)
			})

		.then(response=> {
			return response.json();
		})

		.then(response=> {
			this.trigger('update_cart_list', response);
		})	
	}

	render() {
		if (this.products.product)
		{
			for(let i =0; i<this.products.product.length; i++){
				var add=this.products.product[i]['id'];
				this.template = `<div> ${this.products.product[i]['id']} ${this.products.product[i]['name']} ${this.products.product[i]['price']} 
								<button type='button' id= ${add} >Add to Cart</button></div>`;
				super.render();	
				document.getElementById(add).addEventListener("click",(e)=> {this.add_to_cart(e)});
			}
		}
	}
}

class ProductList extends Base {
	template = "<div><div id='product_list'></div></div>";
	products = [];

	constructor(parent) {
		super(parent);
		this.on('update_list', (data)=>this.update_items(data));
	}

	update_items(data) {
		this.products = data;
		this.render();
	}

	render() {
		super.render();
		var p3 = document.getElementById("product_list");
		let i = new Item(p3);
		i.products = this.products;
		i.render();	
	}

}

class Cart extends Base {

	orders=[]
	template = "<div><div id='checkout'></div><div id='cart'></div></div>";


	constructor(parent) {
		super(parent);
		this.on('update_cart_list', (data)=>this.update_cart_items(data));
	}

	update_cart_items(data) {
		this.orders = data;
		this.render();
	}

	render() {
		super.render();

		if (this.orders.order) {
			var ch = document.getElementById("checkout");
			ch.innerHTML ='';
			var ch_template = "<div><button type= 'button' id ='check'>Checkout</button></div>" 
			var doc = new DOMParser().parseFromString(ch_template, 'text/html').body.childNodes;
			ch.appendChild(doc[0]);
		}
		if (this.orders.Total) {
			var ch = document.getElementById("checkout");
			ch.innerHTML ='';
			var ch1 = document.getElementById("cart");
			ch1.innerHTML='';
			var ch_template = `<div>Total : ${this.orders.Total}</div>` 
			var doc = new DOMParser().parseFromString(ch_template, 'text/html').body.childNodes;
			ch.appendChild(doc[0]);
		}

		var p3 = document.getElementById("cart");
		let i = new CartItem(p3);
		i.orders = this.orders;	
		i.render();	
	}
}

class CartItem extends Base{
	orders = [];
	template = "<div><span id='right'></span></div>";

	remove_t(e){

		fetch("/remove",
		{
			method : 'POST',
			header :{'Content-Type': 'application/json'},
			datatype: "json",
			body : JSON.stringify(e.target.id)
		})

		.then(response=> {
			return response.json();
		})

		.then(response=> {
			this.trigger('update_cart_list', response);
		})
	
	}

	check_out(){

		fetch("/checkout",
		{
			method : 'POST',
			header :{'Content-Type': 'application/json'},
			datatype: "json",
		})

		.then(response=> {
			return response.json();
		})

		.then(response=> {
			this.trigger('update_cart_list', response);
		})

	}

	render() {
		if (this.orders.order && this.orders.order.length > 0) {
			this.parent.innerHTML = '';
		}
		if (this.orders.order)
		{
			for(let i =0; i<this.orders.order.length; i++){
				var product_id = 'btn_' + this.orders.order[i]['product_id']
				this.template = `<div> ${this.orders.order[i]['quantity']} ${this.orders.order[i]['name']} ${this.orders.order[i]['price']} 
								<button type='button' id= ${product_id} >Remove</button></div>`;
				super.render();	
				document.getElementById(product_id).addEventListener("click",(e)=>{this.remove_t(e)});
				document.getElementById("check").addEventListener("click",(e)=>{this.check_out()});


			}
		}
	}

}
			
window.onload = function () {
	var parent =  document.getElementById("container");
	let a = new App(parent);
	a.render();
}