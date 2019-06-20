from django.urls import path,re_path
from . import views
from .views import ListProjectsView,LoginView,RegisterUsers


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('auth/login/', LoginView.as_view(), name="auth_login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth_register"),
    re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
]