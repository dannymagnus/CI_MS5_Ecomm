from django.shortcuts import render, get_object_or_404, reverse
from .models import Product, Inventory
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProductModelForm

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

class ProductCreateView(CreateView):
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()
    success_url = '/products'


class ProductUpdateView(UpdateView):
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug_)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)
