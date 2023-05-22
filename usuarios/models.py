from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save

from smart_selects.db_fields import ChainedForeignKey




# Create your models here.

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50,null=True,blank=True)


class Pais(models.Model):
    nombre = models.CharField(null=True, blank=True,max_length=10, unique=True)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Pais"
        verbose_name_plural = "Paises"
    
class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    cedula = models.CharField(null=True, blank=True,max_length=10)
    primer_nombre = models.CharField(null=True, blank=True,max_length=50)
    segundo_nombre = models.CharField(null=True, blank=True,max_length=50)
    primer_apellido = models.CharField(null=True, blank=True,max_length=50)
    segundo_apellido = models.CharField(null=True, blank=True,max_length=50)
    celular = models.CharField(null=True, blank=True,max_length=10)
    fecha_registro = models.DateField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Cliente.objects.create(user=instance)

def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

# created profile
post_save.connect(create_user_profile, sender=User)
# save created profile
post_save.connect(save_user_profile, sender=User)





class Departamento(models.Model):
    nombre = models.CharField(null=True, blank=True,max_length=255, unique=True)
    pais = models.ForeignKey(Pais,on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Ciudad(models.Model):
    nombre = models.CharField(null=True, blank=True,max_length=255,  default="Medellin", unique=True)
    departamento = models.ForeignKey(
        Departamento,
        on_delete=models.CASCADE, default=1
    )


    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


class Direccion(models.Model):
    direccion = models.CharField(null=True, blank=True,max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    cliente=models.OneToOneField(Cliente, on_delete=models.CASCADE)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE, default=1)
    departamento = ChainedForeignKey(
        Departamento,
        chained_field="pais",
        chained_model_field="pais",
        show_all=False,
        auto_choose=True,
        sort=True,
        default=1
    )
    ciudad = ChainedForeignKey(
        Ciudad,
        chained_field="departamento",
        chained_model_field="departamento",
        show_all=False,
        auto_choose=True,
        sort=True,
        default=1
    )


    def __str__(self):
        return self.direccion
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"