from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from .models import Task

# Create your tests here.

class TasksTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="jhon", email="foo@bar.com")
        cls.token, created = Token.objects.get_or_create(user=cls.user)
        # cls.token = Token.objects.create(user=cls.user)
        cls.task = Task.objects.create(
            name="My Taks", description="My task description", user=cls.user
        )

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.token.delete()
        cls.user.delete()

    def setUp(self):
        self.client.force_authenticate(user=self.user, token=self.token)

    def test_get_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # self.assertEqual(len(response.data.get("results")), 1)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.task.name)

    def test_get_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.task.name)
