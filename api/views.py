from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status as httpstatus
from django.http import JsonResponse
from .serializers import TaskSerializer, TaskCommentSerializer
from .models import Task, TaskStatus, TaskImage, TaskComment

STATUSES_NOT_CHANGABLE_BY_ASIGNEE = ["new","done"]


class TaskListView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated 
    ]
    serializer_class = TaskSerializer
    
    def get_queryset(self):
        status = None

        if "slug" in self.kwargs.keys():
            status = self.kwargs["slug"]
                
        if status:
            queryset = Task.objects.filter(status__name = status)
        else:    
            queryset = Task.objects.all()
        return queryset


class TaskPatchView(APIView):
    permission_classes=[
        permissions.IsAuthenticated
    ]    
    def patch(self, request, pk):
        user = request.user
        task = Task.objects.filter(id=pk).first()
        
        if user == task.author:
            serializer = TaskSerializer(task, data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(data=serializer.data, status=httpstatus.HTTP_200_OK)
            return JsonResponse(data="wrong parameters",status=httpstatus.HTTP_400_BAD_REQUEST) 
        
        elif user in task.asignees.all():
            status = request.data.get("status")
            
            if status in STATUSES_NOT_CHANGABLE_BY_ASIGNEE:
                return Response("Not allowed to change to this status",status=httpstatus.HTTP_400_BAD_REQUEST)
            all_statuses = TaskStatus.objects.all()
            
            status_obj = None
            for obj in all_statuses:
                if obj.name == status:
                    status_obj = obj
                    break
            
            if status_obj:
                task.status = status_obj
                task.save()
                return Response("Status Updated",status=httpstatus.HTTP_200_OK)
            else:
                return Response("No Such Status", status=httpstatus.HTTP_400_BAD_REQUEST)
        
        return Response("YOU CAN NOT EDIT THIS TASK", status=httpstatus.HTTP_403_FORBIDDEN)
      
class TaskImageView(APIView):
    def post(self, request, *args, **kwargs):
        file = request.data.get('file')
        pk = kwargs["pk"]
        if file:
            TaskImage.objects.create(image=file, task_id=pk)
            return Response("Uploaded", status=httpstatus.HTTP_200_OK)
        return Response("Not Uploaded", status=httpstatus.HTTP_400_BAD_REQUEST)
    
class TaskCommentView(generics.ListCreateAPIView):
    permission_classes = [
        permissions.IsAuthenticated
    ]
    queryset = TaskComment.objects.all()
    serializer_class = TaskCommentSerializer