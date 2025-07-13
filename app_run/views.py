from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

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
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']

    def get_queryset(self):
        qs = self.queryset
        param_type = self.request.query_params.get('type', None)
        if param_type is not None and param_type == 'athlete':
            qs = qs.filter(is_staff=False)
        elif param_type is not None and param_type == 'coach':
            qs = qs.filter(is_staff=True)
        return qs


class StartRunAPIView(APIView):
    def post(self, request, run_id):
        qs = Run.objects.select_related('athlete').all()
        obj_run = get_object_or_404(qs, id=run_id)
        if obj_run.status == 'init':
            obj_run.status = 'in_progress'
            obj_run.save()
            return Response({"text": 'Забег стартовал'}, status=status.HTTP_201_CREATED)
        return Response({"text": 'Невозможно выполнить операцию'}, status=status.HTTP_400_BAD_REQUEST)


class StopRunAPIView(APIView):
    def post(self, request, run_id):
        qs = Run.objects.select_related('athlete').all()
        obj_run = get_object_or_404(qs, id=run_id)
        if obj_run.status == 'in_progress':
            obj_run.status = 'finished'
            obj_run.save()
            return Response({"text": 'Забег завершился'}, status=status.HTTP_201_CREATED)
        return Response({"text": 'Невозможно выполнить операцию'}, status=status.HTTP_400_BAD_REQUEST)
