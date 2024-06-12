from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

@receiver(post_save, sender = User)
def create_jwt_token(sender, instance=None, created=False, **kwargs):
    if created:
        refresh = RefreshToken.for_user(instance)
        instance.jwt_access_token = str(refresh.access_token)
        instance.jwt_refresh_token = str(refresh)
        instance.save()