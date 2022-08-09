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

for (let i=0; i < carts.length; i++) {
    carts[i].addEventListener('click', () => {
        cartNumbers();
    })
}

function onLoadCartNumbers() {
    let productNumber = localStorage.getItem('cartNumbers')

    if (productNumber) {
        document.querySelector('.count').textContent = productNumber;
    }
}

function cartNumbers() {
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
}

document.getElementById('clc').addEventListener('click', () => {
    window.open('/homepage', '_self')
});


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
