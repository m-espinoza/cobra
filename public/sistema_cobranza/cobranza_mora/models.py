from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

def get_sentinel_user():
	return get_user_model().objects.get_or_create(username='deleted')[0]

class Empresa(models.Model):
	empresa = models.CharField(max_length=140)
	
	def __str__(self):
		return self.empresa

class Direccion(models.Model):
	numero = models.IntegerField(null=True, blank=True)	
	calle = models.CharField(max_length=140, null=True, blank=True)
	casa = models.CharField(max_length=14, null=True, blank=True)
	manzana = models.CharField(max_length=14, null=True, blank=True)
	barrio = models.CharField(max_length=140,null=True, blank=True)
	piso = models.CharField(max_length=14, null=True, blank=True)
	depto = models.CharField(max_length=14, null=True, blank=True)
	localidad = models.CharField(max_length=140, null=True, blank=True)
	departamento = models.CharField(max_length=140, null=True, blank=True)
	provincia = models.CharField(max_length=140, null=True, blank=True)
	pais = models.CharField(max_length=140, null=True, blank=True)
	ubicacion = models.CharField(max_length=255, null=True, blank=True)

class Cliente(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

	cuenta = models.IntegerField()
	dni = models.IntegerField()
	nombre = models.CharField(max_length=200)
	telefono_celular = models.CharField(max_length=15, null=True, blank=True)
	telefono_fijo = models.CharField(max_length=15, null=True, blank=True)
	correo = models.EmailField(max_length=140, null=True, blank=True)
	deuda_minima = models.FloatField(null=True, blank=True)
	deuda_parcial = models.FloatField(null=True, blank=True)
	deuda_total = models.FloatField(null=True, blank=True)

	def __str__(self):
		return self.nombre
	

class Link_cliente(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	
	fecha_vencimiento = models.DateField()
	link = models.URLField()
	def __str__(self):
		return self.cliente
	
class Mora(models.Model):
	mora = models.CharField(max_length=140)

	def __str__(self):
		return self.mora

class Estado(models.Model):
	estado = models.CharField(max_length=140)

	def __str__(self):
		return self.estado

class Lista(models.Model):
	empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
	mora = models.ForeignKey(Mora, on_delete=models.CASCADE)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

	lista = models.CharField(max_length=140)
	fecha_inicio = models.DateField()
	fecha_vencimiento = models.DateField()
	fecha_creado = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.lista

class Lista_cliente(models.Model):
	lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
	user = models.ForeignKey(
		settings.AUTH_USER_MODEL,
		on_delete=models.SET(get_sentinel_user),
		limit_choices_to={'is_staff': True},
	)

class Evento_tipo(models.Model):
	evento_tipo = models.CharField(max_length=140)

	def __str__(self):
		return self.evento_tipo

class Evento_respuesta(models.Model):
	evento_respuesta = models.CharField(max_length=140)

	def __str__(self):
		return self.evento_respuesta

class Evento(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	evento_tipo = models.ForeignKey(Evento_tipo, on_delete=models.CASCADE)
	evento_respuesta = models.ForeignKey(Evento_respuesta, on_delete=models.CASCADE)

	mensaje = models.CharField(max_length=255, null=True, blank=True)
	fecha_creado = models.DateTimeField(auto_now_add=True)



class Evento_pendiente(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	
	fecha_vencimiento = models.DateField()

	def __str__(self):
		return self.cliente