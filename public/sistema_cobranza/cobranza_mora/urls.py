from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'cobranza_mora'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('login/', LoginView.as_view(template_name='cobranza_mora/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='cobranza_mora/logout.html'), name='logout'),
	path('evento/<int:id_cliente>', views.evento_create_view, name='evento'),
	path('lista_dinamica/<int:id_lista>', views.lista_dinamica_view, name='lista_dinamica'),
	path('cliente_detalle/', views.cliente_detalle_view, name='cliente_detalle'),
]