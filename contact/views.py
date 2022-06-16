# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import render

# Internal:
from .models import Contact
from .forms import ContactForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def contact_us(request):
    """
    A view to contact us page with contact form,
    get contact details and save to model
    Args:
        request (object): HTTP request object.
    Returns:
        Render of contact page with context
    """
    contact_form = ContactForm()
    contacted = False
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save()
            contacted = True
    context = {'contact_form': contact_form,
               'contacted': contacted, }

    return render(request, 'contact/contact.html', context)
