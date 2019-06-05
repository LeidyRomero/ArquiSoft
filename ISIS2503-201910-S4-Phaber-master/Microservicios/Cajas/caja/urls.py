from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt
from .views import *

urlpatterns = [
    url(r'cajas/', cajas_list, name='reportes-list'),
    url(r'cajasCreate/', csrf_exempt(cajas_create), name='cajasCreate')
]