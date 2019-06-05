from django.db import models
from venta.models import Sale
# Create your models here.


class Bill(models.Model):
    client = models.CharField(max_length=50)
    sale = models.ForeignKey(Sale, default=None, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.pk)
