from django.contrib import admin
from .models import Customer, Manager, Cook
# Register your models here.
admin.site.register(Customer)
admin.site.register(Manager)
admin.site.register(Cook)