import io
from django.conf import settings
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import messages
from .forms import *
from .models import *
from Administrador.models import *
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
import json

def index(request):
    user = request.user
    print(user)
    if user.groups.filter(name='Empleado').exists():
        # Si el usuario es Empleado, se recuperan unicamente los proyectos a los que se encuentra asignado
        asignaciones = AsignacionEmpleado.objects.filter(FK_USUARIO_id=user)
        proyectos = Proyecto.objects.filter(pk__in=asignaciones.values_list('SK_PROYECTO', flat=True))
    else:
        # Si el usuario no pertenece a Empleado, se recuperan todos los proyectos
        proyectos = Proyecto.objects.all()
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
            request.session['direccion'] = request.POST['ST_DIRECCION_PROYECTO']
            request.session['descripcion'] = request.POST['ST_DESCRIPCION_PROYECTO']
            request.session['tipo_servicio'] = request.POST['FK_TIPO_SERVICIO']

            context = {
                    "tipoServicio": form.cleaned_data['FK_TIPO_SERVICIO'], 
                    "form": form,
                }
            
            if tipoServicio == "1":
                return redirect('concretoForm')
            elif tipoServicio =="2":
                return redirect('rentaEquipoForm')
            elif tipoServicio =="3":
                return redirect('rentaDesimetroForm')    
            elif tipoServicio =="4":
                return redirect('transporteForm')
            elif tipoServicio == "5":
                return redirect('levantamientoTopograficoForm')
            elif tipoServicio == "6":
                return redirect('estructuraMetalicaForm')
            elif tipoServicio =="7":
                return redirect('senializacionVialForm')
            elif tipoServicio =="8":  
                return redirect('asesoriaForm')            
            
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
    proyecto = Proyecto.objects.get(SK_PROYECTO=id)
    facturas = Factura.objects.filter(FK_PROYECTO=proyecto)
    tipo = proyecto.FK_TIPO_SERVICIO.SK_TIPO_SERVICIO
    especificaciones = None

    personal = AsignacionEmpleado.objects.filter(SK_PROYECTO=id).values(
        'FK_USUARIO__first_name',
        'FK_USUARIO__last_name'
    )
    materiales = AsignacionMaterial.objects.filter(FK_PROYECTO = id).values(
        'SK_MATERIAL__ST_NOMBRE_MATERIAL',
        'ST_DESCRIPCION'
    )      
    equipos = AsignacionEquipo.objects.filter(SK_PROYECTO = id).values(
        'FK_EQUIPO__ST_NOMBRE_EQUIPO',
        'FK_EQUIPO__FK_TIPO_EQUIPO__ST_TIPO_EQUIPO'
    )
    
    if tipo == 1:
        especificaciones = Concreto.objects.get(FK_PROYECTO = id)
    elif tipo ==2:
        especificaciones = RentaEquipo.objects.get(FK_PROYECTO = id)
    elif tipo ==3:
        especificaciones = RentaDesimetro.objects.get(FK_PROYECTO = id)    
    elif tipo ==4:
        especificaciones = Transporte.objects.get(FK_PROYECTO = id)
    elif tipo == 5:
        especificaciones = LevantamientoTopografico.objects.get(FK_PROYECTO = id)
    elif tipo == 6:
        especificaciones = EstructuraMetalica.objects.get(FK_PROYECTO = id)
    elif tipo ==7:
        especificaciones = SenializacionVial.objects.get(FK_PROYECTO = id)
    elif tipo ==8:             
        especificaciones = AsesoriaConstructiva.objects.get(FK_PROYECTO = id)

    contexto = {
        'proyecto': proyecto,
        'personal': personal,
        'materiales': materiales,
        'equipos': equipos,
        'especificaciones': especificaciones,
        'tipo':tipo,
        'facturas': facturas
    }

    return render(request, 'Proyecto/details.html',contexto)

def transporteForm(request):
    if request.method == 'POST':
        form = TransporteForm(request.POST)      
        if form.is_valid():
            form_data = form.cleaned_data
            form_data["NM_VOLUMEN"] = float(form_data["NM_VOLUMEN"])
            request.session['form'] = form_data
        return redirect("registerEquipment")
    else:
        form = TransporteForm()
        return render(request, 'Proyecto/transporte.html', {'form':form})
    

