from django.contrib import admin
from .models import Cliente, Empresa, Direccion, Lista, Mora, Estado, Link_cliente, Lista_cliente, Evento_tipo, Evento_respuesta, Evento, Evento_pendiente

admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(Direccion)
admin.site.register(Lista)
admin.site.register(Mora)
admin.site.register(Estado)
admin.site.register(Link_cliente)
admin.site.register(Lista_cliente)
admin.site.register(Evento)
admin.site.register(Evento_tipo)
admin.site.register(Evento_respuesta)
admin.site.register(Evento_pendiente)

