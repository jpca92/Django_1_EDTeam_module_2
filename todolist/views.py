from django.shortcuts import render
from rest_framework.views import APIView, status
from rest_framework.response import Response

class IndexView(APIView):
    def get(self, request):
        context = {
            'status': True,
            'content': 'Server is running',
        }
        return Response(context, status=status.HTTP_200_OK)

    