from faulthandler import disable
from django.forms import ModelForm, Textarea, HiddenInput
from .models import Evento

class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = [
			'cliente',
			'evento_tipo',
			'evento_respuesta',
			'mensaje',
			'telefono',
			'user'
		]

		widgets = {
			'mensaje': Textarea(attrs={'cols': 20, 'rows': 5}),
			'cliente': HiddenInput(),
			'telefono': HiddenInput(),
			'user': HiddenInput()
		}
