from django.urls import include, path
from rest_framework import routers
from .views import (
    SprintDetailsViewSet,
    TaskCategoryViewSet,
    StatusViewSet,
    TaskViewSet,
    TaskDetailsViewSet,
    ChatTaskViewSet,
    ChatMessageViewSet,
    SprintViewSet,
    SprintLatest,
)

router = routers.DefaultRouter()
router.register('task-categories', TaskCategoryViewSet)
router.register('status', StatusViewSet)
router.register('tasks', TaskViewSet)
router.register('tasks-details', TaskDetailsViewSet)
router.register('chat', ChatTaskViewSet) #id
router.register('chat-messages', ChatMessageViewSet)
router.register('sprint', SprintViewSet)
router.register('sprint-details', SprintDetailsViewSet)
router.register('sprint-latest', SprintLatest)

urlpatterns = [
    path('', include(router.urls)),
]
