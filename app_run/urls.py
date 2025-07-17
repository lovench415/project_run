from django.urls import path, include
from rest_framework.routers import DefaultRouter

from app_run.views import RunModelViewSet, UserReadOnlyModelViewSet, StartRunAPIView, StopRunAPIView, \
    AthleteInfoAPIView, ChallengeUserReadOnlyModelViewSet

router = DefaultRouter()
router.register('runs', RunModelViewSet)
router.register('users', UserReadOnlyModelViewSet)
router.register('challenges', ChallengeUserReadOnlyModelViewSet)
# router.register('positions', PositionsModelViewSet)

urlpatterns = [
    path('runs/<int:run_id>/start/', StartRunAPIView.as_view()),
    path('runs/<int:run_id>/stop/', StopRunAPIView.as_view()),
    path('athlete_info/<int:user_id>/', AthleteInfoAPIView.as_view()),
    path('', include(router.urls))
]