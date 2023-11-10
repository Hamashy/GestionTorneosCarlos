from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser

from tournament.api.serializers import EquipoSerializer, PartidaSerializer, TorneoSerializer

from tournament.models import Equipo, Partida, Torneo




class EquipoApiViewSet(ModelViewSet):
    queryset = Equipo.objects.all()
    serializer_class = EquipoSerializer
    #permission_classes = [IsAdminUser]


class TorneoApiViewSet(ModelViewSet):
    queryset = Torneo.objects.all()
    serializer_class = TorneoSerializer
   # permission_classes = [IsAdminUser]


class PartidaApiViewSet(ModelViewSet):
    queryset = Partida.objects.all()
    serializer_class = PartidaSerializer
    #permission_classes = [IsAdminUser]


