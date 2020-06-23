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

function showAccOptions()
{
    var x = document.getElementById("op-active");
    document.getElementById("acc").style.textDecoration = "none";
    if (x.style.display === "block")
    {
        x.style.display = "none";
    } else
    {
        x.style.display = "block";
        x.style.position = "absolute";
        x.style.background = "white";
        x.style.width = "220px";
        x.style.padding = "0px";
        x.style.margin = "0";
        x.style.left = "-130px";
        x.style.top = "20px";
        x.style.lineHeight = "30px";
        x.style.zIndex = "1";
        x.style.fontSize = "14px";
    }
    
}