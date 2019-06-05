from django.db import models
from datetime import datetime
# Create your models here.


class Report(models.Model):
    date = models.DateTimeField(default=datetime.now)
    # Sales are saved as an array in a csv line.
    sales = models.CharField(max_length=300)
    total = models.FloatField(default=0)

    def __str__(self):
        return str(self.pk)