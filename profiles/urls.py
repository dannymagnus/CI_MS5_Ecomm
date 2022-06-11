from django.urls import path
from . import views

urlpatterns = [
    path('', views.ProfileDetailView.as_view(), name='profile'),
    path('<int:pk>/update/', views.ProfileUpdateView.as_view(), name='update_profile'),
]