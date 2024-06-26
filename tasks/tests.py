from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from .models import Task

class TasksTests(APITestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        user_class = get_user_model()
        cls.user = user_class.objects.create(username="jhon", email="foo@bar.com")
        refresh = RefreshToken.for_user(cls.user)
        cls.access_token = str(refresh.access_token)
        cls.task = Task.objects.create(
            name="My Task", description="My task description", user=cls.user
        )

    @classmethod
    def tearDownClass(cls):
        cls.task.delete()
        cls.user.delete()
        super().tearDownClass()

    def setUp(self):
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_get_task_list(self):
        url = reverse("task-list")
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.task.name)

    def test_get_task_detail(self):
        url = reverse("task-detail", kwargs={"pk": self.task.id})
        response = self.client.get(url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data.get("name"), self.task.name)