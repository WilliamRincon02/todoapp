from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import get_user_model


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=get_user_model().objects.all(), slug_field="username"
    )

    class Meta:
        model = Task
        fields = ["id", "name", "description", "priority", "user", "completed"]

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super(TaskSerializer, self).create(validated_data)
