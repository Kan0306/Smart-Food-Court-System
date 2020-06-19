var orderButton = document.getElementsByClassName("order-button");
var numOfItems = 0;

for (var i = 0; i < orderButton.length; i++) {
    orderButton[i].addEventListener("click",addToCart);
}

function addToCart(){
    alert("Accepted!")
    numOfItems = numOfItems + 1;
    document.querySelector(".cart_icon .badge").textContent = numOfItems;
}
