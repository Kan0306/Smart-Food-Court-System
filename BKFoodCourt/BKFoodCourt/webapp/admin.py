from django.contrib import admin
from .models import Item,Menu,Order,OrderItem
# Register your models here.
admin.site.register(Item)
admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)