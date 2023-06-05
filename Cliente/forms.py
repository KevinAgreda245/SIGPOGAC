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
    ST_DOC_CLIENTE=forms.CharField(
        label="DUI",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'xxxxxxxx-x', 'data-mask': '00000000-0'}),
    )
    ST_NIT_CLIENTE=forms.CharField(
        label="NIT",
        widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'xxxx-xxxxxx-xxx-x', 'data-mask': '0000-000000-000-0'})
    )
    BN_TIPO_CLIENTE=forms.ChoiceField(
        label="Tipo de cliente",
        widget=forms.Select(attrs={'class': 'form-control'}),
        choices = [
       ('False', 'Natural'),
       ('True', 'Jurídico'),
        ]
    )
    class Meta:
        model=Cliente
        exclude=['SK_CLIENTE','SK_USUARIO','FC_INGRESO_CLIENTE','BN_ESTA_ACTIVO'] 

    