from django.db import models
from core.equipo.models import Equipo

class Equipo_tendespectro(models.Model):
    descripcion = models.CharField(max_length=255, blank=False, null=False)
    imagen = models.ImageField(upload_to='tendencias', blank=True, null=False)
    
    #relacion Equipo - Tendencia de vibracion y espectros relevantes
    id_equipo = models.ForeignKey(Equipo, blank=False, null=False, on_delete=models.CASCADE)
    
    creada_en = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    actualizada_en = models.DateTimeField(auto_now_add=True, blank=True, null=True)