from .models import venta
from rest_framework import serializers

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = venta
        fields = ('pk', 'fecha', 'productos', 'valor')
        read_only_fields = ('pk', 'valor')