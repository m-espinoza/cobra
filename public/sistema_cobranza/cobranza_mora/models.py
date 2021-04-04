from django.conf import settings
from django.contrib.auth import get_user_model
from django.db import models

"""
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
"""

def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class Empresa(models.Model):
    empresa = models.CharField(max_length=140)

class Direccion(models.Model):
    numero = models.IntegerField()    
    calle = models.CharField(max_length=140)
    casa = models.CharField(max_length=14)
    manzana = models.CharField(max_length=14)
    barrio = models.CharField(max_length=140)
    piso = models.CharField(max_length=14)
    depto = models.CharField(max_length=14)
    localidad = models.CharField(max_length=140)
    departamento = models.CharField(max_length=140)
    provincia = models.CharField(max_length=140)
    pais = models.CharField(max_length=140)
    ubicacion = models.CharField(max_length=255)

class Cliente(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    cuenta = models.IntegerField()
    dni = models.IntegerField()
    nombre = models.CharField(max_length=200)
    telefono_celular = models.CharField(max_length=15)
    telefono_fijo = models.CharField(max_length=15)
    correo = models.EmailField(max_length=140)
    deuda_minima = models.FloatField()
    deuda_parcial = models.FloatField()
    deuda_total = models.FloatField()

class Link_cliente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    fecha_vencimiento = models.DateField()
    link = models.URLField()
    
class Mora(models.Model):
    mora = models.CharField(max_length=140)

class Estado(models.Model):
    estado = models.CharField(max_length=140)

class Lista(models.Model):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE)
    mora = models.ForeignKey(Mora, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    lista = models.CharField(max_length=140)
    fecha_inicio = models.DateField()
    fecha_vencimiento = models.DateField()
    fecha_creado = models.DateTimeField(auto_now_add=True)

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

class Evento_respuesta(models.Model):
    evento_respuesta = models.CharField(max_length=140)

class Evento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento_tipo = models.ForeignKey(Evento_tipo, on_delete=models.CASCADE)
    evento_respuesta = models.ForeignKey(Evento_respuesta, on_delete=models.CASCADE)

    mensaje = models.CharField(max_length=255)
    fecha_evento = models.DateTimeField(auto_now_add=True)

class Evento_pendiente(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    
    fecha_vencimiento = models.DateField()