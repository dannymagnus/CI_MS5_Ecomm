from django.shortcuts import render, get_object_or_404, reverse, HttpResponseRedirect, redirect
from django.contrib import messages

from .models import UserProfile
from django.views.generic import DetailView, UpdateView
from .models import UserProfile, User
from .forms import UserProfileForm


class ProfileDetailView(DetailView):

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
