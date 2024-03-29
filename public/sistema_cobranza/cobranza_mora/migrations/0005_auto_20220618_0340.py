# Generated by Django 3.2.13 on 2022-06-18 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cobranza_mora', '0004_auto_20220618_0308'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evento_telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.CharField(blank=True, max_length=255, null=True)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True, null=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True, null=True)),
                ('evento_respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.evento_respuesta')),
                ('evento_tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.evento_tipo')),
            ],
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono', models.CharField(max_length=20)),
                ('fecha_creado', models.DateTimeField(auto_now_add=True)),
                ('fecha_modificado', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Telefono_tipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefono_tipo', models.CharField(max_length=140)),
            ],
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_celular',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefono_fijo',
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_creado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='fecha_modificado',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='fecha_creado',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='direccion',
            name='fecha_modificado',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.DeleteModel(
            name='Evento',
        ),
        migrations.AddField(
            model_name='telefono',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.cliente'),
        ),
        migrations.AddField(
            model_name='telefono',
            name='estado',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.estado'),
        ),
        migrations.AddField(
            model_name='telefono',
            name='telefono_tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.telefono_tipo'),
        ),
        migrations.AddField(
            model_name='evento_telefono',
            name='telefono',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cobranza_mora.telefono'),
        ),
    ]
