from rest_framework import serializers
from .models import PedidoMusica, Programacao, Equipe

class PedidoMusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoMusica
        fields = ['id', 'nome_ouvinte', 'pedido', 'criado_em']
        read_only_fields = ['criado_em']

class ProgramacaoSerializer(serializers.ModelSerializer):
    locutor_name = serializers.CharField(source='locutor.nome', read_only=True)
    
    class Meta:
        model = Programacao
        fields = ['id', 'dia_semana', 'dia_semana_display', 'horario_inicio', 'horario_fim', 'nome_programa', 'locutor', 'locutor_name']

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'descricao', 'foto']
