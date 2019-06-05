from .models import reporte
from rest_framework import serializers

class ReporteSerializer(serializers.ModelSerializer):
    class Meta:
        model = reporte
        fields = ('pk', 'fecha', 'productos', 'total')
        read_only_fields = ('pk', 'valor')