
from .models import Task
from django.contrib.auth.models import User
from rest_framework import serializers

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.SlugRelatedField(queryset=User.objects.all(), slug_field='username')

    class Meta:
        model = Task
        fields = ['name', 'description', 'priority', 'user']
    
