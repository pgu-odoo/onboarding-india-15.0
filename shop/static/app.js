    registry = {};

class Base{
    template = "";
    constructor(parent){
        this.parent = parent;
    }
    render(){
        var parser = new DOMParser();
        var tmpl = parser.parseFromString(this.template, "text/html").body.childNodes;
        this.parent.appendChild(tmpl[0]);
    }
    on(key, method){
        registry[key] = method;
    }
    trigger(key, data){
        let fn = registry[key];
        fn(data);
    }
}

class App extends Base{
    template = "<div><div id='topbar'></div><div id='left_panel' style='float: left;'></div><div id='right_panel' style='float: right'></div></div>";

    async render(){
        await super.render();
        let top = document.getElementById("topbar");
        let search = new Search(top);
        search.render();

        let left = document.getElementById("left_panel");
        let product_list = new ProductList(left);
        product_list.render();

        let right = document.getElementById("right_panel");
        let cart = new Cart(right);
        cart.render();
    }
}

class Search extends Base{
    template = "<div><h2>Search Product</h2><input id='p_name' style='margin-right: 10px'/><button id='search'>Search</button</div>";

    onSearch(){
        var name = document.getElementById('p_name').value;
        fetch('/search',{
            method : "POST",
            body : JSON.stringify({'p_name': name}),
            headers : {'Content-Type':'application/json'},
        })
        .then(response=>{
            return response.json();
        })
        .then(response=>{
            this.trigger('update_list', response)
        });
    }

    render(){
        super.render();
        document.getElementById('search').addEventListener("click", (e)=>{this.onSearch()});
    }
}

class Item extends Base{
    data = []

    add_to_cart(e){
        fetch('/add_to_cart',{
            method : "POST",
            headers : {'Content-Type':'application/json'},
            body : JSON.stringify({'product_id': e.target.id})
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            this.trigger('update_cart', data)
        });
    }
    render(){
        let btn = '';
        if (this.data.length > 0) {
            this.parent.innerHTML = '';
        }
        for (var i= 0; i < this.data.length; i++) {
            btn = this.data[i].id;
            this.template = `<div><div>${this.data[i]['name']}, ${this.data[i]['price']}</div><div><button id=${btn} style='margin-top: 5px;'>Add to cart</button></div></div>`
            super.render();
            
            document.getElementById(btn).addEventListener('click', (e)=> {this.add_to_cart(e)});
        }
    }
}

class ProductList extends Base{
    template = "<div><div id='product_list'></div></div>";
    products = [];

    constructor(parent){
        super(parent);
        this.on('update_list', (data)=>{this.onupdate(data)});
    }
    onupdate(data){
        this.products = data['products'];
        this.render();
    }
    render(){
        super.render();
        let root_element = document.getElementById("product_list");
        let item = new Item(root_element);
        item.data = this.products;
        item.render();
    }
}

class Cart extends Base{
    order = []
    template = "<div><h2>Cart Info</h2><div id='cart_list'></div></div>";

    constructor(parent) {
        super(parent);
        this.on('update_cart', (data)=>{this.onupdate(data)});
    }

    onupdate(data) {
        if(data['order_lines']){
            this.order = data['order_lines'];
            this.render();
        }
        if(data['order_detail']){
            this.order = data['order_detail'];
            this.render_checkout();
        }
    }

    remove_from_cart(e) {
        fetch('/remove_from_cart',{
            method : 'POST',
            headers : {'Content-Type':'application/json'},
            // ***********************
            body : JSON.stringify({'product_id': e.target.id})
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            if(data){
                this.trigger('update_cart', data);
            }
        });
    }

    checkout() {
        fetch('/checkout',{
            method : 'POST',
            headers : {'Content-Type':'application/json'},      
        })
        .then(res=>{
            return res.json();
        })
        
        .then(data=>{
            if(data){
                this.trigger('update_cart', data);
            }
        });
    }

    render_checkout(){
        this.parent.innerHTML = '';
        this.template = '<div></div>';
        super.render();

        for(var i=0; i < this.order.products.length; i++){
            this.template = `<div>${this.order['products'][i].p_name}, ${this.order['products'][i].qty}, ${this.order['products'][i].price}</div>`;
            super.render();
        }
        this.template = `<div><hr>Total : ${this.order['total']}</div>`;
        super.render();
    }    

    render() {
        var btn = '';
        if (this.order.length > 0) {
            this.parent.innerHTML = "<div><button id='btn_checkout'/>Checkout<div>";
        }
        for (var i=0; i < this.order.length; i++) {
            btn = `r_${this.order[i].id}`;
            this.template = `<div><div>${this.order[i].name}, ${this.order[i].qty}, ${this.order[i].price}</div><div><button id=${btn} style='margin-top: 5px;'>Remove</button></div></div>`;            
            super.render();       
            document.getElementById(btn).addEventListener('click', (e)=> {this.remove_from_cart(e)});
            document.getElementById('btn_checkout').addEventListener('click', (e)=> {this.checkout()});
        }
        if (this.order.length == 0) {
            this.parent.innerHTML = '';
            this.template = '<div></div>';
            super.render();       
        }
    }
}


window.onload = function(){
    let root_element = document.getElementById('container');
    let app = new App(root_element);
    app.render();
}