from datetime import datetime

from django import forms
from django.forms import ModelForm

from core.erp.models import *




class OrientationForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['orientacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = OrientationPag
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre de la orientación',
                }
            ),
            'orientacion': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese la orientación',
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data



class ConfigForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # for form in self.visible_fields():
        #     form.field.widget.attrs['class'] = 'form-control'
        #     form.field.widget.attrs['autocomplete'] = 'off'
        self.fields['orientacion'].widget.attrs['autofocus'] = True

    class Meta:
        model = ConfigPagina
        fields = '__all__'
        widgets = {
            'color': forms.TextInput(
                attrs={
                    'placeholder': 'Ingrese el color',
                }
            ),
            'orientacion': forms.Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data