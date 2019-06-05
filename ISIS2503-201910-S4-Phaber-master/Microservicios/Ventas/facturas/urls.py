from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r'facturas/', bill_list),
    url(r'^facturasCreate/$', csrf_exempt(bill_create), name='facturasCreate'),
]
