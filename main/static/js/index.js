
const list = document.querySelector('.cart_product-list')

function getProduct(url){
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data)
    })
}
