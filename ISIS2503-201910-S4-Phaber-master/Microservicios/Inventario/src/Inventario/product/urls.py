from django.urls import path
from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    path('productos/<pk>/', views.darProducto, name='detail'),
    path('productos/', views.listarProductos),
    path('', views.index),
    url(r'productocreate/$', csrf_exempt(views.registrar)),
]