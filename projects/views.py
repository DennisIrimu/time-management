from django.shortcuts import render
from rest_framework import generics
from .models import Projects
from .serializers import ProjectsSerializer
# Create your views here.

class ListProjectsView(generics.ListAPIView):
    queryset = Projects.objects.all()
    serializer_class =  ProjectsSerializer
