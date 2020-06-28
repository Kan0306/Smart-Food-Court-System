from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Menu, Order, Manager
from .decorators import allowed_users
from django.core.paginator import Paginator
import json, urllib.request, hmac, hashlib, uuid, socket
import urllib.parse as urlparse
from urllib.parse import parse_qs
from django.urls import reverse
from .forms import ItemForm

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
def order_status(request, id):
    order = get_object_or_404(Order, id=id)
    context = {
        'order': order
    }
    url = request.build_absolute_uri()
    # print(url)
    parsed = urlparse.urlparse(url)
    error = parse_qs(parsed.query)['errorCode'][0]
    if error == 0:
        return render(request, 'webapp/orderstatus.html', context)
    else:
        return render(request, 'webapp/orderstatus.html', context)

@login_required
def online_payment(request):
    return render(request, 'webapp/online-payment.html', {})

def home(request):   
    managers = Manager.objects.all()
    stalls = Menu.objects.all()
    context = {
        'managers': managers,
        'stalls': stalls,
    }    
    return render(request, 'webapp/home.html', context)

def menu(request):
    stalls = Menu.objects.all()
    items = Item.objects.all()
    managers = Manager.objects.all()
    paginator = Paginator(stalls, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'stalls' : stalls,
        'managers': managers,
        'items' : items,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menu.html', context)

def menustall(request, id):
    stall = get_object_or_404(Menu, id=id)
    managers = Manager.objects.all()
    stalls = Menu.objects.all()
    items = Item.objects.filter(belongs_to_stall=stall)
    paginator = Paginator(items, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    context = {
        'items': items,
        'managers': managers,
        'stalls': stalls,
        'stall': stall,
        'page_obj': page_obj
    }
    return render(request, 'webapp/menustall.html', context)

def about(request):
    managers = Manager.objects.all()
    stalls = Menu.objects.all()
    context = {
        'managers': managers,
        'stalls': stalls,
    }    
    return render(request, 'webapp/about.html', context)

def preference(request):
    managers = Manager.objects.all()
    stalls = Menu.objects.all()
    context = {
        'managers': managers,
        'stalls': stalls,
    }    
    return render(request, 'webapp/preference.html', context)

def item_info(request):
    managers = Manager.objects.all()
    stalls = Menu.objects.all()
    context = {
        'managers': managers,
        'stalls': stalls,
    }    
    return render(request, 'webapp/item_info.html', context)


@login_required
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
def update_item(request,id):
    item = Item.objects.get(id=id)
    stall= item.belongs_to_stall
    form = ItemForm(instance=item)
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES,instance=item)
        if form.is_valid():
            form.save()
            return redirect('stall-menu',stall.id)
    context={
        'form':form,
        'stall':stall,
    }
    return render(request,'webapp/item_form.html',context)
@login_required
def create_item(request,id):
    stall = Menu.objects.get(id=id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('stall-menu',id)
    context={
        'form':form,
        'stall':stall,
    }
    return render(request,'webapp/item_form.html',context)

@login_required
def payment(request, id):
    order = Order.objects.get(id=id)
    # orderId = 'BKORDER' + str(id).zfill(13)
    amount = 0
    for item in order.item.all():
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
    orderId = "1505359852732"
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
    with open("4forces.json","w") as x:
        x.write(data)

    g = open('4forces.json')
    req = urllib.request.Request(endpoint, g, {'Content-Type': 'application/json', 'Content-Length': len(data)})
    f = urllib.request.urlopen(req)
    response = f.read()
    f.close()

    a = json.loads(response)
    return redirect(a['payUrl'])
    
    # return render(request, 'webapp/payment.html', {})
