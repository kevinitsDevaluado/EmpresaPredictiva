# Generated by Django 3.1.6 on 2021-05-21 16:39

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
            name='Equipo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100, unique=True)),
                ('nombre', models.CharField(max_length=100)),
                ('imagen', models.ImageField(blank=True, upload_to='equipos')),
                ('esquema', models.ImageField(blank=True, upload_to='esquemas')),
                ('estandar', models.CharField(max_length=100)),
                ('tolerancia', models.CharField(max_length=255)),
                ('mantenimiento', models.CharField(max_length=30)),
                ('diagnostico', models.CharField(max_length=255)),
                ('recomendaciones', models.CharField(max_length=255)),
                ('area', models.CharField(max_length=50)),
                ('tipo', models.CharField(max_length=50)),
                ('potencia', models.CharField(max_length=50)),
                ('vel_nominal', models.CharField(max_length=50)),
                ('transmision', models.CharField(max_length=50)),
                ('carga', models.CharField(max_length=10)),
                ('vel_operacion', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('serie', models.CharField(max_length=50)),
                ('estado', models.IntegerField(choices=[('Activo', 1), ('Inactivo', 0)], default=1)),
                ('creada_en', models.DateTimeField(auto_now_add=True, null=True)),
                ('actualizada_en', models.DateTimeField(auto_now=True, null=True)),
                ('id_auth_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Equipo',
                'verbose_name_plural': 'Equipos',
                'ordering': ['id'],
            },
        ),
    ]
