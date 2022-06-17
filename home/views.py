from django.shortcuts import render
from products.models import Product
from courses.models import Course


def index(request):
    products = Product.objects.filter(promoted=True)
    context = {
        'products': products,
               }
    return render(request, 'home/index.html', context,)
