from dataclasses import field
from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = [
			'url',
			'username',
			'first_name',
			'last_name',
			'email',
			'is_active',
			'groups'
		]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = [
			'url',
			'name'
		]


class EmpresaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Empresa
		fields = "__all__"


class ClienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Cliente
		fields = "__all__"


class MoraSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Mora
		fields = "__all__"


class EstadoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Estado
		fields = "__all__"


class ListaSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lista
		fields = "__all__"


class Lista_clienteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Lista_cliente
		fields = "__all__"


class Telefono_tipoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Telefono_tipo
		fields = "__all__"


class TelefonoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Telefono
		fields = "__all__"
