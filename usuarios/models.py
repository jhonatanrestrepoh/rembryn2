from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
import os
from PIL import Image
from django.db.models.signals import post_save



# Create your models here.

def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name


def user_directory_path_banner(instance, filename):
    profile_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)

    if os.path.exists(full_path):
        os.remove(full_path)

    return profile_picture_name

class User(AbstractUser):
    stripe_customer_id = models.CharField(max_length=50,null=True,blank=True)


class Pais(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=True, blank=True,max_length=10)

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


class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    direccion = models.CharField(null=True, blank=True,max_length=255)
    fecha_registro = models.DateField(auto_now_add=True)
    cliente_id=models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='profile')
    pais_id = models.OneToOneField(Pais, on_delete=models.CASCADE, related_name='pais_id')

    def __str__(self):
        return self.direccion
    
    class Meta:
        verbose_name = "Direccion"
        verbose_name_plural = "Direcciones"


class Departamento(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=True, blank=True,max_length=255)
    pais_id = models.OneToOneField(Pais, on_delete=models.CASCADE, related_name='pais_id_departamento')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Departamento"
        verbose_name_plural = "Departamentos"


class Ciudad(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(null=True, blank=True,max_length=255)
    departamento = models.OneToOneField(Departamento, on_delete=models.CASCADE, related_name='pais_id_departamento')

    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name = "Ciudad"
        verbose_name_plural = "Ciudades"


