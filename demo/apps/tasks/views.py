from djangorestframework_fsm.viewset_mixins import get_drf_fsm_mixin
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from demo.apps.tasks.filters import TaskFilter
from demo.apps.tasks.models import Task
from demo.apps.tasks.serializers import TaskSerializer


class TaskViewSet(get_drf_fsm_mixin(Task, fieldname='state'), ModelViewSet):
    """
    Provides default CRUD operations for a model.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filterset_class = TaskFilter
