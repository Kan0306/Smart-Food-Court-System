from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from webapp.models import Order, OrderItem, Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from webapp.decorators import allowed_users
from django.db.models import Min, Max, Q
from django.http import JsonResponse
import json
# Create your views here.

@login_required
@allowed_users(['Cook'])
def order_list(request):
    cook = request.user.cook
    orderItem = OrderItem.objects.filter(Q(item__belongs_to_stall=cook.own_stall),~Q(order__status='ONGOING')).annotate(lastest=Max('order__start_date')).order_by('-lastest').reverse()
    context = {
        'cook' : cook,
        'orderItem' : orderItem
    }
    return render(request, 'kitchen/orderlist.html', context)

@login_required
@allowed_users(['Cook'])
def inform_ready(request):
    data = json.loads(request.body)
    oitemID = data['oitemID']
    action = data['action']

    orderItem = OrderItem.objects.get(id=oitemID)
    if action == 'ready':
        orderItem.ready = True
   
    orderItem.save()

    return JsonResponse("Successful", safe=False)

@login_required
@allowed_users(['Cook'])
def inform_out(request):
    data = json.loads(request.body)
    itemID = data['itemID']
    action = data['action']

    item = Item.objects.get(id=itemID)
    if action == 'out':
        item.available = False
   
    item.save()

    return JsonResponse("Successful", safe=False)