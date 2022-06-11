import django_filters
from .models import Product, Inventory
from django.forms.widgets import HiddenInput
from django import forms

class ProductFilter(django_filters.FilterSet):
    """
    A class to filter the product model
    """
    
    CHOICES = (
        ('priceasc' , 'Price (Ascending)'),
        ('pricedesc','Price (Descending)'),
        ('namedesc','Name (Descending)'),
        ('nameasc','Name (Ascending)'),
    )
    
    ordering = django_filters.ChoiceFilter(label='Ordering', choices=CHOICES, method='filter_by_order')
    
    class Meta:
        model = Product
        fields = {
            'name': ['iexact'],
            'category__name': ['iexact'],
            'brand__name': ['iexact'],
        }
        widgets = {'name': forms.HiddenInput()}
    
    def filter_by_order(self,queryset,name,value):
        if value == 'priceasc':
            expression = 'price'
        elif value == 'pricedesc':
            expression = '-price'
        elif value == 'namedesc':
            expression = 'name'
        else:
            expression = '-name'
        return queryset.order_by(expression)


class InventoryFilter(django_filters.FilterSet):
    """
    A class to filter the inventory model
    """

    class Meta:
        model = Inventory
        fields = {
            'sku': ['iexact'],
            'product__name': ['icontains'],
            'product__brand__name': ['icontains'],
        }
