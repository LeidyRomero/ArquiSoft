from django.urls import include, path
from django.db import models
from clientes.models import cliente
from ventas.models import venta 

class factura(models.Model):
    cliente = models.ForeignKey(cliente, default=None, blank=True, on_delete=models.CASCADE)
    venta = models.ForeignKey(venta, default=None, blank=True, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.pk)