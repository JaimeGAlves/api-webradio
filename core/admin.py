from django.contrib import admin

from .models import PedidoMusica, Programacao, Equipe, DiaSemana

@admin.register(DiaSemana)
class DiaSemanaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome')

@admin.register(PedidoMusica)
class PedidoMusicaAdmin(admin.ModelAdmin):
    list_display = ('nome_ouvinte', 'pedido', 'lido', 'criado_em')
    list_filter = ('lido',)
    readonly_fields = ('criado_em',)

@admin.register(Programacao)
class ProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('exibir_dias', 'horario_inicio', 'horario_fim', 'nome_programa')
    list_filter = ('dias_semana',)

    def exibir_dias(self, obj):
        return ", ".join([d.nome for d in obj.dias_semana.all()])
    exibir_dias.short_description = 'Dias da Semana'

@admin.register(Equipe)
class EquipeAdmin(admin.ModelAdmin):
    list_display = ('nome',)
