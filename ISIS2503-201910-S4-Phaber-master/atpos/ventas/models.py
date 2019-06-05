from django.db import models
from productos.models import producto
from datetime import datetime


class venta(models.Model):
    fecha = models.DateTimeField(default=datetime.now)
    metodoPago = models.CharField(max_length=50, default='efectivo')
    productos = models.ManyToManyField(producto)
    valor = models.FloatField(default=0)
    def ___str___(self):
        return self.pk