"""
A module for views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render
# Internal:
from .models import Faq
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def about(request):
    """
    A view to show business Faqs
    Args:
        request (object): HTTP request object.
    Returns:
        Render of items page with context
    """
    faqs = Faq.objects.all()
    context = {
        'faqs': faqs,
        }
    return render(request, 'about/about.html', context)
