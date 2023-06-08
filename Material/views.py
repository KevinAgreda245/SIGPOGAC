from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Material
from .forms import MaterialForm
from Seguridad.decorators import *

@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def index(request):
    materiales = Material.objects.filter(BN_ESTADO_MATERIAL = 1)
    return render(request, 'Material/index.html',{
        "materiales": materiales
    })


@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def add(request):
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Material creado exitosamente.")
            return redirect('Material')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = MaterialForm()
    context = {
        "form": form
    }
    return render(request,'Material/add.html',context)


@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def edit(request,id):
    material = Material.objects.get(pk=id)
    form = MaterialForm(request.POST or None, request.FILES or None, instance=material)
    if form.is_valid():
        form.save()
        messages.success(request, "Material modificado exitosamente.")
        return redirect('Material')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)
    context = {
        "form": form
    }
    return render(request,'Material/edit.html',context)


@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def delete(request,id):
    material = Material.objects.get(pk=id)
    material.BN_ESTADO_MATERIAL = False
    material.save()
    messages.success(request, "Material eliminado exitosamente.")
    return redirect('Material')