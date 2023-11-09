from django.db import models
from user.models import User

# Create your models here.

class Equipo(models.Model):
    nombre = models.CharField(max_length=255)
    jugadores = models.JSONField(default=list)  # Usamos JSONField para el array de jugadores
    id_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Torneo(models.Model):
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    id_creador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Partida(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    resultado = models.CharField(max_length=255)
    id_torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    equipo1 = models.ForeignKey(Equipo, related_name='partidas_equipo1', on_delete=models.CASCADE)
    equipo2 = models.ForeignKey(Equipo, related_name='partidas_equipo2', on_delete=models.CASCADE)

    def __str__(self):
        return f"Partida {self.id} - {self.id_torneo}"
