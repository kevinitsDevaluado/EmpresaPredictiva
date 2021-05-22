from django.db import models
from django.contrib.auth.models import User
from django.forms import model_to_dict
from config.settings import MEDIA_URL, STATIC_URL
from django.conf import settings
class Equipo(models.Model):
    estado = (
        ('Activo', 1),
        ('Inactivo', 0)
    )
    codigo = models.CharField(max_length=100, blank=False, unique=True, null=False)
    nombre = models.CharField(max_length=100, blank=False, null=False)
    imagen = models.ImageField(upload_to='equipos', blank=True, null=False)
    esquema = models.ImageField(upload_to='esquemas', blank=True, null=False)
    estandar = models.CharField(max_length=100, blank=False, null=False)
    tolerancia = models.CharField(max_length=255, blank=False, null=False)
    mantenimiento = models.CharField(max_length=30, blank=False, null=False)
    diagnostico = models.CharField(max_length=255, blank=False, null=False)
    recomendaciones = models.CharField(max_length=255, blank=False, null=False)
    
    #detalle del equipo
    area = models.CharField(max_length=50, blank=False, null=False)
    tipo = models.CharField(max_length=50, blank=False, null=False)
    potencia = models.CharField(max_length=50, blank=False, null=False)
    vel_nominal = models.CharField(max_length=50, blank=False, null=False)
    transmision = models.CharField(max_length=50, blank=False, null=False)
    carga = models.CharField(max_length=10, blank=False, null=False)
    vel_operacion = models.CharField(max_length=50, blank=False, null=False)
    marca = models.CharField(max_length=50, blank=False, null=False)
    modelo = models.CharField(max_length=50, blank=False, null=False)
    serie = models.CharField(max_length=50, blank=False, null=False)
    
    estado = models.IntegerField(blank=False, null=False, choices=estado, default=1)
    
    #relación auth_user - equipo
    id_auth_user = models.ForeignKey(settings.AUTH_USER_MODEL, blank=False, null=False, on_delete=models.CASCADE,related_name='posts')
    
    creada_en = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    actualizada_en = models.DateTimeField(auto_now=True, null=True, blank=True)

    def get_image(self):
        if self.imagen:
            return '{}{}'.format(MEDIA_URL, self.imagen)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def get_images(self):
        if self.esquema:
            return '{}{}'.format(MEDIA_URL, self.esquema)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    def toJSON(self):
        item = model_to_dict(self)
        item['imagen'] = self.get_image()
        item['esquema'] = self.get_images()        
        item['creada_en'] = self.creada_en.strftime('%Y-%m-%d')
        item['actualizada_en'] = self.actualizada_en.strftime('%Y-%m-%d')
        item['id_auth_user'] = self.id_auth_user.toJSON()
        return item

    class Meta:
        verbose_name = 'Equipo'
        verbose_name_plural = 'Equipos'
        ordering = ['id']