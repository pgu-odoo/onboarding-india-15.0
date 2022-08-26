const {App, useState, xml, mount, Component, EventBus} = owl;
const bus = new EventBus();

// Owl components
// Search is sub component of Root class needs to be mentioned in Parent as a static component to access it
class Search extends Component{
    // const template = document.createElement("template"); ---> class VHtml
    static template = xml /* xml */`
    <div>
        <h2>Search Product </h2>
        <input id="product_name" style="margin-right: 10px"/>
        <button id="search" t-on-click="() => this.onSearch()">Search</button>
    </div>
    `

    // onSearch method
    onSearch() {
        var name = document.getElementById('product_name').value;
        fetch('/search', {
            method: "POST",
            body: JSON.stringify({'product_name': name}),
            headers: {'Content-Type': 'application/json'}
        })
        .then(response => {
            console.log(response);
            // console.log("response json", response.json());
            return response.json();
        })
        .then(response => {
            bus.trigger('update_list', response);  // name: update_list, handler: response
        })
    }
}

// Items component, subclass of ProductList component
class Items extends Component{
    static template = xml /* xml */`
    <div>
        <!-- <h2> check - 3 </h2> -->
        <t t-esc="this.props.thing.name" />
        <t t-esc="this.props.thing.price" />
        <button t-on-click="() => this.addToCart()">Add to Cart </button>
    </div>
    `

    static props = ["thing"];

    addToCart() {
        fetch('/add_to_cart', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'product_id': this.props.thing.id})
        })
        .then(response => {
            return response.json();
        })
        .then(data => {
            bus.trigger('update_cart', data)
        })
    }
}


// ProductList component
class ProductList extends Component{
    static template = xml /* xml */`
    <div>
        <h3>check - 4</h3>
        <t t-foreach="items" t-as="item" t-key="item.id" >
            <Items thing="item"/>  <!-- thing is props for sub-component Items -->
        </t>
    </div>
    `
    static components = { Items }

    setup() {
        this.items = useState([]);
        bus.addEventListener("update_list", (data) => { this.onUpdate(data)});
    }

    onUpdate(data) {
        for (var i=0; i < data['detail']['products'].length; i++){
            this.items.push(data['detail']['products'][i]);
        }
    }
}

// sub-component of cart
class CartItem extends Component {
    static template = xml /* xml */`
    <div>
        <t t-esc="this.props.line.name" />,
        <t t-esc="this.props.line.qty" />,
        <t t-esc="this.props.line.price" />
        <button t-on-click="() => this.removeFromCart()">Remove</button>
    </div>
    `;

    static props = ["line"];

    removeFromCart () {
        fetch('/remove_from_cart', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({'product_id': this.props.line.id})
        })
        .then( response => {
            console.log("removing from cart");
            return response.json();
        })
        .then( data => {
            if (data) {
                bus.trigger('update_cart', data);
            }
        });
    }
}

// Cart component
class Cart extends Component {
    static template = xml /* xml */`
    <t t-if="order_lines.length > 0 ">
        <div><h2>Cart Info:</h2></div>
        <button t-on-click="() => this.checkout()">Checkout</button>
        <t t-foreach="order_lines" t-as="line" t-key="line.id">
            <CartItem line="line" />
        </t>
    </t>

    <t t-if="order_details.length > 0">
        <div><h2>Cart Details</h2></div>
        <t t-foreach="order_details[0].products" t-as="product" t-key="product.id">
            <div>
                <t t-esc="product.name" />,
                <t t-esc="product.qty" />,
                <t t-esc="product.price" />
            </div>
        </t>
        <div>
            <hr>Total: <t t-esc="order_details[0].total"/></hr>
        </div>
    </t>
    `;

    static components = { CartItem };

    setup() {
        this.order_lines = useState([]);
        this.order_details = useState([]);
        bus.addEventListener("update_cart", (data) => {this.onUpdate(data)});
    }

    onUpdate(data) {
        if(data['detail']['order_lines']){
            var length = this.order_lines.length;
            for(var i=0; i <= length; i++){
                this.order_lines.pop();
            }
            for (var i=0; i < data['detail']['order_lines'].length; i++){
                console.log("prder_lines: ", data['detail']);
                this.order_lines.push(data['detail']['order_lines'][i]);
            }
        }
        if (data['detail']['order_detail']){
            this.order_lines = [];
            this.order_details.push(data['detail']['order_detail'])
        }
    }

    checkout() {
        fetch('/checkout', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
        })
        .then( response => {
            return response.json();
        })
        .then(data => {
            bus.trigger('update_cart', data);
        })
    }
}

// Root class
class Root extends Component {
    static template = xml /* xml */`
    <div>
        <div id="top_bar">
            <h1>check - 1 </h1>
            <Search />
        </div>
        <h1>Check - 2</h1>
        <div id="left_panel" style="float: left;">
            <ProductList />
        </div>
        <div id="right_panel" style="float: right;">
            <Cart />
        </div>
    </div>
    `

    static components = { Search, ProductList, Cart }  // sub-components should be defined in parent as static component
}


mount(Root, document.body, { dev : true });