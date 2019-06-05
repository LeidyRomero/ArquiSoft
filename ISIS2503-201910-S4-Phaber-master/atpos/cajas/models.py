from django.db import models

class caja(models.Model):
      dineroActual = models.CharField(max_length = 15)
      resolucionDeFacturacion = models.CharField(max_length = 15)
      lectorCodigoBarras =  models.BooleanField(default=False)
      bascula = models.DecimalField(max_digits= 2, decimal_places = 2)
      cajonMonedero = models.BooleanField(default=False)
      impresoraPOS = models.BooleanField(default=False)

      def ___str___(self):
          return self.pk 