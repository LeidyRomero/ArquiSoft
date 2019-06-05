from django.urls import include, path
from clientes.views import *

urlpatterns = [
    path('', ClienteListView.as_view(), name='clientes-list'),
    path('<int:pk>', ClienteRudView.as_view(), name='clientes-rud'),
]