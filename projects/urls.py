from django.urls import path
from .views import ListProjectsView,LoginView,RegisterUsers


urlpatterns = [
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('auth/login/', LoginView.as_view(), name="auth_login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth_register")
]