from django.contrib import admin
from sponsors.models import Patrocinador

class PatrocinadorAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')

admin.site.register(Patrocinador, PatrocinadorAdmin)
