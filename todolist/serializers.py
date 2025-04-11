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

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.state == '1':
            state = 'To Do'
        elif instance.state == '2':
            state = 'Completed'
        representation['state'] = state
        return representation