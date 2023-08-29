from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProyectoForm


def index(request):
    return render(request, 'Proyecto/index.html')

def add(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Material creado exitosamente.")
            return redirect('AddProyecto')
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = ProyectoForm()
    context = {
        "form": form
    }
    return render(request, 'Proyecto/add.html',context)