from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import *
from .models import *
from Administrador.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
import json

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
    request.session['equipos'] = []
    request.session['materiales'] = []
    if request.method == 'POST':
        form = ProyectoForm(request.POST)        
        if form.is_valid():
            tipoServicio = request.POST["FK_TIPO_SERVICIO"]

            #Extraer data general de proyecto
            request.session['cliente'] = request.POST['FK_CLIENTE']
            request.session['direcccion'] = request.POST['ST_DIRECCION_PROYECTO']
            request.session['descripcion'] = request.POST['ST_DESCRIPCION_PROYECTO']
            request.session['tipo_servicio'] = request.POST['FK_TIPO_SERVICIO']

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
                return redirect('rentaEquipoForm')
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

def details(request, id):
    proyecto = Proyecto.objects.get(id=id)
    personal = AsignacionEmpleado.objects.get(SK_PROYECTO = id)
    materiales = AsignacionMaterial.objects.get()
    return render(request, 'Proyecto/add.html')

def transporteForm(request):
    if request.method == 'POST':
        form = TransporteForm(request.POST)      
        if form.is_valid():
            request.session['transporteForm_ST_UNIDAD_TRANSPORTE'] = request.POST['ST_UNIDAD_TRANSPORTE']
            request.session['transporteForm_ST_OBSERVACION_EQUIPO'] = request.POST['ST_OBSERVACION_EQUIPO']
        return redirect("registerEquipment")
    else:
        form = TransporteForm()
        return render(request, 'Proyecto/transporte.html', {'form':form})
    

def rentaEquipoForm(request):
    if request.method == 'POST':
        form = RentaEquipoForm(request.POST)      
        if form.is_valid():
            request.session['rentaEquipoForm_ST_TIPO_USO'] = request.POST['ST_TIPO_USO']
            request.session['rentaEquipoForm_ST_OBSERVACION_EQUIPO'] = request.POST['ST_OBSERVACION_EQUIPO']
        return redirect("registerEquipment")
    else:
        form = RentaEquipoForm()
        return render(request, 'Proyecto/rentaequipo.html', {'form':form})
    
        


def registerEmployees(request):
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
    else:
        empleados = request.session['empleados']
        empleados_agregados = [empleado['id'] for empleado in empleados]
        cc_empleados = Usuario.objects.filter(BN_ESTADO_USUARIO=1).exclude(Q(id__in=empleados_agregados))
        context = {'cc_empleados':cc_empleados, 'empleados':empleados}
        return render(request, 'Proyecto/asignacionEmpleado.html', context)
    
def deleteEmployee(request, id):
    index = id - 1
    del request.session['empleados'][index]
    request.session.modified = True
    messages.info(request, "¡El empleado fue retirado del listado!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



def registerEquipment(request):
    if request.method == 'POST':
        if 'equipos' not in request.session:
            request.session['equipos'] = []
        else:
            request.session['equipos'] = request.session['equipos']
        equipo =  Equipo.objects.get(SK_EQUIPO = request.POST['equipo-id'])
        request.session['equipos'].append({
             'id': equipo.SK_EQUIPO,
             'nombre':equipo.ST_NOMBRE_EQUIPO,
             'descripcion': equipo.ST_DESCRIPCION_EQUIPO
        })
        messages.success(request, "¡Equipo añadido!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        equipos = request.session['equipos']
        equipos_agregados = [equipo['id'] for equipo in equipos]
        cc_equipos = Equipo.objects.filter(BN_ESTADO_EQUIPO=1).exclude(Q(SK_EQUIPO__in=equipos_agregados))
        #Tipos de servicios con más pasos
        tipo_servicio = request.session['tipo_servicio']
        servicios = ["1", "4", "5", "6", "7"]
        context = {'cc_equipos':cc_equipos, 'equipos':equipos, 'servicios':servicios, 'tipo_servicio': tipo_servicio}
        return render(request, 'Proyecto/asignacionEquipo.html', context)
    
def deleteEquipment(request, id):
    index = id - 1
    del request.session['equipos'][index]
    request.session.modified = True
    messages.info(request, "¡El equipo fue retirado del listado!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def registerMaterial(request):
    if request.method == 'POST':
        if 'equipos' not in request.session:
            request.session['materiales'] = []
        else:
            request.session['materiales'] = request.session['materiales']
        equipo =  Material.objects.get(SK_MATERIAL = request.POST['material-id'])
        request.session['materiales'].append({
             'id': equipo.SK_MATERIAL,
             'nombre':equipo.ST_NOMBRE_MATERIAL,
             'descripcion': equipo.ST_DESCRIPCION_MATERIAL
        })
        messages.success(request, "¡Material añadido!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        materiales = request.session['materiales']
        materiales_agregados = [material['id'] for material in materiales]
        cc_materiales = Material.objects.filter(BN_ESTADO_MATERIAL=1).exclude(Q(SK_MATERIAL__in=materiales_agregados))
        context = {'cc_materiales':cc_materiales, 'materiales':materiales}
        return render(request, 'Proyecto/asignacionMaterial.html', context)
    
def deleteMaterial(request, id):
    index = id - 1
    del request.session['materiales'][index]
    request.session.modified = True
    messages.info(request, "¡El material fue retirado del listado!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def save(request):
    return redirect("Main")
