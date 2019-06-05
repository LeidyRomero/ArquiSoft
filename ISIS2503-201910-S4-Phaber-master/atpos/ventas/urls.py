from django.urls import include, path
from ventas.views import *

urlpatterns = [
    path('', VentaListView.as_view(), name='ventas-list'),
    path('<int:pk>', VentaRudView.as_view(), name='ventas-rud'),
]