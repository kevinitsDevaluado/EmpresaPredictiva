from django.shortcuts import render
from django.http.response import HttpResponseRedirect
from core.equipo_tendespectro.forms import Equipo_tendespectroForm
from core.equipo_tendespectro.models import Equipo_tendespectro

# Create your views here.
def guardar(request, id):
    if request.method == 'POST':
        form = Equipo_tendespectroForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.instance.id_equipo_id = id
            form.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect('ERROR AL GUARDAR')
    else:
        return HttpResponseRedirect('ERROR AL GUARDAR')

def editar(request, id):
    if request.method == 'POST':
        descripcion = request.POST.get('descripcion')
        tendespectro = Equipo_tendespectro.objects.get(id=id)
        form = Equipo_tendespectroForm(request.POST, instance=tendespectro, files=request.FILES)
        form.instance.descripcion = descripcion
        if form.save():
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            return HttpResponseRedirect('ERROR AL GUARDAR')
    else:
        return HttpResponseRedirect('ERROR AL GUARDAR')

def eliminar(request, id):
    if request.method == 'GET':
        tendespectro = Equipo_tendespectro.objects.get(id=id)
        tendespectro.delete()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponseRedirect('ERROR AL GUARDAR')