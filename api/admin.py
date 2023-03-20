from django.contrib import admin
from .models import Task, TaskImage, TaskStatus 

admin.site.register(Task)
admin.site.register(TaskImage)
admin.site.register(TaskStatus)