# Generated by Django 3.1.7 on 2021-04-04 20:55

import cobranza_mora.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuenta', models.IntegerField()),
                ('dni', models.IntegerField()),
                ('nombre', models.CharField(max_length=200)),
                ('telefono_celular', models.CharField(max_length=15)),
                ('telefono_fijo', models.CharField(max_length=15)),
                ('correo', models.EmailField(max_length=140)),
                ('deuda_minima', models.FloatField()),
                ('deuda_parcial', models.FloatField()),
                ('deuda_total', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.IntegerField()),
                ('calle', models.CharField(max_length=140)),
                ('casa', models.CharField(max_length=14)),
                ('manzana', models.CharField(max_length=14)),
                ('barrio', models.CharField(max_length=140)),
                ('piso', models.CharField(max_length=14)),
                ('depto', models.CharField(max_length=14)),
                ('localidad', models.CharField(max_length=140)),
                ('departamento', models.CharField(max_length=140)),
                ('provincia', models.CharField(max_length=140)),
                ('pais', models.CharField(max_length=140)),
                ('ubicacion', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Evento_respuesta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento_respuesta', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Evento_tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evento_tipo', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lista', models.CharField(max_length=140)),
                ('fecha_inicio', models.DateField()),
                ('fecha_vencimiento', models.DateField()),
                ('fecha_creado', models.DateTimeField(verbose_name='date published')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.empresa')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.estado')),
            ],
        ),
        migrations.CreateModel(
            name='Mora',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mora', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Lista_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.cliente')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.estado')),
                ('lista', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.lista')),
                ('user', models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=models.SET(cobranza_mora.models.get_sentinel_user), to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='lista',
            name='mora',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.mora'),
        ),
        migrations.CreateModel(
            name='Link_cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateField()),
                ('link', models.URLField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Evento_pendiente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_vencimiento', models.DateField()),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(max_length=255)),
                ('fecha_evento', models.DateTimeField(verbose_name='date published')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.cliente')),
                ('evento_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.evento_respuesta')),
                ('evento_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.evento_tipo')),
            ],
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.direccion'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='empresa',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.empresa'),
        ),
    ]
