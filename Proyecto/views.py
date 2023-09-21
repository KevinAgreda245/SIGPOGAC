from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from Administrador.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q

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
    request.session['empleados'] = []
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
                 return redirect('transporteForm')
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

def details(request):
    return render(request, 'Proyecto/add.html')

def transporteForm(request):
    unidades = Transporte.UNIDADES
    form = TransporteForm()
    empleados = request.session['empleados']
    empleados_agregados = [empleado['id'] for empleado in empleados]
    cc_empleados = Usuario.objects.filter(BN_ESTADO_USUARIO=1).exclude(Q(id__in=empleados_agregados))
    context = {'unidades':unidades, 'cc_empleados':cc_empleados, 'empleados':empleados, 'form':form}
    return render(request, 'Proyecto/transporte.html', context)


def agregarEmpleado(request):
    if request.method == 'POST':
        if 'empleados' not in request.session:
            request.session['empleados'] = []
        else:
            request.session['empleados'] = request.session['empleados']
        empleado =  Usuario.objects.get(id = request.POST['empleado-id'])
        request.session['empleados'].append({
             'id': empleado.id,
             'nombre':empleado.first_name,
             'apellido': empleado.last_name
        })
        messages.success(request, "¡Empleado añadido!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    
def eliminarEmpleado(request, id):
    index = id - 1
    del request.session['empleados'][index]
    request.session.modified = True
    messages.info(request, "¡El empleado fue retirado del listado!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
