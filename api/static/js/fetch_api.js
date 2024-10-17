alert('johan')
document.getElementById('name_button').addEventListener("click", function (){
    let name_value = document.getElementById('name_value').value;
    document.getElementById('printed_name').innerText =`{name : '` +name_value +`'}` //+`${name_value}`
    const new_json = {name: name_value}
    const print_json = JSON.stringify(new_json, null, 2)
    document.getElementById('printed_json').textContent = print_json
    })