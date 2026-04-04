from django.contrib import admin

from .models import PedidoMusica, Programacao, Equipe

@admin.register(PedidoMusica)
class PedidoMusicaAdmin(admin.ModelAdmin):
    list_display = ('nome_ouvinte', 'pedido', 'lido', 'criado_em')
    list_filter = ('lido',)
    readonly_fields = ('criado_em',)

@admin.register(Programacao)
class ProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('dia_semana', 'horario_inicio', 'horario_fim', 'nome_programa')
    list_filter = ('dia_semana',)

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
