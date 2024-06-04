from .models import Task
from tasks.serializers import TaskSerializer
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [OrderingFilter]
    ordering_fields = ["priority", "completed"]

    def get_queryset(self):
        return (
            self.request.user.tasks.all()
        )  # Task is the related name in Task Model, return tasks for user has been auth
