from django.db import models
from core.equipo.models import Equipo

class Equipo_valvibracion(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    fecha = models.CharField(max_length=15, blank=False, null=False)
    valor = models.CharField(max_length=10, blank=False, null=False)
    unidad = models.CharField(max_length=10, blank=False, null=False)
    
    #relacion Equipo - Valor de vibracion
    id_equipo = models.ForeignKey(Equipo, blank=False, null=False, on_delete=models.CASCADE)
    
    creada_en = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    actualizada_en =models.DateTimeField(auto_now=True, blank=True, null=True)