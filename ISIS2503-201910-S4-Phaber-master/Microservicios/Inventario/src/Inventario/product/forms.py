from django import forms

from .models import product

class ProductForm(forms.ModelForm):

    codigoBarras = forms.CharField(label='Codigo de Barras',
                             widget=forms.TextInput(attrs={"placeholder": "Codigo de Barras"}))
    nombre = forms.CharField(label='Nombre',
                             widget=forms.TextInput(attrs={"placeholder": "Nombre del producto"}))
    precio = forms.DecimalField()
    unidades = forms.IntegerField(initial=0)
    iva = forms.DecimalField(max_digits=2, decimal_places=2, initial=0.0)
    categoria = forms.CharField(label='Categoria',
                           widget=forms.TextInput(attrs={"placeholder": "Categoria del producto"}))


    class Meta:
        model = product
        fields = [
            'codigoBarras',
            'nombre',
            'precio',
            'unidades',
            'iva',
            'categoria'
        ]
        labels = {
            'codigoBarras': 'CodigoBarras',
            'nombre': 'Nombre',
            'precio': 'Precio',
            'unidades': 'Unidades',
            'iva': 'Iva',
            'categoria': 'Categoria'
        }