# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.contrib import admin

# Internal
from .models import Category, Product, Brand, Size, Inventory, Color
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin Class for Category Model
    """
    list_display = (
        'name',
    )


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    """
    Admin Class for Category Model
    """
    list_display = (
        'name',
    )


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Admin Class for Product Model
    """
    list_display = (
        'name',
        'category',
        'brand',
    )
    prepopulated_fields = {
        "slug": ("name",)
        }  # new
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
    inlines = (
        InventoryInline,
        )

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    """
    Admin class for Brand Model
    """
    list_display = (
        'name',
    )


@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    """
    Admin class for Sizes Model
    """
    list_display = (
        'name',
    )
