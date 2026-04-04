from django.contrib import admin
from notices.models import Noticias, Fonte, Imagem

class NoticiasAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'created_at', 'updated_at', 'updated_by')
    readonly_fields = ('created_at', 'updated_at', 'created_by', 'updated_by')

admin.site.register(Noticias, NoticiasAdmin)
admin.site.register(Fonte)
admin.site.register(Imagem)

# Register your models here.
