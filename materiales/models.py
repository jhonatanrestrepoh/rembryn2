from django.db import models

# Create your models here.

class Material(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    valor = models.PositiveIntegerField(default=0)
    fecha_actualizacion=models.DateField(auto_now_add=False)
    fecha_registro =models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Material"
        verbose_name_plural = "Materiales"