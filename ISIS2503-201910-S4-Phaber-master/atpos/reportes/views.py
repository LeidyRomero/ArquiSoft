from rest_framework import generics
from .models import reporte, venta
from .serializers import ReporteSerializer
from django.shortcuts import render, redirect
from datetime import datetime, timedelta, time
from reportes.forms import ReporteForm
from django.http import HttpRequest
import requests
import hashlib
from django.conf import settings 
import os
class ReporteListView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = ReporteSerializer

    def get_queryset(self):
        return reporte.objects.all()

class ReporteRudView(generics.RetrieveAPIView):
    lookup_field = 'pk'
    serializer_class = ReporteSerializer

    def get_queryset(self):
        return reporte.objects.all()


def generar_reporte(request):
    today = datetime.now().date()
    tomorrow = today + timedelta(1)
    today_start = datetime.combine(today, time())
    today_end = datetime.combine(tomorrow, time())
    ventas = venta.objects.filter(fecha__range=[today_start, today_end])
    total = 0
    productos = []
    for i in ventas:
        total+=i.valor
        prod = i.productos.all()
        for j in prod:
            productos.append(j)
    
    #Genera json
    path = settings.REPORTES_ROOT+"Reporte-"+str(today_start.strftime("%Y-%m-%d"))+".json"
    print(path)
    file = open(path,"w+") 
    file.write("{\n\"fecha\": \""+str(today_start.strftime("%Y-%m-%d"))+"\",\n") 
    file.write("\"productos\": [\n") 
    for val in productos:
        file.write("{\n\"codigoBarras\": \""+str(val.codigoBarras)+"\",\n")
        file.write("\"precio\": \""+str(val.precio)+"\",\n")
        file.write("\"iva\": \""+str(val.iva)+"\",\n")
        file.write("\"nombre\": \""+str(val.nombre)+"\"\n},\n")
    file.seek(file.tell() - 2, os.SEEK_SET)
    file.write("\n],\n\"total\": \""+str(total)+"\"\n}") 
    file.close()

    #Envio request al server
    f = open(path, "r")
    if f.mode == "r":
        contentJson = f.read()
        hashEnviar = hashlib.sha256(str(contentJson).encode('utf-8'))
        digestEnviar = hashEnviar.hexdigest()
        payload = {'hash': digestEnviar, 'informacion': contentJson}
        r = requests.post('https://apidian.club/reportes/reportes/post', data=payload)
        if r.status_code == requests.codes.ok :
            print('Envio a la DIAN realizado con exito.')
        else:
            print('Error con el envio. Codigo error:')
        print(r.status_code)
    #Realiza el post del reporte
    form = ReporteForm()
    post = form.save(commit=False)
    post.fecha = today_start
    post.total = total
    #post.productos = productos
    post.save()
    return redirect('/api/reportes/')