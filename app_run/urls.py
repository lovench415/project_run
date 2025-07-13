from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import RunModelViewSet, UserReadOnlyModelViewSet

router = DefaultRouter()
router.register('runs', RunModelViewSet)
router.register('users', UserReadOnlyModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]