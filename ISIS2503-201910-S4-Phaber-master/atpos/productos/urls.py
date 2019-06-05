from django.urls import include, path
from productos.views import *
from django.conf.urls import url, include

urlpatterns = [
    path('', ProductoListView.as_view(), name='productos-list'),
    path('<int:pk>', ProductoRudView.as_view(), name='productos-rud'),
    url(r'login/auth0', include('django.contrib.auth.urls')),
    url(r'^', include('social_django.urls')),
]