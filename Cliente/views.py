from django.shortcuts import render,redirect
from Cliente.models import Cliente
from .forms import ClienteForm
from django.contrib import messages

def index(request):
    clientes=Cliente.objects.all()
    return render(request, 'Cliente/index.html',{'clientes':clientes})

def detailsCliente(request,id):
    cliente=Cliente.objects.get(SK_CLIENTE=id)
    return render(request,'Cliente/details.html',{"cliente":cliente})

def createCliente(request):
    if request.method == 'POST':
        cliente=Cliente()
        form = ClienteForm(request.POST)
        if form.is_valid() and form.cleaned_data:
            cliente=form.save(commit=False)
            cliente.SK_USUARIO=request.user
            cliente.save()
            messages.success(request, "Cliente creado exitosamente.")
            return redirect('Cliente')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = ClienteForm()
    return render(request,'Cliente/add.html',{"form":form})

def editCliente(request,id):
    cliente=Cliente.objects.get(SK_CLIENTE=id)
    form = ClienteForm(request.POST or None,instance=cliente)
    if request.method == 'POST':
        if form.is_valid() and form.cleaned_data:
            cliente=form.save()
            messages.success(request, "Cliente creado exitosamente.")
            return redirect('Cliente')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    return render(request,'Cliente/edit.html',{"form":form})

def changeStatus(request, id):
    cliente = Cliente.objects.get(SK_CLIENTE=id)
    cliente.BN_ESTA_ACTIVO = not cliente.BN_ESTA_ACTIVO
    if (cliente.BN_ESTA_ACTIVO):
        msg = "Usuario activado correctamente."
    else:
        msg = "Usuario desactivado correctamente."
    cliente.save()
    messages.success(request, msg)
    return redirect('Cliente')

