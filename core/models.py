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

class DiaSemana(models.Model):
    id = models.IntegerField(primary_key=True)  # 0-6 seguindo o padrão atual
    nome = models.CharField(max_length=20)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.nome

class Programacao(models.Model):
    # Novo campo ManyToMany consolidado
    dias_semana = models.ManyToManyField(DiaSemana, related_name='programas', blank=True)
    
    horario_inicio = models.TimeField()
    horario_fim = models.TimeField()
    nome_programa = models.CharField(max_length=150)
    locutor = models.ForeignKey(Equipe, on_delete=models.SET_NULL, null=True, blank=True, related_name='programas')

    class Meta:
        ordering = ['horario_inicio']

    def __str__(self):
        return f"{self.nome_programa} ({self.horario_inicio} - {self.horario_fim})"
