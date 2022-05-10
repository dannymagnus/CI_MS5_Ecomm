# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Category, Product, Brand
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(Category)
class MealAdmin(admin.ModelAdmin):
    """
    Admin Class for Category Model
    """
    list_display = (
        'name',
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin Class for Product Model
    """
    list_display = (
        'name',
        'category',
        'brand',
        'sku',
    )
    list_filter = (
        'category',
        'brand',
        )
    search_fields = (
        'name',
        'description',
        'category',
        'sku',
        'brand',
        'color',
        )


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Admin class for Brand Model
    """
    list_display = (
        'name',
    )