from django import forms

from Equipo.models import Equipo


class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = '__all__'
        exclude = ['BN_ESTADO_EQUIPO']
        widgets = {
            'ST_NOMBRE_EQUIPO': forms.TextInput(attrs={'class': 'form-control'}),
            'ST_DESCRIPCION_EQUIPO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'SK_TIPO_EQUIPO': forms.Select(attrs={'class': 'form-control'}),
            'FC_INGRESO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'ST_IMG_EQUIPO': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

