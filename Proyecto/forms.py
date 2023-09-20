from django import forms
from Proyecto.models import Proyecto,EstadoProyecto,TipoServicio
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

class FiltroProyectosForm(forms.Form):
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
        required=False,
        widget=forms.Select(attrs={'class': 'form-control select2'}),
        label="Tipo de Servicio:"
    )