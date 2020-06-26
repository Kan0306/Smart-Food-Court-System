from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    stall_id = models.CharField(max_length=20,blank=False,unique=True,primary_key=True)
    stallname = models.CharField(max_length=500)

    def __str__(self):
        return self.stallname
    def get_absolute_url(self):
        return reverse("stall-menu",kwargs={"id":self.id})

class Item(models.Model):
    item_id = models.CharField(max_length=20,blank=False,unique=True,primary_key=True)
    name = models.CharField(max_length=500)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.TextField(blank=True, max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    available = models.BooleanField(default=True)
    belongs_to_stall = models.ForeignKey(Menu, on_delete=models.CASCADE)

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)
    SIZE_CHOICES = (
        ("NHỎ", "Nhỏ"),
        ("VỪA", "Vừa"),
        ("LỚN", "Lớn")
    )
    size = models.CharField(max_length=20, choices=SIZE_CHOICES, default="VỪA")


class Order(models.Model):
    order_id = models.CharField(max_length=20,blank=False,unique=True,primary_key=True)
    item = models.ManyToManyField(OrderItem)
    is_ready = models.BooleanField(default=False)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateTimeField(auto_now_add=True)
    ORDER_STAT_CHOICES = (
        ("ONGOING", "Ongoing"),
        ("ACCEPT","Accept"),
        ("CONFIRMED", "Confirmed"),
        ("WAITING", "Waiting"),
        ("READY", "Ready"),
        ("COMPLETED", "Completed")
    )
    status = models.CharField(max_length=100, choices=ORDER_STAT_CHOICES, default="ONGOING")


    