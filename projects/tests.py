from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Projects
from .serializers import ProjectsSerializer

# Create your tests here.

class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_project(name="", description="", start_date="", duration="",):
        if name != "" and description != "" and start_date !="" and duration !="":
            Projects.objects.create(name=name, description=description, start_date=start_date, duration=duration)

    def login_a_user(self, username="", password="")
        url = reverse(
            "auth-login",
            kwargs={
                "version":"v1"
            }
        )
        return self.client.post(
            url,
            data=json.dumps({
                "username": username
                "password": password
            }),
            content_type="application/json"
        )

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="dnyt",
            email = "haia@gmail.com",
            password = "1234567890",
            first_name = "boro",
            last_name = "yeng",
        )
        self.create_project("e-commerce","website to sell vehicles", "Monday", duration="two months")

class GetAllProjectsTest(BaseViewTest):

    def test_get_all_projects(self):
        response = self.client.get(
            reverse("songs-all", kwargs={"version": "v1"})
        )
    
    expected = Projects.objects.all()