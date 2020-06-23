var submit = document.getElementById("add_cart");
var orderButton = document.getElementsByClassName("order-button");
var numOfItems = 0;

for (var i = 0; i < orderButton.length; i++) {
    orderButton[i].addEventListener("click",addToCart);
}
submit.addEventListener("click",addToCartWithNum);


function addToCart(){
    alert("Accepted!")
    numOfItems = numOfItems + 1;
    document.querySelector(".cart_icon .badge").textContent = numOfItems;
}
function addToCartWithNum()
{  
    var y = document.getElementById("num_item").value;
    if (y === "0")
        alert("Empty to add to cart!")
    else
    {
        alert("Accepted!")
        numOfItems = numOfItems + Number(y);
        document.querySelector(".cart_icon .badge").textContent = numOfItems;
    }
}
