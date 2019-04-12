from rest_framework import routers

from demo.apps.tasks.views import TaskViewSet

router = routers.SimpleRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')
urlpatterns = router.urls
