from django import forms
from .models import Usuario

class CreateUserForm(forms.ModelForm):
    password_confirm = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        label='Confirmar contraseña:'
    )

    class Meta:
        model = Usuario
        fields = ['first_name','last_name','username','password','password_confirm','email','ST_DUI_USUARIO','ST_NIT_USUARIO','ST_AFP_USUARIO','ST_ISSS_USUARIO','FC_NACIMIENTO'] 

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['ST_DUI_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_NIT_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_AFP_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['ST_ISSS_USUARIO'].widget.attrs['class'] = 'form-control'
        self.fields['FC_NACIMIENTO'].widget.attrs['class'] = 'form-control'
        self.fields['FC_NACIMIENTO'].widget.attrs['type'] = 'date'
        self.fields['FC_NACIMIENTO'].label = "Fecha de Nacimiento"
    