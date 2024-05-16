from .models import Task
from tasks.serializers import TaskSerializer
from rest_framework import viewsets

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def get_queryset(self):
        return self.request.user.task.all() #Task is the related name in Task Model, return tasks for user has been auth
    
    '''
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer
    '''
