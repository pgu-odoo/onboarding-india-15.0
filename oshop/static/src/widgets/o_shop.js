import AbstractAction from 'web.AbstractAction';

const { Component, xml, useRef, useState } = owl;
const { EventBus } = owl.core;

const bus = new EventBus();

// Owl component
class Search extends Component {
    static template = xml /* xml */`
        <div>
            <input id='product_name' style='margin-right: 10px' />
            <button t-on-click="onSearch">Search</button>
        </div>
        `;
    onSearch() {
        var name = document.getElementById('product_name').value;
        // fetch
        this.env.services.rpc({  // find
            route: "/search",
            params: {'name': name},
        })
        .then(response => {
            this.env.bus.trigger('update_list', response);  // name: update_list, handler: response
        })
    }
}

class Items extends Component {
    static template = xml /* xml */`
        <div class="o_item">
            <div>
                <t t-esc="props.item.name"/>
                <span style="float: right">
                    <t t-esc="props.item.price"/>
                </span>
            </div>
            <button t-on-click="addToCart" style="margin-top: 5px;"> Add To Cart </button>
        </div>
        `;
    static props = ['item'];

    addToCart() {
        this.env.services.rpc({
            route: '/add_to_cart',
            params: {'product_id': this.props.item.id},
        })
        .then(response => {
            this.env.bus.trigger('update_cart', response)
        });
    }
}

class ProductList extends Component {
    static template = xml /* xml */`
        <div class="d-flex">
            <t t-foreach="items" t-as="item" t-key="item.id">
                <Items item="item" />
            </t>
        </div>
        `;
    static components = { Items };

    setup(){
        this.items = useState([]);
        this.env.bus.on("update_list", this, (data) => {this.onUpdate(data)});
    }
    onUpdate(data){
        for (var i=0; i < data['products'].length; i++){
            this.items.push(data['products'][i]);
        }
    }
}

class CartItem extends Component {
    static template = xml /* xml */`
        <div class="d-flex">
            <div>
                <span style="padding: 5px;"><t t-esc="props.line.name" /></span>
                <span style="padding: 5px;"><t t-esc="props.line.qty" /></span>
                <span style="padding: 5px;"><t t-esc="props.line.price" /></span>
            </div>
            <button t-on-click="removeFromCart">Remove</button>
        </div>
        `;

    static props = ["line"]

    removeFromCart() {
        this.env.services.rpc({
            route: "/remove_from_cart",
            params: {'product_id': this.props.line.id},
        })
        .then(response => {
            this.env.bus.trigger('update_cart', response);
        });
    }
}