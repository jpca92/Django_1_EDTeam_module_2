from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import Task

class IndexView(APIView):
    def get(self, request):
        context = {
            'status': True,
            'content': 'Server is running',
        }
        return Response(context, status=status.HTTP_200_OK)


class TaskView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

