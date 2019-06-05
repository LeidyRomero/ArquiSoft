from django import forms
from  .models import reporte
from productos.models import producto
from django.forms.widgets import CheckboxSelectMultiple
from django.contrib.auth.models import Group

class ReporteForm(forms.ModelForm):
    fecha = forms.DateTimeField()
    total = forms.FloatField()
    #productos = forms.ModelMultipleChoiceField(queryset=producto.objects.all())

    class Meta:
        model = reporte
        fields = ("fecha", 
        #        "productos", 
                "total")