from django import forms
from .models import Usuario

class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirmar contraseña',
        required=True
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
    