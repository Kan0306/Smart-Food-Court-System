from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Item
# Create your views here.
@login_required
def shopping_cart(request):
    return render(request, 'webapp/shopping_cart.html', {})

@login_required
def pay_by_account(request):
    return render(request, 'webapp/pay_by_account.html', {})

@login_required
def bill(request):
    return render(request, 'webapp/bill.html', {})

@login_required
def order_status(request):
    return render(request, 'webapp/orderstatus.html', {})

@login_required
def online_payment(request):
    return render(request, 'webapp/online-webapp.html', {})

def home(request):
    return render(request, 'webapp/home.html', {})

def menu(request):
    return render(request, 'webapp/menu.html', {})

def menustall(request):
    items = Item.objects.all()
    context = {
        'items': items
    }
    return render(request, 'webapp/menustall.html', context)

# class ItemListView(ListView):
#     model = Item
#     template_name = 'webapp/menustall.html'
#     context_objects_name = 'items'


def about(request):
    return render(request, 'webapp/about.html', {})

def preference(request):
    return render(request, 'webapp/preference.html', {})

def item_info(request):
    return render(request, 'webapp/item_info.html', {})

@login_required
def manage_menu(request):
    pass