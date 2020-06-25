from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Customer
from django.core.exceptions import ValidationError
# Create your views here.

def register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('name')
        phone    = request.POST.get('phoneNumber')
        email    = request.POST.get('email')
        password = request.POST.get('password')
        authpass = request.POST.get('authpassword')
        if User.objects.filter(username=username).exists() == False and password == authpass:
            user = User(username=username, password=password, email=email)
            customer = Customer(user=user, phone=phone)
            user.save()
            customer.save()
            return redirect('login-page')  
        else:
            context['user'] = 1     
    return render(request, 'users/signup.html', context)