from django.http import HttpResponse, Http404, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.utils.timezone import localtime
import os
from pytz import timezone
from datetime import date, datetime
from django.contrib.auth.models import User
from .models import *
from .forms import EventoForm
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets, permissions
from .serializers import *

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



"""
# ejemplo de vista generica basada en modelo

class ListaView(generic.DetailView):
	model = Lista
	template_name = 'cobranza_mora/lista.html'
	#context_object_name = 'detalle_list'


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


def lista_dinamica_view(request, id_lista):

	template_name = 'cobranza_mora/lista_dinamica.html'

	lista_elegida = Lista.objects.filter(
				pk = id_lista,
				fecha_inicio__lte = date.today(),
				fecha_vencimiento__gte = date.today(),
			)

	if lista_elegida:

		lista_cliente = Lista_cliente.objects.filter(
				estado = 1,
				lista = id_lista,
				user_id = request.user.id
			).order_by('cliente__empresa', 'cliente__nombre')
	else:
		lista_cliente = ""
	

	context = {
		'title' : lista_elegida,
		'lista' : lista_cliente
	}

	return render(request, template_name, context)


@csrf_protect
def cliente_detalle_view(request):

	if request.method == 'POST' and request.is_ajax():

		id_cliente = request.POST['id_cliente']
		data = {}

		cliente = Cliente.objects.filter(
			pk=id_cliente
		).values(
			'nombre',
			'dni',
			'cuenta',
			'correo',
			'deuda_minima',
			'deuda_parcial',
			'deuda_total'
		)

		telefono = Telefono.objects.filter(
			cliente_id = id_cliente,
			estado = 1
		).values(
			'telefono_tipo__telefono_tipo',
			'telefono'
		)

		evento = Evento.objects.filter(
			cliente_id = id_cliente
		).values(
			'id',
			'evento_tipo__evento_tipo',
			'evento_respuesta__evento_respuesta',
			'telefono__telefono_tipo__telefono_tipo',
			'telefono__telefono',
			'mensaje',
			'user__username',
			'fecha_creado',
		).order_by(
			'-fecha_creado'
		)

		for k in range(0, len(list(evento))):
			evento[k]['fecha_creado'] = evento[k]['fecha_creado'].astimezone(timezone(os.environ['TZ'])).strftime("%d/%m/%Y %H:%M")
			

		data = {
			'cliente': list(cliente),
			'telefono': list(telefono),
			'evento': list(evento),
		}

		if cliente:
			return JsonResponse(data, safe=False)
			
		else:
			return HttpResponse("El cliente no existe")					

	


class UserViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows users to be viewed or edited.
	"""
	queryset = User.objects.all().order_by('-date_joined')
	serializer_class = UserSerializer
	permission_classes = [permissions.IsAdminUser]


class GroupViewSet(viewsets.ModelViewSet):
	"""
	API endpoint that allows groups to be viewed or edited.
	"""
	queryset = Group.objects.all()
	serializer_class = GroupSerializer
	permission_classes = [permissions.IsAdminUser]


class EmpresaViewSet(viewsets.ModelViewSet):
	
	queryset = Empresa.objects.all()
	serializer_class = EmpresaSerializer
	permission_classes = [permissions.IsAdminUser]


class ClienteViewSet(viewsets.ModelViewSet):
	
	queryset = Cliente.objects.all()
	serializer_class = ClienteSerializer
	permission_classes = [permissions.IsAdminUser]


class MoraViewSet(viewsets.ModelViewSet):

	queryset = Mora.objects.all()
	serializer_class = MoraSerializer
	permission_classes = [permissions.IsAdminUser]


class EstadoViewSet(viewsets.ModelViewSet):

	queryset = Estado.objects.all()
	serializer_class = EstadoSerializer
	permission_classes = [permissions.IsAdminUser]


class ListaViewSet(viewsets.ModelViewSet):

	queryset = Lista.objects.all()
	serializer_class = ListaSerializer
	permission_classes = [permissions.IsAdminUser]


class Lista_clienteViewSet(viewsets.ModelViewSet):

	queryset = Lista_cliente.objects.all()
	serializer_class = Lista_clienteSerializer
	permission_classes = [permissions.IsAdminUser]


class Telefono_tipoViewSet(viewsets.ModelViewSet):

	queryset = Telefono_tipo.objects.all()
	serializer_class = Telefono_tipoSerializer
	permission_classes = [permissions.IsAdminUser]


class TelefonoViewSet(viewsets.ModelViewSet):

	queryset = Telefono.objects.all()
	serializer_class = TelefonoSerializer
	permission_classes = [permissions.IsAdminUser]


class Evento_tipoViewSet(viewsets.ModelViewSet):

	queryset = Evento_tipo.objects.all()
	serializer_class = Evento_tipoSerializer
	permission_classes = [permissions.IsAdminUser]


class Evento_respuestaViewSet(viewsets.ModelViewSet):

	queryset = Evento_respuesta.objects.all()
	serializer_class = Evento_respuestaSerializer
	permission_classes = [permissions.IsAdminUser]


class EventoViewSet(viewsets.ModelViewSet):

	queryset = Evento.objects.all()
	serializer_class = EventoSerializer
	permission_classes = [permissions.IsAdminUser]


class PagoViewSet(viewsets.ModelViewSet):

	queryset = Pago.objects.all()
	serializer_class = PagoSerializer
	permission_classes = [permissions.IsAdminUser]