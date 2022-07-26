from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'cobranza_mora'

urlpatterns = [
	path('listas', views.IndexView.as_view(), name='index'),
	path('', LoginView.as_view(template_name='cobranza_mora/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='cobranza_mora/logout.html'), name='logout'),
	path('evento/', views.evento_crear_view, name='evento_crear'),
	path('listas_detalle/<int:id_lista>', views.lista_dinamica_view, name='lista_dinamica'),
	path('cliente_detalle/', views.cliente_detalle_view, name='cliente_detalle'),
]