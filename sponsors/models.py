from django.db import models

class Patrocinador(models.Model):
    nome = models.CharField(max_length=255, unique=True, blank=False, null=False)
    link = models.URLField(max_length=255, blank=False, null=False)
    imagem_app = models.ImageField(upload_to='patrocinador_app/', blank=False, null=False)
    imagem_site = models.ImageField(upload_to='patrocinador_site/', blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome