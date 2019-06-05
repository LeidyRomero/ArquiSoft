from .models import caja
from rest_framework import serializers

class CajaSerializer(serializers.ModelSerializer):
    class Meta:
        model = caja
        fields = ('pk', 'dineroActual', 'resolucionDeFacturacion', 'lectorCodigoBarras', 'bascula', 'cajonMonedero', 'impresoraPOS',)
        read_only_fields = ('pk',)