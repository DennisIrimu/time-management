from django.urls import path,re_path,include
from . import views
from .views import ListProjectsView,LoginView,RegisterUsers,DetailsView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    #path('signup/', views.signup, name='signup'),
    path('projects/', ListProjectsView.as_view(), name="projects-all"),
    re_path('projects/(?P<pk>[0-9]+)/$',DetailsView.as_view(), name="details"),
    re_path(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    #path('auth/login/', LoginView.as_view(), name="auth_login"),
    #path('auth/register/', RegisterUsers.as_view(), name="auth_register"),
    #re_path(r'^ajax/validate_username/$', views.validate_username, name='validate_username'),
    re_path(r'^users/$', UserView.as_view(), name="users"),
    re_path(r'users/(?P<pk>[0-9]+)/$',UserDetailsView.as_view(), name="user_details"),
    re_path(r'^get-token/', obtain_auth_token),
]