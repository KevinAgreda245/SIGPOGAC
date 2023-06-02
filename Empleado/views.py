from django.shortcuts import redirect, render
from django.contrib import messages
from Administrador.models import Usuario, DocumentoUsuario
from .forms import *
from tarfile import NUL


class DocumentUserForm(forms.ModelForm):
    class Meta:
        model = DocumentoUsuario
        fields = ['ST_DOC_USUARIO']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ST_DOC_USUARIO'].required = False


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'FC_INGRESO_USUARIO','password']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'FC_NACIMIENTO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'ST_DUI_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxxxxxx-x', 'data-mask': '00000000-0'}),
            'ST_NIT_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxx-xxxxxx-xxx-x', 'data-mask': '0000-000000-000-0'}),
            'ST_AFP_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite su NUP'}),
            'ST_ISSS_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite su N° de Afiliacion'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['maxlength'] = 60
        self.fields['last_name'].widget.attrs['maxlength'] = 60
        self.fields['username'].widget.attrs['maxlength'] = 50
        self.fields['email'].widget.attrs['maxlength'] = 60


def main(request):
    return render(request, 'Empleado/main.html')


def index(request):
    empleados = Usuario.objects.filter(is_staff=0)
    context = {
        "empleados": empleados
    }
    return render(request, 'Empleado/index.html', context)


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


def details(request, id):
    empleado = Usuario.objects.get(id=id)
    docs = DocumentoUsuario.objects.filter(SK_USUARIO_id=id)
    context = {
        "empleado": empleado,
        "docs": docs
    }
    return render(request, 'Empleado/details.html', context)


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