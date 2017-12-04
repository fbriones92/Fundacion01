from django.contrib import admin
from voluntarios.models import Voluntario
#from django.contrib.admin.options import ModelAdmin
#from django.contrib.admin import actions
#from django_extensions.management.commands.admin_generator import LIST_FILTER

def activar_voluntario(modelAdmin, request, queryset):
    queryset.update(estado=Voluntario.ESTADO_ACTIVO)
    
activar_voluntario.short_description = "Activar voluntario"


class VoluntarioAdmin(admin.ModelAdmin):
    fields = (('estado', 'nombres'), 'parentesco')
    list_filter = [ 'estado']
    actions = [activar_voluntario]
    list_display = ('nombres', 'apellidos', 'correo', 'idioma','estado')
admin.site.register(Voluntario, VoluntarioAdmin)