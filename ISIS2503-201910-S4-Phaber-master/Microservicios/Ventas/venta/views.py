from .models import Sale
from django.http import HttpResponse, JsonResponse
from datetime import datetime
from django.conf import settings
import json
import requests

def get_product_price(product_id):
    r = requests.get(settings.PATH_APIGATEWAY + "/productos/" + product_id, headers={"Accept": "application/json"})
    product = r.json()
    if product_id == product["codigoBarras"]:
        return product["precio"]
    else:
        return 0


def sale_list(request):
    queryset = Sale.objects.all()
    context = list(queryset.values('id', 'date', 'paymentType', 'products', 'value'))
    return JsonResponse(context, safe=False)


def sale_create(request):
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        sale_json = json.loads(data)
        sale = Sale()
        sale.date = datetime.now().date()
        sale.paymentType = sale_json["paymentType"]
        sale.products = sale_json["products"]
        # Now we calculate the value of the sale.
        product_list = sale.products.split(',')
        value = 0
        for product in product_list:
            price = get_product_price(product)
            if price != 0:
                value += float(price)
            else:
                return HttpResponse("One of the products does not exit.")
        sale.value = value
        sale.save()
        return HttpResponse("Sale registered")
    else:
        return HttpResponse("This is a POST method")