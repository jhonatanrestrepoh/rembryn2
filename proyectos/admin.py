from django.contrib import admin

from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

class ProyectoResource(resources.ModelResource):
    class Meta:
        model = Proyecto

class ProyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = ProyectoResource

admin.site.register(Proyecto, ProyectoAdmin)

class Detalles_proyectoResource(resources.ModelResource):
    class Meta:
        model = Detalles_proyecto

class Detalles_proyectoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['proyecto_id']
    resource_class = ProyectoResource

admin.site.register(Detalles_proyecto, Detalles_proyectoAdmin)


