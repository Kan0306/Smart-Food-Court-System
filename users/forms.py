from django.forms import ModelForm
from .models import Customer

class UserForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'address']
        labels = { 
            'name': 'Họ tên',
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ'
        }