from rest_framework import serializers

from .models import Task, TaskImage, TaskComment


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("title", "status","description", "author", "created_at","edited_at", "images","comments")

class TaskCommentSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = TaskComment
        fields = ("task", "author", "text", "parent")