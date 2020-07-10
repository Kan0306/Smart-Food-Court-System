var readyButton = document.getElementsByClassName("is-ready");
var outButton = document.getElementsByClassName("out-of-order");

for (var i = 0; i < readyButton.length; i++) {
    readyButton[i].addEventListener("click",informReady);
}
for (var j = 0; j < outButton.length; j++) {
    outButton[j].addEventListener("click",informOutOfOrder);
}

function informReady() {
    var oitemID = this.dataset.oitem;
    var action = this.dataset.action;
    updateOrderList(oitemID, action);
}
function informOutOfOrder() {
    var itemID = this.dataset.item;
    var action = this.dataset.action;
    updateMenu(itemID, action);
}

function updateOrderList(oitemID, action) {
    var url = '/inform_ready/'

    fetch(url, {
        method: "POST",
        headers: {
            "Content-Type" : "application/json",
            "X-CSRFToken" : csrftoken
        },
        body: JSON.stringify({'oitemID': oitemID, 'action': action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log("data:", data)
        location.reload()
    })
}
function updateMenu(itemID, action) {
    var url = '/inform_out/'

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