"""sistema_cobranza URL Configuration

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
from django.urls import include, path
from cobranza_mora import views
from django.conf import settings

from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'empresa', views.EmpresaViewSet)
router.register(r'cliente', views.ClienteViewSet)
router.register(r'mora', views.MoraViewSet)
router.register(r'estado', views.EstadoViewSet)
router.register(r'lista', views.ListaViewSet)
router.register(r'lista_cliente', views.Lista_clienteViewSet)
router.register(r'telefono_tipo', views.Telefono_tipoViewSet)
router.register(r'telefono', views.TelefonoViewSet)
router.register(r'evento_tipo', views.Evento_tipoViewSet)
router.register(r'evento_respuesta', views.Evento_respuestaViewSet)
router.register(r'evento', views.EventoViewSet)



urlpatterns = [
	path('', include('cobranza_mora.urls')),
	path('admin/', admin.site.urls),
	path('api/', include(router.urls)),
	path('api/auth/', include('knox.urls'))
]
