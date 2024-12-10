from django.contrib import admin

from .models import Carrera,Entregable,Estudiante,Profesor


# Register your models here.

admin.site.register(Carrera)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)