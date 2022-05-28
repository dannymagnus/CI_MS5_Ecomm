from django import forms

from .models import Product, Inventory


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ['slug','holding', 'color',]


class InventoryModelForm(forms.ModelForm):
    class Meta:
        model = Inventory
        exclude = ['size', 'color', 'product',]