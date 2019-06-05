from rest_framework import generics, mixins
from .models import factura
from .serializers import FacturaSerializer

class FacturaListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = FacturaSerializer

    def get_queryset(self):
        return factura.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class FacturaRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = FacturaSerializer

    def get_queryset(self):
        return factura.objects.all()