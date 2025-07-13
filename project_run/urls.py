
from django.contrib import admin
from django.urls import path, include
from app_run.views import company_detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/company_details/', company_detail),
    path('api/', include('app_run.urls')),
]