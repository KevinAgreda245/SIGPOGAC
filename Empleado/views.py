from django.shortcuts import redirect, render
from django.contrib import messages
from Administrador.models import Usuario, DocumentoUsuario
from .forms import *

def main(request):
    return render(request, 'Empleado/main.html')

def index(request):
    empleados = Usuario.objects.filter(is_staff = 0)
    context = {
        "empleados": empleados
    }
    return render(request, 'Empleado/index.html',context)    

def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Empleado creado exitosamente.")
            return redirect('Empleado')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })           
                messages.error(request,errors)
    else:
        form = CreateUserForm()
    context = {
       "form": form
    }
    return render(request, 'Empleado/add.html',context)

def details(request,id):
    empleado = Usuario.objects.get(id = id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id = id)
    context = {
        "empleado": empleado,
        "docs": docs
    }
    return render(request, 'Empleado/details.html',context)

def changeStatus(request,id):
    empleado = Usuario.objects.get(id = id)
    empleado.is_active = not empleado.is_active
    if (empleado.is_active):
        msg = "Usuario activado correctamente."
    else:
        msg = "Usuario desactivado correctamente."
    empleado.save()
    messages.success(request,msg)
    return redirect('Empleado')