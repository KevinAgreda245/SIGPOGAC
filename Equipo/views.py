from django.contrib import messages
from django.contrib.auth.decorators import login_required
from Equipo.forms import EquipoForm
from Equipo.models import Equipo
from django.shortcuts import redirect, render
from Seguridad.decorators import *


@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def index(request):
    equipos = Equipo.objects.filter(BN_ESTADO_EQUIPO=True)
    context = {"equipos": equipos}
    return render(request, 'Equipo/index.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def add(request):
    form = EquipoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "Equipo ha sido ingresado exitosamente.")
        return redirect('Equipo')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form}
    return render(request, 'Equipo/add.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def edit(request, id):
    equipo = Equipo.objects.get(pk=id)

    form = EquipoForm(request.POST or None, request.FILES or None, instance=equipo)
    if form.is_valid():
        form.save()
        messages.success(request, "Equipo ha sido actualizado exitosamente.")
        return redirect('Equipo')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form}
    return render(request, 'Equipo/edit.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador', 'Empleado'])
def details(request, id):
    equipo = Equipo.objects.get(pk=id)
    context = {
        "equipo": equipo,
    }
    return render(request, 'Equipo/details.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def Delete(request, id):
    equipo = Equipo.objects.get(pk=id)
    equipo.BN_ESTADO_EQUIPO = not equipo.BN_ESTADO_EQUIPO
    msg = "Equipo ha sido eliminado correctamente."
    equipo.save()
    messages.success(request, msg)
    return redirect('Equipo')
