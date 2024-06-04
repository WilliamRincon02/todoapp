from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import User


# class Task (models.Model):
#     name = models.CharField(max_length=200)
#     description = models.TextField()

class Task (models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.PositiveSmallIntegerField(default=0)
    user = models.ForeignKey(
        User,
        on_delete=models.RESTRICT,
        limit_choices_to={'is_superuser': False},
        related_name='tasks',
        null = True
    )

    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name