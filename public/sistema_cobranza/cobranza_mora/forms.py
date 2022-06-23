from faulthandler import disable
from django.forms import ModelForm, Textarea
from .models import Evento

class EventoForm(ModelForm):
	class Meta:
		model = Evento
		fields = '__all__'
		widgets = {
			'mensaje': Textarea(attrs={'cols': 20, 'rows': 5})
		}

		
