from django.db.models import Q
from django.contrib import messages
from django.utils.http import urlencode
from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect, redirect
from .models import Product, Inventory, Category, Color
from django.views.generic import View, ListView, DetailView, CreateView, DeleteView, UpdateView
from .forms import ProductModelForm, InventoryModelForm
from .filters import ProductFilter, InventoryFilter, ProductOrderFilter
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin


class ProductListView(ListView):
    """
    A class view to view all products
    """
    model = Product
    paginate_by = 12
    
    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        # Returns the default queryset if an empty queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())
        return context


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


class ProductCreateView(UserPassesTestMixin, CreateView):
    """
    A class view to create products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()
    
    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name='/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'
    
    def form_valid(self, form):
        messages.success(self.request, f'Product created successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        return self.render_to_response(context)

    success_url = '/products'


class ProductUpdateView(UpdateView):
    """
    A class view to update products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug_)

    # def form_valid(self, form):
    #     return super().form_valid(form)
    def form_valid(self, form):
        messages.success(self.request, "Product updated succesfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())


class ProductDeleteView(DeleteView):
    """
    A class view to delete products
    """
    template_name = 'products/delete_product.html'
    success_url = '/products'

    def get_object(self):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug_)


class ProductSearchView(ListView):
    """
    A class view to view all products
    """
    model = Product
    paginate_by = 12
  
    def get_queryset(self, **kwargs):
        queryset = Product.objects.all()
        query = self.request.GET.get('q')
        categories= Category.objects.all()
        if query:
            queryset = Product.objects.filter(                
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(brand__name__icontains=query)  |
                Q(holding__name__icontains=query)   |
                Q(holding__friendly_name__icontains=query)).distinct()
        search_results = ProductFilter(self.request.GET, queryset)
        self.no_search_result = True if not search_results.qs else False
        # Returns the default queryset if an empty queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductOrderFilter(self.request.GET, queryset=self.get_queryset())
        return context


class InventoryListView(ListView):
    """
    A class to render all the product inventory
    """
    model = Inventory
    paginate_by = 15

    def get_queryset(self, **kwargs):
        search_results = InventoryFilter(self.request.GET, self.queryset)
        self.no_search_result = True if not search_results.qs else False
        # Returns the default queryset if an empty queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = InventoryFilter(self.request.GET, queryset=self.get_queryset())
        return context


def update_inventory(request, slug):
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
    return render(request, 'products/update_inventory.html', context)


class InventoryUpdateView(UpdateView):
    """
    A class to update the product inventory item count
    """
    template_name = 'products/update_inventory.html'
    form_class = InventoryModelForm
    queryset = Inventory.objects.all()
    success_url = '/products/inventory'

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory, id=id_)

    def form_valid(self, form):
        messages.success(self.request, f'Inventory updated successfully')
        return super().form_valid(form)


class ColorListView(ListView):
    
    model = Color
    template_name = '/products/color_list.html'


class ColorDeleteView(DeleteView):
    """
    A class view to delete colors
    """
    model = Color
    template_name = 'products/delete_color.html'
    
    
    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Color removed successfully')
        success_url = '/products/colors/'
        return success_url


class ColorUpdateView(UpdateView):
    """
    A class view to update colors
    """
    model = Color
    fields = ('__all__')
    template_name = 'products/update_color.html'
    success_url = '/products/colors/'
    
    def form_valid(self, form):
        messages.success(self.request, f'Color updated successfully')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.success(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)


class ColorCreateView(UserPassesTestMixin, CreateView):
    """
    A class view to create products
    """
    model = Color
    fields = ('__all__')
    template_name = 'products/add_color.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name='/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, f'Color added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        return self.render_to_response(context)

    success_url = '/products/colors'
