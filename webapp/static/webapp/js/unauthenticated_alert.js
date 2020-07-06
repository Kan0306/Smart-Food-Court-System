var alertButton = document.getElementsByClassName("alert-button");

for (var i = 0; i < alertButton.length; i++) {
    alertButton[i].addEventListener("click",alert_func);
}

function alert_func(){
    alert('Xin vui lòng đăng nhập trước khi đặt hàng')
}