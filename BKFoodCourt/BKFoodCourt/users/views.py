from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import Customer
from .forms import UserForm
from webapp.models import Order
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from webapp.decorators import allowed_users
# Create your views here.

CUSTOMER_GROUP_ID = 1

def register(request):
    if request.user.is_authenticated:
        return redirect('home-page')
    context = {}
    if request.method == 'POST':
        username = request.POST.get('name')
        phone    = request.POST.get('phoneNumber')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        authpass = request.POST.get('authpassword')
        if User.objects.filter(username=username).exists() == False and password == authpass:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.groups.add(CUSTOMER_GROUP_ID)
            customer = Customer(user=user, phone=phone)
            user.save()
            customer.save()
            return redirect('login-page')  
        else:
            context['user'] = 1     
    return render(request, 'users/signup.html', context)

@login_required
@allowed_users(['Customer'])
def profile(request):
    customers = request.user.customer
    orders = Order.objects.filter(order_by=request.user, status="CONFIRMED")
    context = {
        'customers': customers,
        'orders': orders, 
    }
    return render(request, 'users/profile.html', context)

@login_required
@allowed_users(['Customer'])
def edit_profile(request):
    customers = request.user.customer
    orders = Order.objects.filter(order_by=request.user, status="CONFIRMED")
    form = UserForm(instance=customers)
    if request.method == 'POST':
        form = UserForm(data=request.POST, files=request.FILES, instance=customers)
        print(request.POST)
        print(request.FILES)
        print(request.body)
        if form.is_valid():
            form.save()
            return redirect('profile')
    context = {
        'form': form,
        'customers': customers,
        'orders': orders,
    }
    return render(request, 'users/edit_profile.html', context)
