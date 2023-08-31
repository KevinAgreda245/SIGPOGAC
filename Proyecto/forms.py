from django import forms
from Proyecto.models import Proyecto,Transporte,Concreto
from Cliente.models import Cliente



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
        
    def __init__(self, *args, **kwargs):
        super(ProyectoForm, self).__init__(*args, **kwargs)
        self.fields['FK_CLIENTE'].queryset = Cliente.objects.filter(BN_ESTA_ACTIVO=True)


class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'
        exclude = ['NM_VOLUMEN,FK_PROYECTO']
        widgets = {
            'ST_UNIDAD_TRANSPORTE': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class ConcretoForm(forms.ModelForm):
    class Meta:
        model = Concreto
        fields = '__all__'
        exclude = ['ST_DOC_CONCRETO', 'FK_PROYECTO']
        widgets={
          'ST_TIPO_DOC_CONCRETO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
          'ST_DOC_CONCRETO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }