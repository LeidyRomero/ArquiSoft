from rest_framework import generics, mixins
from .models import venta, producto
from .serializers import VentaSerializer

class VentaListView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = VentaSerializer

    def get_queryset(self):
        return venta.objects.all()

    def post(self, request, *args, **kwargs):
        rta = self.create(request, *args, **kwargs)
        ventas = venta.objects.all()
        for i in ventas:
            productos = i.productos.all()
            total = 0
            for j in productos:
                total+=j.precio
            i.valor = total
            i.save()
        total = venta.objects.get(pk=rta.data['pk']).valor
        rta.data['valor']=total
        return rta

class VentaRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    serializer_class = VentaSerializer

    def get_queryset(self):
        return venta.objects.all()