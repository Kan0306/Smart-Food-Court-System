from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from webapp.models import Order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from webapp.decorators import allowed_users
# Create your views here.

@login_required
#@allowed_users(['Cook'])
def order_list(request):
    #orders = Order.get
    return render(request, 'kitchen/orderlist.html', {})