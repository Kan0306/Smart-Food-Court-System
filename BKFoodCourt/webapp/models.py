from django.db import models
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
#from maintenance_mode.core import set_maintenance_mode
#from django.contrib.sites.models import Site

# Create your models here.
class Menu(models.Model):
    stallname = models.CharField(max_length=500)

    def __str__(self):
        return self.stallname

class Item(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    description = models.TextField(blank=True)
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

"""def maintenance_mode_off(request):
    #Deactivate maintenance-mode and redirect to site root.
    #Only superusers are allowed to use this view.
    if request.user.is_superuser:
        set_maintenance_mode(False)

    return HttpResponseRedirect('/')


def maintenance_mode_on(request):
    #Activate maintenance-mode and redirect to site root.
    #Only superusers are allowed to use this view.
    if request.user.is_superuser:
        set_maintenance_mode(True)

    return HttpResponseRedirect('/')

class Maintenance(models.Model):
    site = models.OneToOneField(Site, on_delete=models.CASCADE, related_name='sites')
    is_being_performed = models.BooleanField(
        ('In Maintenance Mode'), default=False
    )
    class Meta:
        verbose_name = verbose_name_plural = ('Maintenance Mode')

    def __str__(self):
        return self.site.domain

    def ignored_url_patterns(self):
        qs = self.ignoredurl_set.values_list(
            "pattern", flat=True
            )
        return list(qs)

class IgnoredURL(models.Model):
    maintenance = models.ForeignKey(Maintenance, on_delete=models.CASCADE)
    pattern = models.CharField(max_length=255)
    description = models.CharField(
        max_length=75, help_text= ('What this URL pattern covers.')
    )

    def __str__(self):
        return self.pattern"""
