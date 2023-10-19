from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.db.models import F
from Proyecto.models import *
from Reporte.utils import crearPDF

from .forms import *

def index(request):
    if request.method == 'POST':
        form = ReportesForm(request.POST)
        if form.is_valid():
            estado = form.cleaned_data['estado']
            cliente = form.cleaned_data['cliente']
            tipo_servicio = form.cleaned_data['tipo']
            fecha_desde = form.cleaned_data['fechaDesde']
            fecha_hasta = form.cleaned_data['fechaHasta']
            todos_proyecto = form.cleaned_data['todos_proyectos']
            proyectos = Proyecto.objects.filter(FK_TIPO_SERVICIO = tipo_servicio).values(
                    'SK_PROYECTO', 
                    'ST_DIRECCION_PROYECTO', 
                    'ST_DESCRIPCION_PROYECTO', 
                    'FK_CLIENTE__ST_NOMBRE_CLIENTE',  
                    'FK_ESTADO_PROYECTO__ST_ESTADO_PROYECTO',  
                    'FK_USUARIO__username', 
                    'FC_INGRESO_PROYECTO'
                )
            if estado:
                proyectos = proyectos.filter(FK_ESTADO_PROYECTO=estado)
            if cliente:
                proyectos = proyectos.filter(FK_CLIENTE=cliente)
            if not todos_proyecto:
                if fecha_desde and fecha_hasta:
                    fecha_desde = datetime.strptime(fecha_desde, '%d/%m/%Y').strftime('%Y-%m-%d')
                    fecha_hasta = datetime.strptime(fecha_hasta, '%d/%m/%Y').strftime('%Y-%m-%d')
                    proyectos = proyectos.filter(FC_INGRESO_PROYECTO__range = (fecha_desde, fecha_hasta))
            asignaciones_empleado = AsignacionEmpleado.objects.all().values(
                'FK_USUARIO__first_name',
                'FK_USUARIO__last_name',
            )
            asignaciones_equipo = AsignacionEquipo.objects.all().values(
                'FK_EQUIPO__ST_NOMBRE_EQUIPO',
                'FK_EQUIPO__FK_TIPO_EQUIPO__ST_TIPO_EQUIPO'
            )
            asignaciones_material = AsignacionMaterial.objects.all().values(
                'SK_MATERIAL__ST_NOMBRE_MATERIAL',
                'ST_DESCRIPCION'
            )      
            proyecto_data = []
            for proyecto in proyectos:
                proyecto_dict = {
                    'proyecto': proyecto,
                    'especificaciones': getEspecificaciones(request.POST['tipo'], proyecto['SK_PROYECTO']),
                    'asignaciones_empleado': asignaciones_empleado.filter(SK_PROYECTO=proyecto['SK_PROYECTO']),
                    'asignaciones_equipo': asignaciones_equipo.filter(SK_PROYECTO=proyecto['SK_PROYECTO']),
                    'asignaciones_material': asignaciones_material.filter(FK_PROYECTO=proyecto['SK_PROYECTO']),
                }
                proyecto_data.append(proyecto_dict)
            return generarReporte(request.POST['tipo'], proyecto_data, request)                                                           
    else:
        form = ReportesForm()
    return render(request, 'Reporte/index.html', {'form':form})


class ReporteConcretoPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/concretoPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')


class ReporteRentaEquipoPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/rentaEquipoPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class ReporteRentaDensimetroPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/rentaDensimetroPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class ReporteTransportePDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/transportePDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')    

class ReporteLevantamientoPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/levantamientoPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')    
    
class ReporteEstructuraMetalicaPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/estructuraPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class ReporteSenalizacionVialPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/senalizacionPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    
class ReporteAsesoriaPDF(View):
    def post(self, request, proyectos, *args, **kwargs):
        pdf = crearPDF('Reporte/asesoriaPDF.html', {"data": proyectos, "user": request.user.first_name + " " + request.user.last_name, "date": timezone.now()})
        return HttpResponse(pdf, content_type='application/pdf')
    

def getEspecificaciones(tipo_servicio, proyecto):
    especificaciones = {
        "1": Concreto.objects,
        "2": RentaEquipo.objects,
        "3": RentaDesimetro.objects,
        "4": Transporte.objects,
        "5": LevantamientoTopografico.objects,
        "6": EstructuraMetalica.objects,
        "7": SenializacionVial.objects,
        "8": AsesoriaConstructiva.objects,
    }
    if tipo_servicio in especificaciones:
        return especificaciones[tipo_servicio].filter(FK_PROYECTO=proyecto).values()
    else:
        return None 

def generarReporte(tipo_servicio, data, request):
    reporte_pdfs = {
        "1": ReporteConcretoPDF.as_view(),
        "2": ReporteRentaEquipoPDF.as_view(),
        "3": ReporteRentaDensimetroPDF.as_view(),
        "4": ReporteTransportePDF.as_view(),
        "5": ReporteLevantamientoPDF.as_view(),
        "6": ReporteEstructuraMetalicaPDF.as_view(),
        "7": ReporteSenalizacionVialPDF.as_view(),
        "8": ReporteAsesoriaPDF.as_view(),
    }
    if tipo_servicio in reporte_pdfs:
        pdf_view = reporte_pdfs[tipo_servicio]
        response = pdf_view(request, data)
        return response
    else:
        return None 