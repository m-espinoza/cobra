from .models import Evento_telefono
from django.forms import ModelForm

class EventoForm(ModelForm):
	class Meta:
		model = Evento_telefono
		fields = [
			'evento_tipo',
			'evento_respuesta',
			'mensaje'
		]