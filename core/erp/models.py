#CARGAR MATERIA PRIMA
from django.db import models
from django.forms import model_to_dict

class OrientationPag(models.Model):
    nombre = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    orientacion = models.CharField(max_length=150, verbose_name='Orientacion', unique=True)
    
    def toJSON(self):
        item = model_to_dict(self)
#        item['orientacion'] = self.orientacion.toJSON()
        #item['date_ven'] = self.date_ven.strftime('%Y-%m-%d')
        #item['date_add'] = self.date_add.strftime('%Y-%m-%d')
        return item


    def __str__(self):
        return self.nombre

class ConfigPagina(models.Model):
    color = models.CharField(max_length=150, verbose_name='Color')
    orientacion = models.ForeignKey(OrientationPag, on_delete=models.CASCADE, verbose_name='Orientacion')
    
    def toJSON(self):
        item = model_to_dict(self)
        item['orientacion'] = self.orientacion.toJSON()
        #item['color'] = self.color.toJSON()
        #item['date_ven'] = self.date_ven.strftime('%Y-%m-%d')
        #item['date_add'] = self.date_add.strftime('%Y-%m-%d')
        return item
    
    def __str__(self):
        return self.id 
