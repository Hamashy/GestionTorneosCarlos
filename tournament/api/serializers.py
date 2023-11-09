from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from tournament.models import Equipo, Partida, Torneo

# equipo,torneo,partida

class EquipoSerializer(ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'

class TorneoSerializer(ModelSerializer):
    class Meta:
        model = Torneo
        fields = '__all__'

class PartidaSerializer(ModelSerializer):
    class Meta:
        model = Partida
        fields = '__all__'