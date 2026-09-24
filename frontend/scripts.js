const API_URL = 'http://127.0.0.1:8000/api/products/';

function getproducts(){
    fetch(API_URL)
    .then(response => response.json())
    .then(data => {
        const listDIv = document.getElementById('products-list');
        listDIv.innerHTML = '';

        data.forEach(product => {
            listDIv.innerHTML += `<div class="card">
                                    <h4>${product.name}</h4>
                                    <p>price : ${product.price} , stock : ${product.stock}</p>
                                  </div>`;
        });
    })
    .catch(error => console.error('Error fetching data:', error));
}

function addproduct(){
    const name = document.getElementById('name').value;
    const price = document.getElementById('price').value;
    const stock = document.getElementById('stock').value;

    const newproduct = {
        name: name,
        price: parseInt(price),
        stock: parseInt(stock)
    };

    fetch(API_URL, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(newproduct)
    })
    .then(response => {
        if(response.status === 201){
            alert('Product added successfully!');

            document.getElementById('name').value = '';
            document.getElementById('price').value = '';
            document.getElementById('stock').value = '';

            getproducts();
        } else {
            alert('Error submitting information!');
        }
    })
    .catch(error => console.error('Error adding product:', error));
}
getproducts();