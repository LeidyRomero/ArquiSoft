from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r'ventas/', sale_list),
    url(r'ventasCreate/$', csrf_exempt(sale_create), name='ventasCreate')
]