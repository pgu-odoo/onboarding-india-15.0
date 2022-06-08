/** @odoo-module **/

import AbstractAction from 'web.AbstractAction';

const { Component, tags: { xml },  useRef, useState } = owl;
const { EventBus } = owl.core;
const bus = new EventBus();

class Search extends Component {
    static template = xml/* xml*/`
    <div>
        <input id='p_name' style='margin-right: 10px'/>
        <button t-on-click="on_seach">Search</button>
    </div>`
    on_seach() {
        var name = document.getElementById('p_name').value;
        this.env.services.rpc({
            route: "/search",
            params: {'name': name},
        }).then (response => {   
            this.env.bus.trigger('update_list', response);
        });
    }
}

class CartItem extends Component {
    static template = xml/* xml */`
        <div class="d-flex">
            <div>
                <span style="padding: 5px;"><t t-esc="props.line.name"/></span>
                <span style="padding: 5px;"><t t-esc="props.line.qty"/></span>
                <span style="padding: 5px;"><t t-esc="props.line.price"/></span>
            </div>
            <button t-on-click="remove_from_cart">Remove</button>
        </div>`
    static props = ["line"];

    remove_from_cart () {
        this.env.services.rpc({
            route: "/remove_from_cart",
            params: {'pid': this.props.line.id},
        }).then(response=>{   
            this.env.bus.trigger('update_cart', response);
        }); 
    }
}

class Cart extends Component {
    static template = xml/* xml */`
    <div>
        <div>
            <t t-if="order_lines.length > 0">
                <button t-on-click="checkout">Checkout</button>
                <t t-foreach="order_lines" t-as="line" t-key="line.id">
                    <CartItem line="line"/>
                </t>
            </t>
            <t t-else="">
                <div>Cart is empty!</div>
            </t>
        </div>
        <div>
            <t t-if="order_details.length > 0">
                <h2>Cart Details</h2>
                <t t-foreach="order_details[0].products" t-as="product" t-key="product.id">
                    <div><t t-esc="product.name"/>, <t t-esc="product.qty"/>, <t t-esc="product.price"/></div>
                </t>
                <div><hr>Total : <t t-esc="order_details[0].total"/></hr></div>
            </t>
        </div>
    </div>`

    static components = { CartItem };

    setup() {
        this.order_lines = useState([]);
        this.order_details = useState([]);
        this.env.bus.on("update_cart", this, (data)=>{this.on_update(data)});
    }

    on_update(data) {
        if (data['order_lines']) {
            var length = this.order_lines.length;
            for (var i=0; i <= length; i++) {
                this.order_lines.pop();
            }
            for (var i=0; i < data['order_lines'].length; i++) {
                this.order_lines.push(data['order_lines'][i]);
            }
        }
        if (data['order_detail']) {
            this.order_lines = [];
            this.order_details.push(data['order_detail']);
        }
    }

    checkout() {
        this.env.services.rpc({route: "/checkout",}).then(response=>{   
            this.env.bus.trigger('update_cart', response);
        });
    }
}

class Items extends Component {
    static template = xml/* xml */`
        <div class="o_item">
            <div>
                <t t-esc="props.item.name"/>
                    <span style="float: right"><t t-esc="props.item.price"/></span>
            </div>
            <button t-on-click="add_to_cart" style="margin-top: 5px;">Add to cart</button>
        </div>
    `
    static props = ["item"];

    add_to_cart() {
        this.env.services.rpc({
            route: "/add_to_cart",
            params: {'p_id': this.props.item.id},
        }).then(response=>{   
            this.env.bus.trigger('update_cart', response);
        });
    }

}
class ProductList extends Component {
    static template = xml/* xml */`
        <div class="d-flex">
            <t t-foreach="items" t-as="item" t-key="item.id">
                <Items item="item"/>
            </t>
        </div>
        `
    static components = { Items };

    setup() {
        this.items = useState([]);
        this.env.bus.on("update_list", this, (data) =>{this.on_update(data)});
    }
    on_update(data) {
        for (var i=0; i < data['products'].length; i++) {
            this.items.push(data['products'][i]);
        }
    }
}

class Shop extends Component {
    static template = xml/* xml */`
    <div>
        <div class="o_search_panel">
            <h2>Search Product</h2>
            <Search/>
        </div>
        <div class="o_left_panel">
            <h2>Product List</h2>
            <ProductList/>
        </div>
        <div class="o_right_panel">
            <h2>Cart Info</h2>
            <Cart/>
        </div>
    </div>
    `

    static components = { Search, ProductList, Cart };
}

export const LunchOrderWidget = AbstractAction.extend({
    on_attach_callback() {
        this._super(...arguments);
        if (this.component) {
            return;
        }
        this.component = new Shop();
        return this.component.mount(this.el.firstElementChild);
    }
});


