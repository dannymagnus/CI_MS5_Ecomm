# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render


# Internal:
from .models import Faq
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def about(request):
    """
    A view to show restaurant bio,
    reasons to dine, chef images and bio,
    and comments
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
