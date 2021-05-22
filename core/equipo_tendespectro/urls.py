from django.urls import path
from core.equipo_tendespectro.views import guardar,editar, eliminar

urlpatterns = [
    path('guardar/<int:id>/', guardar, name="Tendespectro_guardar"),
    path('editar/<int:id>/', editar, name="Tendespectro_editar"),
    path('eliminar/<int:id>/', eliminar, name="Tendespectro_eliminar"),
]