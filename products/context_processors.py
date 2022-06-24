"""
A module for context in the products app
"""
from .models import Brand, Category


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
