from django.shortcuts import render

# Create your views here.

from django.core.serializers import serialize
from django.http import JsonResponse

from .models import Task
from django.contrib.auth.models import User

def index(request):
    tasks = Task.objects.all()
    data = serialize('python', tasks)
    return JsonResponse(data, safe=False)

def users(request):
    users = []

    for user in User.objects.all():
        if (user.is_superuser != True):
            users.append(user)

    data = serialize('python', users)
    return JsonResponse(data, safe=False)
