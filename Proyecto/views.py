from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import Proyecto
from django.core.paginator import Paginator
from django.contrib import messages

def index(request):
    proyectos = Proyecto.objects.all()  # Inicialmente, obtén todos los proyectos
    if request.method == 'POST':
        form = FiltroProyectosForm(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data['cliente']
            estado = form.cleaned_data['estado']
            tipo = form.cleaned_data['tipo']
    
            # Aplica los filtros según los valores seleccionados en el formulario
            if cliente:
                proyectos = proyectos.filter(FK_CLIENTE=cliente)
            if estado:
                proyectos = proyectos.filter(FK_ESTADO_PROYECTO=estado)
            if tipo:
                proyectos = proyectos.filter(FK_TIPO_SERVICIO=tipo)
            
    else:
        form = FiltroProyectosForm()
    

    # Aplicar paginación
    page_number = request.GET.get('page')
    per_page = 10  # Número de proyectos por página
    paginator = Paginator(proyectos, per_page)
    paged_proyecto = paginator.get_page(page_number)

    return render(request, 'Proyecto/index.html',{'form': form, 'proyectos': paged_proyecto})

def add(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)        
        if form.is_valid():
            tipoServicio = request.POST["FK_TIPO_SERVICIO"]

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

def details(request):
    return render(request, 'Proyecto/add.html')