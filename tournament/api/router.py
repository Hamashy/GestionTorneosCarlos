from rest_framework.routers import DefaultRouter

from tournament.api.views import EquipoApiViewSet, TorneoApiViewSet, PartidaApiViewSet

# equipo,torneo,partida

router_equipo = DefaultRouter()
router_torneo = DefaultRouter()
router_partida = DefaultRouter()

router_equipo.register(prefix='equipo', basename='equipo', viewset=EquipoApiViewSet)
router_torneo.register(prefix='torneo', basename='torneo', viewset=TorneoApiViewSet)
router_partida.register(prefix='partida', basename='partida', viewset=PartidaApiViewSet)


