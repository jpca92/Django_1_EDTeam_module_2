from rest_framework import serializers
from .models import Task

"""First way to do the serializer"""
# class TaskSerializer(serializers.Serializer):
#     title = serializers.CHarField(required=True)
#     description = serializers.CharField(required=True)

"""Second way to do the serializer"""
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'