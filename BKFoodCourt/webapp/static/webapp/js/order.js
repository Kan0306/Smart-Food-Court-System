var orderButton = document.getElementsByClassName("order-button");

for (var i = 0; i < orderButton.length; i++) {
    orderButton[i].addEventListener("click",addToCart);
}

function addToCart(){
    var itemID = this.dataset.item;
    var action = this.dataset.action;
    updateOrder(itemID, action);
}

function updateOrder(itemID, action){
    var url = '/update_order/'

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrftoken
        },
        body: JSON.stringify({'itemID': itemID, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log("data:", data)
        location.reload()
    })
}
