from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from notices.models import (
    Noticias, 
    Fonte, 
    Imagem,
)

from notices.serializers import (
    NoticiasSerializer, 
    FonteSerializer, 
    ImagemSerializer,
)

class NoticiasCreateView(APIView):
    
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = NoticiasSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class NoticiasDetalhesView(APIView):
    
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """Retorna o último registro da notícia
           Chave primária: pk
        """
        result = Noticias.objects.filter(pk=pk).last()
        
        return result
    
    def get(self, request, pk=None):
        
        if pk:
            noticia = self.get_object(pk)
            if noticia:
                serializer = NoticiasSerializer(noticia)
                return Response(serializer.data)
            return Response({"message": "Notícia não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        noticias = Noticias.objects.all()
        
        serializer = NoticiasSerializer(noticias, many=True)
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        noticia = self.get_object(pk)
        serializer = NoticiasSerializer(noticia, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        noticia = self.get_object(pk)
        noticia.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FonteCreateView(APIView):
    
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = FonteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class FonteDetalhesView(APIView):
    
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        """Retorna o último registro da fonte
           Chave primária: pk
        """
        result = Fonte.objects.filter(pk=pk).last()
        
        return result
    
    def get(self, request, pk=None):
        
        if pk:
            fonte = self.get_object(pk)
            if fonte:
                serializer = FonteSerializer(fonte)
                return Response(serializer.data)
            return Response({"message": "Fonte não encontrada"}, status=status.HTTP_404_NOT_FOUND)
        
        fontes = Fonte.objects.all()
        
        serializer = FonteSerializer(fontes, many=True)
        
        return Response(serializer.data)
    
    def put(self, request, pk):
        
        fonte = self.get_object(pk)
        serializer = FonteSerializer(fonte, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        
        fonte = self.get_object(pk)
        fonte.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)