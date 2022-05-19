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
    path('detail/<slug:slug>/', views.ProductDetailView.as_view(), name='product_detail'),
]
