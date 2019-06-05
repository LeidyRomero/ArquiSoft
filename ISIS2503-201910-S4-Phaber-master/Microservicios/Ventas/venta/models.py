from django.db import models
from datetime import datetime


# Create your models here.
class Sale(models.Model):
    date = models.DateTimeField(default=datetime.now)
    paymentType = models.CharField(max_length=50, default='efectivo')
    products = models.CharField(max_length=150)
    value = models.FloatField(default=0)
    
    def __str__(self):
        return str(self.pk)
