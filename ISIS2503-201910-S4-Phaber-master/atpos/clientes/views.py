from rest_framework import generics, mixins
from .models import cliente
from .serializers import ClienteSerializer

class ClienteListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return cliente.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ClienteRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = ClienteSerializer

    def get_queryset(self):
        return cliente.objects.all()