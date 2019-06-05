from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('venta.urls'), name='ventas'),
    path('', include('facturas.urls'), name='facturas'),
    path('', include('reportes.urls'), name='reportes'),
    path('', admin.site.urls),
]