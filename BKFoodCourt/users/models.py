from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer')
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)