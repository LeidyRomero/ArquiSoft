from rest_framework import generics, mixins
from .models import producto
from .serializers import ProductoSerializer
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
import requests

class ProductoListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ProductoSerializer
    def get_queryset(self):
        return producto.objects.all()

    @login_required
    def post(self, request, *args, **kwargs):
        role = getRole(request)
        if role == "Administrador" or "Manejador Inventario":
            return self.create(request, *args, **kwargs)
        else:
            return HttpResponse("Unauthorized User")


def getRole(request):
    user = request.user
    auth0user = user.social_auth.get(provider="auth0")
    accessToken = auth0user.extra_data['access_token']
    url = "https://atpos-phaber.auth0.com/userinfo"
    headers = {'authorization': 'Bearer ' + accessToken}
    resp = requests.get(url, headers=headers)
    userinfo = resp.json()
    role = userinfo['https://atpos-phaber.auth0.com/role']
    return (role)

class ProductoRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ProductoSerializer

    def get_queryset(self):

        return producto.objects.all()

