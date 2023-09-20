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

            context = {
                    "tipoServicio": form.cleaned_data['FK_TIPO_SERVICIO'], 
                    "form": form,
                }
            
            if tipoServicio == "1":
                    return render(request, 'Proyecto/concreto.html', context)
            elif tipoServicio == "5":
                    return render(request, 'Proyecto/levantamiento.html', context)
            elif tipoServicio == "6":
                     return render(request, 'Proyecto/metalica.html', context)
            elif tipoServicio =="7":
                    return render(request, 'Proyecto/senializacionvial.html', context)
            elif tipoServicio =="2":
                    return render(request, 'Proyecto/rentaequipo.html', context)
            elif tipoServicio =="3":
                    return render(request, 'Proyecto/rentadesimetro.html', context)
            elif tipoServicio =="4":
                 return render(request, 'Proyecto/transporte.html', context)
            elif tipoServicio =="8":  
                 return render(request, 'Proyecto/asesoria.html', context)            
            else: messages.error(request, "En construcción")
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