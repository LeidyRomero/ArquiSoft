from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken import views
from atpos.views import base
from reportes.views import generar_reporte

from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('api/cajas/', include('cajas.urls'), name='cajas'),
    path('api/productos/', include('productos.urls'), name='productos'),
    path('api/ventas/', include('ventas.urls'), name='ventas'),
    path('api/facturas/', include('facturas.urls'), name='facturas'),
    path('api/clientes/', include('clientes.urls'), name='clientes'),
    path('api/reportes/', include('reportes.urls'), name='reportes'),
    path('admin/', admin.site.urls),
    path('', base, name='home'),
    url(r'^#/$', generar_reporte, name='generar_reporte'),
]

urlpatterns += [
    path('api/auth', include('rest_framework.urls'), name='rest_framework')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)