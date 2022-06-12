from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]