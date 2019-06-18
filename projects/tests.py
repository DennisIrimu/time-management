from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Projects
from .serializers import SongsSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_project(name="", description="", start_date="", duration="",):
        if name != "" and description != "" and start_date !="" and duration !="":
            Projects.objects.create(name=name, description=description, start_date=start_date, duration=duration)

    def setUp(self):
        self.create_project("e-commerce","website to sell vehicles", "Monday", duration="two months")

class GetAllProjectsTest(BaseViewTest):

    def test_get_all_projects(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
    
    expected = Projects.objects.all()