from django.urls import include, path
from facturas.views import *

urlpatterns = [
    path('', FacturaListView.as_view(), name='facturas-list'),
    path('<int:pk>', FacturaRudView.as_view(), name='facturas-rud'),
]
