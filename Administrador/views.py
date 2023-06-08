from tarfile import NUL
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import Usuario, DocumentoUsuario
from .forms import *


@login_required(login_url='login')
def main(request):
    return render(request, 'Administrador/main.html')


@login_required(login_url='login')
def management(request):
    admins = Usuario.objects.filter(is_staff=1)
    context = {
        "admins": admins
    }
    return render(request, 'Administrador/management.html', context)


@login_required(login_url='login')
def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Administrador creado exitosamente.")
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

        messages.success(request, "Administrador actualizado exitosamente.")
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
def details(request, id):
    admin = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id=id)
    context = {
        "admin": admin,
        "docs": docs
    }
    return render(request, 'Administrador/details.html', context)


@login_required(login_url='login')
def changeStatus(request, id):
    admin = Usuario.objects.get(id=id)
    admin.is_active = not admin.is_active
    if (admin.is_active):
        msg = "Usuario activado correctamente."
    else:
        msg = "Usuario desactivado correctamente."
    admin.save()
    messages.success(request, msg)
    return redirect('Administrador')
