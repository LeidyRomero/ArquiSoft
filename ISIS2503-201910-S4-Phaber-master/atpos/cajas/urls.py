from django.urls import include, path
from cajas.views import *

urlpatterns = [
    path('', CajaListView.as_view(), name='cajas-list'),
    path('<int:pk>', CajaRudView.as_view(), name='cajas-rud'),
]