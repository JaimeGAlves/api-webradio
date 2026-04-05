# Configuração e Execução do Projeto

Este documento explica como configurar o ambiente de desenvolvimento e executar o projeto **API Webradio** localmente.

## Pré-requisitos

- **Python 3.10+** instalado (ou versão compatível)
- Ferramenta de versionamento **Git**

## Passo a Passo

### 1. Clonar o repositório

```bash
git clone https://github.com/JaimeGAlves/api-webradio.git
cd api-webradio
```

### 2. Criar e Ativar um Ambiente Virtual (Venv)

Crie um ambiente virtual para instalar as dependências de forma isolada:

**No Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**No Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as Dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias contidas no `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Executar as Migrações do Banco de Dados

O projeto utiliza SQLite3 por padrão. Para criar o banco de dados e as tabelas, rode o comando:

```bash
python manage.py migrate
```

### 5. Inicializar Dados do Sistema (Importante)
Para que a grade de programação funcione, os dias da semana devem estar cadastrados. Você pode criar um superusuário e cadastrá-los manualmente no painel ou rodar o comando abaixo no shell do Django:

```bash
python manage.py shell
```
Dentro do shell:
```python
from core.models import DiaSemana
dias = ['Domingo', 'Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado']
for i, nome in enumerate(dias):
    DiaSemana.objects.get_or_create(id=i, nome=nome)
```

### 6. Criar um Superusuário
Para acessar o painel de administração (`/painel/`), crie um superusuário:

```bash
python manage.py createsuperuser
```

Siga os prompts de e-mail e senha.

### 6. Executar o Servidor de Desenvolvimento

Inicie o servidor local do Django:

```bash
python manage.py runserver
```

A API estará disponível no endereço: `http://127.0.0.1:8000/`.

---

## Estrutura do Projeto

- `core/`: Aplicativo central tratando de Pedidos de Música, Programação e Equipe.
- `notices/`: Aplicativo responsável por tratar notícias, fontes e galerias de imagens.
- `settings/`: Diretório de configurações do Django (`settings.py`, `urls.py`).
- `sponsors/`: Aplicativo focado no gerenciamento de patrocinadores (para web e app).
- `webadmin/`: Painel Administrativo moderno (TailwindCSS) para os usuários finais da rádio.

## Painel de Controle
O projeto oferece duas formas de gestão:
1. **Django Admin (`/api/admin/`)**: Gestão técnica e profunda dos dados.
2. **Painel WebRádio (`/painel/`)**: Interface amigável, visual e rápida com Dashboard informativo.

Voltar para o [README](../README.md).
