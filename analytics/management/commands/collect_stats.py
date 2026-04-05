import json
import urllib.request
import ssl
from django.core.management.base import BaseCommand
from analytics.models import ListenerStat

class Command(BaseCommand):
    help = 'Coleta estatísticas de ouvintes da API SonicPanel'

    def handle(self, *args, **options):
        url = "https://stream1.svrdedicado.org/cp/get_info.php?p=8238"
        
        # Ignorar erros de SSL se houver (o SonicPanel às vezes tem certificados auto-assinados ou expirados)
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        try:
            with urllib.request.urlopen(url, context=ctx, timeout=15) as response:
                data = json.loads(response.read().decode())
                
                listeners = int(data.get('listeners', 0))
                ulistener = int(data.get('ulistener', 0))
                
                stat = ListenerStat.objects.create(
                    count=listeners,
                    unique_count=ulistener
                )
                
                self.stdout.write(self.style.SUCCESS(f'Estatística coletada com sucesso: {listeners} ouvintes.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Erro ao coletar estatísticas: {str(e)}'))
