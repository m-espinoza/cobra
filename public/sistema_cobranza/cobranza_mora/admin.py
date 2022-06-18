from django.contrib import admin
from .models import Cliente, Empresa, Direccion, Evento_telefono, Lista, Mora, Estado, Lista_cliente, Evento_tipo, Evento_respuesta, Evento_pendiente, Telefono, Telefono_tipo

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Direccion)
admin.site.register(Lista)
admin.site.register(Mora)
admin.site.register(Estado)
admin.site.register(Lista_cliente)
admin.site.register(Evento_telefono)
admin.site.register(Evento_tipo)
admin.site.register(Evento_respuesta)
admin.site.register(Evento_pendiente)
admin.site.register(Telefono)
admin.site.register(Telefono_tipo)
