
const inputList = document.querySelectorAll(`.form input`)
const selectList = document.querySelector(`.form select`)
const new_button = document.querySelector(`.form button`)
console.log(inputList)
console.log(selectList)
console.log(new_button)

function add_to_json() {
    const new_json = new FormData()
    new_json.append('product_title', inputList[1].value)
    new_json.append('product_image', inputList[2].files[0])
    new_json.append('product_price', inputList[3].value)
    new_json.append('product_unit', selectList.value)
    fetch('http://127.0.0.1:8000/send_data/', {
        method: 'POST',
        headers: {
            'X-CSRFToken': inputList[0].value
        },
        body: new_json
    })
        .then(response => response.json())
        .then(data => console.log(data))
}

new_button.addEventListener('click', add_to_json)
