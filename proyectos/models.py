from django.db import models
from django.conf import settings
from empleados.models import Empleado

User = settings.AUTH_USER_MODEL

ESTADOS=(
    ('Pendiente', 'Pendiente'),
    ('Validado', 'Validado'),
    ('Cotizado', 'Cotizado'),
    ('Cancelado', 'Cancelado'),
    ('Terminado', 'Terminado'),
)


# Create your models here.

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(max_length=500)
    fecha_fin =models.DateField(auto_now_add=False)
    fecha_registro =models.DateField(auto_now_add=True)
    cliente_id =models.ForeignKey(User, on_delete=models.CASCADE, related_name="cliente")
    estados = models.CharField(blank=False, null=False, default='Pendiente',max_length=100, choices=ESTADOS)

    def __str__(self):
        return self.nombre

class Detalles_proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_visita =models.DateField(auto_now_add=False)
    empleados_id= models.ManyToManyField(Empleado, blank=True, related_name='empleados')
    proyecto_id =models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto")
    fecha_registro=models.DateField(auto_now_add=True)
    descripcion = models.TextField(max_length=500)

    def __int__(self):
        return self.proyecto_id