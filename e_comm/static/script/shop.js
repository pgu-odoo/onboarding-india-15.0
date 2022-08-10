let carts = document.querySelectorAll('.add-cart');

let products = [
    {
        name: 'Odoo GAP Analysis',
        price: 100,
        inCart: 0,
    },
    {
        name: 'Odoo Enterprise',
        price: 500,
        inCart: 0,
    },
    {
        name: 'CRM',
        price: 8,
        inCart: 0,
    },
    {
        name: 'Invoicing',
        price: 4,
        inCart: 0,
    },
    {
        name: 'Website',
        price: 8,
        inCart: 0,
    },
    {
        name: 'Manufacturing',
        price: 16,
        inCart: 0,
    },
    {
        name: 'Email Marketing',
        price: 16,
        inCart: 0,
    }
]

// 
for (let i=0; i < carts.length; i++) {
    carts[i].addEventListener('click', () => {
        cartNumbers(products[i]);
        totalCost(products[i])
    })
}

// save the count when refresh page, get data from localStorage
function onLoadCartNumbers() {
    let productNumber = localStorage.getItem('cartNumbers')

    if (productNumber) {
        document.querySelector('.count').textContent = productNumber;
    }
}

function cartNumbers(product) {
    // console.log("On click of product ", product);
    let productNumber = localStorage.getItem('cartNumbers')  // this gives string
    productNumber = parseInt(productNumber)  // convert it into INT
    // console.log(productNumber);
    if( productNumber ) {
        localStorage.setItem('cartNumbers', productNumber + 1);  // we can check this key:val pair in browser application->local storage
        document.querySelector('.count').textContent = productNumber + 1;
    } else {
        localStorage.setItem('cartNumbers', 1);
        document.querySelector('.count').textContent = 1;
    }

    setItems(product);
}

// add product in cart
function setItems(product) {
    // console.log("inside setItems function \n My product ", product);
    let cartItems = localStorage.getItem('productsInCart');
    cartItems = JSON.parse(cartItems);
    console.log("cart items: ", cartItems);

    if (cartItems != null) {
        if (cartItems[product.name] == undefined) {
            cartItems = {
                ...cartItems,  // rest operator
                [product.name]: product
            }
        }
        cartItems[product.name].inCart += 1;
    } else {
        product.inCart = 1;
        cartItems = {  // this will return JS object, we need to convert this into JSON object
            [product.name]: product
        }
    }
    localStorage.setItem("productsInCart", JSON.stringify(cartItems));  // using JSON.stringify, convert JS object to JSON object
}

// redirect to homepage on lick homepage
document.getElementById('clc').addEventListener('click', () => {
    window.open('/homepage', '_self')
});

// calculate total cost
function totalCost(prod) {
    // console.log("the products price is", prod.price);
    let cartCost = localStorage.getItem('totalCost');  // whenever we get something for localStorage it comes as a string
    
    if (cartCost != null) {
        cartCost = parseInt(cartCost)
        localStorage.setItem("totalCost", cartCost + prod.price)
    } else {
        localStorage.setItem("totalCost", prod.price);
    }

}


onLoadCartNumbers()  // load the page for fisrt time this function gets called to check local storage of add cart count













/* + or - button logic
    document.addEventListener('DOMContentLoaded', () => {
        document.querySelectorAll('button').forEach(button => {  // get all elements with button tag, or class
            button.onclick = () => {
                const request = new XMLHttpRequest();  // exchange data with a web server
                request.open('POST', `/${button.id}`);  // open(method, url, async)
                request.onload = () => {  // onload event occurs when an object has been loaded
                    const response = request.responseText;  // returns the text received from a server following a request being sent.
                    // console.log("response", response)
                    document.getElementById('count').innerHTML = response;
                }; 
                request.send();  // Sends the request to the server
            };
        });
    });
*/
