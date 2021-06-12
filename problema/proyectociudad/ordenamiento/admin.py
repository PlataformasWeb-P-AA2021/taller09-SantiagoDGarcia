from django.contrib import admin
from ordenamiento.models import Parroquia, BarrioCiudadela
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class mostrar_parroquias_admin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ( 'id', 'nombre', 'tipo')

class mostrar_barrios_admin (ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('nombre', 'numero_viviendas', 'numero_parques', 'numero_edificios', 'id_parroquia')
    search_fields = ('id', 'nombre')
 
admin.site.register(Parroquia, mostrar_parroquias_admin)
admin.site.register(BarrioCiudadela, mostrar_barrios_admin)
