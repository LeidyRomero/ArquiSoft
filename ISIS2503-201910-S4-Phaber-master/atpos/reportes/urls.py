from django.urls import include, path
from reportes.views import *

urlpatterns = [
    path('', ReporteListView.as_view(), name='reportes-list'),
    path('<int:pk>', ReporteRudView.as_view(), name='reportes-rud'),
]