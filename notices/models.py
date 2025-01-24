from django.db import models

# Create your models here.

class Noticias(models.Model):
    titulo = models.CharField(max_length=255, unique=True, blank=False, null=False)
    subtitulo = models.TextField(blank=False, null=False)
    conteudo = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo
    

class Fonte(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='fontes')
    nome = models.CharField(max_length=255, blank=False, null=False)
    link = models.URLField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.nome
    
    
class Imagem(models.Model):
    noticia = models.ForeignKey(Noticias, on_delete=models.CASCADE, related_name='imagens')
    imagem = models.ImageField(upload_to='noticias/', blank=False, null=False)
    rodape = models.CharField(max_length=255, blank=False, null=False)
    
    def __str__(self):
        return self.imagem.url