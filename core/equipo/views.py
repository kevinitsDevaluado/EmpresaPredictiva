from core.equipo_valvibracion.forms import Equipo_valvibracionForm
from core.equipo.models import Equipo
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from core.equipo.forms import EquipoForm
from core.fechas.views import get_fecha_hora
from django.contrib.auth.models import User
from django.conf import settings
from django.http import JsonResponse
from crum import get_current_request
from django.contrib import messages

import os
from django.template.loader import get_template
from xhtml2pdf import pisa
from core.erp.mixins import ValidatePermissionRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from core.equipo_valvibracion.models import Equipo_valvibracion
from core.equipo_tendespectro.models import Equipo_tendespectro
from core.equipo_tendespectro.forms import Equipo_tendespectroForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.views.generic import CreateView, ListView, DeleteView, UpdateView, View

# Create your views here.

#CLASE CON LA QUE PODEMOS VER TODOS LOS DATOS
class EquipoListView(LoginRequiredMixin, ListView):
    model = Equipo
    template_name = 'equipo/list.html'
    request = get_current_request()
	

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                position = 1

                for i in Equipo.objects.all():
                    item = i.toJSON()
                    item['position'] = position
                    data.append(item)
                    position += 1
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Equipos'
        context['create_url'] = reverse_lazy('equipo_create')
        context['list_url'] = reverse_lazy('equipo_list')
        context['entity'] = 'Equipos'
        context['form'] = EquipoForm()
        return context

#CON ESTO OBTENEMOS LOS DATOS POR CADA UNO DE LOS EMPLEADOS
def EquiposEmpleadosPDF(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		equipos = user.posts.all()
        
	else:
		equipos = current_user.posts.all()
		user = current_user
	return render(request, 'modal/index.html', {'user':user, 'equipos':equipos,'form':EquipoForm()})

def guardar(request):
    if request.method == 'POST':
            id_usuario = request.user.id
            mantenimiento = request.POST.get('mantenimiento')
            fecha = get_fecha_hora()
            
            form = EquipoForm(request.POST, files=request.FILES)
            if form.is_valid():
                form.instance.mantenimiento = mantenimiento
                form.instance.id_auth_user_id = id_usuario
                form.instance.creada_en = fecha
                form.instance.actualizada_en = fecha
                form.save()
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            else:
                return HttpResponse('ERROR AL GUARDAR')
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def vista_editar(request, id):
    if request.method == 'GET':
        equipo = Equipo.objects.get(id=id)
        form = EquipoForm(instance=equipo)
        return render(request, 'modal/editar.html', {'form': form, 'id_equipo': id, 'equipo': equipo})
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def editar(request, id):
    if request.method == 'POST':
        equipo = Equipo.objects.get(id=id)
        mantenimiento = request.POST.get('mantenimiento')
        fecha = get_fecha_hora()
        
        form = EquipoForm(request.POST, instance=equipo, files=request.FILES)
        if form.is_valid():
            form.instance.mantenimiento = mantenimiento
            form.instance.actualizada_en = fecha
            form.save()
            return redirect('equipo_list')
        else:
            return HttpResponse('ERROR AL GUARDAR')
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def valores_vibracion(request, id):
    if request.method == 'GET':
        valor_vibracion = Equipo_valvibracion.objects.filter(id_equipo_id=id).order_by('id')
        equipo = Equipo.objects.get(id=id)
        form = Equipo_valvibracionForm()
        return render(request, 'equipos_valvibracion/index.html', {'valor_vibracion': valor_vibracion, 'form': form, 'equipo': equipo})
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def tendencia_espectro(request, id):
    if request.method == 'GET':
        tendespectro = Equipo_tendespectro.objects.filter(id_equipo_id=id).order_by('id')
        equipo = Equipo.objects.get(id=id)
        form = Equipo_tendespectroForm()
        return render(request, 'equipo_tendespectro/index.html', {'tendespectro': tendespectro, 'form': form, 'equipo': equipo})
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def activar(request, id):
    if request.method == 'GET':
        equipo = Equipo.objects.get(id=id)
        equipo.estado = '1'
        equipo.save()
        messages.info(request, 'Se activo el equipo..')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('ERROR AL GUARDAR')
    
def desactivar(request, id):
    if request.method == 'GET':
        equipo = Equipo.objects.get(id=id)
        equipo.estado = '0'
        equipo.save()
        messages.info(request, 'Al dar clic en Aceptar, este equipo se deshabilitara. Podrás habilitarlo desde el boton de activar.')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else:
        return HttpResponse('ERROR AL GUARDAR')



class SaleInvoicePdfView(View):

    def link_callback(self, uri, rel):
        """
        Convert HTML URIs to absolute system paths so xhtml2pdf can access those
        resources
        """
        # use short variable names
        sUrl = settings.STATIC_URL  # Typically /static/
        sRoot = settings.STATIC_ROOT  # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL  # Typically /static/media/
        mRoot = settings.MEDIA_ROOT  # Typically /home/userX/project_static/media/

        # convert URIs to absolute system paths
        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri  # handle absolute uri (ie: http://some.tld/foo.png)

        # make sure that file exists
        if not os.path.isfile(path):
            raise Exception(
                'media URI must start with %s or %s' % (sUrl, mUrl)
            )
        return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('documentos/invoice.html')
            context = {
                'equipo': Equipo.objects.get(pk=self.kwargs['pk']),
                'equipo_valvibracion': Equipo_valvibracion.objects.filter(id_equipo = self.kwargs['pk']),
                'equipo_tendespectro': Equipo_tendespectro.objects.objects.filter(id_equipo = self.kwargs['pk']),                
                'icon': '{}{}'.format(settings.MEDIA_URL, 'logo.png')
            }
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            pisaStatus = pisa.CreatePDF(
                html, dest=response,
                link_callback=self.link_callback
            )
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('HTTP_REFERER'))
