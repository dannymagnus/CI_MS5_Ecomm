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
    path('', views.ProductListView.as_view(), name='all_products'),
    # path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('detail/<slug:slug>/', views.product_detail, name='product_detail'),
    path('create/', views.ProductCreateView.as_view(), name='create_product'),
    path('<slug:slug>/update/', views.ProductUpdateView.as_view(), name='update_product'),
    path('<slug:slug>/delete/', views.ProductDeleteView.as_view(), name='delete_product'),
]
