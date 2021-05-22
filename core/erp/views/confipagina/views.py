from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,View
from django.contrib.auth.decorators import  login_required
from django.template.loader import get_template
from django.shortcuts import redirect, render

from core.erp.forms import *
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import *

from django.shortcuts import render, redirect 

class ConfigPaginaListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = ConfigPagina
    template_name = 'confipagina/list.html'
    permission_required = 'view_category'

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
                for i in ConfigPagina.objects.all():
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
        context['title'] = 'CONFIGURACIÓN'
        context['create_url'] = reverse_lazy('erp:config_create')
        context['list_url'] = reverse_lazy('erp:config_list')
        context['entity'] = 'Configuracion'
        return context






class ConfigPaginaCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = ConfigPagina
    form_class = ConfigForm
    template_name = 'confipagina/create.html'
    success_url = reverse_lazy('erp:config_list')
    permission_required = 'add_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Configuracion'
        context['entity'] = 'Configuracion'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ConfigPaginaUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = ConfigPagina
    form_class = ConfigForm
    template_name = 'confipagina/create.html'
    success_url = reverse_lazy('erp:config_list')
    permission_required = 'change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Configuracion'
        context['entity'] = 'orientacion'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class OrientacionDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = OrientationPag
    template_name = 'confipagina/delete.html'
    success_url = reverse_lazy('erp:config_list')
    permission_required = 'delete_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'CONFIGURACION'
        context['entity'] = 'CONFIGURACION'
        context['list_url'] = self.success_url
        return context
