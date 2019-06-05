from django.db import models
from ventas.models import venta
from productos.models import producto
from datetime import datetime

class reporte(models.Model):
    fecha = models.DateTimeField(default=datetime.now)
    productos = models.ManyToManyField(producto)
    total = models.FloatField(default=0)
    def __str__(self):
        return str(self.pk)