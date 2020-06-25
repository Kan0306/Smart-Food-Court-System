from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Item, Menu
from django.core.paginator import Paginator
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
    stalls = Menu.objects.all()
    items = Item.objects.all()
    paginator = Paginator(stalls, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'stalls' : stalls,
        'items' : items,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menu.html', context)

def menustall(request, id):
    items = Item.objects.all()
    stall = get_object_or_404(Menu, id=id)
    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'items': items,
        'stall': stall,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menustall.html', context)


def about(request):
    return render(request, 'webapp/about.html', {})

def preference(request):
    return render(request, 'webapp/preference.html', {})

def item_info(request):
    return render(request, 'webapp/item_info.html', {})

@login_required
def manage_menu(request):
    pass