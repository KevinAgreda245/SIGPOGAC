from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from Administrador.models import Usuario, DocumentoUsuario
from .forms import *
from tarfile import NUL
from Seguridad.decorators import *

@login_required(login_url='login')
def main(request):
    return render(request, 'Empleado/main.html')


@login_required(login_url='login')
@allowed_users(['Administrador'])
def index(request):
    empleados = Usuario.objects.filter(is_staff=0)
    context = {
        "empleados": empleados
    }
    return render(request, 'Empleado/index.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def add(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Empleado creado exitosamente.")
            return redirect('Empleado')
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
    return render(request, 'Empleado/add.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def details(request, id):
    empleado = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id=id)
    context = {
        "empleado": empleado,
        "docs": docs
    }
    return render(request, 'Empleado/details.html', context)


@login_required(login_url='login')
@allowed_users(['Administrador'])
def changeStatus(request, id):
    empleado = Usuario.objects.get(id=id)
    empleado.is_active = not empleado.is_active
    if (empleado.is_active):
        msg = "Usuario activado correctamente."
    else:
        msg = "Usuario desactivado correctamente."
    empleado.save()
    messages.success(request, msg)
    return redirect('Empleado')


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

        messages.success(request, "Empleado actualizado exitosamente.")
        return redirect('Empleado')
    else:
        for field, errors in form.errors.items():
            form.fields[field].widget.attrs.update({
                'class': "form-control is-invalid"
            })
            messages.error(request, errors)

    context = {"form": form, "form_documents": form_documents}
    return render(request, 'Empleado/edit.html', context)