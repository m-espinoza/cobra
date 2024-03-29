# Generated by Django 3.1.7 on 2021-04-04 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

	dependencies = [
		('cobranza_mora', '0002_auto_20210404_2117'),
	]

	operations = [
		migrations.RenameField(
			model_name='evento',
			old_name='fecha_evento',
			new_name='fecha_creado',
		),
		migrations.AlterField(
			model_name='cliente',
			name='correo',
			field=models.EmailField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='cliente',
			name='deuda_minima',
			field=models.FloatField(blank=True, null=True),
		),
		migrations.AlterField(
			model_name='cliente',
			name='deuda_parcial',
			field=models.FloatField(blank=True, null=True),
		),
		migrations.AlterField(
			model_name='cliente',
			name='deuda_total',
			field=models.FloatField(blank=True, null=True),
		),
		migrations.AlterField(
			model_name='cliente',
			name='telefono_celular',
			field=models.CharField(blank=True, max_length=15, null=True),
		),
		migrations.AlterField(
			model_name='cliente',
			name='telefono_fijo',
			field=models.CharField(blank=True, max_length=15, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='barrio',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='calle',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='casa',
			field=models.CharField(blank=True, max_length=14, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='departamento',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='depto',
			field=models.CharField(blank=True, max_length=14, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='localidad',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='manzana',
			field=models.CharField(blank=True, max_length=14, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='numero',
			field=models.IntegerField(blank=True, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='pais',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='piso',
			field=models.CharField(blank=True, max_length=14, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='provincia',
			field=models.CharField(blank=True, max_length=140, null=True),
		),
		migrations.AlterField(
			model_name='direccion',
			name='ubicacion',
			field=models.CharField(blank=True, max_length=255, null=True),
		),
		migrations.AlterField(
			model_name='evento',
			name='mensaje',
			field=models.CharField(blank=True, max_length=255, null=True),
		),
	]
