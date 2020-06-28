from django.db import models
from django.contrib.auth.models import User
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
    def deleteItem(self,id):
        Item.objects.filter(id=id).delete()
        pass

class Item(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.TextField(blank=True, max_length=300)
    price = models.DecimalField(max_digits=8, decimal_places=0)
    available = models.BooleanField(default=True)
    belongs_to_stall = models.ForeignKey(Menu, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

class Order(models.Model):
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
    
    def get_absolute_url(self):
        return reverse("payment",kwargs={"id":self.id})

    def get_absolute_return_url(self):
        return reverse("order-status", kwargs={"id":self.id})

class Manager(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='manager')
    phone = models.CharField(max_length=500, blank=True)
    address = models.CharField(max_length=500, blank=True)
    own_stall = models.ManyToManyField(Menu)
    