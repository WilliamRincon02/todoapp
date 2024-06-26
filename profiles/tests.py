# from django.test import TestCase
# from django.urls import reverse
# from django.contrib.auth.models import User
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import Profile

# class Profile(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_superuser(
#             username='admin',
#             email='admin@example.com',
#             password='admin123',
#             first_name='Admin',
#             last_name='User',
#             bio='This is the admin user.',
#             is_superuser=True
#         )
#         self.client.force_authenticate(user=self.user)

#     def test_create_profile(self):
#         url = reverse('profile-list')
#         data = {
#             "username": "testuser",
#             "first_name": "Test",
#             "last_name": "User",
#             "email": "testuser@example.com",
#             "bio": "Test bio",
#             "is_superuser": False
#         }
#         response = self.client.post(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)
#         self.assertEqual(Profile.objects.count(), 1)
#         self.assertEqual(Profile.objects.get().username, 'testuser')

#     def test_retrieve_profile(self):
#         profile = Profile.objects.create(
#             username='testuser',
#             first_name='Test',
#             last_name='User',
#             email='testuser@example.com',
#             bio='Test bio',
#             is_superuser=False
#         )
#         url = reverse('profile-detail', kwargs={'pk': profile.pk})
#         response = self.client.get(url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['username'], 'testuser')

#     def test_update_profile(self):
#         profile = Profile.objects.create(
#             username='testuser',
#             first_name='Test',
#             last_name='User',
#             email='testuser@example.com',
#             bio='Test bio',
#             is_superuser=False
#         )
#         url = reverse('profile-detail', kwargs={'pk': profile.pk})
#         data = {
#             "username": "updateduser",
#             "first_name": "Updated",
#             "last_name": "User",
#             "email": "updateduser@example.com",
#             "bio": "Updated bio",
#             "is_superuser": False
#         }
#         response = self.client.put(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Profile.objects.get(pk=profile.pk).username, 'updateduser')

#     def test_partial_update_profile(self):
#         profile = Profile.objects.create(
#             username='testuser',
#             first_name='Test',
#             last_name='User',
#             email='testuser@example.com',
#             bio='Test bio',
#             is_superuser=False
#         )
#         url = reverse('profile-detail', kwargs={'pk': profile.pk})
#         data = {"bio": "Updated bio"}
#         response = self.client.patch(url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(Profile.objects.get(pk=profile.pk).bio, 'Updated bio')

#     def test_delete_profile(self):
#         profile = Profile.objects.create(
#             username='testuser',
#             first_name='Test',
#             last_name='User',
#             email='testuser@example.com',
#             bio='Test bio',
#             is_superuser=False
#         )
#         url = reverse('profile-detail', kwargs={'pk': profile.pk})
#         response = self.client.delete(url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         self.assertEqual(Profile.objects.count(), 0)
