from django.db import models

class ListenerStat(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, verbose_name="Horário da Leitura")
    count = models.IntegerField(default=0, verbose_name="Ouvintes Totais")
    unique_count = models.IntegerField(default=0, verbose_name="Ouvintes Únicos")

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Estatística de Ouvinte"
        verbose_name_plural = "Estatísticas de Ouvintes"

    def __str__(self):
        return f"{self.timestamp.strftime('%d/%m/%Y %H:%M')} - {self.count} ouvintes"
