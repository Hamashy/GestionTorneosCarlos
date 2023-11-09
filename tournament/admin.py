from django.contrib import admin
from django.contrib.auth.models import User

from tournament.models import Equipo, Partida, Torneo

# Register your models here.

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

@admin.register(Torneo)
class TorneoAdmin(admin.ModelAdmin):
    pass

@admin.register(Partida)
class PartidaAdmin(admin.ModelAdmin):
    pass


