from django.contrib import admin

from django.contrib import admin
from .models import Usuario
from .models import Cancha
from .models import Sede
from .models import Reserva

class Usuario(admin.ModelAdmin):
    ordering = ['-nombre']
    search_fields=('ci','nombre','apellido')

class Sede(admin.ModelAdmin):
    ordering = ['-nombre']
    search_fields=('nombre',)

class Reserva(admin.ModelAdmin):
    ordering = ['-fecha']
    search_fields=('fecha',)

class Cancha(admin.ModelAdmin):
    ordering = ['-nombre']
    search_fields=('nombre',)


