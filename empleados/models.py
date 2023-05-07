from django.db import models

# Create your models here.
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Tipos_empleado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.IntegerField(blank=False)
    primer_nombre = models.CharField(max_length=100, blank=False)
    segundo_nombre = models.CharField(max_length=100,blank=True,null=True)
    primer_apellido = models.CharField(max_length=100,blank=False)
    segundo_apellido = models.CharField(max_length=100,blank=True,null=True)
    celular = models.IntegerField(blank=True, null=True)
    fecha_registro =models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="empleado")
    tipos_empleado = models.ForeignKey(Tipos_empleado, on_delete=models.CASCADE, related_name="tipo_empleado")

    def __str__(self):
        return self.primer_nombre

