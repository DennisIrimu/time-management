from django.shortcuts import render
from .models import Projects
from .rest_framework import generics
from .serializers import ProjectsSerializer
# Create your views here.

class ListProjectsView(generics.LisyAPIView):
    queryset = Projects.objects.all()
    serializer_class =  ProjectsSerializer
