from django import forms
from .models import Product, Inventory


class ProductModelForm(forms.ModelForm):
    """
    A form class for the Product model.
    """
    class Meta:
        model = Product
        fields = ['name',
                  'description',
                  'friendly_name',
                  'description',
                  'category',
                  'gender',
                  'brand',
                  'holding',
                  'color',
                  'price',
                  'image',
                  ]
        widgets = {
            'holding': forms.CheckboxSelectMultiple,
        }


class InventoryModelForm(forms.ModelForm):
    """
    A form class for the Product model.
    """
    class Meta:
        model = Inventory
        fields = ['count',]
