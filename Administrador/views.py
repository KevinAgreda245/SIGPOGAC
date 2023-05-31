from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Usuario, DocumentoUsuario
from .forms import *

def main(request):
    return render(request, 'Administrador/main.html')

def management(request):
    admins = Usuario.objects.filter(is_staff = 1)
    context = {
        "admins": admins
    }
    return render(request, 'Administrador/management.html',context)    

def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Administrador creado exitosamente.")
            return redirect('Administrador')
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
    return render(request, 'Administrador/add.html',context)

def details(request,id):
    admin = Usuario.objects.get(id = id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id = id)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Administrador/details.html',context)    

def changeStatus(request,id):
    admin = Usuario.objects.get(id = id)
    admin.is_active = not admin.is_active
    if (admin.is_active):
        msg = "Usuario activado correctamente."
    else:
        msg = "Usuario desactivado correctamente."
    admin.save()
    messages.success(request,msg)
    return redirect('Administrador')