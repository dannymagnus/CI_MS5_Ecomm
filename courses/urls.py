from django.urls import path
from . import views

urlpatterns = [
    path(
        '',
        views.CourseListView.as_view(),
        name = 'course_list'
        ),
        path(
        'create/',
        views.CourseCreateView.as_view(),
        name='create_course'
        ),
        path(
        '<slug:slug>/',
        views.CourseDetailView.as_view(),
        name='course_detail'
        ),
        path(
        '<slug:slug>/update/',
        views.CourseUpdateView.as_view(),
        name='update_course'
        ),
        path(
        '<slug:slug>/delete/',
        views.CourseDeleteView.as_view(),
        name='delete_course'
        ),
]
