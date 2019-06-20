from django.urls import path
from . import views
#from .views import ListProjectsView,LoginView,RegisterUsers


urlpatterns = [
    path('signup/', views.SignUP.as_view(), name='signup'),
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    path('auth/login/', LoginView.as_view(), name="auth_login"),
    path('auth/register/', RegisterUsers.as_view(), name="auth_register"),
    
]