from django.db import models

class PedidoMusica(models.Model):
    nome_ouvinte = models.CharField(max_length=150)
    pedido = models.CharField(max_length=255)
    lido = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-criado_em']

    def __str__(self):
        return f"{self.nome_ouvinte} - {self.pedido}"

class Equipe(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    foto = models.ImageField(upload_to='equipe/')

    def __str__(self):
        return self.nome

class Programacao(models.Model):
    DIAS_DA_SEMANA = [
        (0, 'Domingo'),
        (1, 'Segunda-feira'),
        (2, 'Terça-feira'),
        (3, 'Quarta-feira'),
        (4, 'Quinta-feira'),
        (5, 'Sexta-feira'),
        (6, 'Sábado'),
    ]
    dia_semana = models.IntegerField(choices=DIAS_DA_SEMANA)
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    nome_programa = models.CharField(max_length=150)
    locutor = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name='programas')

    class Meta:
        ordering = ['dia_semana', 'horario_inicio']

    def __str__(self):
        return f"{self.get_dia_semana_display()} {self.horario_inicio} - {self.nome_programa}"
