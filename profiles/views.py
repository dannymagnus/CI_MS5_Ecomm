"""
A module for views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd party:
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import DetailView, UpdateView
# Internal
from .models import UserProfile
from .forms import UserProfileForm
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class ProfileDetailView(DetailView):
    """
    Display the user's profile.
    Args:
        request (object): HTTP request object.
    Returns:
        Render of users profile page with context
    """
    model = UserProfile
    context_object_name = 'user_object'
    template_name = 'profiles/profile.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        return context

class ProfileUpdateView(UpdateView):
    """
    A class view to update userprofile
    """
    model = UserProfile
    form_class = UserProfileForm
    template_name = 'profiles/update_profile.html'

    def form_valid(self, form):
        messages.success(self.request, "Profile updated succesfully")
        super().form_valid(form)
        return HttpResponseRedirect(self.get_success_url())
