# API Webradio

Bem-vindo ao repositório do **API Webradio**!
Este projeto é uma API backend robusta desenvolvida em Django e Django Rest Framework (DRF) para dar suporte a uma aplicação de Web Rádio completa. Além de fornecer endpoints para o gerenciamento de notícias e patrocinadores com autenticação JWT, o projeto agora conta com um **Painel Administrativo Moderno** (TailwindCSS) e recursos de **Interatividade com Ouvintes** (Pedidos de Música, Grade de Programação e Equipe).

## Documentação

Toda a documentação técnica foi dividida em arquivos específicos na pasta `docs/` para melhor organização:

- [Configuração e Execução Local](docs/setup.md): Instruções passo a passo sobre como instalar as dependências, configurar o ambiente virtual e rodar o projeto na sua máquina.
- [Modelos e Banco de Dados](docs/models.md): Detalhes sobre os modelos de dados utilizados no projeto (Notícias, Patrocinadores, Pedidos, Grade de Programação, Equipe).
- [Endpoints da API](docs/api_endpoints.md): Lista e descrição de todos os endpoints disponíveis na aplicação, incluindo rotas de autenticação, notícias, patrocinadores e recursos interativos.
- [Arquitetura do Ecossistema](docs/architecture.md): Visão técnica detalhada de como a API gerencia e entrega dados para o App Mobile e o Site.

## Tecnologias Utilizadas

- **Python & Django** (Framework Backend)
- **Django Rest Framework** (Construção da API)
- **Simple JWT** (Autenticação baseada em tokens JWT)
- **Pillow** (Processamento de Imagens)
- **SQLite3** (Banco de dados padrão)