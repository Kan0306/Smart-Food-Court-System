from django.shortcuts import render

# Create your views here.
def shopping_cart(request):
    return render(request, 'webapp/shopping_cart.html', {})

def pay_by_account(request):
    return render(request, 'webapp/pay_by_account.html', {})

def bill(request):
    return render(request, 'webapp/bill.html', {})

def order_status(request):
    return render(request, 'webapp/orderstatus.html', {})

def online_payment(request):
    return render(request, 'webapp/online-webapp.html', {})

def home(request):
    return render(request, 'webapp/home.html', {})

def temphome(request):
    return render(request, 'webapp/home_logined.html', {})

def menu(request):
    return render(request, 'webapp/menu.html', {})

def menustall(request):
    return render(request, 'webapp/menustall.html', {})

def about(request):
    return render(request, 'webapp/about.html', {})

def preference(request):
    return render(request, 'webapp/preference.html', {})

def item_info(request):
    return render(request, 'webapp/item_info.html', {})