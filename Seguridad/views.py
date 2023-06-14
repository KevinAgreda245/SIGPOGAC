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
            if usuarioAutenticado.BN_ESTADO_USUARIO:
                login(request, usuarioAutenticado)
                return redirect('Main')
            else:
                messages.error(request, 'Lamentablemente, tu cuenta ya no tiene acceso al sistema.')
        else:
            try:
                user = Usuario.objects.get(username=usuario)
                if not user.is_active:
                    # Usuario inactivo, mostrar mensaje de error
                    messages.error(request, 'Tu cuenta está bloqueada. Contacta al administrador.')
                else: 
                    messages.error(request, 'El usuario o la contraseña incorrectos. Intenta nuevamente')
            except:
                messages.error(request, 'El usuario o la contraseña incorrectos. Intenta nuevamente')
            return render(request, 'Seguridad/index.html')
    return render(request, 'Seguridad/index.html')


@login_required(login_url='login')
def cerrarSesion(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def details(request):
    admin = Usuario.objects.get(id=request.user.pk)
    docs = DocumentoUsuario.objects.filter(FK_USUARIO_id=request.user.pk)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Seguridad/details.html', context)


@login_required(login_url='login')
def edit(request):
    usuario = Usuario.objects.get(pk=request.user.pk)

    form = UpdateUserForm(request.POST or None, instance=usuario)

    if form.is_valid():
        with transaction.atomic():
            usuario = form.save()

        messages.success(request, "Perfil ha sido actualizado exitosamente.")
        return redirect('DetailsProfile')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form}
    return render(request, 'Seguridad/edit.html', context)

