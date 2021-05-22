"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.login.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LoginFormView.as_view(), name='login'),
    path('user/', include('core.user.urls')),
    path('erp/', include('core.erp.urls')),
    path('login/', include('core.login.urls')),
    path('equipo/', include('core.equipo.urls')),
    
    path('equipo/valvibracion/', include('core.equipo_valvibracion.urls'), name="Equipo_valvibracion"),
    path('equipo/tendespectro/', include('core.equipo_tendespectro.urls'), name="Equipo_tendespectro"),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
