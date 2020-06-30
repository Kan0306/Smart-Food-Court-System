from django import forms
from .models import Customer

class UserForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'image', 'phone', 'address']
        labels = {
            'name': 'Họ tên',
            'image': 'Ảnh đại diện',
            'phone': 'Số điện thoại',
            'address': 'Địa chỉ',
        }
