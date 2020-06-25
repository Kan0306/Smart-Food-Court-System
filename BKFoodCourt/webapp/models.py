from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Menu(models.Model):
    stallname = models.CharField(max_length=500)

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


class Order(models.Model):
    item = models.ManyToManyField(Item)
    is_ready = models.BooleanField(default=False)
    order_by = models.ForeignKey(User, on_delete=models.CASCADE)
    ORDER_STAT_CHOICES = (
        ("ONGOING", "Ongoing"),
        ("ACCEPT","Accept"),
        ("CONFIRMED", "Confirmed"),
        ("WAITING", "Waiting"),
        ("READY", "Ready"),
        ("COMPLETED", "Completed")
    )
    status = models.CharField(max_length=100, choices=ORDER_STAT_CHOICES, default="ONGOING")


    