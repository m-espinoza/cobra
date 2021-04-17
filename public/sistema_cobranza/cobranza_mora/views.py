from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib.auth.models import User

from datetime import date  

from .models import Lista, Lista_cliente, Cliente, Empresa

#def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")

class IndexView(generic.ListView):
    template_name = 'cobranza_mora/index.html'
    context_object_name = 'latest_list'

    def get_queryset(self):
        """Busco las listas que estan activas"""
        return Lista.objects.filter(
            fecha_inicio__lte = date.today(),
            fecha_vencimiento__gte = date.today()
            ).exclude(
                estado_id=2
                )

class DetailView(generic.DetailView):
    model = Lista
    template_name = 'cobranza_mora/detail.html'
    #context_object_name = 'detalle_list'

    """
    def get_queryset(self):
              
        return Lista_cliente.objects.filter(
            estado_id = 1            
        )
    """