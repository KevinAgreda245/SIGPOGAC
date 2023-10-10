from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from Proyecto.models import *
from Reporte.utils import crearPDF

from .forms import *

def index(request):
 
    if request.method == 'POST':
        form = ReportesForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            estado = form.cleaned_data['estado']
            tipo_servicio = form.cleaned_data['tipo']
            fecha_desde = form.cleaned_data['fechaDesde']
            fecha_hasta = form.cleaned_data['fechaHasta']
            proyectos = Proyecto.objects.filter(FK_TIPO_SERVICIO = tipo_servicio)
            print(tipo_servicio)
            if cliente:
                proyectos = proyectos.filter(FK_CLIENTE=cliente)
            if estado:
                proyectos = proyectos.filter(FK_ESTADO_PROYECTO=estado)
            if fecha_desde and fecha_hasta:
                fecha_desde = datetime.strptime(fecha_desde, '%d/%m/%Y').strftime('%Y-%m-%d')
                fecha_hasta = datetime.strptime(fecha_hasta, '%d/%m/%Y').strftime('%Y-%m-%d')
                proyectos = proyectos.filter(FC_INGRESO_PROYECTO__range = (fecha_desde, fecha_hasta))

            data = list(proyectos.values())

            if(request.POST['tipo'] == "1"):
                especificaciones = list(Concreto.objects.all().values())
                pdf_view = ReporteConcretoPDF.as_view()
                response = pdf_view(request,data, especificaciones)              
                return response  
                                                                 
    else:
        form = ReportesForm()
    return render(request, 'Reporte/index.html', {'form':form})


class ReporteConcretoPDF(View):
    def post(self, request, proyectos, especificaciones, *args, **kwargs):
        pdf = crearPDF('Reporte/concretoPDF.html', {"data": proyectos, "detalle": especificaciones, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')



