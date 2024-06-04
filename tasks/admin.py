from django.contrib import admin

# Register your models here.

from django.contrib import admin

from .models import Task


class TasksAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "description", "user_id", "priority", "completed")
    search_fields = ["name"]


admin.site.register(Task)
