"""
A module for filters in the products app
"""
import django_filters
from django import forms
from .models import Course

class CourseFilter(django_filters.FilterSet):
    """
    A class to filter the product model
    """

    class Meta:
        model = Course
        fields = {
            'level': ['iexact'],
        }
