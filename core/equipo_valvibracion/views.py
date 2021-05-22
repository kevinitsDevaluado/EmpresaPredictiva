from core.fechas.views import get_fecha_hora
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from core.equipo_valvibracion.models import Equipo_valvibracion
from core.equipo_valvibracion.forms import Equipo_valvibracionForm
from core.fechas.views import get_fecha_hora

# Create your views here.
def guardar(request, id):
    if request.method == 'POST':
        fecha_actual = request.POST.get('fecha')
        form = Equipo_valvibracionForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.id_equipo_id = id
            form.instance.fecha = str(fecha_actual)
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect('ERROR AL GUARDAR')
    else:
        return HttpResponseRedirect('ERROR AL GUARDAR')
    
def editar(request, id):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        fecha = request.POST.get('fecha')
        unidad = request.POST.get('unidad')
        valor = request.POST.get('valor')
        
        valvibracion = Equipo_valvibracion.objects.get(id=id)
        valvibracion.nombre = nombre
        valvibracion.fecha = fecha
        valvibracion.unidad = unidad
        valvibracion.valor = valor
        if valvibracion.save():
            return HttpResponseRedirect('ERROR AL EDITAR')
        else:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect('ERROR AL EDITAR')
    
def eliminar(request, id):
    if request.method == 'GET':
        valvibracion = Equipo_valvibracion.objects.get(id=id)
        valvibracion.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect('ERROR AL ELIMINAR')