from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app_run.models import Run
from app_run.serializer import RunSerializer, UserSerializer

User = get_user_model()

@api_view(['GET'])
def company_detail(request):
    details = {'company_name': settings.COMPANY_NAME,
               'slogan': settings.SLOGAN,
               'contacts': settings.CONTACTS,
               }

    return Response(details)


class RunModelViewSet(viewsets.ModelViewSet):
    queryset = Run.objects.select_related('athlete').all()
    serializer_class = RunSerializer


class UserReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.filter(is_superuser=False)
    serializer_class = UserSerializer

    def get_queryset(self):
        qs = self.queryset
        param_type = self.request.query_params.get('type', None)
        if param_type is not None and param_type == 'athlete':
            qs = qs.filter(is_staff=False)
        elif param_type is not None and param_type == 'coach':
            qs = qs.filter(is_staff=True)
        return qs