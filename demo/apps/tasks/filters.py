from django_filters import rest_framework as filters
from demo.apps.tasks.models import Task


class TaskFilter(filters.FilterSet):
    """
    Filter to enable searching on the `Task` models
    """

    class Meta:
        model = Task
        fields = {
            'title': ['iexact', 'icontains']
        }
