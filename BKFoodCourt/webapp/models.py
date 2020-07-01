from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    stallname = models.CharField(max_length=500)
    owner = models.CharField(max_length=50, blank=True)
    contact_phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.stallname
    def get_absolute_url(self):
        return reverse("stall-menu",kwargs={"id":self.id})

class Item(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.TextField(blank=True, max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    available = models.BooleanField(default=True)
    belongs_to_stall = models.ForeignKey(Menu, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("item-info",kwargs={"id":self.id})

class Order(models.Model):
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
    
    def get_absolute_url(self):
        return reverse("payment",kwargs={"id":self.id})

    def get_absolute_return_url(self):
        return reverse("bill", kwargs={"id":self.id})

    def get_status_url(self):
        return reverse("order-status", kwargs={"id":self.id})
    
    def sum_price(self):
        sum = 0
        for item in self.orderitem_set.all():
            sum += item.get_sum()
        return sum
    def sum_item(self):
        sum = 0
        for item in self.orderitem_set.all():
            sum += item.quantity
        return sum

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def get_sum(self):
        return self.item.price * self.quantity




    