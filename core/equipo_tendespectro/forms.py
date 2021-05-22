from django import forms
from core.equipo_tendespectro.models import Equipo_tendespectro

class Equipo_tendespectroForm(forms.ModelForm):
    class Meta:
        model = Equipo_tendespectro
        fields = [
            'descripcion',
            'imagen',
        ]
        labels = {
            'descripcion': 'Descripción',
            'imagen': 'Imagen',
        }
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows': '5','placeholder': 'Ingrese una descripción'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Ingrese la imagen'}),
        }