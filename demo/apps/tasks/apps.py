from django.apps import AppConfig


class TasksAppConfig(AppConfig):

    name = "demo.apps.tasks"
    label = "tasks"
    verbose_name = "Tasks"

    def ready(self):
        try:
            import users.signals  # noqa F401
        except ImportError:
            pass
