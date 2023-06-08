from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Administrador.forms import DocumentUserForm, UpdateUserForm
from Administrador.models import Usuario, DocumentoUsuario
from .decorators import *


@authenticated_user
def index(request):
    if request.method == 'POST':
        usuario = request.POST['usuario']
        contraseña = request.POST['password']
        usuarioAutenticado = authenticate(request, username=usuario, password=contraseña)
        if usuarioAutenticado is not None:
            login(request, usuarioAutenticado)
            # Pendiente validación para redigirir de acuerdo al rol del usuario
            return redirect('Main')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
            return render(request, 'Seguridad/index.html')
    return render(request, 'Seguridad/index.html')


@login_required(login_url='login')
def cerrarSesion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def details(request, id):
    admin = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id=id)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Seguridad/details.html', context)


@login_required(login_url='login')
def edit(request, id):
    usuario = Usuario.objects.get(pk=id)

    form = UpdateUserForm(request.POST or None, instance=usuario)

    if form.is_valid():
        with transaction.atomic():
            usuario = form.save()

        messages.success(request, "Perfil actualizado exitosamente.")
        return redirect('DetailsProfile', id)
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form}
    return render(request, 'Seguridad/edit.html', context)

