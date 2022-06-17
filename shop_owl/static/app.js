const { App, Component, mount, xml, useState, EventBus } = owl;
const bus = new EventBus();
// Owl Components

class Search extends Component{
	static template = xml/* xml */ `
    <div>
    <h2>Search Product</h2>
    <input id='p_name' style='margin-right: 10px'/>
    <button id='search' t-on-click="() => this.on_seach()">Search</button>
    </div>`;

    on_seach(){
		var name = document.getElementById('p_name').value;
        fetch('/search', {
            method: "POST",
            body: JSON.stringify({'p_name': name}),
            headers : {'Content-Type':'application/json'},
        })
        .then(response=>{  
            return response.json(); 
        })
        .then(response=>{   
            bus.trigger('update_list', response);
        });
    }   
}

class Items extends Component{
	static template = xml`
	<div>
		<t t-esc="this.props.item.name"/>, <t t-esc="this.props.item.price"/> <button t-on-click="() => this.add_to_cart()">Add to cart</button>
	</div>`;

	static props = ["item"];

	add_to_cart(){
		fetch('/add_to_cart',{
			method : "POST",
			headers : {'Content-Type':'application/json'},
			body : JSON.stringify({'product_id': this.props.item.id})
		})
		.then(res=>{
			return res.json();
		})
		.then(data=>{
			bus.trigger('update_cart', data)
		});
	}
}

class ProductList extends Component{
	static template = xml`
	<div>
		<h2>Product List</h2>
		<t t-foreach="items" t-as="item" t-key="item.id">
            <Items item="item"/>                
        </t>
	</div>`;
	static components = { Items }
	setup(){
		this.items = useState([]);
		bus.addEventListener("update_list", (data) =>{this.on_update(data)});
	}

	on_update(data){
		for (var i=0; i < data['detail']['products'].length; i++) {
            this.items.push(data['detail']['products'][i]);
        }
	}
}

class CartItem extends Component {
	static template = xml`
		<div>
		<t t-esc="this.props.line.name" />,<t t-esc="this.props.line.qty" />,<t t-esc="this.props.line.price" />
		<button t-on-click="() => this.remove_from_cart()">Remove</button>
		</div>
	`;
	static props = ["line"];

	remove_from_cart(){
		fetch('/remove_from_cart',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
            body : JSON.stringify({'product_id': this.props.line.id})
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            if (data) {
                bus.trigger('update_cart', data);
            }
        });  
	}
}

class Cart extends Component{
	static template = xml`
	<t t-if="order_lines.length > 0">
		<div><h2>Cart Info</h2></div>
		<button t-on-click="() => this.checkout()">Checkout</button>
		<t t-foreach="order_lines" t-as="line" t-key="line.id">
			<CartItem line="line"/>
		</t>
	</t>

	<t t-if="order_details.length > 0">
		<div><h2>Cart Details</h2></div>
		<t t-foreach="order_details[0].products" t-as="product" t-key="product.id">
			<div><t t-esc="product.name"/>,<t t-esc="product.qty" />,<t t-esc="product.price" /></div>
		</t>
		<div><hr>Total : <t t-esc="order_details[0].total"/></hr></div>
	</t>
	`;

	static components = { CartItem };

	setup(){
		this.order_lines = useState([]);
        this.order_details = useState([]);
        bus.addEventListener("update_cart", (data)=>{this.on_update(data)});
	}

	on_update(data){
		if(data['detail']['order_lines']){
			var length = this.order_lines.length;
			for(var i=0; i <= length; i++){
				this.order_lines.pop();
			}
			for(var i=0; i < data['detail']['order_lines'].length; i++){
				this.order_lines.push(data['detail']['order_lines'][i]);
			}
		}
		if(data['detail']['order_detail']){
			this.order_lines = [];
			this.order_details.push(data['detail']['order_detail']);
		}
	}

	checkout(){
		fetch('/checkout',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            if (data) {
                bus.trigger('update_cart', data);
            }
        });
	}
}

class Root extends Component {
  static template = xml`
	<div>
	<div id='topbar'>
  		<Search search="search"/>
	</div>
	<div id='left_panel' style='float: left;'>
		<ProductList productlist="productlist"/>
	</div>
	<div id='right_panel' style='float: right'>
		<Cart cart="cart"/>
	</div>
	</div>`;

  static components = { Search, ProductList, Cart };

}

mount(Root, document.body, { dev : true });
