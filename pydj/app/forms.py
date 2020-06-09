#app/forms.py
from django import forms
from .models import *

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
    description = forms.CharField(max_length=300, label="Mô tả", widget=forms.Textarea)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class ContactForm(forms.Form):
    full_name = forms.CharField(max_length=30,label='Họ tên')
    phone = forms.CharField(max_length=20,label='Số điện thoại')
    address = forms.CharField(max_length=200,label='Địa chỉ')