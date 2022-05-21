from django.shortcuts import render, get_object_or_404
from .models import Product, Inventory
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView

# Create your views here.
class ProductListView(ListView):
    model = Product
    paginate_by = 15

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


# def all_products(request):
    
#     products = Product.objects.all()
    
    
#     context = {
#         'products':products,
#         # 'inventory':inventory,
#         }
    
#     return render(request, 'products/all_products.html', context)

# class ProductDetailView(DetailView):
#     model = Product
#     template_name = 'products/product_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context
    

def product_detail(request, slug):
    """
    A view to detailed product view, all product information
    Args:
        request (object): HTTP request object.
    Returns:
        Render of products page with context
    """
    product = get_object_or_404(Product, slug=slug)
    variants = product.inventory_set.all()
    context = {
        'product': product,
        'variants': variants,
        }
    return render(request, 'products/product_detail.html', context)