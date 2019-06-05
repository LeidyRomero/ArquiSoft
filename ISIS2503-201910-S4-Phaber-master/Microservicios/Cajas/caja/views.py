from django.shortcuts import render
from .models import Caja
# Create your views here.
from django.http import HttpResponse, JsonResponse
from datetime import datetime, timedelta, time
import json
import decimal
from .models import Caja


def cajas_list(request):
    queryset = Caja.objects.all()
    context = list(queryset.values('id', 'dineroActual',
                                   'resolucionDeFacturacion',
                                   'lectorCodigoBarras',
                                   'bascula',
                                   'cajonMonedero',
                                   'impresoraPOS'))
    return JsonResponse(context, safe=False)


def cajas_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        cajas_json = json.loads(data)
        caja = Caja()
        caja.dineroActual = cajas_json["dineroActual"]
        caja.resolucionDeFacturacion = cajas_json["resolucionDeFacturacion"]
        caja.lectorCodigoBarras = bool(cajas_json["lectorCodigoBarras"])
        caja.bascula = float(cajas_json["bascula"])
        caja.cajonMonedero = cajas_json["cajonMonedero"]
        caja.impresoraPOS = cajas_json["impresoraPOS"]
        caja.save()
        return HttpResponse("Caja registered.")
    else:
        return HttpResponse("This is a POST method")