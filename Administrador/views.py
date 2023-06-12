import os

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from django.db.models import Count
from .models import Usuario, DocumentoUsuario
from Proyecto.models import Proyecto
from .forms import *
from tarfile import NUL
from Seguridad.decorators import *
from django.db import transaction


@login_required(login_url='login')
def main(request):
    context = {
        "registrados": Proyecto.objects.filter(FK_ESTADO_PROYECTO_id=1).count(),
        "ejecución": Proyecto.objects.filter(FK_ESTADO_PROYECTO_id=2).count(),
        "finalizados": Proyecto.objects.filter(FK_ESTADO_PROYECTO_id=3).count(),
        "completados": Proyecto.objects.filter(FK_ESTADO_PROYECTO_id=4).count(),
        "data": Proyecto.objects.values('FK_TIPO_SERVICIO__ST_TIPO_SERVICIO').annotate(cant=Count('FK_TIPO_SERVICIO__ST_TIPO_SERVICIO'))
    }
    return render(request, 'Administrador/main.html',context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def management(request):
    admins = Usuario.objects.filter(is_staff=1, BN_ESTADO_USUARIO=1)
    context = {
        "admins": admins
    }
    return render(request, 'Administrador/management.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Administrador ha sido creado exitosamente.")
            return redirect('Administrador')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = CreateUserForm()
    context = {
        "form": form
    }
    return render(request, 'Administrador/add.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def edit(request, id):
    usuario = Usuario.objects.get(pk=id)

    form = UpdateUserForm(request.POST or None, instance=usuario)

    form_documents = {
        "NIT": DocumentUserForm(request.POST or None, request.FILES or None, prefix='NIT'),
        "DUI": DocumentUserForm(request.POST or None, request.FILES or None, prefix='DUI'),
        "ISSS": DocumentUserForm(request.POST or None, request.FILES or None, prefix='ISSS'),
        "AFP": DocumentUserForm(request.POST or None, request.FILES or None, prefix='AFP')
    }

    archivos_url = {}

    if DocumentoUsuario.objects.filter(FK_USUARIO=usuario.pk).exists():
        documentos = DocumentoUsuario.objects.filter(FK_USUARIO=usuario.pk)

        for documento in documentos:
            prefix = documento.ST_TIPO_DOC_USUARIO

            form_documents[documento.ST_TIPO_DOC_USUARIO] = DocumentUserForm(
                request.POST or None,
                request.FILES or None,
                instance=documento,
                prefix=prefix
            )

            # Obtener la dirección del archivo adjunto
            archivo_url = documento.ST_DOC_USUARIO if documento.ST_DOC_USUARIO else None
            archivos_url[prefix] = archivo_url

    if form.is_valid():
        with transaction.atomic():
            usuario = form.save()
            # group = Group.objects.get(name='Administrador')
            # usuario.groups.add(group)

            for doc_type, form_doc in form_documents.items():
                if form_doc.is_valid():
                    if form_doc.cleaned_data.get('ST_DOC_USUARIO'):
                        archivo_doc = form_doc.save(commit=False)
                        archivo_doc.ST_TIPO_DOC_USUARIO = doc_type
                        archivo_doc.FK_USUARIO = usuario
                        archivo_doc.save()

                        if doc_type in archivos_url:
                            if not archivos_url[doc_type] == archivo_doc.ST_DOC_USUARIO:
                                ruta_archivo = archivos_url[doc_type].path
                                if os.path.exists(ruta_archivo):
                                    os.remove(ruta_archivo)
                    else:
                        archivo_doc = form_doc.save(commit=False)

                        if archivo_doc.ST_TIPO_DOC_USUARIO:
                            archivo_doc.ST_DOC_USUARIO = archivos_url[archivo_doc.ST_TIPO_DOC_USUARIO]
                            archivo_doc.delete()

        messages.success(request, "Administrador ha sido actualizado exitosamente.")
        return redirect('Administrador')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form, "form_documents": form_documents}
    return render(request, 'Administrador/edit.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def details(request, id):
    admin = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(FK_USUARIO_id=id)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Administrador/details.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def changeStatus(request, id):
    admin = Usuario.objects.get(id=id)
    admin.is_active = not admin.is_active
    if (admin.is_active):
        msg = "Usuario ha sido activado correctamente."
    else:
        msg = "Usuario ha sido desactivado correctamente."
    admin.save()
    messages.success(request, msg)
    return redirect('Administrador')


@login_required(login_url='login')
@allowed_users(['Administrador'])
def delete(request, id):
    admin = Usuario.objects.get(id=id)
    admin.BN_ESTADO_USUARIO = 0
    msg = "Usuario ha sido eliminado correctamente."
    admin.save()
    messages.success(request, msg)
    return redirect('Administrador')
