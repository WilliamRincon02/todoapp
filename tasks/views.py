from .models import Task
from tasks.serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class TaskViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter, DjangoFilterBackend]
    filterset_fields = ['completed']
    ordering_fields = ["priority", "completed"]

    def get_queryset(self):
        return (
            self.request.user.tasks.all()
        )  # Task is the related name in Task Model, return tasks for user has been auth
