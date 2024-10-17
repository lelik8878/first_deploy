
const inputList = document.querySelectorAll(`.form input`)
const selectList = document.querySelector(`.form select`)
const new_button = document.querySelector(`.form button`)
console.log(inputList)
console.log(selectList)
console.log(new_button)

function add_to_json() {
    const new_json = JSON.stringify({
        product_title: inputList[1].value,
        product_image: inputList[2].files[0],
        product_price: inputList[3].value,
        product_unit: selectList.value
    })
    console.log(new_json)
    console.log(inputList[2].files[0])
}

new_button.addEventListener('click', add_to_json)
