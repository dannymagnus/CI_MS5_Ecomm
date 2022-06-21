"""
about/urls.py: urls for the about app
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.urls import path
# Internal
from . import views
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('<slug:slug>/add/', views.add_to_bag, name='add_to_bag'),
    path('adjust/<inventory_id>/', views.adjust_bag, name='adjust_bag'),
    path('remove/<inventory_id>/', views.remove_from_bag, name='remove_from_bag'),
]
