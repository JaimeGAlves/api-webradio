from django import forms
from notices.models import Noticias
from sponsors.models import Patrocinador
from core.models import Programacao, Equipe

class MultipleFileInput(forms.FileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def to_python(self, data):
        if not data:
            return []
        if not isinstance(data, list):
            data = [data]
        # Valida cada arquivo individualmente usando o FileField padrão
        for item in data:
            super().to_python(item)
        return data

    def clean(self, data, initial=None):
        out = self.to_python(data)
        if not out and self.required:
            raise forms.ValidationError(self.error_messages['empty'])
        return out

class NoticiaForm(forms.ModelForm):
    imagens = MultipleFileField(
        widget=MultipleFileInput(attrs={
            'multiple': True, 
            'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'
        }), 
        required=False, 
        label="Adicionar Imagens", 
        help_text="Você pode selecionar várias imagens de uma vez para a notícia."
    )

    class Meta:
        model = Noticias
        fields = ['titulo', 'subtitulo', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'subtitulo': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all', 'rows': 3}),
            'conteudo': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all', 'rows': 6}),
        }

class PatrocinadorForm(forms.ModelForm):
    class Meta:
        model = Patrocinador
        fields = ['nome', 'link', 'imagem_app', 'imagem_site']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'link': forms.URLInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'imagem_app': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white'}),
            'imagem_site': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white'}),
        }

class ProgramacaoForm(forms.ModelForm):
    class Meta:
        model = Programacao
        fields = ['dias_semana', 'horario_inicio', 'horario_fim', 'nome_programa', 'locutor']
        widgets = {
            'dias_semana': forms.CheckboxSelectMultiple(attrs={'class': 'flex flex-wrap gap-4 p-4 bg-gray-50 dark:bg-gray-800 rounded-xl border border-gray-200 dark:border-white/10'}),
            'horario_inicio': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'horario_fim': forms.TimeInput(attrs={'type': 'time', 'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'nome_programa': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'locutor': forms.Select(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
        }

class EquipeForm(forms.ModelForm):
    class Meta:
        model = Equipe
        fields = ['nome', 'descricao', 'foto']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all'}),
            'descricao': forms.Textarea(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white focus:outline-none focus:ring-2 focus:ring-teal/50 transition-all', 'rows': 4}),
            'foto': forms.FileInput(attrs={'class': 'w-full px-4 py-2 border border-gray-200 dark:border-white/10 rounded-xl bg-white dark:bg-gray-800 text-gray-800 dark:text-white'}),
        }
