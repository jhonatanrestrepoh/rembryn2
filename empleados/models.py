from django.db import models
from django.core.validators import RegexValidator

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
    celular = models.CharField(
        max_length=10,
        null=False,
        default='3000000000',
        validators=[
            RegexValidator(
                regex=r'^(3[0-9]{9}|39[0-9]{8})$',
                message='El número de celular debe tener 10 dígitos y debe empezar por 3'
            )
        ]
    )
    fecha_registro = models.DateField(auto_now_add=True)
    usuario_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="empleado_usuario")
    tipos_empleado = models.ForeignKey(Tipos_empleado, on_delete=models.CASCADE, related_name="tipo_empleado")

    def __str__(self):
        return self.primer_nombre

