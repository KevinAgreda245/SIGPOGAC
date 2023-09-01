from django import forms
from Proyecto.models import Proyecto,Concreto,Transporte,RentaEquipo,RentaDesimetro,LevantamientoTopografico,EstructuraMetalica,SenializacionVial,AsesoriaConstructiva
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

class ConcretoForm(forms.ModelForm):
    class Meta:
        model = Concreto
        fields = '__all__'
        exclude = ['FK_PROYECTO']
        widgets={
          'ST_TIPO_DOC_CONCRETO': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
          'ST_DOC_CONCRETO': forms.ClearableFileInput(attrs={'class': 'form-control'}),
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

class RentaDesimetroForm(forms.ModelForm):
    class Meta:
        model = RentaDesimetro
        fields = '__all__'
        exclude = ['SK_RENTA_DESIMETRO, FC_ENTRADA_DESIMETRO, FC_SALIDA_DESIMETRO, FK_PROYECTO']
        widgets ={
            'ST_NOMBRE_TECNICO' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'ST_OBSERVACION_DESIMETRO' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

class TransporteForm(forms.ModelForm):
    class Meta:
        model = Transporte
        fields = '__all__'
        exclude = ['NM_VOLUMEN,FK_PROYECTO']
        widgets = {
            'ST_UNIDAD_TRANSPORTE': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
            'NM_VOLUMEN' : forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
        }


class LevantamientoToporgraficoForm(forms.ModelForm):
    class Meta:
        model = LevantamientoTopografico
        fields = '__all__'
        exclude = ['SK_LEVANTAMIENTO_TOPOGRAFICO, FK_PROYECTO']
        widgets = {
            'NM_AREA' : forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
            'ST_UNIDAD_LEVANTAMIENTO' : forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
        }


class EstructuraMetalicaForm(forms.ModelForm):
    class Meta:
        model = EstructuraMetalica
        fields = '__all__'
        exclude = ['SK_ESTRUCTURA_METALICA, FK_PROYECTO']
        widgets = {
            'ST_TIPO_DOC_CONCRETO' : forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
            'ST_DOC_CONCRETO' : forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class SenializacionVialForm(forms.ModelForm):
    class Meta:
        model = SenializacionVial
        fields = '__all__'
        exclude = ['SK_SENIALIZACION_VIAL, FK_PROYECTO']
        widgets = {
            'ST_ESPECIFICACION_VIAL' : forms.Textarea(attrs={'class': 'form-control', 'rows' : '3'}),
        }

class AsesoriaConstructivaForm(forms.ModelForm):
    class Meta:
        model = AsesoriaConstructiva
        fields = '__all__'
        exclude = ['SK_ASESORIA, FK_PROYECTO']
        widgets = {
            'NM_TIEMPO' : forms.TextInput(attrs={'class': 'form-control'}),
            'ST_UNIDAD_ASESORIA' : forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }