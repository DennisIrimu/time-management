from django.urls import path
from .views import ListProjectsView


urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name="projects-all")
]