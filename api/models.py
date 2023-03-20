from django.db import models
from django.contrib.auth import get_user_model
User=get_user_model()

class TaskStatus(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=10000)
    status = models.ForeignKey(TaskStatus, on_delete=models.PROTECT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="created_tasks")
    asignees = models.ManyToManyField(User, related_name="assigned_tasks", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class TaskImage(models.Model):
    task = models.ForeignKey(Task, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media')

    def __str__(self):
        return "image"

class TaskComment(models.Model):
    task = models.ForeignKey(Task, related_name="comments", on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name="comments", on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=False)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')

    def __str__(self):
        return self.text[:50]

