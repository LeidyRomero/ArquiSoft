# Generated by Django 2.2 on 2019-04-17 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='caja',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dineroActual', models.CharField(max_length=15)),
                ('resolucionDeFacturacion', models.CharField(max_length=15)),
                ('lectorCodigoBarras', models.BooleanField(default=False)),
                ('bascula', models.DecimalField(decimal_places=2, max_digits=2)),
                ('cajonMonedero', models.BooleanField(default=False)),
                ('impresoraPOS', models.BooleanField(default=False)),
            ],
        ),
    ]
