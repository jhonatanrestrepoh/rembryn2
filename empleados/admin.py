from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin
# Register your models here.

class Tipos_empleadosResource(resources.ModelResource):
    class Meta:
        model = Tipos_empleado

class Tipos_empleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = Tipos_empleadosResource

admin.site.register(Tipos_empleado, Tipos_empleadoAdmin)


class EmpleadosResource(resources.ModelResource):
    class Meta:
        model = Empleado
        

class EmpleadoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['primer_nombre']
    resource_class = EmpleadosResource


admin.site.register(Empleado, EmpleadoAdmin)
