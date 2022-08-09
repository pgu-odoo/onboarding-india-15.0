// search product
const searchProduct = () => {
    const searchBox = document.getElementById('search').value.toUpperCase();
    // console.log(searchBox);
    // const storeItems = document.getElementById('product-list')
    const product = document.querySelectorAll('.product')
    const pname = document.getElementsByTagName('h3')
    
    for (var i = 0; i < pname.length; i++){
        let match = product[i].getElementsByTagName('h3')[0];  // we'll get all products containing `h3` tag
        
        if(match){
            let textValue = match.textContent || match.innerHTML
            
            if (textValue.toUpperCase().indexOf(searchBox) > -1){
                // console.log(textValue.toUpperCase().indexOf(searchBox));
                product[i].style.display = '';
            } else{
                product[i].style.display = 'none';
            }
        }
    }
}



/*
    innerText: returns all text contained by an element and all its child elements.
    innerHtml: returns all text, including html tags, that is contained by an element.
*/