from django.db import models
from django.contrib.auth.models import User
from webapp.models import Menu
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=500, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return self.name

class Manager(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    own_stall = models.ForeignKey(Menu, on_delete=models.CASCADE)