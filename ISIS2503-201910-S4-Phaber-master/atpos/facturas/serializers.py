from .models import factura
from rest_framework import serializers

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = factura
        fields = ('pk', 'cliente', 'venta',)
        read_only_fields = ('pk',) 
