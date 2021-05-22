from django.urls import path
from core.equipo_valvibracion.views import guardar,editar, eliminar

urlpatterns = [
    path('guardar/<int:id>/', guardar, name="Valvibracion_guardar"),
    path('editar/<int:id>/', editar, name="Valvibracion_editar"),
    path('eliminar/<int:id>/', eliminar, name="Valvibracion_eliminar"),
]