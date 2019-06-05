# Generated by Django 2.2 on 2019-04-18 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ventas', '0004_auto_20190417_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='venta',
            name='metodoPago',
            field=models.CharField(default='efectivo', max_length=50),
        ),
        migrations.AlterField(
            model_name='venta',
            name='valor',
            field=models.FloatField(default=0),
        ),
    ]