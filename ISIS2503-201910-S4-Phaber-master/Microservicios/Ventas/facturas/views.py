# Create your views here.

from .models import Bill
from django.http import HttpResponse
from django.http import JsonResponse
from django.conf import settings
import requests
import json
from venta.models import Sale


def check_client(data):
    document = data["client"]
    r = requests.get(settings.PATH_APIGATEWAY + "/clientes/" + document, headers={"Accept":"application/json"})
    client = r.json()
    if document == client["identificacion"]:
        return True
    return False


def bill_list(request):
    queryset = Bill.objects.all()
    context = list(queryset.values('id', 'client', 'sale'))
    return JsonResponse(context, safe=False)


def bill_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        data_json = json.loads(data)
        if check_client(data_json):
            bill = Bill()
            bill.client = data_json["client"]
            bill.sale = Sale.objects.get(id=data_json["sale"])
            bill.save()
            return HttpResponse("Bill created.")
        else:
            return HttpResponse("Could not create the bil, client is not in the system.")
    else:
        return HttpResponse("This is a POST method")
