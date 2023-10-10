from datetime import datetime
from django import forms

from Cliente.models import Cliente
from Proyecto.models import EstadoProyecto, TipoServicio

class ReportesForm(forms.Form):
    cliente = forms.ModelChoiceField(
        queryset=Cliente.objects.all(),  
        required=False,
        empty_label="Todos los clientes",
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="Cliente:"
    )
    estado = forms.ModelChoiceField(
        queryset=EstadoProyecto.objects.all(), 
        required=False,
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="Estado:"
    )
    tipo = forms.ModelChoiceField(
        queryset=TipoServicio.objects.all(), 
        required=True,
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="Tipo de Servicio:"
    )
    fechaDesde = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control data-picker', 'placeholder': 'dd/mm/aaaa'}),
        label = "Fecha Desde:"
    )
    fechaHasta = forms.CharField(
        required = False,
        widget = forms.TextInput(attrs={'class': 'form-control data-picker', 'placeholder': 'dd/mm/aaaa'}),
        label = "Fecha Hasta:"
    )
    def clean(self):
        cleaned_data = super().clean()
        fecha_desde = cleaned_data.get('fechaDesde')
        fecha_hasta = cleaned_data.get('fechaHasta')
        
        if (fecha_desde and not fecha_hasta) or (not fecha_desde and fecha_hasta):
            raise forms.ValidationError("Para realizar una búsqueda por fechas, ambas deben de ser seleccionadas.")

        if fecha_desde and fecha_hasta:
            try:
                fecha_desde_obj = datetime.strptime(fecha_desde, '%d/%m/%Y')
                fecha_hasta_obj = datetime.strptime(fecha_hasta, '%d/%m/%Y')
            except ValueError:
                raise forms.ValidationError("Formato inválido. El formato es el siguiente: dd/mm/yyyy.")

            if fecha_hasta_obj < fecha_desde_obj:
                raise forms.ValidationError("La fecha hasta no puede ser menor a la fecha desde.")

        return cleaned_data

