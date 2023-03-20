from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIRequestFactory, force_authenticate
from django.contrib.auth import get_user_model
from .views import TaskListView, TaskPatchView
from .models import Task
User=get_user_model()

factory = APIRequestFactory()

class TaskListViewTest(TestCase):
    def test_not_authenticated(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 401)
    
    def test_authenticated(self):
        user = User.objects.create(username="testuser",password="testuser")
        request = factory.get("/tasks/")
        force_authenticate(request, user=user)
        view = TaskListView.as_view()
        response = view(request)
        self.assertEqual(response.status_code, 200)


class TaskPatchViewTest(TestCase):
    def test_not_authenticated(self):
        response = self.client.get(reverse("tasks"))
        self.assertEqual(response.status_code, 401)
    
    def test_authenticated(self):
        user = User.objects.create(username="testuser",password="testuser")
        task = Task.objects.create(title="testtask",description="test task",status_id=1, author=user)
        request = factory.patch("/task/1/")
        force_authenticate(request, user=user)
        view = TaskPatchView.as_view()
        response = view(request,pk=1)
        self.assertEqual(response.status_code, 200)