def rentaEquipoForm(request):
    if request.method == 'POST':
        form = RentaEquipoForm(request.POST)    
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['FC_ENTRADA_EQUIPO'] = form_data['FC_ENTRADA_EQUIPO'].strftime('%Y-%m-%d %H:%M:%S')
            form_data['FC_SALIDA_EQUIPO'] = form_data['FC_SALIDA_EQUIPO'].strftime('%Y-%m-%d %H:%M:%S')
            request.session['form'] = form_data
            return redirect("registerEquipment")
    else:
        form = RentaEquipoForm()
        return render(request, 'Proyecto/rentaequipo.html', {'form':form})
    
def rentaDesimetroForm(request):
    if request.method == 'POST':
        form = RentaDesimetroForm(request.POST)    
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['FC_SALIDA_DESIMETRO'] = form_data['FC_SALIDA_DESIMETRO'].strftime('%Y-%m-%d %H:%M:%S')
            form_data['FC_ENTRADA_DESIMETRO'] = form_data['FC_ENTRADA_DESIMETRO'].strftime('%Y-%m-%d %H:%M:%S')
            if form_data['FC_SALIDA_DESIMETRO'] >= form_data['FC_ENTRADA_DESIMETRO']:
                messages.error(request, 'La fecha de salida debe ser anterior a la fecha de entrada.')
            else:
                request.session['form'] = form_data
                return redirect("registerEquipment")
    else:
        form = RentaDesimetroForm()
        return render(request, 'Proyecto/rentadesimetro.html', {'form':form})
    
def concretoForm(request):
    if request.method == 'POST':
        form = ConcretoForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['ST_DOC_CONCRETO']

            # Define la ubicación en la que deseas guardar el archivo en el servidor
            file_path = os.path.join(settings.MEDIA_ROOT, 'temp', uploaded_file.name)

            # Abre el archivo y guárdalo en el servidor
            with open(file_path, 'wb') as file:
                for chunk in uploaded_file.chunks():
                    file.write(chunk)
            request.session['form'] = {
                'post_data': request.POST,
                'files_data': file_path,
            }
            return redirect("registerEquipment")
    else:
        form = ConcretoForm()
    return render(request, 'Proyecto/concreto.html', {'form':form})

def levantamientoTopograficoForm(request):
    if request.method == 'POST':
        form = LevantamientoTopograficoForm(request.POST)      
        if form.is_valid():
            form_data = form.cleaned_data
            form_data['NM_AREA'] = int(form_data['NM_AREA'])
            request.session['form'] = form_data
        return redirect("registerEquipment")
    else:
        form = LevantamientoTopograficoForm()
    return render(request, 'Proyecto/levantamiento.html', {'form':form})

def estructuraMetalicaForm(request):
    if request.method == 'POST':
        form = EstructuraMetalicaForm(request.POST,request.FILES)
        if form.is_valid():
            uploaded_file = request.FILES['ST_DOC_CONCRETO']

            # Define la ubicación en la que deseas guardar el archivo en el servidor
            file_path = os.path.join(settings.MEDIA_ROOT, 'temp', uploaded_file.name)

            # Abre el archivo y guárdalo en el servidor
            with open(file_path, 'wb') as file:
                for chunk in uploaded_file.chunks():
                    file.write(chunk)
            request.session['form'] = {
                'post_data': request.POST,
                'files_data': file_path,
            }
            return redirect("registerEmployees")
    else:
        form = EstructuraMetalicaForm()
    return render(request, 'Proyecto/metalica.html', {'form': form})

def senializacionVialForm(request):
    if request.method == 'POST':
        form = SenializacionVialForm(request.POST)      
        if form.is_valid():
            form_data = form.cleaned_data
            request.session['form'] = form_data
        return redirect("registerEquipment")
    else:
        form = SenializacionVialForm()
    return render(request, 'Proyecto/senializacionvial.html', {'form':form})

