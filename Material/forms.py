from django import forms

from .models import Material

class MaterialForm(forms.ModelForm):
    class Meta:
        model = Material
        fields = ["ST_NOMBRE_MATERIAL","ST_DESCRIPCION_MATERIAL"]
        widgets = {
            'ST_NOMBRE_MATERIAL': forms.TextInput(attrs={'class': 'form-control'}),
            'ST_DESCRIPCION_MATERIAL': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }