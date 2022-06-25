"""
A module for context in the products app
"""
from .models import Brand, Category, Product


def brands(request):
    """
    A function to return brands
    """
    return {
        'brands': Brand.objects.all()
    }


def categories(request):
    """
    A function to return categories
    """
    return{
        'categories': Category.objects.all()
    }

def products(request):
    """
    A function to return products
    """
    return{
        'products':Product.objects.all()
    }
