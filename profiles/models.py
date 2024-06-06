from django.db import models

from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

# Create your models here.


class Profile(AbstractUser):
    bio = models.TextField(verbose_name="Biography", null=True, blank=True)
    jwt_access_token = models.TextField(blank=True, null=True)
    jwt_refresh_token = models.TextField(blank=True, null=True)
    
    @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    def create_auth_token(sender, instance=None, created=False, **kwargs):
        if created:
            Token.objects.create(user=instance)
