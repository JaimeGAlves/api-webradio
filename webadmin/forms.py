from django import forms
from notices.models import Noticias
from sponsors.models import Patrocinador
from core.models import Programacao, Equipe

class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class NoticiaForm(forms.ModelForm):
    imagens = forms.FileField(widget=MultipleFileInput(attrs={'multiple': True, 'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}), required=False, label="Adicionar Imagens", help_text="Você pode selecionar várias imagens de uma vez para a notícia.")

    class Meta:
        model = Noticias
        fields = ['titulo', 'subtitulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'subtitulo': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]', 'rows': 3}),
            'conteudo': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]', 'rows': 6}),
        }

class PatrocinadorForm(forms.ModelForm):
    class Meta:
        model = Patrocinador
        fields = ['nome', 'link', 'imagem_app', 'imagem_site']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'imagem_app': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded'}),
            'imagem_site': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded'}),
        }

class ProgramacaoForm(forms.ModelForm):
    class Meta:
        model = Programacao
        fields = ['dia_semana', 'horario_inicio', 'horario_fim', 'nome_programa', 'locutor']
        widgets = {
            'dia_semana': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'nome_programa': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'locutor': forms.Select(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]'}),
            'descricao': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border rounded focus:outline-none focus:ring-2 focus:ring-[#0A7DD1]', 'rows': 4}),
            'foto': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border rounded'}),
        }
