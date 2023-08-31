from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProyectoForm, TransporteForm, ConcretoForm


def index(request):
    return render(request, 'Proyecto/index.html')

def add(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)        
        if form.is_valid():
            tipoServicio = request.POST["FK_TIPO_SERVICIO"]

            if tipoServicio == "1" or tipoServicio == "5" or tipoServicio == "6" or tipoServicio == "7":
                context = {
                    "tipo": tipoServicio,
                    "form": form,
                }               
                return render(request, 'Proyecto/step-5.html',context)            
            else:
                messages.error(request, "En construcción")
        else:
            for field, errors in form.errors.items():
                form.fields[field].widget.attrs.update({
                    'class': "form-control is-invalid"
                })
                messages.error(request, errors)
    else:
        form = ProyectoForm()
        
    context = {
        "form": form,
    }
    return render(request, 'Proyecto/add.html',context)

