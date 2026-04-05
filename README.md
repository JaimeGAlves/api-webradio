# 📡 API WebRádio Dimúsica

O **API WebRádio** é o motor central (backend) desenvolvido em **Django** e **Django Rest Framework (DRF)**, projetado para gerenciar conteúdos de forma robusta e segura para todo o ecossistema Dimúsica (Portal Web e Aplicativo Mobile).

Este projeto fornece uma interface administrativa moderna e uma API escalável com autenticação **JWT**, garantindo que as notícias, patrocinadores e a interatividade com os ouvintes sejam entregues com rapidez e segurança.

---

## 🚀 Highlights Técnicos

- **Django 6.x & DRF:** Core de última geração para gestão de dados e criação de endpoints RESTful eficientes.
- **Painel Administrativo Premium:** Interface totalmente revitalizada com **TailwindCSS**, focada em produtividade e estética moderna.
- **Modo Escuro Nativo:** Suporte completo com persistência de preferência, proporcionando conforto visual ao administrador.
- **Segurança (Simple JWT):** Autenticação robusta baseada em tokens para integração segura com dispositivos mobile.
- **Gestão de Mídia Otimizada:** Processamento e redimensionamento inteligente de imagens para garantir performance.

---

## 🛠️ Principais Recursos

### 📰 Gestão de Conteúdo
- **Módulo de Notícias:** Suporte a múltiplas imagens, categorias e formatação rica.
- **Patrocinadores:** Gerenciamento de marcas parceiras com controle de visibilidade.

### 🎙️ Interatividade e Programação
- **Grade de Programação:** Agendamento flexível de programas por dia e horário.
- **Pedidos de Música:** Endpoint dedicado para capturar interações de ouvintes em tempo real.
- **Gestão de Equipe:** Perfil completo de locutores e colaboradores com fotos e biografias.

---

## 📂 Estrutura do Projeto

```text
api-webradio/
├── core/           # App principal: modelos globais e lógica de negócio
├── notices/        # Módulo especializado em notícias e mídia
├── sponsors/       # Módulo de gestão de patrocinadores e parceiros
├── webadmin/       # Customizações do painel administrativo
├── settings/       # Configurações globais e de ambiente (Django Settings)
├── media/          # Armazenamento de uploads (notícias, fotos)
└── manage.py       # Utilitário de gerenciamento do Django
```

---

## ⚙️ Guia de Instalação e Execução

### 1. Requisitos
- Python 3.10 ou superior
- Pip (Gerenciador de pacotes)

### 2. Configuração do Ambiente
```bash
# Clone o projeto
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente (Windows)
.\venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Banco de Dados e Superusuário
```bash
# Rode as migrações
python manage.py migrate

# Crie um administrador
python manage.py createsuperuser
```

### 4. Executando o Servidor
```bash
python manage.py runserver
```
Acesse o painel em: `http://127.0.0.1:8000/admin`

---

## 📱 Integração Mobile
A API disponibiliza rotas sob o prefixo `/api/v1/`, protegidas por JWT. Consulte a documentação técnica em `docs/api_endpoints.md` para detalhes dos contratos de dados.

---
> [!TIP]
> Em ambiente de desenvolvimento, utilize o `db.sqlite3` incluído. Para produção, recomendamos a configuração de variáveis de ambiente no arquivo `.env` para apontar para um banco PostgreSQL.

---
© {% now "Y" %} **Web Rádio Dimúsica** - A qualidade que se ouve.