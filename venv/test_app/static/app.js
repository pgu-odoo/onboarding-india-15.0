
const { Component, mount, xml, useRef, EventBus, useState} = owl;
const bus=new EventBus();


class Cart extends Component{

	static template = xml`
						<div>
							<div id="ProductList">
								<button t-on-click="()=>check_out()">Checkout</button><br/>
								<t t-foreach="this.orders" t-as="order" t-key="order.product_id">
									<div><t t-esc="order['name']"/>
										<t t-esc="order['price']"/>
										<t t-esc="order['quantity']"/>
										<button t-on-click="()=>remove_to_cart(order)">Remove</button><br/>
									</div>
								</t>
							</div>							
						</div>`
	
	setup(){
		bus.addEventListener("update_cart", (data)=>this.update_cart(data));
		this.orders = useState([]);
	}

	update_cart(data){
		let order_length = data.detail.order.length;
		for (let i=0; i<= this.orders.length; i++) {
			this.orders.pop();
		}
	
		for (let i=0; i<order_length; i++) {
			// this.orders.pop();
			this.orders.push(data['detail']['order'][i]);
		}
	}

		remove_to_cart(order){
			debugger;
			let val=order.product_id;
			fetch("/remove",
			{
				method : 'POST',
				header :{'Content-Type': 'application/json'},
				datatype: "json",
				body : JSON.stringify(val)
			})

			.then(response=> {
				return response.json();
			})

			.then(response=> {
				bus.trigger('update_cart', response);
			})
		}

	// static components = { CartItem };

}

class ProductItem extends Component{

	static template = xml`
						<div>
							<t t-esc="this.props.item.id"/>
							<t t-esc="this.props.item.name"/>
							<t t-esc="this.props.item.price"/>
	 						<button t-on-click="() => add_to_cart(props.item)">Add to Cart</button>
						</div>`


	static props = ['item']

	add_to_cart(item){
		
		let val = item.id;
		fetch("/add", 
		{
			method: 'POST',
			header: {'Content-Type':'application/json'},
			datatype: "json",
			body: JSON.stringify(val)
			})

		.then(response=> {
			return response.json();
		})
		.then(response=> {
			bus.trigger('update_cart', response);
		debugger;

		})	
	}

} 

class ProductList extends Component{

	static template = xml`
						<div>
							<div id="ProductList">
								<t t-foreach="products" t-as="product" t-key="product.id">
									<ProductItem item="product"/>
								</t>

							</div>
						</div>`
	setup(){
		bus.addEventListener("update_list", (data)=>this.update_items(data));
		this.products = useState([]);
	}

	update_items(data){
		this.products.push(data['detail']['product'][0]);
	}


	static components = { ProductItem };

}

class Search extends Component{
	static template = xml`
					<div>
    					<input placeholder="Search Products" id="input"/>
 						<button t-on-click="onSearch">Submit</button>
					</div>`
	
	onSearch() {

		var val=document.getElementById("input").value;
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
			bus.trigger('update_list', response);
		})
	}
}

class App extends Component{

	static template = xml` 
				<div class ="app"> 
					<div id='top' align='center'><Search/></div>
					<div id='left' align='left'><ProductList/></div>
					<div id='right' align='right'><Cart/></div>
				</div>`

	static components = { Search, ProductList, Cart };

}

mount(App, document.body, { dev : true });
