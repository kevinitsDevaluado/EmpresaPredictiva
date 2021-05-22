from django.urls import path
from core.erp.views.dashboard.views import *
from core.erp.views.orientacion.views import *
from core.erp.views.confipagina.views import *



app_name = 'erp'

urlpatterns = [
    # home
    path('dashboard/', DashboardView.as_view(), name='dashboard'),


    path('config/list/', ConfigPaginaListView.as_view(), name='config_list'),
    path('config/add/', ConfigPaginaCreateView.as_view(), name='config_create'),
    path('config/update/<int:pk>/', ConfigPaginaUpdateView.as_view(), name='config_update'),
    path('config/delete/<int:pk>/', OrientacionDeleteView.as_view(), name='config_delete'),
    # client
    path('orientacion/list/', OrientacionListView.as_view(), name='orientacion_list'),
    path('orientacion/add/', OrientacionCreateView.as_view(), name='orientacion_create'),
    path('orientacion/update/<int:pk>/', OrientacionUpdateView.as_view(), name='orientacion_update'),
    path('orientacion/delete/<int:pk>/', OrientacionDeleteView.as_view(), name='orientacion_delete'),
]
