from django import forms

from Proyecto.models import Proyecto


class ProyectoForm(forms.ModelForm):
    class Meta:
        model = Proyecto
        fields = '__all__'
        exclude = ['NM_LATITUD_PROYECTO','NM_LONGITUD_PROYECTO','FK_ESTADO_PROYECTO','FK_USUARIO','FC_INGRESO_PROYECTO']
        widgets = {
            'ST_DIRECCION_PROYECTO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ST_DESCRIPCION_PROYECTO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'FK_CLIENTE': forms.Select(attrs={'class': 'form-control select2', 'data-bs-toggle':'select2'}),
            'FK_TIPO_SERVICIO': forms.Select(attrs={'class': 'form-control select2', 'data-bs-toggle':'select2'}),
        }