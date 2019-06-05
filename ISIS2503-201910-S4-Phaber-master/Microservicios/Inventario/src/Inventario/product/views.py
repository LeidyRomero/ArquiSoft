from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.http import JsonResponse
from .models import product
import json

from .forms import ProductForm
from .models import product


# Create your views here.
def buscar(request, codigoBarras):
    return HttpResponseRedirect("Detalles del producto %s" %codigoBarras)

def registrar(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        producto = product()
        producto.codigoBarras = data_json["codigoBarras"]
        producto.precio = data_json["precio"]
        producto.unidades = data_json["unidades"]
        producto.iva = data_json["iva"]
        producto.nombre = data_json["nombre"]
        producto.categoria = data_json["categoria"]
        producto.save()
        return HttpResponse("El registro del producto fue exitoso")




def listarProductos(request):
    queryset = product.objects.all()
    context = list(queryset.values('codigoBarras', 'precio', 'unidades', 'iva', 'nombre', 'categoria'))
    return JsonResponse(context, safe=False)

def darProducto(request, pk = None):
    if pk:
        producto = product.objects.get(codigoBarras= pk)

    return JsonResponse({'codigoBarras':  producto.codigoBarras, "precio": producto.precio, "unidades": producto.unidades, "iva": producto.iva, "nombre": producto.nombre, "categoria": producto.categoria})


def index(request):
    return render(request, 'index.html')

