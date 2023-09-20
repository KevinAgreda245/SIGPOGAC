from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Proyecto
from django.core.paginator import Paginator

def index(request):
    proyectos = Proyecto.objects.all()  # Inicialmente, obtén todos los proyectos
    if request.method == 'POST':
        form = FiltroProyectosForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            fecha_inicio = form.cleaned_data['fecha_inicio']
            fecha_fin = form.cleaned_data['fecha_fin']
            estado = form.cleaned_data['estado']

            # Aplica los filtros según los valores seleccionados en el formulario
            if cliente:
                proyectos = proyectos.filter(SK_CLIENTE=cliente)
            if fecha_inicio:
                proyectos = proyectos.filter(FC_INGRESO_PROYECTO__gte=fecha_inicio)
            if fecha_fin:
                proyectos = proyectos.filter(FC_INGRESO_PROYECTO__lte=fecha_fin)
            if estado:
                proyectos = proyectos.filter(SK_ESTADO_PROYECTO=estado)

    else:
        form = FiltroProyectosForm()
    paginator = Paginator(proyectos,1)
    page = request.GET.get('page')
    paged_proyecto = paginator.get_page(page)
    proyecto_count = proyectos.count()
    return render(request, 'Proyecto/index.html',{'form': form, 'proyectos': paged_proyecto,'proyecto_count': proyecto_count})

def add(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)        
        if form.is_valid():
            tipoServicio = request.POST["FK_TIPO_SERVICIO"]

            form_mapping = {
                "1": ConcretoForm,
                "2": RentaEquipoForm,
                "3": RentaDesimetroForm,
                "4": TransporteForm,
                "5": LevantamientoToporgraficoForm,
                "6": EstructuraMetalicaForm,
                "7": SenializacionVialForm,
                "8": AsesoriaConstructivaForm,
            }

            if tipoServicio in form_mapping:
                formEspecificaciones = form_mapping[tipoServicio]
                
                context = {
                    "tipoServicio": form.cleaned_data['FK_TIPO_SERVICIO'], 
                    "form": form,
                    "formEspecificaciones": formEspecificaciones 
                }

                if tipoServicio in ["1", "5", "6", "7"]:
                    return render(request, 'Proyecto/step-5.html', context)
                elif tipoServicio in ["2", "3", "4", "8"]:
                    return render(request, 'Proyecto/step-3.html', context)   
            else:
                messages.error(request, "En construcción")
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = ProyectoForm()
        
    context = {
        "form": form,
    }
    return render(request, 'Proyecto/add.html',context)

