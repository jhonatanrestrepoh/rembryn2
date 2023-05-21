from django.contrib import admin
from .models import User,Cliente, Pais, Direccion, Departamento, Ciudad
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class UsersResource(resources.ModelResource):
    class Meta:
        model = User
        ordering = ['username','password']

class UsersAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['username']
    resource_class = UsersResource







admin.site.register(User,UsersAdmin)
admin.site.register(Cliente)
admin.site.register(Pais)
admin.site.register(Direccion)
admin.site.register(Departamento)
admin.site.register(Ciudad)



