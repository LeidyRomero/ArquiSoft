from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r'reportes/', report_list, name='report-list'),
    url(r'generarReporte/', csrf_exempt(generate_report), name='generarReporte')
]