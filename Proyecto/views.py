from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProyectoForm, TransporteForm, ConcretoForm, LevantamientoToporgraficoForm,RentaEquipoForm,RentaDesimetroForm,AsesoriaConstructivaForm,EstructuraMetalicaForm, SenializacionVialForm


def index(request):
    return render(request, 'Proyecto/index.html')

def add(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)        
        if form.is_valid():
            tipoServicio = request.POST["FK_TIPO_SERVICIO"]

            form_mapping = {
                "1": ConcretoForm,
                "2": RentaEquipoForm,
                "3": RentaDesimetroForm,
                "4": TransporteForm,
                "5": LevantamientoToporgraficoForm,
                "6": EstructuraMetalicaForm,
                "7": SenializacionVialForm,
                "8": AsesoriaConstructivaForm,
            }

            if tipoServicio in form_mapping:
                formEspecificaciones = form_mapping[tipoServicio]
                
                context = {
                    "tipoServicio": form.cleaned_data['FK_TIPO_SERVICIO'], 
                    "form": form,
                    "formEspecificaciones": formEspecificaciones 
                }

                if tipoServicio in ["1", "5", "6", "7"]:
                    return render(request, 'Proyecto/step-5.html', context)
                elif tipoServicio in ["2", "3", "4", "8"]:
                    return render(request, 'Proyecto/step-3.html', context)   
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

