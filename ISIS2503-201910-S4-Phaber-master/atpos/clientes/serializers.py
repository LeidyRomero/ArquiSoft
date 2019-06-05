from .models import cliente
from rest_framework import serializers

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = cliente
        fields = ('pk', 'nombre', 'identificacion', 'puntos',)
        read_only_fields = ('pk',)

    def validate_identificacion(self, value):
        qs = cliente.objects.filter(identificacion__iexact=value)
        if qs.exists():
            raise serializers.ValidationError('Ya existe un usuario con la identificacion dada')
        return value