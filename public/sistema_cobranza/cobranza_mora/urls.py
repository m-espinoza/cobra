from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'cobranza_mora'

urlpatterns = [
	path('', views.IndexView.as_view(), name='index'),
	path('login/', LoginView.as_view(template_name='cobranza_mora/login.html'), name='login'),
	path('logout/', LogoutView.as_view(template_name='cobranza_mora/logout.html'), name='logout'),
	path('<int:pk>/', views.DetailView.as_view(), name='detail'),
	path('evento/', views.evento_create_view, name='evento'),
]