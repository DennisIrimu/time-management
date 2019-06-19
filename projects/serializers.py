from rest_framework import serializers
from .models import Projects
from django.contrib.auth.models import User


class ProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = ("name", "description" ,"start_date", "duration")

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
