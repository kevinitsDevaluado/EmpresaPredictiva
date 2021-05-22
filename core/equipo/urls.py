from django.urls import path
from core.equipo.views import *


urlpatterns = [
    path('list/', EquipoListView.as_view(), name='equipo_list'),
    path('add/', guardar, name="Equipo_guardar"),
    path('update/<int:id>/', vista_editar, name="vista_editar"),
    path('editar/<int:id>/', editar, name="Equipo_editar"),
    path('activar2/<int:id>/', activar, name="equipo_activar"),
    path('desactivar2/<int:id>/', desactivar, name="equipo_desactivar"),
    path('listPerfil/', EquiposEmpleadosPDF, name="user_equipos"),


       
    #Listar valores de vibracion
    path('valores/vibracion/<int:id>/', valores_vibracion, name="Equipo_valores_vibracion"),
    #Listar tendencias de espectro
    path('tendencia/espectro/<int:id>/', tendencia_espectro, name="Equipo_tendencia_espectro"),

    #
    path('document/invoice/pdf/<int:pk>/', SaleInvoicePdfView.as_view(), name='sale_invoice_pdf'),
    
    #path('add/', EquipoCreateView.as_view(), name='equipo_create'),
    #path('cargarRawMaterial/update/<int:pk>/', CargarRawMaterialUpdateView.as_view(), name='cargarRawMaterial_update'),
    #path('cargarRawMaterial/delete/<int:pk>/', CargarRawMaterialDeleteView.as_view(), name='cargarRawMaterial_delete'),
]