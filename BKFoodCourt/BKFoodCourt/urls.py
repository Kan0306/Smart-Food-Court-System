"""BKFoodCourt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp import views as web_views
from users import views as users_views
from kitchen import views as cook_views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from maintenance_mode.views import maintenance_mode_off, maintenance_mode_on


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', web_views.home, name='home-page'),
    path('menu/', web_views.menu, name='main-menu'),
    path('item-info/<int:id>', web_views.item_info, name='item-info'),
    path('about/', web_views.about, name='about'),
    path('preference/', web_views.preference, name='preference'),
    path('stall-menu/<int:id>/', web_views.menustall, name='stall-menu'),
    path('login/', auth_views.LoginView.as_view(template_name='users/signin.html', redirect_authenticated_user='home-page'), name='login-page'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/signout.html'), name='logout-page'),
    path('register/', users_views.register, name='register'),
    path('cart/', web_views.shopping_cart, name='shopping-cart'),
    path('bill/<int:id>', web_views.bill, name='bill'), 
    path('status/<int:id>', web_views.order_status, name='order-status'),  
    path('payment/<int:id>/', web_views.payment, name='payment'),
    path('search/', web_views.search, name='search'),
    path('update_order/', web_views.update_order, name='update-order'),
    path('profile/', users_views.profile, name='profile'),
    path('profile/edit', users_views.edit_profile, name='edit-profile'),
    path('delete-item/<int:id>/',web_views.delete_item, name='delete-item'),
    path('update-item/<int:id>/',web_views.update_item, name='update-item'),
    path('create-item/<int:id>/',web_views.create_item, name='create-item'),
    path('checkout/<int:id>/', web_views.checkout, name='checkout'),
    re_path(r'^maintenance-mode/off/$', maintenance_mode_off, name='maintenance_mode_off'),
    re_path(r'^maintenance-mode/on/$', maintenance_mode_on, name='maintenance_mode_on'),
    path('order-list/',cook_views.order_list, name='order-list'),
    path('inform_ready/',cook_views.inform_ready, name='inform-ready'),
    path('inform_out/',cook_views.inform_out, name='inform-out'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)