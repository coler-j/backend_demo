from django.contrib.auth import get_user_model
from django.db import models
from django_fsm import FSMField, transition
from model_utils.models import TimeStampedModel


class Task(TimeStampedModel):
    """
    A model to contain task data.

    :param created_by: The user who create the task (assigned on creation)
    :param assigned_to: The user that the task is assigned to (can also be NULL).
    :param title: The task title (what the task is about).
    :param details: The task details and description (optional).
    :param due_date: The task due date (optional)

    """

    class STATE:
        NEW = 'NEW'
        CANCELED = 'XXX'
        IN_PROGRESS = 'INP'
        COMPLETED = 'CMP'

    STATE_CHOICES = ((STATE.NEW, 'New'),
                     (STATE.CANCELED, 'Canceled'),
                     (STATE.IN_PROGRESS, 'In progress'),
                     (STATE.COMPLETED, 'Completed'))
    state = FSMField(default=STATE.NEW, choices=STATE_CHOICES)
    created_by = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='tasks',
                                   editable=False)
    assigned_to = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                                    null=True, blank=True,
                                    related_name='assigned_tasks')
    title = models.CharField(max_length=255)
    details = models.TextField(null=True, blank=True)
    due_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title

    @transition(field=state, source=STATE.NEW, target=STATE.IN_PROGRESS)
    def start(self):
        """
        The `start` FSM transition (has no side effects).
        """
        pass

    @transition(field=state, source=[STATE.NEW, STATE.IN_PROGRESS], target=STATE.CANCELED)
    def cancel(self):
        """
        The `cancel` FSM transition (has no side effects).
        """
        pass

    @transition(field=state, source=[STATE.NEW, STATE.IN_PROGRESS], target=STATE.COMPLETED)
    def complete(self):
        """
        The `complete` FSM transition (has no side effects).
        """
        pass
