regitries = {}

class Core 
{
    template = "<div></div>";

    constructor(parent) 
    {
        this.parent= parent;
        console.log(this.parent);
    }

    on(key, fn)
    {
      regitries[key] = fn
    }         

    trigger(key, data)
    {  
        let fn = regitries[key];
        console.log(fn);
        fn(data);   // ? where its data is going?
    }
    
    render() 
    {
        var parser = new DOMParser();
        var tmpl = parser.parseFromString(this.template, "text/html").body.childNodes;
        console.log(this.template);
        this.parent.appendChild(tmpl[0]);
    }

}

class App extends Core 
{

    template = "<div><div id='topbar'></div><div id='left_panel' style='float: left;'></div><div id='right_panel' style='float: right;'></div></div>";

    render() 
    {
        super.render(); //for non argumented functions

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

class Search extends Core 
{

    template = "<div><h2>Search Product</h2><input id=\"values\" style='margin-right: 10px'/><button id=\"search\">Search</button></div>";
    
    fetch_data()
    {
        var name = document.getElementById('values').value;
        fetch('/search',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
            body : JSON.stringify({product_name : name})
        })
        // the path to the resource you want to fetch — and does not directly return the JSON response body 
        // but instead returns a promise that resolves with a Response object.
        // The Response object, in turn, does not directly contain the actual JSON response body but is instead a representation of the entire HTTP response.
        //  So, to extract the JSON body content from the Response object, we use the json() method, 
        // which returns a second promise that resolves with the result of parsing the response body text as JSON.
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            this.trigger('update_product_list',data['result']);
        });
    }

    render()
    {
    super.render();
    document.getElementById("search").addEventListener('click', (e)=>{this.fetch_data()}); 
    }
}


class ProductList extends Core
 {
    products = [];
    template = "<div><h2>Product Info</h2><div id='product_list'></div></div>";

    constructor(parent)
    {
        super(parent);
        this.on('update_product_list', (data)=>{this.onupdate(data)});
        super.render();
    }
    onupdate(data)
    {
        this.products = data;
        this.render();
    }

    render()
    {
        let list = document.getElementById("product_list");
        for (var i=0; i<this.products.length; i++) 
        {
            let item = new Item(list);
            item.data = this.products[i]
            item.product_render(); 
        }
    }
}



class Item extends Core 
{
    data = [];
   
      
    fetch_to_cart(e) 
    {   
        fetch('/add_to_cart',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
            body : JSON.stringify({'price':e.target.price ,'product_id':e.target.id})
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            this.trigger('update_cart',data); //to access order of array changed data['order] to data
            console.log(data);
        });
     
    }

    product_render()
    {
        let addbtn = `btn_${this.data.id}`
        this.template = `<div id="products_details"> ${this.data.name}, ${this.data.price}<button id=${addbtn} style='margin-top: 5px;'>Add to cart</button></div>` ;
        console.log(this.data.name);
        super.render();
        document.getElementById(addbtn).addEventListener('click', (e)=>{this.fetch_to_cart(e)});
    } 
    
}

class Cart extends Core 
{
    order = [];

    template = "<div><h2>Cart Info</h2><div id='cart_list'></div><button id='btnn'style='margin-top: 5px;'>Checkout</button></div></div>";


constructor(parent)
    {
        super(parent);
        this.on('update_cart', (data)=>{this.onupdate(data)}); 
        super.render();
    }

onupdate(data)
    {

        if (data['order']) {
            this.order = data['order'];
            this.render();
        }
        if (data['orders']) {
            this.order = data['orders']
            this.render_checkout();
        }
    }
    
remove_the_item() 
    {   
        fetch('/remove_from_cart',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
            body : JSON.stringify({'product_name':this.order.product_name}) //or try 'bd'
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
        if(data){ 
            this.trigger('updated_cart',data['orders']);
            console.log(data);
        }
        });
     
    }
    checkout() 
    {
        fetch('/checkout',{
            method:'POST',
            headers : {'Content-Type':'application/json'},
        })
        .then(res=>{
            return res.json();
        })
        .then(data=>{
            if (data) {
                this.trigger('update_cart', data);
            }
        });
    }   

render()
    {
    var btn = '';
    if (this.order.length > 0) {
        // this.parent.innerHTML = "<div><h2>Cart Info</h2><div id='cart_list'></div><button id='btnn'style='margin-top: 5px;'>Checkout</button></div></div>";
    }  
    for(var i=0; i<this.order.length;i++)
    {
    let rem_btn = `r_${this.order[i].order_id}`
    this.template = `<div>${this.order[i].product_id},${this.order[i].price},${this.order[i].qty}<button id=${rem_btn} style='margin-top: 5px;'>Remove_from_cart</button></div></div>`;
    super.render(); 
    document.getElementById(rem_btn).addEventListener('click', (e)=>{this.remove_the_item()});
    document.getElementById('btn_checkout').addEventListener('click', (e)=> {this.checkout()});

    }
    if (this.order.length == 0) {
        this.parent.innerHTML = '';
        this.template = "<div><h2>Cart Info</h2><div id='cart_list'></div><button id='btn_checkout'style='margin-top: 5px;'>Checkout</button></div></div>";
        super.render();       
    }
    }
}

window.onload = function() 
{
    let root_element = document.getElementById("container");
    let app = new App(root_element);
    app.render();
}



















// <---------------------------------------------TESTING OF THE PARSE METHOD USING DOMPARSER------------------------------------------->

// class App {
//     template = "<div id=\"topbar\"></div><div id=\"right_panel\"></div><div id=\"left_panel\"></div>";

//     constructor(parent)
//     {
//     this.parent= parent;
//     }

//     render(){
//     var parser = new DOMParser().parseFromString(this.template, "text/html").body.childNode;
//     this.parent.appendChild(tmpl[0]);
//     // var temp = new DOMParser().parseFromString(this.parser, "text/html");
//     this.parent.append(parser);
//     // const fragment = document.createRange().createContextualFragment(html)
//     // var doc = parser.querySelector('body').innerHTML; 
//     // var temp_document = parser.parseFromString(this.template, "text/html").body;   
//     // this.parent.innerHTML = this.template;
//     // return temp_document;
//     // return doc;
//     }
        
//     }

//     window.onload = function(){
//       
//     // let app1 = new App()
//     // let temp_document = app1.render()
//     let root_element = document.getElementById("container");
//     // root_element.innerHTML.append(temp_document)
//     let app = new App(root_element);

//     app.render();
//     }
























// <--------------------------------------------- PLAYAROUnd code: ------------------------------------------------------------>

// window.onload = function(){
//     let root_element = document.getElementById("container");

//     let div = document.createElement("div");  //created new div ?? to keeep the button from diappering
    // let btn_html = "<button  id=\"btn\">Click Here </button";  //button obj
    //let btn = document.createElement(btn_html);

    // var parser = new DOMParser(); 
    // var btn = parser.parseFromString(btn_html, "text/html").documentElement;

    //let btn = document.parse(btn_html);
//     div.innerText = "Hello World";
//     root_element.append(div);
//     root_element.append(btn);

//     let btn_element = document.getElementById("btn");
//     btn_element.onclick = function(){
//         div.innerText = "Welcome";
//     }
// }
