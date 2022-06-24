"""
A module for views in the products app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import render, get_object_or_404
from django.shortcuts import HttpResponseRedirect, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView
# Internal
from .models import Product, Inventory, Category, Color, Brand
from .forms import ProductModelForm, InventoryModelForm
from .filters import ProductFilter, InventoryFilter, ProductOrderFilter
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class ProductListView(ListView):
    """
    A class view to view all products
    """
    model = Product
    paginate_by = 12
    ordering = ['name']

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        if search_results.qs:
            self.no_search_result = False
        # Returns the default queryset if an empty
        # queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductFilter(
            self.request.GET, queryset=self.get_queryset()
            )
        return context


class ProductSearchView(ListView):
    """
    A class view to view all products
    """
    model = Product
    paginate_by = 12

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = ProductFilter(self.request.GET, self.queryset)
        queryset = search_results.qs.distinct()
        query = self.request.GET.get('q')
        if not query:
            messages.info(
                self.request, 'You did not enter any search criteria'
                )
            return Product.objects.none()
        if query:
            search_results = queryset.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query) |
                Q(category__name__icontains=query) |
                Q(brand__name__icontains=query) |
                Q(holding__name__icontains=query) |
                Q(holding__friendly_name__icontains=query)).distinct()
        if search_results:
            self.no_search_result = False
        # Returns the queryset returned by the django_filters
        return search_results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = ProductOrderFilter(
            self.request.GET, queryset=Product.objects.all()
            )
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
    raise_exception = True
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Product created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)


class ProductUpdateView(UserPassesTestMixin, UpdateView):
    """
    A class view to update products
    """
    template_name = 'products/create_product.html'
    form_class = ProductModelForm
    queryset = Product.objects.all()

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = True
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_object(self, queryset=queryset):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug_)

    def form_valid(self, form):
        messages.success(self.request, "Product updated succesfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, "Sorry there was an error")
        return self.render_to_response(self.get_context_data(form=form))


class ProductDeleteView(UserPassesTestMixin, DeleteView):
    """
    A class view to delete products
    """
    template_name = 'products/delete_product.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_object(self, queryset=None):
        slug_ = self.kwargs.get("slug")
        return get_object_or_404(Product, slug=slug_)

    def get_success_url(self, **kwargs):
        messages.success(self.request, "Product removed successfully")
        success_url = reverse('all_products')
        return success_url


class InventoryListView(UserPassesTestMixin, ListView):
    """
    A class to render all the product inventory
    """
    model = Inventory
    paginate_by = 15

    def __init__(self):
        self.no_search_result = True

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_queryset(self, **kwargs):
        search_results = InventoryFilter(
            self.request.GET, self.queryset
            )
        if search_results.qs:
            self.no_search_result = False
        # Returns the default queryset if an empty
        # queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['filter'] = InventoryFilter(
            self.request.GET, queryset=self.get_queryset()
            )
        return context


class InventoryUpdateView(UserPassesTestMixin, UpdateView):
    """
    A class to update the product inventory item count
    """
    template_name = 'products/update_inventory.html'
    form_class = InventoryModelForm
    queryset = Inventory.objects.all()
    success_url = '/products/inventory'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_object(self, queryset=queryset):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Inventory, id=id_)

    def form_valid(self, form):
        messages.success(self.request, 'Inventory updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, "Sorry there was an error")
        return self.render_to_response(self.get_context_data(form=form))


class ColorListView(UserPassesTestMixin, ListView):
    """
    A class view to list colors
    """
    model = Color
    template_name = '/products/color_list.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'


class ColorDeleteView(UserPassesTestMixin, DeleteView):
    """
    A class view to delete colors
    """
    model = Color
    template_name = 'products/delete_color.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Color removed successfully')
        success_url = '/products/colors/'
        return success_url


class ColorUpdateView(UserPassesTestMixin, UpdateView):
    """
    A class view to update colors
    """
    model = Color
    fields = ('__all__')
    template_name = 'products/update_color.html'
    success_url = '/products/colors/'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Color updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
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
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Color added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Something went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)

    success_url = '/products/colors'


class BrandListView(UserPassesTestMixin, ListView):
    """
    A view for to list brands
    """
    model = Brand
    template_name = '/products/brand_list.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'


class BrandDeleteView(UserPassesTestMixin, DeleteView):
    """
    A class view to delete brands
    """
    model = Brand
    template_name = 'products/delete_brand.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Brand removed successfully')
        success_url = '/products/brands'
        return success_url


class BrandUpdateView(UserPassesTestMixin, UpdateView):
    """
    A class view to update brands
    """
    model = Brand
    fields = ('__all__')
    template_name = 'products/update_brand.html'
    success_url = '/products/brands'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Brand updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)


class BrandCreateView(UserPassesTestMixin, CreateView):
    """
    A class view to create brands
    """
    model = Brand
    fields = ('__all__')
    template_name = 'products/add_brand.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Brand added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)

    success_url = '/products/brands'


class CategoryListView(UserPassesTestMixin, ListView):
    """
    A class view to list categories
    """
    model = Category
    template_name = '/products/category_list.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'


class CategoryDeleteView(UserPassesTestMixin, DeleteView):
    """
    A class view to delete categories
    """
    model = Category
    template_name = 'products/delete_category.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_success_url(self, **kwargs):
        messages.success(self.request, 'Category removed successfully')
        success_url = '/products/categories'
        return success_url


class CategoryUpdateView(UserPassesTestMixin, UpdateView):
    """
    A class view to update colors
    """
    model = Category
    fields = ('__all__')
    template_name = 'products/update_category.html'
    success_url = '/products/categories'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Category updated successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Something went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)


class CategoryCreateView(UserPassesTestMixin, CreateView):
    """
    A class view to create brands
    """
    model = Category
    fields = ('__all__')
    template_name = 'products/update_category.html'

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Category added successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)

    success_url = '/products/categories'
