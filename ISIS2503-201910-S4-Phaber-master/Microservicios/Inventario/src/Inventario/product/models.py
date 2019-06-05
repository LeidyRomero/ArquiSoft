from django.db import models

# Create your models here.
class product(models.Model):
    codigoBarras = models.CharField(max_length = 14, primary_key= True)
    precio =  models.DecimalField(max_digits = 7, decimal_places = 3)
    unidades = models.IntegerField(default = 0)
    iva = models.DecimalField(max_digits = 2, decimal_places = 2)
    nombre = models.CharField(max_length = 15)
    categoria = models.CharField(max_length=15)

    def ___str___(self):
        return self.nombre
