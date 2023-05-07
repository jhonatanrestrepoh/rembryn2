from django.db import models
from proyectos.models import Proyecto
from materiales.models import *
# Create your models here.

class Cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    subtotal = models.IntegerField(default=0)
    descuento= models.IntegerField(default=0)
    totol_pagar= models.IntegerField(default=0)
    fecha_actualizacion=models.DateField(auto_now_add=False)
    fecha_registro =models.DateField(auto_now_add=True)
    proyecto_id = models.ForeignKey(Proyecto, on_delete=models.CASCADE, related_name="proyecto_cotizacion")
    
    def __int__(self):
        return self.subtotal
    
    class Meta:
        verbose_name = "Cotizacion"
        verbose_name_plural = "Cotizaciones"

class Detalle_cotizacion(models.Model):
    id = models.AutoField(primary_key=True)
    cantidad = models.IntegerField(default=0)
    valor_total=models.IntegerField(default=0)
    cotizacion_id = models.ForeignKey(Cotizacion, on_delete=models.CASCADE, related_name="proyecto")
    materiales_id = models.ManyToManyField(Material, blank=True, related_name='materiales_cotizacion')

    def __int__(self):
        return self.id

    class Meta:
        verbose_name = "Detalle_cotizacion"
        verbose_name_plural = "Detalle_cotizaciones"
    

