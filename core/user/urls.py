from django.urls import path
from core.user.views import *
from core.user.views import activar, desactivar
app_name = 'user'

urlpatterns = [
    # user
    path('list/', UserListView.as_view(), name='user_list'),
    path('add/', UserCreateView.as_view(), name='user_create'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='user_delete'),
    path('change/group/<int:pk>/', UserChangeGroup.as_view(), name='user_change_group'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
    path('change/password/', UserChangePasswordView.as_view(), name='user_change_password'),

    path('activar/<int:pk>/', UserUpdateView.as_view(), name='user_activar'),
    path('desactivar/<int:pk>/', UserUpdateView.as_view(), name='user_desactivar'),

    path('activar2/<int:id>/', activar, name="Empleado_activar"),
    path('desactivar2/<int:id>/', desactivar, name="Empleado_desactivar"),
]
