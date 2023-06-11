from django import forms
from Administrador.models import Usuario,DocumentoUsuario
from django.contrib.auth.hashers import make_password
from django.core.validators import MaxLengthValidator
from django.db import transaction
from django.contrib.auth.models import Group

class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                'placeholder': "Ingrese de nuevo la contraseña",
        }),
        label='Confirmación contraseña',
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
            'first_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el nombre",
                    'required': 'required'
                },
            ),
            'last_name': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el apellido",
                    'required': 'required'
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el nombre de usuario",
                    'required': 'required'
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese la contraseña",
                    'required': 'required'
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese la dirección de correo electrónico",
                    'required': 'required'
                }
            ),
            'ST_DUI_USUARIO': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el DUI",
                    'data-mask': "00000000-0",
                    'maxlength': "10",
                    'minlength': "10",
                    'required': 'required'
                },
            ),
            'ST_NIT_USUARIO': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el NIT",
                    'data-mask': "0000-000000-000-0",
                    'maxlength': "17",
                    'minlength': "17"
                },
            ), 
            'ST_AFP_USUARIO': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el NUP",
                    'data-mask': "000000000000",
                    'maxlength': "12",
                    'minlength': "12",
                },
            ),
            'ST_ISSS_USUARIO': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': "Ingrese el N° de Afiliación",
                    'data-mask': "000000000",
                    'maxlength': "9",
                    'minlength': "9"
                },
            ),
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
        #Asignación de rol (grupo)
        group = Group.objects.get(name='Empleado')
        user.groups.add(group)

        if (self.cleaned_data['nit_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['nit_file']
            documento.FK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "NIT"
            documento.save()
        
        if (self.cleaned_data['dui_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['dui_file']
            documento.FK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "DUI"
            documento.save()
        
        if (self.cleaned_data['afp_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['afp_file']
            documento.FK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "AFP"
            documento.save()
        
        if (self.cleaned_data['isss_file']):
            documento = DocumentoUsuario()
            documento.ST_DOC_USUARIO = self.cleaned_data['isss_file']
            documento.FK_USUARIO = user
            documento.ST_TIPO_DOC_USUARIO = "ISSS"
            documento.save()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['FC_NACIMIENTO'].widget.attrs['placeholder'] = 'dd/mm/aaaa'
        self.fields['FC_NACIMIENTO'].widget.attrs['class'] = 'form-control'
    
class DocumentUserForm(forms.ModelForm):
    class Meta:
        model = DocumentoUsuario
        fields = ['ST_DOC_USUARIO']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['ST_DOC_USUARIO'].required = False


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined', 'FC_INGRESO_USUARIO','password',"BN_ESTADO_USUARIO"]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'FC_NACIMIENTO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'dd/mm/aaaa'}),
            'ST_DUI_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxxxxxx-x', 'data-mask': '00000000-0'}),
            'ST_NIT_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'xxxx-xxxxxx-xxx-x', 'data-mask': '0000-000000-000-0'}),
            'ST_AFP_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite su NUP'}),
            'ST_ISSS_USUARIO': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite su N° de Afiliacion'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['maxlength'] = 60
        self.fields['last_name'].widget.attrs['maxlength'] = 60
        self.fields['username'].widget.attrs['maxlength'] = 50
        self.fields['email'].widget.attrs['maxlength'] = 60