from django import forms
from core.equipo.models import Equipo

class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'codigo',
            'nombre',
            'imagen',
            'esquema',
            'estandar',
            'tolerancia',
            'mantenimiento',
            'diagnostico',
            'recomendaciones',
            
            'area',
            'tipo',
            'potencia',
            'vel_nominal',
            'transmision',
            'carga',
            'vel_operacion',
            'marca',
            'modelo',
            'serie',
        ]
        labels = {
            'codigo': 'Código',
            'nombre': 'Nombre del equipo',
            'imagen': ' Imagen',
            'esquema': 'Esquema',
            'estandar': 'Estándares',
            'tolerancia': 'Tolerancia de Alarma y Peligro',
            'mantenimiento': 'Prioridad de mantenimiento',
            'diagnostico': 'Diagnóstico',
            'recomendaciones': 'Recomendaciones',
            
            'area': 'Área',
            'tipo': 'Tipo',
            'potencia': 'Potencia',
            'vel_nominal': 'Vel. nominal',
            'transmision': 'Transmisión',
            'carga': 'Carga',
            'vel_operacion': 'Vel. Operación',
            'marca': 'Marca',
            'modelo': 'Modelo',
            'serie': 'Serie',
        }
        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el código'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el nombre del equipo'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Ingrese la imagen del equipo'}),
            'esquema': forms.FileInput(attrs={'class': 'form-control','placeholder': 'Ingrese el esquema'}),
            'estandar': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese los estándares'}),
            'tolerancia': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la tolerancia de alarma y peligro'}),
            'mantenimiento': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la prioridad de mantenimiento'}),
            'diagnostico': forms.Textarea(attrs={'class': 'form-control','rows': '5', 'placeholder': 'Ingrese el diagnóstico'}),
            'recomendaciones': forms.Textarea(attrs={'class': 'form-control','rows': '5', 'placeholder': 'Ingrese las recomendaciones'}),
            
            'area': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el área'}),
            'tipo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el tipo'}),
            'potencia': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la potencia'}),
            'vel_nominal': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el Vel. nominal'}),
            'transmision': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la transmisión'}),
            'carga': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la carga'}),
            'vel_operacion': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el Vel. Operación'}),
            'marca': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la marca'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese el modelo'}),
            'serie': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Ingrese la serie'}),
        }