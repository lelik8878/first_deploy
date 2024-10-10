const list = document.querySelector('.cart_product-list')

function getProduct(url){
    fetch(url)
    .then(response => response.json())
    .then(data => {
        console.log(data)
        for(let i of data){
            const li = document.createElement('li')
            li.innerHTML = `
            <article class="cart_product ">
                            <div class="cart_product-img">
                                <img src="${i.image}" alt="">
                            </div>
                            <h3 class="cart_product-title">
                                <a href="#">
                                    ${i.title}
                                </a>
                            </h3>
                            <ul class="cart_product-weight-list">
                                ${i.quantity_set.map(item =>`<li>${item.weight}<span>${item.unit}</span></li>`).join('')}
                            </ul>
                            <div class="cart_product-price-wrapper">
                                <p>
                                    ${i.price} BYN
                                </p>
                                <div>
                                    <svg width="7.203125" height="7.203369" viewBox="0 0 7.20312 7.20337" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                        <desc>
                                                Created with Pixso.
                                        </desc>
                                        <defs/>
                                        <path id="Label" d="M4.31 7.2L2.88 7.2L2.88 4.31L-0.01 4.31L-0.01 2.88L2.88 2.88L2.88 0L4.31 0L4.31 2.88L7.2 2.88L7.2 4.31L4.31 4.31L4.31 7.2Z" fill="#5C5F62" fill-opacity="1.000000" fill-rule="evenodd"/>
                                    </svg>
                                    <svg width="18.000000" height="20.000000" viewBox="0 0 18 20" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
                                        <desc>
                                                Created with Pixso.
                                        </desc>
                                        <defs/>
                                        <path id="Primary fill" d="M0 1C0 0.44 0.44 0 1 0L2.5 0C3.34 0 4.01 0.67 4.01 1.5L4.01 2.06L16.58 2.96C17.46 3.02 18.1 3.81 17.98 4.67L17.11 10.71C17.01 11.45 16.37 12 15.62 12L4.01 12L4.01 14L14.05 14C15.72 14 17.06 15.34 17.06 17C17.06 18.65 15.72 20 14.05 20C12.39 20 11.04 18.65 11.04 17C11.04 16.64 11.1 16.31 11.21 16L5.85 16C5.96 16.31 6.02 16.64 6.02 17C6.02 18.65 4.67 20 3.01 20C1.34 20 0 18.65 0 17C0 15.69 0.83 14.58 2 14.17L2 3C2 3 2 2.99 2 2.99L2 2L1 2C0.44 2 0 1.55 0 1ZM4.01 4.06L4.01 10L15.19 10L15.92 4.93L4.01 4.06ZM13.05 17C13.05 16.44 13.5 16 14.05 16C14.61 16 15.06 16.44 15.06 17C15.06 17.55 14.61 18 14.05 18C13.5 18 13.05 17.55 13.05 17ZM2 17C2 16.44 2.45 16 3.01 16C3.56 16 4.01 16.44 4.01 17C4.01 17.55 3.56 18 3.01 18C2.45 18 2 17.55 2 17Z" fill="#5C5F62" fill-opacity="1.000000" fill-rule="evenodd"/>
                                    </svg>                
                                </div>            
                            </div>
                            <button class="cart_product-buy">
                                Купить в 1 клик
                            </button>
                            </article>
            `
            list.append(li)
        }
    })
}

getProduct('http://127.0.0.1:8000/product_list/')