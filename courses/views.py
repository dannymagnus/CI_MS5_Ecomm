"""
A module for views
"""
# Imports
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 3rd Party
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.views.generic import DetailView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib import messages
# Internal
from .filters import CourseFilter
from .models import Course
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class CourseListView(ListView):
    """
    A class view to view all products
    """
    model = Course
    ordering = ['level']

    def __init__(self):
        self.no_search_result = True

    def get_queryset(self, **kwargs):
        search_results = CourseFilter(
            self.request.GET, self.queryset
            )
        if search_results.qs:
            self.no_search_result = False
        # Returns the default queryset if an
        # empty queryset is returned by the django_filters
        return search_results.qs.distinct() or self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CourseFilter(
            self.request.GET, queryset=self.get_queryset()
            )
        return context


class CourseDetailView(DetailView):
    """
    A view for Course details
    """
    model = Course


class CourseCreateView(UserPassesTestMixin, CreateView):
    """
    A view for Course details
    """
    model = Course
    fields = ('__all__')

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Course created successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        context.update({"Error": "Soemthing went wrong"})
        messages.error(self.request, 'Sorry, something went wrong')
        return self.render_to_response(context)


class CourseUpdateView(UserPassesTestMixin, UpdateView):
    """
    A view for Course details
    """
    model = Course
    fields = ('__all__')

    def test_func(self):
        """
        Function to verify that user is staff level
        """
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def form_valid(self, form):
        messages.success(self.request, 'Course updated successfully')
        return super().form_valid(form)


class CourseDeleteView(UserPassesTestMixin, DeleteView):
    """
    A class view to delete products
    """
    model = Course

    def test_func(self):
        return self.request.user.is_staff
    raise_exception = False
    redirect_field_name = '/'
    permission_denied_message = "You are not authorised to view this page"
    login_url = '/accounts/login'

    def get_object(self, queryset=None):
        """
        A method to get the object
        """
        slug_ = self.kwargs.get('slug')
        return get_object_or_404(Course, slug=slug_)

    def get_success_url(self):
        messages.success(self.request, "Course removed successfully")
        return reverse('course_list')
