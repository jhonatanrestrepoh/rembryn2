from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class MaterialsResource(resources.ModelResource):
    class Meta:
        model = Material

class MaterialAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    resource_class = MaterialsResource

admin.site.register(Material,MaterialAdmin)

# Register your models here.





