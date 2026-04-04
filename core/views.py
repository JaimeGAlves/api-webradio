from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from .models import PedidoMusica, Programacao, Equipe
from .serializers import PedidoMusicaSerializer, ProgramacaoSerializer, EquipeSerializer

class PedidoMusicaViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = PedidoMusica.objects.all()
    serializer_class = PedidoMusicaSerializer
    permission_classes = [AllowAny]

class ProgramacaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Programacao.objects.all()
    serializer_class = ProgramacaoSerializer
    permission_classes = [AllowAny]

class EquipeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer
    permission_classes = [AllowAny]
