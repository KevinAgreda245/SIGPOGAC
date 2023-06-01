from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from Administrador.forms import DocumentUserForm, UpdateUserForm
from Administrador.models import Usuario, DocumentoUsuario


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


def details(request, id):
    admin = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id=id)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Seguridad/details.html', context)


def edit(request, id):
    usuario = Usuario.objects.get(pk=id)

    form = UpdateUserForm(request.POST or None, instance=usuario)

    form_documents = {
        "NIT": DocumentUserForm(request.POST or None, request.FILES or None, prefix='NIT'),
        "DUI": DocumentUserForm(request.POST or None, request.FILES or None, prefix='DUI'),
        "ISSS": DocumentUserForm(request.POST or None, request.FILES or None, prefix='ISSS'),
        "AFP": DocumentUserForm(request.POST or None, request.FILES or None, prefix='AFP')
    }

    if DocumentoUsuario.objects.filter(SK_USUARIO=usuario.pk).exists():
        documentos = DocumentoUsuario.objects.filter(SK_USUARIO=usuario.pk)

        for documento in documentos:
            form_documents[documento.ST_TIPO_DOC_USUARIO] = DocumentUserForm(
                request.POST or None,
                request.FILES or None,
                instance=documento,
                prefix=documento.ST_TIPO_DOC_USUARIO
            )

    if form.is_valid():
        with transaction.atomic():
            usuario = form.save()

            for doc_type, form_doc in form_documents.items():
                if form_doc.is_valid() and form_doc.cleaned_data.get('ST_DOC_USUARIO'):
                    archivo_doc = form_doc.save(commit=False)
                    archivo_doc.ST_TIPO_DOC_USUARIO = doc_type
                    archivo_doc.SK_USUARIO = usuario
                    archivo_doc.save()

        messages.success(request, "Perfil actualizado exitosamente.")
        return redirect('DetailsProfile', id)
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form, "form_documents": form_documents}
    return render(request, 'Seguridad/edit.html', context)

