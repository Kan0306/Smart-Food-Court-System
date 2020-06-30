from django.contrib import admin
from .models import Item, Menu, OrderItem, Order
# Register your models here.
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(OrderItem)
admin.site.register(Order)