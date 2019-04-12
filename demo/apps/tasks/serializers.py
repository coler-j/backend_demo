from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from demo.apps.tasks.models import Task


class TaskSerializer(ModelSerializer):
    """
    A serialize for the Task model. Sets the `created_by` user to `current_user` by default.
    """
    created_by = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )

    class Meta:
        model = Task
        fields = ['created_by', 'assigned_to', 'task_description']
