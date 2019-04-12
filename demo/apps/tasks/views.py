from rest_framework.viewsets import ModelViewSet
from demo.apps.tasks.models import Task
from demo.apps.tasks.serializers import TaskSerializer


class TaskViewSet(ModelViewSet):
    """
    Provides default CRUD operations for a model.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
