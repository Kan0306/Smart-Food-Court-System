from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from .models import Customer
from .forms import UserForm
from webapp.models import Order
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

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
            customer = Customer(user=user, phone=phone)
            group = Group.objects.get(name='Customer')
            user.group.add(group)
            user.save()
            customer.save()
            return redirect('login-page')  
        else:
            context['user'] = 1     
    return render(request, 'users/signup.html', context)

@login_required
def profile(request):
    customers = request.user.customer
    orders = Order.objects.filter(order_by=request.user)
    context = {
        'customers': customers,
        'orders': orders, 
    }
    return render(request, 'users/profile.html', context)

@login_required
def edit_profile(request):
    customers = request.user.customer
    orders = Order.objects.filter(order_by=request.user)
    form = UserForm(instance=customers)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=customers)
        if form.is_valid():
            form.save()
            #messages.success(request,f'Tài khoản của bạn đã được cập nhật!')
            #customers.save()
            return redirect('profile')
    context = {
        'form': form,
        'customers': customers,
        'orders': orders,
    }
    return render(request, 'users/edit_profile.html', context)
