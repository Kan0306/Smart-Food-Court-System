from django.forms import ModelForm
from .models import Item
from users.models import Customer

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name','image','description','price']
        labels = {
            "name" : "Tên món ăn",
            "image" : "Hình ảnh",
            "description" : "Miêu tả món ăn",
            "price" : "Giá"
        }
