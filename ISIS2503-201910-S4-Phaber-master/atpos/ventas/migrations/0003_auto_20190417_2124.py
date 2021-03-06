# Generated by Django 2.2 on 2019-04-17 21:24

import datetime
from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_auto_20190417_1050'),
        ('ventas', '0002_auto_20190417_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venta',
            name='cantidad',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='idProducto',
        ),
        migrations.RemoveField(
            model_name='venta',
            name='idVenta',
        ),
        migrations.AddField(
            model_name='venta',
            name='fecha',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='venta',
            name='productos',
            field=models.ManyToManyField(to='productos.producto'),
        ),
        migrations.AddField(
            model_name='venta',
            name='valor',
            field=models.FloatField(default=Decimal('2342.000')),
        ),
    ]
