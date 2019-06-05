from .models import Report
from venta.models import Sale
from datetime import datetime, timedelta, time
from django.http import HttpResponse
from django.http import JsonResponse
import hashlib
import requests
import os

# Constraints
REPORTS_ROOT = "./generated_reports/"


# Views


def report_list(request):
    queryset = Report.objects.all()
    context = list(queryset.values('id', 'date', 'sales', 'total'))
    return JsonResponse(context, safe=False)


def generate_report(request):
    if request.method == 'GET':
        today = datetime.now().date()
        tomorrow = today + timedelta(1)
        today_start = datetime.combine(today, time())
        today_end = datetime.combine(tomorrow, time())
        sales = Sale.objects.filter(date__range=[today_start, today_end])
        total = 0
        report = Report()
        report.date = today_start
        for sale in sales:
            report.sales += str(sale.id) + ','
            total += sale.value
        report.total = total
        report.save()

        # Generate Json File
        path = REPORTS_ROOT + "Reporte-" + str(today_start.strftime("%Y-%m-%d")) + ".json"
        if os.path.isdir(REPORTS_ROOT) == False:
            os.mkdir(REPORTS_ROOT)
        file = open(path, "w+")
        file.write("{\n\"date\": \"" + str(today_start.strftime("%Y-%m-%d")) + "\",\n")
        file.write("\"sales\": [\n")
        for sale in sales:
            file.write("{ \n\"date\":\"" + str(sale.date.strftime("%Y-%m-%d")) + "\"\n")
            file.write("\"paymentType\":\"" + sale.paymentType + "\"\n")
            file.write("\"products\":\"" + sale.products + "\"\n")
            file.write("\"value\":\"" + str(sale.value) + "\"\n},")
        file.seek(file.tell() - 2, os.SEEK_SET)
        file.write("\n],\n\"total\": \"" + str(total) + "\"\n}")
        file.close()

        # Senging request to API DIAN simulator
        f = open(path, "r")
        if f.mode == "r":
            content_json = f.read()
            hash_a_enviar = hashlib.sha256(str(content_json).encode('utf-8'))
            digest_a_enviar = hash_a_enviar.hexdigest()
            payload = {'hash': digest_a_enviar, 'informacion': content_json}
            r = requests.post('https://apidian.club/reportes/reportes/post', data=payload)
            if r.status_code == requests.codes.ok:
                print('Envio a la DIAN realizado con exito.')
            else:
                print('Error con el envio. Codigo error:')
            print(r.status_code)

        return HttpResponse("Report" + str(report.date) + " generated. \n \n" + content_json)
    else:
        return HttpResponse("This is a GET method")
