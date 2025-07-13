from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import RunModelViewSet, UserReadOnlyModelViewSet, StartRunAPIView, StopRunAPIView

router = DefaultRouter()
router.register('runs', RunModelViewSet)
router.register('users', UserReadOnlyModelViewSet)

urlpatterns = [
    path('runs/<int:run_id>/start/', StartRunAPIView.as_view()),
    path('runs/<int:run_id>/stop/', StopRunAPIView.as_view()),
    path('', include(router.urls))
]