from rest_framework import generics, mixins
from .models import caja
from .serializers import CajaSerializer

class CajaListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = CajaSerializer

    def get_queryset(self):
        return caja.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CajaRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = CajaSerializer

    def get_queryset(self):
        return caja.objects.all()