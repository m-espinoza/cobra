from .models import Evento
from django.forms import ModelForm

class EventoForm(ModelForm):
    class Meta:
        model = Evento
        fields = [
            'cliente',
            'evento_tipo',
            'evento_respuesta',
            'mensaje'
        ]