from django.db import models


# MODELS
class Caja(models.Model):
    dineroActual = models.CharField(max_length=15)
    resolucionDeFacturacion = models.CharField(max_length=15)
    lectorCodigoBarras = models.BooleanField(default=False)
    bascula = models.FloatField()
    cajonMonedero = models.BooleanField(default=False)
    impresoraPOS = models.BooleanField(default=False)

    def ___str___(self):
        return str(self.pk)
