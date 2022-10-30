from rest_framework import serializers

from tasks.models import Task

class TaskSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'created_at', 'completed_at', 'owner']