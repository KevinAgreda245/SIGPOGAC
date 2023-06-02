from django import forms
from Administrador.models import Usuario,DocumentoUsuario
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxLengthValidator
from django.db import transaction

class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirmar contraseña',
        required=True
    )
    nit_file = forms.FileField(
        label='Archivo de NIT',
        required=False
    )
    dui_file = forms.FileField(
        label='Archivo de DUI',
        required=False
    )
    isss_file = forms.FileField(
        label='Archivo de ISSS',
        required=False
    )
    afp_file = forms.FileField(
        label='Archivo de AFP',
        required=False
    )

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','password','password_confirm','email','ST_DUI_USUARIO','ST_NIT_USUARIO','ST_AFP_USUARIO','ST_ISSS_USUARIO','FC_NACIMIENTO'] 
        widgets = {
            'password': forms.PasswordInput()
        }


    def clean_password_confirm(self):
        pass1 = self.cleaned_data.get('password')
        pass2 = self.cleaned_data.get('password_confirm')

        if pass1 and pass2 and pass1 != pass2:
            raise forms.ValidationError('Las contraseña no coinciden.')

    def save(self):
        user = Usuario()
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = make_password(self.cleaned_data['password'])
        user.ST_DUI_USUARIO = self.cleaned_data['ST_DUI_USUARIO']
        user.ST_NIT_USUARIO = self.cleaned_data['ST_NIT_USUARIO']
        user.ST_AFP_USUARIO = self.cleaned_data['ST_AFP_USUARIO']
        user.ST_ISSS_USUARIO = self.cleaned_data['ST_ISSS_USUARIO']
        user.FC_NACIMIENTO = self.cleaned_data['FC_NACIMIENTO']
        user.is_staff = 0
        user.save()

        if (self.cleaned_data['nit_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['nit_file']
            documento.SK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "NIT"
            documento.save()
        
        if (self.cleaned_data['dui_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['dui_file']
            documento.SK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "DUI"
            documento.save()
        
        if (self.cleaned_data['afp_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['afp_file']
            documento.SK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "AFP"
            documento.save()
        
        if (self.cleaned_data['isss_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['isss_file']
            documento.SK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "ISSS"
            documento.save()
        




    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['first_name'].required = True

        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].required = True

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].required = True

        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].required = True

        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].required = True
        
        self.fields['ST_DUI_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_DUI_USUARIO'].widget.attrs['data-mask'] = '00000000-0'
        self.fields['ST_DUI_USUARIO'].label = "DUI"

        self.fields['ST_NIT_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_NIT_USUARIO'].widget.attrs['data-mask'] = '0000-000000-000-0'
        self.fields['ST_NIT_USUARIO'].label = "NIT"

        self.fields['ST_AFP_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_AFP_USUARIO'].label = "AFP"
        
        self.fields['ST_ISSS_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_ISSS_USUARIO'].label = "ISSS"
        
        self.fields['FC_NACIMIENTO'].widget.attrs['class'] = 'form-control'
        self.fields['FC_NACIMIENTO'].label = "Fecha de Nacimiento"
    