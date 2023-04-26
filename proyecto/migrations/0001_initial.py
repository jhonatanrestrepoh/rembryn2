# Generated by Django 3.2.2 on 2023-04-26 00:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cotizaciones', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cita',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField(unique=True)),
                ('hora', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.PositiveIntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=100)),
                ('fecha_inicio', models.DateField()),
                ('fecha_Final', models.DateField()),
                ('cita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.cita')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='proyecto', to=settings.AUTH_USER_MODEL)),
                ('cotizacion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectoCotizado', to='cotizaciones.cotizacion')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='proyecto.estado')),
            ],
        ),
    ]
