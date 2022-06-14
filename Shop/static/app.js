registry = {};

class Base {
    // template = "";
    constructor(parent) {
        this.parent= parent;
    }
    render() {
        console.log("1111111111111111111111111111111111111111111111111111111111111111")
        var parser = new DOMParser();
        var tmpl = parser.parseFromString(this.template, "text/html").body.childNodes;
        this.parent.appendChild(tmpl[0]);
    }
    on(key, method) {
        registry[key] = method;
    }
    trigger(key, data) {
        let fn = registry[key];
        fn(data);
    }
}

class App extends Base {
    template = `<div>
                    <div id='topbar'></div>
                    <div id='left_panel' style='float: left;'>
                        <h2>Product List</h2>
                    </div>
                    <div id='right_panel' style='float: right;'></div>
                </div>`;

    async render () {
        console.log("2222222222222222222222222222222222222222222222222222222222222222222222222222222")
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
class Search extends Base {
    template = `<div>
                    <h2>Search Product</h2>
                    <input id='p_name' style='margin-right: 10px'/>
                <button id='search'>Search</button><div>`;

    onSeach() {
        console.log("3333333333333333333333333333333333333333333333333333333333333333333333333333333")
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
            this.trigger('update_list', response);
        });

        // const response = await fetch('/search', {
        //     method: "POST",
        //     body: JSON.stringify({'p_name': name}),
        //     headers : {'Content-Type':'application/json'},
        // })

        // const ans = await response.json();
          
    }
    render() {
        super.render();
        document.getElementById('search').addEventListener("click", (e)=>{this.onSeach()});
    }
}

class Item extends Base {
    data = []

    add_to_cart(e){
        fetch('/add_to_cart', {
            method: "POST",
            body: JSON.stringify({'p_name': name}),
            headers : {'Content-Type':'application/json'},
        }) 

        .then(response=>{
            return respons.json();
        })
        .then(response=>{
            this.trigger('product_id',e.target_id);
        });
    }

    render(){
        let btn="";
        if (this.data.length>0){
            this.parent.innerHTML='';
        }
        for (var i= 0; i < this.data.length; i++) {
            btn = this.data[i].id;
            this.template = `<div><div>${this.data[i]['name']}, ${this.data[i]['price']}</div><div><button id=${btn} style='margin-top: 5px;'>Add to cart</button></div></div>`
            super.render();

            document.getElementById('btn').addEventListener("click", (e)=>{this.add_to_cart})
        }
}


window.onload = function() {
    let root_element = document.getElementById("container");
    let app = new App(root_element);
    app.render();
}



