from django import forms
from django.contrib.auth.forms import PasswordResetForm, PasswordChangeForm, SetPasswordForm

class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)


    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ingresa tu correo electrónico',
        'type': 'email',
        'name': 'email'
        }))
    
    def clean_email(self):
        email = self.cleaned_data.get('email')

        self.fields['email'].widget.attrs['class'] = 'form-control is-invalid'

        if (email != 'kevin.ale24@gmail.com'):
            raise forms.ValidationError('Correo malo 2.')
        
        return email


#Se utiliza el SetPasswordForm ya que no requiere contraseña antigua
class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordChangeForm, self).__init__(*args, **kwargs)
        #self.fields["old_password"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password1"].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields["new_password2"].widget = forms.PasswordInput(attrs={"class": "form-control"})  

    

    
    
    
    
    

        