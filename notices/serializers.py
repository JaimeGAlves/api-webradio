from rest_framework import serializers
from notices.models import (
    Noticias, Fonte, Imagem
)

class NoticiasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticias
        fields = '__all__'

class FonteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fonte
        fields = '__all__'
        
class ImagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imagem
        fields = '__all__'