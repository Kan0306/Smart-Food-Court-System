from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Menu, Order, OrderItem
from django.core.paginator import Paginator
import json, urllib.request, hmac, hashlib, uuid, socket
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.urls import reverse
from django.http import JsonResponse
import json
import random
from datetime import datetime
from .forms import ItemForm
from .decorators import allowed_users
from users.models import Manager
# Create your views here.

@login_required
@allowed_users(['Customer'])
def shopping_cart(request):
    order, created = Order.objects.get_or_create(order_by=request.user, status="ONGOING")
    items = order.orderitem_set.all()
    context = {
        'order' : order,
        'items' : items
    }
    return render(request, 'webapp/shopping_cart.html', context)

@login_required
@allowed_users(['Customer'])
def bill(request, id):
    url = request.build_absolute_uri()
    parsed = urlparse.urlparse(url)
    error = parse_qs(parsed.query)['errorCode'][0]
    time = parse_qs(parsed.query)['responseTime'][0]
    order = get_object_or_404(Order, id=id)
    items = order.orderitem_set.all()
    orderId = 'BKORDER' + str(id).zfill(13)

    if error == "0":
        order.status = "CONFIRMED"
        order.save()
    context = {
        'order': order,
        'orderId': orderId,
        'items': items,
        'error': error,
        'time' : time
    }
    return render(request, 'webapp/bill.html', context)

@login_required
@allowed_users(['Customer'])
def order_status(request, id):
    order = get_object_or_404(Order, id=id)
    context = {
        'order': order
    }
    return render(request, 'webapp/orderstatus.html', context)

def home(request):    
    return render(request, 'webapp/home.html', {})

def menu(request):
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(order_by=request.user, status="ONGOING")
    else:
        order = "none"
    stalls = Menu.objects.all()
    items = Item.objects.all()
    paginator = Paginator(stalls, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'stalls' : stalls,
        'items' : items,
        'order' : order,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menu.html', context)

def menustall(request, id):
    stall = get_object_or_404(Menu, id=id)
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(order_by=request.user, status="ONGOING")
    else:
        order = "none"
    items = Item.objects.filter(belongs_to_stall=stall)
    query_list = items
    query = request.GET.get('query')
    if query:
        query_list = query_list.filter(name__icontains=query)
    if len(query_list) == 0 or query == "":
        none = 'True'
    else:
        none = 'False'
    paginator = Paginator(query_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'none' : none,
        'stall': stall,
        'order' : order,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menustall.html', context)


def about(request):  
    return render(request, 'webapp/about.html', {})

def preference(request):
    return render(request, 'webapp/preference.html', {})

def item_info(request, id):
    item = Item.objects.get(id=id)
    stall = item.belongs_to_stall
    if request.user.is_authenticated:
        order, created = Order.objects.get_or_create(order_by=request.user, status="ONGOING")
        context = {
            'item' : item,
            'stall' : stall,
            'order' : order
        }
    else:
        context = {
            'item' : item,
            'stall' : stall,
        }
    return render(request, 'webapp/item_info.html', context)

@login_required
@allowed_users(['Customer'])
def payment(request, id):
    order = Order.objects.get(id=id)
    amount = 0
    for item in order.orderitem_set.all():
        amount += item.item.price * item.quantity
    amount = str(amount)
    endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
    partnerCode = "MOMOVL8T20200626"
    accessKey = "d6FwBIfUxCeJESLJ"
    serectkey = "YmCHInPx2bjVUWgImtmFt9xIAQkuHaZm"
    requestId = "MM" + str(id).zfill(13)
    orderInfo = order.order_by.customer.name
    returnUrl = "http://127.0.0.1:8000"+order.get_absolute_return_url()
    notifyurl = "https://dummy.url/notify"
    requestType = "captureMoMoWallet"
    extraData = "merchantName=;merchantId="
    orderId = "1505359852743"
    # orderID = random.seed(datetime.now())
    rawSignature = "partnerCode="+partnerCode+"&accessKey="+accessKey+"&requestId="+requestId+"&amount="+amount+"&orderId="+orderId+"&orderInfo="+orderInfo+"&returnUrl="+returnUrl+"&notifyUrl="+notifyurl+"&extraData="+extraData
    signature = hmac.new( bytes(serectkey, 'latin-1'), bytes(rawSignature, 'latin-1'), hashlib.sha256 ).hexdigest()

    # #json object send to MoMo endpoint

    data = {
        "accessKey": accessKey,
        "partnerCode": partnerCode,
        "requestType": requestType,
        "notifyUrl": notifyurl,
        "returnUrl": returnUrl,
        "orderId": orderId,
        "amount": amount,
        "orderInfo": orderInfo,
        "requestId": requestId,
        "extraData": extraData,
        "signature": signature
    }

    data = json.dumps(data)

    req = urllib.request.Request(endpoint, data.encode('utf-8'), {'Content-Type': 'application/json', 'Content-Length': len(data)})
    f = urllib.request.urlopen(req)
    response = f.read()
    f.close()
    a = json.loads(response)
    return redirect(a['payUrl'])
    
    # return render(request, 'webapp/payment.html', {})

def search(request):
    query_list = Item.objects.all()
    query = request.GET.get('query')
    if query:
        query_list = query_list.filter(name__icontains=query)
    if len(query_list) == 0 or query == "":
        none = 'True'
    else:
        none = 'False'
    paginator = Paginator(query_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'none' : none,
        'page_obj': page_obj
    }
    return render(request, 'webapp/search.html', context)

@login_required
@allowed_users(['Customer'])
def update_order(request):
    data = json.loads(request.body)
    itemID = data['itemID']
    action = data['action']
    
    item = Item.objects.get(id=itemID)
    order, created = Order.objects.get_or_create(order_by=request.user, status="ONGOING")
    orderItem, created = OrderItem.objects.get_or_create(order=order, item=item)
    if action == "add":
        orderItem.quantity += 1
    elif action == "remove":
        orderItem.quantity -= 1

    orderItem.save()

    if orderItem.quantity <= 0 or action == "delete":
        orderItem.delete()

    return JsonResponse("Successful", safe=False)

@login_required
@allowed_users(['Manager'])
def delete_item(request,id):
    item = Item.objects.get(id=id)
    stall = item.belongs_to_stall
    if request.method == "POST":
        item.delete()
        return redirect('stall-menu',stall.id)
    context = {
        'item':item,
        'stall':stall
    }
    return render(request,'webapp/form_delete.html',context)

@login_required
@allowed_users(['Manager'])
def update_item(request,id):
    item = Item.objects.get(id=id)
    stall= item.belongs_to_stall
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        print(request.POST)
        print(request.FILES)
        print(request.body)

        if form.is_valid():
            form.save()
            return redirect('stall-menu',stall.id)
    context={
        'form':form,
        'stall':stall,
    }
    return render(request,'webapp/item_form.html',context)

@login_required
@allowed_users(['Manager'])
def create_item(request,id):
    stall = Menu.objects.get(id=id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.belongs_to_stall = stall
            obj.save()
            return redirect('stall-menu',id)
    context={
        'form':form,
        'stall':stall,
    }
    return render(request,'webapp/item_form.html',context)

