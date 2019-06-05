from django.db import models

class cliente(models.Model):
    nombre = models.CharField(max_length=50)
    identificacion = models.CharField(max_length=50)
    puntos = models.IntegerField(default=0)
    def __str__(self):
        return self.nombre