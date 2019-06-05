from .models import producto
from rest_framework import serializers

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = producto
        fields = ('pk', 'codigoBarras', 'precio', 'unidades', 'iva', 'nombre', 'categoria',)
        read_only_fields = ('pk',)