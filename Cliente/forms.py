from django import forms
from django.core.validators import MaxLengthValidator
from django.db import transaction

from .models import Cliente
from django.contrib.auth.hashers import make_password

class ClienteForm(forms.ModelForm):
    ST_NOMBRE_CLIENTE=forms.CharField(
        label="Nombre",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese el nombre del cliente'})
    )
    BN_TIPO_CLIENTE=forms.ChoiceField(
        label="Tipo de cliente",
        widget=forms.Select(attrs={'class': 'form-control select2', 'data-bs-toggle':'select2'}),
        choices = [
        ('', 'Seleccione una opción'),
        ('False', 'Natural'),
        ('True', 'Jurídico'),
        ]
    )
    ST_DOC_CLIENTE=forms.CharField(
        label="DUI/NRC",
        widget=forms.TextInput(attrs={'class': 'form-control'}),
    )
    ST_NIT_CLIENTE=forms.CharField(
        label="NIT",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el NIT del cliente', 'data-mask': '0000-000000-000-0','minlength':"17"})
    )
    class Meta:
        model=Cliente
        fields=['ST_NOMBRE_CLIENTE','BN_TIPO_CLIENTE','ST_NIT_CLIENTE','ST_DOC_CLIENTE'] 

    