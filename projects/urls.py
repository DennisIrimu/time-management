from django.urls import path
from .views import ListProjectsView


urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('auth/login/' LoginView.as_view(), name="auth_login")
]