def asesoramientoForm(request):
    if request.method == 'POST':
        form = AsesoriaConstructivaForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            request.session['form'] = form_data
        return redirect("registerEmployees")
    else:
        form = AsesoriaConstructivaForm()
    return render(request, 'Proyecto/asesoria.html', {'form':form})

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
        tipo_servicio = request.session['tipo_servicio']
        if (tipo_servicio == "8" or request.session["equipos"] != []):
            empleados = request.session['empleados']
            empleados_agregados = [empleado['id'] for empleado in empleados]
            cc_empleados = Usuario.objects.filter(BN_ESTADO_USUARIO=1).filter(is_staff = 0).exclude(Q(id__in=empleados_agregados))
            context = {'cc_empleados':cc_empleados, 'empleados':empleados, 'tipo_servicio':tipo_servicio}
            return render(request, 'Proyecto/asignacionEmpleado.html', context)
        else:
            messages.warning(request,"¡No se ha asignado ningún equipo!")
            return redirect("registerEquipment")
    
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
        if 'materiales' not in request.session:
            request.session['materiales'] = []
        else:
            request.session['materiales'] = request.session['materiales']
        equipo =  Material.objects.get(SK_MATERIAL = request.POST['material-id'])
        request.session['materiales'].append({
             'id': equipo.SK_MATERIAL,
             'nombre':equipo.ST_NOMBRE_MATERIAL,
             'cantidad': request.POST['cant-material'],
             'descripcion': equipo.ST_DESCRIPCION_MATERIAL
        })
        messages.success(request, "¡Material añadido!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        if (request.session["empleados"] != []):
            materiales = request.session['materiales']
            materiales_agregados = [material['id'] for material in materiales]
            cc_materiales = Material.objects.filter(BN_ESTADO_MATERIAL=1).exclude(Q(SK_MATERIAL__in=materiales_agregados))
            context = {'cc_materiales':cc_materiales, 'materiales':materiales}
            return render(request, 'Proyecto/asignacionMaterial.html', context)
        else: 
            messages.warning(request,"¡No se ha asignado ningún empleado!")
            return redirect("registerEmployees")
    
def deleteMaterial(request, id):
    index = id - 1
    del request.session['materiales'][index]
    request.session.modified = True
    messages.info(request, "¡El material fue retirado del listado!")
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def save(request):
    if 'tipo_servicio' in request.session:
        tipo_servicio = request.session['tipo_servicio']
        servicios = ["1", "4", "5", "6", "7"]
        if (tipo_servicio == "8"):
            if 'empleados' not in request.session or request.session["empleados"] == []:
                messages.warning(request,"¡No se ha asignado ningún empleado!")
                return redirect("registerEmployees")
        elif tipo_servicio in servicios:
            print(request.session["materiales"])
            if 'materiales' not in request.session or request.session["materiales"] == []:
                messages.warning(request,"¡No se ha asignado ningún material!")
                return redirect("registerMaterial")
        else:
            if 'equipos' not in request.session or request.session["equipos"] == []:
                messages.warning(request,"¡No se ha asignado ningún equipo!")
                return redirect("registerEquipment")
            
        cliente = Cliente.objects.get(SK_CLIENTE = request.session['cliente'])
        tipo_servicio = TipoServicio.objects.get(SK_TIPO_SERVICIO = request.session['tipo_servicio'])
        estado_proyecto = EstadoProyecto.objects.get(SK_ESTADO_PROYECTO = 1)
        proyecto = Proyecto.objects.create(
            FK_CLIENTE = cliente,
            FK_TIPO_SERVICIO = tipo_servicio,
            FK_ESTADO_PROYECTO = estado_proyecto,
            ST_DESCRIPCION_PROYECTO = request.session['descripcion'],
            ST_DIRECCION_PROYECTO = request.session['direccion'],
            FK_USUARIO = request.user
        )
        if 'form' in request.session:
            form_data = request.session['form']        
            form = saveEspecifications(form_data, request.session['tipo_servicio'])
            if form.is_valid():
                especificaciones = form.save(commit=False)
                especificaciones.FK_PROYECTO = proyecto
                especificaciones.save()
        if 'empleados' in request.session:
            for empleado in request.session['empleados']:
                usuario = Usuario.objects.get(id = empleado['id'])
                AsignacionEmpleado.objects.create(
                    SK_PROYECTO = proyecto,
                    FK_USUARIO = usuario
                )
        if 'equipos' in request.session:
                for equipo in request.session['equipos']:
                    equipo = Equipo.objects.get(SK_EQUIPO = equipo['id'])
                    AsignacionEquipo.objects.create(
                        SK_PROYECTO = proyecto,
                        FK_EQUIPO = equipo
                    )
        if 'materiales' in request.session:
            for mat in request.session['materiales']:
                material = Material.objects.get(SK_MATERIAL = mat['id'])
                cant = mat['cantidad']
                AsignacionMaterial.objects.create(
                    SK_MATERIAL = material,
                    FK_PROYECTO = proyecto,
                    ST_DESCRIPCION = cant
                )
        del request.session['tipo_servicio']
        del request.session['empleados']
        del request.session['equipos']
        del request.session['materiales']
        request.session.modified = True
        messages.success(request, "El proyecto fue creado exitosamente.")
        return redirect("Main")
            
    else:
        return redirect("AddProyecto")
    

def saveEspecifications(form_data, tipo_servicio):
    if tipo_servicio == "1":
        # Ruta de archivo
        archivo_ruta = form_data['files_data']

        # Nombre de archivo y extensión
        nombre_archivo = os.path.basename(archivo_ruta)
        nombre, extension = os.path.splitext(nombre_archivo)

        # Abre el archivo en modo binario
        with open(archivo_ruta, 'rb') as archivo:
            archivo_bytes = archivo.read()

        # Crea un objeto BytesIO para simular un archivo en memoria
        archivo_en_memoria = io.BytesIO(archivo_bytes)
        
        # Crea un objeto InMemoryUploadedFile
        archivo_upload = InMemoryUploadedFile(
            archivo_en_memoria,
            None,  
            nombre_archivo,
            'application/pdf',
            len(archivo_bytes),
            None
        )
        return ConcretoForm(form_data['post_data'],files={'ST_DOC_CONCRETO': archivo_upload})    
    elif tipo_servicio == "5":
        return LevantamientoTopograficoForm(form_data)
    elif tipo_servicio == "6":
                # Ruta de archivo
        archivo_ruta = form_data['files_data']

        # Nombre de archivo y extensión
        nombre_archivo = os.path.basename(archivo_ruta)
        nombre, extension = os.path.splitext(nombre_archivo)

        # Abre el archivo en modo binario
        with open(archivo_ruta, 'rb') as archivo:
            archivo_bytes = archivo.read()

        # Crea un objeto BytesIO para simular un archivo en memoria
        archivo_en_memoria = io.BytesIO(archivo_bytes)
        
        # Crea un objeto InMemoryUploadedFile
        archivo_upload = InMemoryUploadedFile(
            archivo_en_memoria,
            None,  
            nombre_archivo,
            'application/pdf',
            len(archivo_bytes),
            None
        )
        return EstructuraMetalicaForm(form_data['post_data'],files={'ST_DOC_CONCRETO': archivo_upload}) 
    elif tipo_servicio =="7":
        return SenializacionVialForm(form_data)
    elif tipo_servicio =="2":
        return RentaEquipoForm(form_data)
    elif tipo_servicio =="3":
        return RentaDesimetroForm(form_data)
    elif tipo_servicio =="4":
        return TransporteForm(form_data)
    elif tipo_servicio =="8":  
        return AsesoriaConstructivaForm(form_data)
    

def getEstados(request):
    estados = EstadoProyecto.objects.all()
    estados_list = [{'id': estado.SK_ESTADO_PROYECTO, 'nombre': estado.ST_ESTADO_PROYECTO} for estado in estados]
    return JsonResponse(estados_list, safe=False)


def saveEstado(request, proyecto_id, nuevo_estado_id):
    proyecto = Proyecto.objects.get(SK_PROYECTO=proyecto_id)
    nuevo_estado = EstadoProyecto.objects.get(SK_ESTADO_PROYECTO=nuevo_estado_id)
    proyecto.FK_ESTADO_PROYECTO = nuevo_estado
    proyecto.save()
    estado_nombre = nuevo_estado.ST_ESTADO_PROYECTO
    return JsonResponse({'success': True, 'estado_nombre': estado_nombre})


def uploadFactura(request, proyecto_id):
    if request.method == 'POST':
        factura_file = request.FILES.get('facturaFile')
        if factura_file:
            factura = Factura(ST_FACTURA=factura_file, FK_PROYECTO_id=proyecto_id)
            factura.save()
            return HttpResponse('Factura subida exitosamente.')
    return HttpResponse('Error al subir la factura.')

def deleteFactura(request, factura_id ):
    factura = get_object_or_404(Factura, SK_FACTURA=factura_id)
    factura.delete()
    return JsonResponse({'message': 'Factura eliminada correctamente.'})

def getFacturas(request, proyecto_id):
    facturas = Factura.objects.filter(FK_PROYECTO_id=proyecto_id)
    facturas_data = []
    for factura in facturas:
        facturas_data.append({
            'id': factura.SK_FACTURA,
            'url': factura.ST_FACTURA.url,
            'nombre': factura.ST_FACTURA.name
        })
    return JsonResponse(facturas_data, safe=False)