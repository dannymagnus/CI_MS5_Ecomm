from django.shortcuts import render, get_object_or_404
from .models import Product, Inventory

# Create your views here.
def all_products(request):
    
    products = Product.objects.all()
    
    
    context = {
        'products':products,
        # 'inventory':inventory,
        }
    
    return render(request, 'products/all_products.html', context)