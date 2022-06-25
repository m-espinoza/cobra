from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User
#from django.contrib import messages
from datetime import date
from .models import *
from .forms import EventoForm

class IndexView(generic.ListView):
	template_name = 'cobranza_mora/index.html'
	context_object_name = 'latest_list'

	def get_queryset(self):
		"""
		Busco las listas que estan activas y 
		los clientes que solo el usuario logueado puede ver
		
		"""

		return Lista.objects.filter(
				fecha_inicio__lte = date.today(),
				fecha_vencimiento__gte = date.today(),
				lista_cliente__estado_id = 1,
				lista_cliente__user_id = self.request.user.id
			).order_by('fecha_creado').distinct()

class ListaView(generic.DetailView):
	model = Lista
	template_name = 'cobranza_mora/lista.html'
	#context_object_name = 'detalle_list'

	"""
	def get_queryset(self):
			  
		return Lista_cliente.objects.filter(
			estado_id = 1			
		)
	"""

def evento_create_view(request, id_cliente):
	""" basado en el get me fijo si el cliente existe y habilito el formulario con el cliente seteado"""
	
	template_name = 'cobranza_mora/eventos.html'

	cliente = get_object_or_404(Cliente, pk=id_cliente)
	
	telefono_habilitado = Telefono.objects.filter(estado_id = 1)
	telefonos = get_list_or_404(telefono_habilitado, cliente=id_cliente)
	

	initial_dict = {
		"cliente" : cliente,
		'user' : request.user
	}

	form_event = EventoForm(request.POST or None, initial = initial_dict)

	if form_event.is_valid():
		form_event.save()
		#messages.success(request, 'Successfully saved')

	context = {
		'title' : "Cargar Evento",
		'form_event' : form_event,
		'telefonos': telefonos
	}

	return render(request, template_name, context)


def evento_list_view(request, id_cliente):

	template_name = 'cobranza_mora/lista_eventos.html'

	cliente = get_object_or_404(Cliente, pk=id_cliente)

	lista = Evento.objects.filter(
			cliente_id = id_cliente
		).order_by('-fecha_creado')
	
	context = {
		'title' : cliente.nombre + " DNI: " + str(cliente.dni),
		'lista_eventos' : lista
	}

	return render(request, template_name, context)
