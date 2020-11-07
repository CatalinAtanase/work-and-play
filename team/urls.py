from django.urls import include, path
from rest_framework import routers
from .views import (
   TeamViewSet,
   TeamPointsViewSet,
   TeamDetailsViewSet
)

router = routers.DefaultRouter()
router.register('details', TeamDetailsViewSet)
router.register('points', TeamPointsViewSet)
router.register('', TeamViewSet)

urlpatterns = [
    path('team/', include(router.urls)),
]
