from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoMusicaViewSet, ProgramacaoViewSet, EquipeViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoMusicaViewSet, basename='pedidos')
router.register(r'programacao', ProgramacaoViewSet, basename='programacao')
router.register(r'equipe', EquipeViewSet, basename='equipe')

urlpatterns = [
    path('', include(router.urls)),
]
