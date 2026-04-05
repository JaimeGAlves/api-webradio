from rest_framework import serializers
from .models import PedidoMusica, Programacao, Equipe

class PedidoMusicaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PedidoMusica
        fields = ['id', 'nome_ouvinte', 'pedido', 'criado_em']
        read_only_fields = ['criado_em']

class ProgramacaoSerializer(serializers.ModelSerializer):
    locutor_name = serializers.SerializerMethodField()
    dia_semana_display = serializers.SerializerMethodField()
    # Mantemos 'dia_semana' como campo calculado para compatibilidade com o Site
    dia_semana = serializers.SerializerMethodField()

    def get_locutor_name(self, obj):
        return obj.locutor.nome if obj.locutor else None

    def get_dia_semana_display(self, obj):
        # Retorna o display do primeiro dia associado
        primeiro_dia = obj.dias_semana.first()
        return primeiro_dia.nome if primeiro_dia else "Vários Dias"

    def get_dia_semana(self, obj):
        # Retorna o ID do primeiro dia para não quebrar a lógica atual do Site
        primeiro_dia = obj.dias_semana.first()
        return primeiro_dia.id if primeiro_dia else 0

    class Meta:
        model = Programacao
        fields = ['id', 'dia_semana', 'dias_semana', 'dia_semana_display', 'horario_inicio', 'horario_fim', 'nome_programa', 'locutor', 'locutor_name']

class EquipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipe
        fields = ['id', 'nome', 'descricao', 'foto']
