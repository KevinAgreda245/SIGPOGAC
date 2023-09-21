from django import forms
from Proyecto.models import Proyecto,EstadoProyecto, RentaEquipo,TipoServicio, Transporte
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


class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'
        exclude = ['NM_VOLUMEN,FK_PROYECTO']
        widgets = {
            'ST_UNIDAD_TRANSPORTE': forms.Select(attrs={'class': 'form-control select2', 'data-bs-toggle':'select2'}),
            'NM_VOLUMEN' :  forms.TextInput(attrs={'class': 'form-control','required': 'required', 'type': 'number', 'step': '.01', 'min':'0.00'}),
        }


class RentaEquipoForm(forms.ModelForm):
    class Meta:
        model = RentaEquipo
        fields = '__all__'
        exclude = ['SK_RENTA_EQUIPO, FK_PROYECTO,FC_SALIDA_EQUIPO,FC_ENTRADA_EQUIPO']
        widgets = {
            'ST_TIPO_USO' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ST_OBSERVACION_EQUIPO' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }