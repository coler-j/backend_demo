from django.contrib.auth import get_user_model
from django.db import models
from model_utils.models import TimeStampedModel


class Task(TimeStampedModel):
    """
    A model to contain task data.

    :param created_by: The user who create the task (assigned on creation)
    :param assigned_to: The user that the task is assigned to (can also be NULL).
    :param task_description: The task details (what the task is about).

    """
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks',
                                   editable=False)
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='assigned_tasks')
    task_description = models.CharField(max_length=255)

    def __str__(self):
        return self.task_description
