"""
A module for urls in the products app
"""
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports
# 3rd Party
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


# Provide an app name to fix namespace error

urlpatterns = [
    # path('', views.all_products, name='all_products'),
    path(
        '', views.ProductListView.as_view(),
         name='all_products'
         ),
    # path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path(
        'detail/<slug:slug>/',
         views.product_detail,
         name='product_detail'
         ),
    path(
        'create_product/',
         views.ProductCreateView.as_view(),
         name='create_product'
         ),
    path(
        '<slug:slug>/update/',
         views.ProductUpdateView.as_view(),
         name='update_product'
         ),
    path(
        '<slug:slug>/delete/',
         views.ProductDeleteView.as_view(),
         name='delete_product'
         ),
    path(
        'search/', views.ProductSearchView.as_view(),
         name='search_products'
         ),
    path(
        '<int:id>/update-inventory/',
         views.InventoryUpdateView.as_view(),
         name='update_inventory'
         ),
    path(
        'inventory/',
        views.InventoryListView.as_view(),
        name='inventory_list'
        ),
    path(
        'colors/', views.ColorListView.as_view(),
        name='color_list'
        ),
    path(
        '<int:pk>/delete_color/',
        views.ColorDeleteView.as_view(),
        name='delete_color'
        ),
    path(
        '<int:pk>/update_color/',
        views.ColorUpdateView.as_view(),
        name='update_color'
        ),
    path(
        'create_color/',
        views.ColorCreateView.as_view(),
        name='add_color'
        ),
    path(
        'brands/',
        views.BrandListView.as_view(),
        name='brand_list'
        ),
    path(
        '<int:pk>/delete_brand/',
        views.BrandDeleteView.as_view(),
        name='delete_brand'
        ),
    path(
        '<int:pk>/update_brand/',
        views.BrandUpdateView.as_view(),
        name='update_brand'
        ),
    path(
        'create_brand/',
        views.BrandCreateView.as_view(),
        name='add_brand'
        ),
    path(
        'categories/',
        views.CategoryListView.as_view(),
        name='category_list'
        ),
    path(
        '<int:pk>/delete_category/',
        views.CategoryDeleteView.as_view(),
        name='delete_category'
        ),
    path(
        '<int:pk>/update_category/',
        views.CategoryUpdateView.as_view(),
        name='update_category'
        ),
    path(
        'create_category/',
        views.CategoryCreateView.as_view(),
        name='add_category'
        ),
]
