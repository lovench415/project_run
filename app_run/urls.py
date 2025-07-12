from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import RunModelViewSet

router = DefaultRouter()
router.register('runs', RunModelViewSet)

urlpatterns = [
    path('', include(router.urls))
]