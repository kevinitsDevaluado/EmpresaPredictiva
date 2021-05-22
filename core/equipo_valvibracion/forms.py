from django import forms
from core.equipo_valvibracion.models import Equipo_valvibracion

class Equipo_valvibracionForm(forms.ModelForm):
    class Meta:
        model = Equipo_valvibracion
        fields = [
            'nombre',
            'fecha',
            'valor',
            'unidad',
        ]
        labels = {
            'nombre': 'Nombre',
            'fecha': 'Fecha',
            'valor': 'Valor',
            'unidad': 'Unidad',
        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre'}),
            'fecha': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Ingrese la fecha'}),
            'valor': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el valor'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la unidad'}),
        }