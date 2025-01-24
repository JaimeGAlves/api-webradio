from django.contrib import admin
from notices.models import Noticias, Fonte, Imagem

admin.site.register(Noticias)
admin.site.register(Fonte)
admin.site.register(Imagem)

# Register your models here.
