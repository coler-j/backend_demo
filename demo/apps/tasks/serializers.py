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
    state_display = serializers.CharField(source='get_state_display', read_only=True)

    class Meta:
        model = Task
        fields = ['created_by', 'assigned_to', 'title', 'details', 'due_date', 'state', 'state_display']
