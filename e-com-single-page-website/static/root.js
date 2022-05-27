const { Component, mount, xml, useRef, onMounted, useState, reactive, useEnv } = (owl); 

(function() {
    function useStore() {
        const env = useEnv();
        return useState(env.store);
    }
    function StoreData() {
        return reactive(new DataList());
    } 

    class DataList  {
        
        data = [];
        items=[];
        remains=[];
        clear(array) {
            while (array.length) {
              array.pop();
            }
          }

        addData(Json_response) {
            this.clear(this.data);
            Json_response.products.forEach(product => {
                if (this.data.findIndex(datum => datum.id === product.id)) {
                    this.data.push(product);
                }
            });
             
            console.log(Json_response);
            
        }

        addItemToCart(Json_response) {
            this.clear(this.items);
             
            Json_response.order_lines.forEach(item => {
                if (this.items.findIndex(datum => datum.name === item.name)) {
                    this.items.push(item);
                }
            });
            console.log(Json_response);
        }

        removeItem(Json_response){
            this.clear(this.items);
            Json_response.order_lines.forEach(item => {
                if (this.items.findIndex(datum => datum.name === item.name)) {
                    this.items.pop(item);
                }
            });
            console.log(Json_response);            
        }

        remainingItem(Json_response){
            debugger;
            this.clear(this.items);
            Json_response.products.forEach(item => {
                if (this.remains.findIndex(datum => datum.name === item.name)) {
                    this.remains.push(item);
                }
            });
            console.log(Json_response);
        }
        
    }

    class Cart extends Component
    {
        static template = xml/*xml*/`
        <div id="Cart">
            <t t-set="total" t-value="0"/>
            <div class="Items">
                <t t-if="store.items.length">
                <div>Cart Info</div>
                <div><button t-on-click="Checkout">Checkout</button></div>
                    <t t-foreach="store.items" t-as="item" t-key="item.name">
                        <div>
                        <t t-esc="item.name"/><t t-esc="item.price"/><t t-esc="item.qty"/><button t-att-id='item.id' t-on-click= "remove_from_cart" t-ref="remove-from-cart">Remove</button>
                        </div>
                    </t>
                </t>
            </div>
        </div>
        <div id="check">
            <div class="checkout">
                <t t-if="store.remains.length">
                    <div>
                        <t t-foreach="store.remains" t-as="item" t-key="item.name">
                            <div>
                            <t t-esc="item.name"/><t t-esc="item.price"/><t t-esc="item.qty"/>
                            </div>
                            <t t-set="total" t-value="total+item.price"/>
                        </t>
                        <div>
                        <hr>   Total = <t t-esc="total"/> </hr>
                        </div>
                    </div>
                </t>
            </div>
        </div>`;

        setup()
        {
            this.store = useStore();      
        }

        remove_from_cart(e) 
        {
            fetch('/remove_from_cart',{
                method:'POST',
                headers : {'Content-Type':'application/json'},
                body : JSON.stringify({'product_id': e.target.id})
            }).then(res=>{
                return res.json();
            }).then(Json_response=>{
                this.store.removeItem(Json_response);
            }); 
        }

        Checkout() 
        {
            fetch('/checkout',{
                method:'POST',
                headers : {'Content-Type':'application/json'},
            }).then(res=>{
                return res.json();
            }).then(Json_response=>{
                this.store.remainingItem(Json_response);
            });
            console.log(Json_response);
        }
}

    class ProductList extends Component {  
        product = [];
        static template = xml/*xml*/`
            <div id="ProductList">Product Info
                <div class= "product">
                    <!-- <t t-debug="1"/> -->
                    <t t-if="store.data.length">
                        <t t-foreach="store.data" t-as="product" t-key="product.id">
                            <div>
                            <t t-esc="product.name"/><t t-esc="product.price"/><button t-att-id='product.id' t-on-click= "add_to_cart" t-ref="add-to-cart">Add to cart</button>
                            </div>
                        </t>
                    </t>
                </div> 
            </div>`;
       
        setup() {
             

            this.store = useStore();
        }

        add_to_cart(e) {
            fetch('/add_to_cart',{
                method:'POST',
                headers : {'Content-Type':'application/json'},
                body : JSON.stringify({'product_id': e.target.id})
            }).then(res=>{
                return res.json();
            }).then(Json_response=>{   
                this.store.addItemToCart(Json_response);
            });
            
        }
        
    }

    class Search extends Component
    { 
        static template = xml/*xml*/`
        <div class="p_list">
        <input id="input" placeholder="Search here"/><button t-on-click="SearchProduct">Search</button>
        </div>`;

        SearchProduct()
        {  
            var pname = document.getElementById('input').value;
            fetch('/search', {
                method: "POST",
                body: JSON.stringify({'p_name': pname}),
                headers : {'Content-Type':'application/json'},
            }).then(response=>{  
                return response.json(); 
            }).then(Json_response=>{   
                this.store.addData(Json_response);
            });
        }

        setup()
        {
            this.store = useStore();      
        }
    }

    class Root extends Component
    {
            
        static template = xml/*xml*/`
        <div class = "container">
        <div class="topbar">
        <Search/>
        </div>
        <div class="left_panel" style='float: left'>
        <ProductList/>
        </div>
        <div class="right_panel" style='float: right'>
        <Cart/>
        </div>
        </div>`;

        static components = { Search, ProductList, Cart  };

    }

    const env = { store : StoreData()}
    mount(Root, document.body, { test: true, env });

})();

